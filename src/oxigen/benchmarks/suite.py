"""Operational evidence suite for the PT-BR benchmark vertical slice.

The suite compares several deterministic baselines over the same frozen dataset
and emits an inspectable evidence pack. The bundled dataset remains synthetic;
results are engineering evidence for the evaluation pipeline, not a claim of
real-world Brazilian Portuguese model quality.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import platform
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from sklearn import __version__ as sklearn_version
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.pipeline import Pipeline

from oxigen.benchmarks.ptbr_intent import Example, Prediction, load_examples

SUITE_NAME = "ptbr-public-interest-intent-suite"
SUITE_VERSION = "0.2.0"
CLAIM_BOUNDARY = (
    "Repository-authored synthetic fixture for reproducibility, evaluation plumbing, "
    "negative controls and operational evidence only. Metrics are not evidence of "
    "real-world PT-BR model quality, safety, fairness or production readiness."
)


@dataclass(frozen=True)
class ModelEvidence:
    """Metrics and predictions for one deterministic baseline."""

    model_id: str
    configuration: dict[str, Any]
    accuracy: float
    macro_f1: float
    confusion_matrix: list[list[int]]
    predictions: list[Prediction]

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["accuracy"] = round(self.accuracy, 6)
        payload["macro_f1"] = round(self.macro_f1, 6)
        return payload


@dataclass(frozen=True)
class SuiteResult:
    """Complete machine-readable evidence for one suite execution."""

    suite: str
    suite_version: str
    dataset_sha256: str
    train_examples: int
    eval_examples: int
    labels: list[str]
    runtime: dict[str, str]
    models: list[ModelEvidence]
    claim_boundary: str

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["models"] = [model.to_dict() for model in self.models]
        return payload


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(64 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _majority_label(labels: list[str]) -> str:
    counts: dict[str, int] = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return sorted(counts, key=lambda label: (-counts[label], label))[0]


def _evaluate(
    *,
    model_id: str,
    configuration: dict[str, Any],
    evaluation: list[Example],
    expected: list[str],
    predicted: list[str],
    labels: list[str],
) -> ModelEvidence:
    predictions = [
        Prediction(
            id=example.id,
            expected=expected_label,
            predicted=predicted_label,
            correct=expected_label == predicted_label,
        )
        for example, expected_label, predicted_label in zip(
            evaluation, expected, predicted, strict=True
        )
    ]
    matrix_raw = confusion_matrix(expected, predicted, labels=labels)
    matrix = [[int(value) for value in row] for row in matrix_raw.tolist()]
    return ModelEvidence(
        model_id=model_id,
        configuration=configuration,
        accuracy=float(accuracy_score(expected, predicted)),
        macro_f1=float(f1_score(expected, predicted, labels=labels, average="macro")),
        confusion_matrix=matrix,
        predictions=predictions,
    )


def _linear_pipeline(*, analyzer: str, ngram_range: tuple[int, int]) -> Pipeline:
    return Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    analyzer=analyzer,
                    ngram_range=ngram_range,
                    min_df=1,
                    sublinear_tf=True,
                ),
            ),
            (
                "classifier",
                LogisticRegression(max_iter=1_000, solver="lbfgs"),
            ),
        ]
    )


def run_suite(dataset_path: Path) -> SuiteResult:
    """Run three deterministic baselines over one frozen dataset."""

    examples = load_examples(dataset_path)
    train = [example for example in examples if example.split == "train"]
    evaluation = [example for example in examples if example.split == "eval"]
    labels = sorted({example.label for example in examples})

    train_texts = [example.text for example in train]
    train_labels = [example.label for example in train]
    eval_texts = [example.text for example in evaluation]
    expected = [example.label for example in evaluation]

    majority = _majority_label(train_labels)
    models = [
        _evaluate(
            model_id="majority-class",
            configuration={"strategy": "most-frequent-train-label", "label": majority},
            evaluation=evaluation,
            expected=expected,
            predicted=[majority] * len(evaluation),
            labels=labels,
        )
    ]

    word_model = _linear_pipeline(analyzer="word", ngram_range=(1, 2))
    word_model.fit(train_texts, train_labels)
    word_predictions = [str(label) for label in word_model.predict(eval_texts)]
    models.append(
        _evaluate(
            model_id="tfidf-word-logreg",
            configuration={
                "vectorizer": "word tf-idf",
                "ngram_range": [1, 2],
                "classifier": "LogisticRegression(lbfgs,max_iter=1000)",
            },
            evaluation=evaluation,
            expected=expected,
            predicted=word_predictions,
            labels=labels,
        )
    )

    char_model = _linear_pipeline(analyzer="char_wb", ngram_range=(3, 5))
    char_model.fit(train_texts, train_labels)
    char_predictions = [str(label) for label in char_model.predict(eval_texts)]
    models.append(
        _evaluate(
            model_id="tfidf-char-logreg",
            configuration={
                "vectorizer": "character-boundary tf-idf",
                "ngram_range": [3, 5],
                "classifier": "LogisticRegression(lbfgs,max_iter=1000)",
            },
            evaluation=evaluation,
            expected=expected,
            predicted=char_predictions,
            labels=labels,
        )
    )

    return SuiteResult(
        suite=SUITE_NAME,
        suite_version=SUITE_VERSION,
        dataset_sha256=_sha256(dataset_path),
        train_examples=len(train),
        eval_examples=len(evaluation),
        labels=labels,
        runtime={
            "python": platform.python_version(),
            "scikit_learn": sklearn_version,
        },
        models=models,
        claim_boundary=CLAIM_BOUNDARY,
    )


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _eval_card(result: SuiteResult) -> str:
    rows = "\n".join(
        f"| `{model.model_id}` | {model.accuracy:.3f} | {model.macro_f1:.3f} |"
        for model in result.models
    )
    return f"""# Eval card — {result.suite}@{result.suite_version}

## Purpose

This card records one reproducible engineering benchmark execution over the bundled frozen fixture.

| Baseline | Accuracy | Macro F1 |
|---|---:|---:|
{rows}

## Dataset

- train examples: {result.train_examples}
- eval examples: {result.eval_examples}
- labels: {", ".join(result.labels)}
- dataset SHA-256: `{result.dataset_sha256}`

## Runtime

- Python: `{result.runtime['python']}`
- scikit-learn: `{result.runtime['scikit_learn']}`

## Claim boundary

{result.claim_boundary}

## Promotion rule

A real PT-BR quality claim requires an independently sourced dataset with verified reuse terms,
recorded provenance, frozen preprocessing/splits and a separately versioned benchmark contract.
"""


def _html_report(result: SuiteResult) -> str:
    rows = "".join(
        "<tr>"
        f"<td><code>{html.escape(model.model_id)}</code></td>"
        f"<td>{model.accuracy:.3f}</td>"
        f"<td>{model.macro_f1:.3f}</td>"
        "</tr>"
        for model in result.models
    )
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<title>Oxigênio benchmark evidence</title>"
        "<style>body{font-family:system-ui;max-width:900px;margin:40px auto;padding:0 20px;}"
        "table{border-collapse:collapse;width:100%;}td,th{border:1px solid #ddd;padding:8px;}"
        "code{font-family:ui-monospace,monospace;}small{color:#555;}</style></head><body>"
        f"<h1>{html.escape(result.suite)}</h1>"
        f"<p>Suite version <code>{html.escape(result.suite_version)}</code></p>"
        "<table><thead><tr><th>Baseline</th><th>Accuracy</th><th>Macro F1</th></tr></thead>"
        f"<tbody>{rows}</tbody></table>"
        f"<p><small>{html.escape(result.claim_boundary)}</small></p>"
        f"<p>Dataset SHA-256: <code>{result.dataset_sha256}</code></p>"
        "</body></html>\n"
    )


def write_evidence_pack(
    result: SuiteResult,
    *,
    output_dir: Path,
    source_manifest_path: Path,
) -> list[Path]:
    """Write a deterministic, inspectable evidence pack and digest manifest."""

    output_dir.mkdir(parents=True, exist_ok=True)
    experiment_path = output_dir / "experiment.json"
    metrics_path = output_dir / "metrics.json"
    dataset_manifest_path = output_dir / "dataset-manifest.json"
    eval_card_path = output_dir / "eval-card.md"
    report_path = output_dir / "report.html"

    _write_json(experiment_path, result.to_dict())
    _write_json(
        metrics_path,
        {
            "suite": result.suite,
            "suite_version": result.suite_version,
            "dataset_sha256": result.dataset_sha256,
            "models": [
                {
                    "model_id": model.model_id,
                    "accuracy": round(model.accuracy, 6),
                    "macro_f1": round(model.macro_f1, 6),
                }
                for model in result.models
            ],
            "claim_boundary": result.claim_boundary,
        },
    )

    source_manifest = json.loads(source_manifest_path.read_text(encoding="utf-8"))
    if not isinstance(source_manifest, dict):
        raise ValueError("source dataset manifest must contain a JSON object")
    promoted_manifest = dict(source_manifest)
    promoted_manifest["computed_sha256"] = result.dataset_sha256
    promoted_manifest["evidence_suite"] = f"{result.suite}@{result.suite_version}"
    _write_json(dataset_manifest_path, promoted_manifest)

    eval_card_path.write_text(_eval_card(result), encoding="utf-8")
    report_path.write_text(_html_report(result), encoding="utf-8")

    evidence_paths = [
        dataset_manifest_path,
        eval_card_path,
        experiment_path,
        metrics_path,
        report_path,
    ]
    digest_manifest = {
        "schema": "oxigenio-evidence-manifest.v1",
        "files": {path.name: _sha256(path) for path in sorted(evidence_paths)},
    }
    manifest_path = output_dir / "evidence-manifest.json"
    _write_json(manifest_path, digest_manifest)
    return [*evidence_paths, manifest_path]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("data/benchmarks/ptbr-public-interest-intent-v0.jsonl"),
    )
    parser.add_argument(
        "--source-manifest",
        type=Path,
        default=Path("data/benchmarks/ptbr-public-interest-intent-v0.manifest.json"),
    )
    parser.add_argument("--out-dir", type=Path, default=Path("artifacts/ptbr-suite"))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = run_suite(args.dataset)
    paths = write_evidence_pack(
        result,
        output_dir=args.out_dir,
        source_manifest_path=args.source_manifest,
    )
    print(f"{result.suite}@{result.suite_version}")
    for model in result.models:
        print(f"{model.model_id}: accuracy={model.accuracy:.3f} macro_f1={model.macro_f1:.3f}")
    print(f"dataset_sha256={result.dataset_sha256}")
    print("evidence=" + ",".join(str(path) for path in paths))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
