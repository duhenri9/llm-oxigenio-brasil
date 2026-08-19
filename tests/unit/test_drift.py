from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from oxigen.benchmarks.ptbr_intent import load_examples
from oxigen.monitoring.drift import compare_profiles, profile_examples

DATASET = Path("data/benchmarks/ptbr-public-interest-intent-v0.jsonl")


def test_reference_profile_matches_itself() -> None:
    examples = load_examples(DATASET)
    reference = profile_examples(examples, split="eval")

    result = compare_profiles(reference, reference)

    assert result.status == "PASS"
    assert result.label_total_variation == 0.0
    assert result.mean_chars_relative_delta == 0.0
    assert result.mean_tokens_relative_delta == 0.0
    assert result.reasons == []


def test_length_shift_is_detected_as_drift() -> None:
    examples = load_examples(DATASET)
    shifted = [
        replace(example, text=(example.text + " contexto") * 8)
        if example.split == "eval"
        else example
        for example in examples
    ]

    reference = profile_examples(examples, split="eval")
    candidate = profile_examples(shifted, split="eval")
    result = compare_profiles(reference, candidate)

    assert result.status == "DRIFT"
    assert result.mean_chars_relative_delta > result.thresholds["max_mean_chars_delta"]
    assert result.mean_tokens_relative_delta > result.thresholds["max_mean_tokens_delta"]
    assert result.reasons
