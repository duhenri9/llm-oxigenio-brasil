from __future__ import annotations

import hashlib
import json
from pathlib import Path

from oxigen.benchmarks.suite import run_suite, write_evidence_pack

DATASET = Path("data/benchmarks/ptbr-public-interest-intent-v0.jsonl")
SOURCE_MANIFEST = Path("data/benchmarks/ptbr-public-interest-intent-v0.manifest.json")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_suite_compares_three_deterministic_baselines() -> None:
    first = run_suite(DATASET)
    second = run_suite(DATASET)

    assert first.to_dict() == second.to_dict()
    assert first.train_examples == 36
    assert first.eval_examples == 12
    assert [model.model_id for model in first.models] == [
        "majority-class",
        "tfidf-word-logreg",
        "tfidf-char-logreg",
    ]
    assert all(0.0 <= model.accuracy <= 1.0 for model in first.models)
    assert all(0.0 <= model.macro_f1 <= 1.0 for model in first.models)
    assert all(len(model.predictions) == 12 for model in first.models)
    assert "not evidence" in first.claim_boundary.lower()


def test_evidence_pack_has_verified_digests(tmp_path: Path) -> None:
    result = run_suite(DATASET)
    output_dir = tmp_path / "evidence"
    paths = write_evidence_pack(
        result,
        output_dir=output_dir,
        source_manifest_path=SOURCE_MANIFEST,
    )

    expected = {
        "dataset-manifest.json",
        "eval-card.md",
        "experiment.json",
        "metrics.json",
        "report.html",
        "evidence-manifest.json",
    }
    assert {path.name for path in paths} == expected

    manifest = json.loads((output_dir / "evidence-manifest.json").read_text(encoding="utf-8"))
    assert manifest["schema"] == "oxigenio-evidence-manifest.v1"
    for name, digest in manifest["files"].items():
        assert _sha256(output_dir / name) == digest

    experiment = json.loads((output_dir / "experiment.json").read_text(encoding="utf-8"))
    assert experiment["suite"] == "ptbr-public-interest-intent-suite"
    assert len(experiment["models"]) == 3
