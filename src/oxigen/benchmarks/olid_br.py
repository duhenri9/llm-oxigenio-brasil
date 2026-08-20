"""Pinned external PT-BR benchmark using OLID-BR offensive-language labels.

The external dataset is loaded from a fixed Hugging Face revision. Raw text is
used in-memory for evaluation but is never written to the evidence pack.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_recall_fscore_support
from sklearn.pipeline import Pipeline

BENCHMARK_NAME = "olid-br-offensive-language"
BENCHMARK_VERSION = "1.0.0"
DATASET_ID = "dougtrajano/olid-br"
DATASET_REVISION = "84b0d7dd4309be677a47c535632a9398ff1897bd"
DATASET_LICENSE = "CC BY 4.0"
SOURCE_REPOSITORY = "https://github.com/DougTrajano/olid-br"
SOURCE_DATASET = "https://huggingface.co/datasets/dougtrajano/olid-br"
EXPECTED_SPLITS = ("train", "test")
EXPECTED_LABELS = ("NOT", "OFF")

CLAIM_BOUNDARY = (
    "These metrics describe one fixed OLID-BR offensive-language classification task and one "
    "simple TF-IDF/logistic-regression baseline. They do not establish broad Brazilian Portuguese "
    "quality, cultural coverage, fairness, safety, production fitness or model generalisation to "
    "other domains."
)


@dataclass(frozen=True)
class Example:
    """One validated external benchmark example."""

    id: str
    text: str
    label: str
    split: str
    text_sha256: str


@dataclass(frozen=True)
class DatasetManifest:
    """Source, licence, split and leakage evidence for the external dataset."""

    dataset_id: str
    revision: str
    licence: str
    source_repository: str
    source_dataset: str
    task: str
    train_examples: int
    test_examples: int
    labels: tuple[str, ...]
    train_sha256: str
    test_sha256: str
    dataset_sha256: str
    duplicate_ids: int
    cross_split_text_duplicates: int
    raw_text_persisted: bool
    privacy_note: str


@dataclass(frozen=True)
class PredictionEvidence:
    """Per-example evidence without persisting source text."""

    id: str
    text_sha256: str
    expected: str
    predicted: str
    correct: bool


@dataclass(frozen=True)
class BenchmarkResult:
    """One deterministic baseline execution over the official frozen splits."""

    benchmark: str
    benchmark_version: str
    model: dict[str, Any]
    accuracy: float
    macro_f1: float
    labels: tuple[str, ...]
    confusion_matrix: tuple[tuple[int, ...], ...]
    per_label: dict[str, dict[str, float | int]]
    predictions: tuple[PredictionEvidence, ...]
    claim_boundary: str

    def metrics_dict(self) -> dict[str, Any]:
        return {
            "benchmark": self.benchmark,
            "benchmark_version": self.benchmark_version,
            "model": self.model,
            "accuracy": round(self.accuracy, 6),
            "macro_f1": round(self.macro_f1, 6),
            "labels": list(self.labels),
            "confusion_matrix": [list(row) for row in self.confusion_matrix],
            "per_label": self.per_label,
            "claim_boundary": self.claim_boundary,
        }


def _canonical_sha256(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _validated_examples(split: str, rows: Iterable[Mapping[str, Any]]) -> list[Example]:
    examples: list[Example] = []
    for index, row in enumerate(rows):
        raw_id = row.get("id")
        raw_text = row.get("text")
        raw_label = row.get("is_offensive")
        if not isinstance(raw_id, str) or not raw_id.strip():
            raise ValueError(f"{split}[{index}] has invalid id")
        if not isinstance(raw_text, str) or not raw_text.strip():
            raise ValueError(f"{split}[{index}] has invalid text")
        if raw_label not in EXPECTED_LABELS:
            raise ValueError(f"{split}[{index}] has unsupported is_offensive label {raw_label!r}")
        text = raw_text.strip()
        examples.append(
            Example(
                id=raw_id.strip(),
                text=text,
                label=str(raw_label),
                split=split,
                text_sha256=_text_sha256(text),
            )
        )
    if not examples:
        raise ValueError(f"{split} split is empty")
    return examples


def _split_digest(examples: list[Example]) -> str:
    rows = [
        {
            "id": example.id,
            "text": example.text,
            "label": example.label,
            "split": example.split,
        }
        for example in examples
    ]
    return _canonical_sha256(rows)


def build_manifest(train: list[Example], test: list[Example]) -> DatasetManifest:
    """Validate official split identity and return a deterministic manifest."""

    ids = [example.id for example in train + test]
    duplicate_ids = len(ids) - len(set(ids))
    if duplicate_ids:
        raise ValueError(f"dataset contains {duplicate_ids} duplicate ids across official splits")

    train_texts = {example.text_sha256 for example in train}
    test_texts = {example.text_sha256 for example in test}
    cross_split_text_duplicates = len(train_texts & test_texts)
    if cross_split_text_duplicates:
        raise ValueError(
            "dataset contains exact text overlap across official train/test splits: "
            f"{cross_split_text_duplicates}"
        )

    train_labels = tuple(sorted({example.label for example in train}))
    test_labels = tuple(sorted({example.label for example in test}))
    expected = tuple(sorted(EXPECTED_LABELS))
    if train_labels != expected or test_labels != expected:
        raise ValueError("official train/test splits must both contain the expected binary label set")

    train_digest = _split_digest(train)
    test_digest = _split_digest(test)
    dataset_digest = _canonical_sha256(
        {
            "dataset_id": DATASET_ID,
            "revision": DATASET_REVISION,
            "train_sha256": train_digest,
            "test_sha256": test_digest,
        }
    )

    return DatasetManifest(
        dataset_id=DATASET_ID,
        revision=DATASET_REVISION,
        licence=DATASET_LICENSE,
        source_repository=SOURCE_REPOSITORY,
        source_dataset=SOURCE_DATASET,
        task="binary offensive-language identification in Brazilian Portuguese",
        train_examples=len(train),
        test_examples=len(test),
        labels=expected,
        train_sha256=train_digest,
        test_sha256=test_digest,
        dataset_sha256=dataset_digest,
        duplicate_ids=0,
        cross_split_text_duplicates=0,
        raw_text_persisted=False,
        privacy_note=(
            "Source texts may contain social-media and offensive-language content. Oxigenio loads "
            "them in memory for this benchmark but writes only dataset/example identities, hashes, "
            "labels, predictions and aggregate metrics to the evidence pack."
        ),
    )


def run_external_benchmark(
    train_rows: Iterable[Mapping[str, Any]],
    test_rows: Iterable[Mapping[str, Any]],
) -> tuple[DatasetManifest, BenchmarkResult]:
    """Run the deterministic baseline over supplied OLID-BR-shaped rows."""

    train = _validated_examples("train", train_rows)
    test = _validated_examples("test", test_rows)
    manifest = build_manifest(train, test)
    labels = manifest.labels

    model: Pipeline = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=(1, 2),
                    min_df=1,
                    sublinear_tf=True,
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    solver="lbfgs",
                    max_iter=1_000,
                    random_state=0,
                ),
            ),
        ]
    )
    model.fit([example.text for example in train], [example.label for example in train])

    expected = [example.label for example in test]
    predicted = [str(item) for item in model.predict([example.text for example in test])]
    matrix_raw = confusion_matrix(expected, predicted, labels=list(labels))
    matrix = tuple(tuple(int(value) for value in row) for row in matrix_raw.tolist())
    precision, recall, f1, support = precision_recall_fscore_support(
        expected,
        predicted,
        labels=list(labels),
        zero_division=0,
    )
    per_label = {
        label: {
            "precision": round(float(precision[index]), 6),
            "recall": round(float(recall[index]), 6),
            "f1": round(float(f1[index]), 6),
            "support": int(support[index]),
        }
        for index, label in enumerate(labels)
    }
    predictions = tuple(
        PredictionEvidence(
            id=example.id,
            text_sha256=example.text_sha256,
            expected=expected_label,
            predicted=predicted_label,
            correct=expected_label == predicted_label,
        )
        for example, expected_label, predicted_label in zip(test, expected, predicted, strict=True)
    )

    result = BenchmarkResult(
        benchmark=BENCHMARK_NAME,
        benchmark_version=BENCHMARK_VERSION,
        model={
            "family": "tfidf-logistic-regression",
            "vectorizer": "TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)",
            "classifier": "LogisticRegression(solver='lbfgs', max_iter=1000, random_state=0)",
        },
        accuracy=float(accuracy_score(expected, predicted)),
        macro_f1=float(f1_score(expected, predicted, labels=list(labels), average="macro")),
        labels=labels,
        confusion_matrix=matrix,
        per_label=per_label,
        predictions=predictions,
        claim_boundary=CLAIM_BOUNDARY,
    )
    return manifest, result


def load_pinned_dataset() -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]]]:
    """Load OLID-BR from the exact documented Hugging Face revision."""

    dataset = load_dataset(DATASET_ID, revision=DATASET_REVISION)
    missing = [split for split in EXPECTED_SPLITS if split not in dataset]
    if missing:
        raise ValueError(f"pinned dataset revision is missing required splits: {missing}")
    train = [dict(row) for row in dataset["train"]]
    test = [dict(row) for row in dataset["test"]]
    return train, test


def _write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_evidence_pack(
    output_dir: Path,
    manifest: DatasetManifest,
    result: BenchmarkResult,
) -> None:
    """Persist the complete redacted external-benchmark evidence pack."""

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_payload = asdict(manifest)
    manifest_payload["labels"] = list(manifest.labels)
    _write_json(output_dir / "dataset-manifest.json", manifest_payload)
    _write_json(output_dir / "metrics.json", result.metrics_dict())
    _write_json(
        output_dir / "experiment.json",
        {
            "benchmark": BENCHMARK_NAME,
            "benchmark_version": BENCHMARK_VERSION,
            "dataset_sha256": manifest.dataset_sha256,
            "dataset_revision": manifest.revision,
            "model": result.model,
            "train_examples": manifest.train_examples,
            "test_examples": manifest.test_examples,
        },
    )
    predictions_path = output_dir / "predictions.jsonl"
    predictions_path.write_text(
        "".join(
            json.dumps(asdict(item), ensure_ascii=False, sort_keys=True) + "\n"
            for item in result.predictions
        ),
        encoding="utf-8",
    )
    (output_dir / "eval-card.md").write_text(
        "\n".join(
            [
                "# OLID-BR external benchmark eval card",
                "",
                f"- Dataset: `{manifest.dataset_id}`",
                f"- Revision: `{manifest.revision}`",
                f"- Licence: {manifest.licence}",
                f"- Task: {manifest.task}",
                f"- Train examples: {manifest.train_examples}",
                f"- Test examples: {manifest.test_examples}",
                f"- Accuracy: {result.accuracy:.6f}",
                f"- Macro-F1: {result.macro_f1:.6f}",
                "- Raw source text persisted in evidence: no",
                "",
                "## Claim boundary",
                "",
                CLAIM_BOUNDARY,
                "",
                "## Data/privacy note",
                "",
                manifest.privacy_note,
                "",
            ]
        ),
        encoding="utf-8",
    )
    (output_dir / "report.txt").write_text(
        "\n".join(
            [
                f"benchmark={BENCHMARK_NAME}@{BENCHMARK_VERSION}",
                f"dataset={manifest.dataset_id}@{manifest.revision}",
                f"dataset_sha256={manifest.dataset_sha256}",
                f"train_examples={manifest.train_examples}",
                f"test_examples={manifest.test_examples}",
                f"accuracy={result.accuracy:.6f}",
                f"macro_f1={result.macro_f1:.6f}",
                f"claim_boundary={CLAIM_BOUNDARY}",
                "",
            ]
        ),
        encoding="utf-8",
    )

    evidence_files = [
        "dataset-manifest.json",
        "eval-card.md",
        "experiment.json",
        "metrics.json",
        "predictions.jsonl",
        "report.txt",
    ]
    digests = {
        name: hashlib.sha256((output_dir / name).read_bytes()).hexdigest()
        for name in evidence_files
    }
    _write_json(
        output_dir / "evidence-digests.json",
        {
            "schema": "oxigenio.external-benchmark-evidence.v1",
            "files": digests,
            "pack_sha256": _canonical_sha256(digests),
        },
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("artifacts/olidbr-v1"),
        help="Directory for the redacted external-benchmark evidence pack.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    train, test = load_pinned_dataset()
    manifest, result = run_external_benchmark(train, test)
    write_evidence_pack(args.out_dir, manifest, result)
    print(
        f"{BENCHMARK_NAME}@{BENCHMARK_VERSION}: accuracy={result.accuracy:.3f} "
        f"macro_f1={result.macro_f1:.3f} train={manifest.train_examples} "
        f"test={manifest.test_examples}"
    )
    print(f"dataset_revision={manifest.revision}")
    print(f"dataset_sha256={manifest.dataset_sha256}")
    print(f"evidence={args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
