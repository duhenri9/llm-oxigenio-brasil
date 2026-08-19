"""Deterministic PT-BR text-classification benchmark.

This module is intentionally narrow. It proves the repository can execute a
versioned ML workflow end to end without presenting the bundled synthetic
fixture as evidence of real-world model quality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer  # type: ignore[import-untyped]
from sklearn.linear_model import LogisticRegression  # type: ignore[import-untyped]
from sklearn.metrics import (  # type: ignore[import-untyped]
    accuracy_score,
    confusion_matrix,
    f1_score,
)
from sklearn.pipeline import Pipeline  # type: ignore[import-untyped]

BENCHMARK_NAME = "ptbr-public-interest-intent"
BENCHMARK_VERSION = "0.1.0"
EXPECTED_SPLITS = {"train", "eval"}


@dataclass(frozen=True)
class Example:
    """One versioned benchmark example."""

    id: str
    text: str
    label: str
    split: str


@dataclass(frozen=True)
class Prediction:
    """One evaluation prediction retained as inspectable evidence."""

    id: str
    expected: str
    predicted: str
    correct: bool


@dataclass(frozen=True)
class BenchmarkResult:
    """Machine-readable result for one exact benchmark execution."""

    benchmark: str
    benchmark_version: str
    dataset_sha256: str
    model: dict[str, Any]
    train_examples: int
    eval_examples: int
    labels: list[str]
    accuracy: float
    macro_f1: float
    confusion_matrix: list[list[int]]
    predictions: list[Prediction]
    claim_boundary: str

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serialisable representation."""

        payload = asdict(self)
        payload["accuracy"] = round(self.accuracy, 6)
        payload["macro_f1"] = round(self.macro_f1, 6)
        return payload


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(64 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_examples(path: Path) -> list[Example]:
    """Load and validate JSONL examples from ``path``."""

    examples: list[Example] = []
    seen_ids: set[str] = set()
    seen_text: set[str] = set()

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                raw = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at line {line_number}") from exc

            if not isinstance(raw, dict):
                raise ValueError(f"line {line_number} must contain a JSON object")

            required = {"id", "text", "label", "split"}
            if set(raw) != required:
                raise ValueError(f"line {line_number} must contain exactly {sorted(required)}")

            values = {key: raw[key] for key in required}
            if not all(isinstance(value, str) and value.strip() for value in values.values()):
                raise ValueError(f"line {line_number} contains an empty or non-string field")

            example = Example(
                id=values["id"].strip(),
                text=values["text"].strip(),
                label=values["label"].strip(),
                split=values["split"].strip(),
            )

            if example.split not in EXPECTED_SPLITS:
                raise ValueError(f"line {line_number} has unsupported split {example.split!r}")
            if example.id in seen_ids:
                raise ValueError(f"duplicate id {example.id!r}")
            if example.text.casefold() in seen_text:
                raise ValueError(f"duplicate text detected at line {line_number}")

            seen_ids.add(example.id)
            seen_text.add(example.text.casefold())
            examples.append(example)

    if not examples:
        raise ValueError("dataset is empty")

    splits = {example.split for example in examples}
    if splits != EXPECTED_SPLITS:
        raise ValueError(f"dataset must contain exactly the splits {sorted(EXPECTED_SPLITS)}")

    train_labels = {example.label for example in examples if example.split == "train"}
    eval_labels = {example.label for example in examples if example.split == "eval"}
    if train_labels != eval_labels:
        raise ValueError("train and eval splits must contain the same label set")
    if len(train_labels) < 2:
        raise ValueError("benchmark requires at least two labels")

    return examples


def run_benchmark(dataset_path: Path) -> BenchmarkResult:
    """Train the deterministic baseline and evaluate the frozen eval split."""

    examples = load_examples(dataset_path)
    train = [example for example in examples if example.split == "train"]
    evaluation = [example for example in examples if example.split == "eval"]
    labels = sorted({example.label for example in examples})

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
                    max_iter=1_000,
                    solver="lbfgs",
                ),
            ),
        ]
    )

    train_texts = [example.text for example in train]
    train_labels = [example.label for example in train]
    eval_texts = [example.text for example in evaluation]
    expected = [example.label for example in evaluation]

    model.fit(train_texts, train_labels)
    predicted_raw = model.predict(eval_texts)
    predicted = [str(label) for label in predicted_raw]

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

    return BenchmarkResult(
        benchmark=BENCHMARK_NAME,
        benchmark_version=BENCHMARK_VERSION,
        dataset_sha256=_sha256(dataset_path),
        model={
            "family": "tfidf-logistic-regression",
            "vectorizer": "TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)",
            "classifier": "LogisticRegression(solver='lbfgs', max_iter=1000)",
        },
        train_examples=len(train),
        eval_examples=len(evaluation),
        labels=labels,
        accuracy=float(accuracy_score(expected, predicted)),
        macro_f1=float(f1_score(expected, predicted, labels=labels, average="macro")),
        confusion_matrix=matrix,
        predictions=predictions,
        claim_boundary=(
            "Synthetic repository-authored fixture for pipeline and evaluation evidence only; "
            "metrics are not a claim of real-world PT-BR model quality or generalisation."
        ),
    )


def write_result(result: BenchmarkResult, output_path: Path) -> None:
    """Write deterministic benchmark evidence to JSON."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result.to_dict(), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("data/benchmarks/ptbr-public-interest-intent-v0.jsonl"),
        help="Versioned JSONL dataset path.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("artifacts/ptbr-public-interest-intent-v0.json"),
        help="Machine-readable evidence output path.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = run_benchmark(args.dataset)
    write_result(result, args.out)
    print(
        f"{result.benchmark}@{result.benchmark_version}: "
        f"accuracy={result.accuracy:.3f} macro_f1={result.macro_f1:.3f} "
        f"train={result.train_examples} eval={result.eval_examples}"
    )
    print(f"evidence={args.out}")
    print(f"dataset_sha256={result.dataset_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
