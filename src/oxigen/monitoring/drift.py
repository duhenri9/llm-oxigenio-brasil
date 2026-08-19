"""Deterministic drift checks for versioned Oxigênio benchmark datasets."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Literal

from oxigen.benchmarks.ptbr_intent import Example, load_examples

DriftStatus = Literal["PASS", "DRIFT", "INDETERMINATE"]


@dataclass(frozen=True)
class DatasetProfile:
    """Simple distributional profile for one dataset split."""

    split: str
    examples: int
    labels: dict[str, int]
    label_distribution: dict[str, float]
    mean_chars: float
    mean_tokens: float


@dataclass(frozen=True)
class DriftResult:
    """Bounded drift decision with inspectable metrics and thresholds."""

    status: DriftStatus
    label_total_variation: float
    mean_chars_relative_delta: float
    mean_tokens_relative_delta: float
    thresholds: dict[str, float]
    reasons: list[str]
    reference: DatasetProfile
    candidate: DatasetProfile

    def to_dict(self) -> dict[str, object]:
        payload = asdict(self)
        payload["label_total_variation"] = round(self.label_total_variation, 6)
        payload["mean_chars_relative_delta"] = round(self.mean_chars_relative_delta, 6)
        payload["mean_tokens_relative_delta"] = round(self.mean_tokens_relative_delta, 6)
        return payload


def profile_examples(examples: list[Example], *, split: str = "eval") -> DatasetProfile:
    """Create a deterministic profile for the requested split."""

    selected = [example for example in examples if example.split == split]
    if not selected:
        return DatasetProfile(
            split=split,
            examples=0,
            labels={},
            label_distribution={},
            mean_chars=0.0,
            mean_tokens=0.0,
        )

    counts: dict[str, int] = {}
    total_chars = 0
    total_tokens = 0
    for example in selected:
        counts[example.label] = counts.get(example.label, 0) + 1
        total_chars += len(example.text)
        total_tokens += len(example.text.split())

    total = len(selected)
    distribution = {label: counts[label] / total for label in sorted(counts)}
    return DatasetProfile(
        split=split,
        examples=total,
        labels={label: counts[label] for label in sorted(counts)},
        label_distribution=distribution,
        mean_chars=total_chars / total,
        mean_tokens=total_tokens / total,
    )


def _total_variation(reference: dict[str, float], candidate: dict[str, float]) -> float:
    labels = sorted(set(reference) | set(candidate))
    return 0.5 * sum(abs(reference.get(label, 0.0) - candidate.get(label, 0.0)) for label in labels)


def _relative_delta(reference: float, candidate: float) -> float:
    if reference == 0.0:
        return 0.0 if candidate == 0.0 else 1.0
    return abs(candidate - reference) / reference


def compare_profiles(
    reference: DatasetProfile,
    candidate: DatasetProfile,
    *,
    max_label_tvd: float = 0.20,
    max_mean_chars_delta: float = 0.30,
    max_mean_tokens_delta: float = 0.30,
) -> DriftResult:
    """Compare two profiles using explicit, bounded thresholds."""

    thresholds = {
        "max_label_tvd": max_label_tvd,
        "max_mean_chars_delta": max_mean_chars_delta,
        "max_mean_tokens_delta": max_mean_tokens_delta,
    }
    if reference.examples == 0 or candidate.examples == 0:
        return DriftResult(
            status="INDETERMINATE",
            label_total_variation=0.0,
            mean_chars_relative_delta=0.0,
            mean_tokens_relative_delta=0.0,
            thresholds=thresholds,
            reasons=["reference or candidate split contains zero examples"],
            reference=reference,
            candidate=candidate,
        )

    label_tvd = _total_variation(reference.label_distribution, candidate.label_distribution)
    chars_delta = _relative_delta(reference.mean_chars, candidate.mean_chars)
    tokens_delta = _relative_delta(reference.mean_tokens, candidate.mean_tokens)

    reasons: list[str] = []
    if label_tvd > max_label_tvd:
        reasons.append(f"label distribution TVD {label_tvd:.3f} exceeds {max_label_tvd:.3f}")
    if chars_delta > max_mean_chars_delta:
        reasons.append(
            f"mean character-length delta {chars_delta:.3f} exceeds {max_mean_chars_delta:.3f}"
        )
    if tokens_delta > max_mean_tokens_delta:
        reasons.append(
            f"mean token-count delta {tokens_delta:.3f} exceeds {max_mean_tokens_delta:.3f}"
        )

    return DriftResult(
        status="DRIFT" if reasons else "PASS",
        label_total_variation=label_tvd,
        mean_chars_relative_delta=chars_delta,
        mean_tokens_relative_delta=tokens_delta,
        thresholds=thresholds,
        reasons=reasons,
        reference=reference,
        candidate=candidate,
    )


def compare_dataset_files(
    reference_path: Path,
    candidate_path: Path,
    *,
    split: str = "eval",
    max_label_tvd: float = 0.20,
    max_mean_chars_delta: float = 0.30,
    max_mean_tokens_delta: float = 0.30,
) -> DriftResult:
    """Load two benchmark datasets and compare the requested split."""

    reference = profile_examples(load_examples(reference_path), split=split)
    candidate = profile_examples(load_examples(candidate_path), split=split)
    return compare_profiles(
        reference,
        candidate,
        max_label_tvd=max_label_tvd,
        max_mean_chars_delta=max_mean_chars_delta,
        max_mean_tokens_delta=max_mean_tokens_delta,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--split", default="eval")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--expect", choices=["PASS", "DRIFT", "INDETERMINATE"])
    parser.add_argument("--max-label-tvd", type=float, default=0.20)
    parser.add_argument("--max-mean-chars-delta", type=float, default=0.30)
    parser.add_argument("--max-mean-tokens-delta", type=float, default=0.30)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = compare_dataset_files(
        args.reference,
        args.candidate,
        split=args.split,
        max_label_tvd=args.max_label_tvd,
        max_mean_chars_delta=args.max_mean_chars_delta,
        max_mean_tokens_delta=args.max_mean_tokens_delta,
    )
    payload = result.to_dict()
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
    if args.expect is not None and result.status != args.expect:
        print(f"expected={args.expect} observed={result.status}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
