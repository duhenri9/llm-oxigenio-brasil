from __future__ import annotations

import json
from pathlib import Path

import pytest

from oxigen.benchmarks.ptbr_intent import load_examples, run_benchmark, write_result

DATASET = Path("data/benchmarks/ptbr-public-interest-intent-v0.jsonl")


def test_dataset_has_explicit_train_eval_contract() -> None:
    examples = load_examples(DATASET)

    assert len(examples) == 48
    assert {example.split for example in examples} == {"train", "eval"}
    assert len([example for example in examples if example.split == "train"]) == 36
    assert len([example for example in examples if example.split == "eval"]) == 12

    train_labels = {example.label for example in examples if example.split == "train"}
    eval_labels = {example.label for example in examples if example.split == "eval"}
    assert train_labels == eval_labels
    assert len(train_labels) == 6


def test_benchmark_emits_inspectable_deterministic_evidence(tmp_path: Path) -> None:
    first = run_benchmark(DATASET)
    second = run_benchmark(DATASET)

    assert first.to_dict() == second.to_dict()
    assert first.train_examples == 36
    assert first.eval_examples == 12
    assert len(first.predictions) == 12
    assert 0.0 <= first.accuracy <= 1.0
    assert 0.0 <= first.macro_f1 <= 1.0
    assert len(first.dataset_sha256) == 64
    assert "not a claim" in first.claim_boundary.lower()

    output = tmp_path / "benchmark.json"
    write_result(first, output)
    payload = json.loads(output.read_text(encoding="utf-8"))

    assert payload["benchmark"] == "ptbr-public-interest-intent"
    assert payload["benchmark_version"] == "0.1.0"
    assert payload["dataset_sha256"] == first.dataset_sha256
    assert len(payload["predictions"]) == 12


def test_loader_rejects_duplicate_text_across_splits(tmp_path: Path) -> None:
    fixture = tmp_path / "invalid.jsonl"
    fixture.write_text(
        "\n".join(
            [
                json.dumps({"id": "a", "text": "texto duplicado", "label": "x", "split": "train"}),
                json.dumps({"id": "b", "text": "texto duplicado", "label": "x", "split": "eval"}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="duplicate text"):
        load_examples(fixture)
