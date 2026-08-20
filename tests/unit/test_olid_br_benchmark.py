from __future__ import annotations

import json
from pathlib import Path

import pytest

from oxigen.benchmarks.olid_br import run_external_benchmark, write_evidence_pack


def _rows() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    train = [
        {"id": "t1", "text": "Que atendimento excelente e educado", "is_offensive": "NOT"},
        {"id": "t2", "text": "Obrigado pela ajuda, resolveu meu problema", "is_offensive": "NOT"},
        {"id": "t3", "text": "A conversa foi tranquila e respeitosa", "is_offensive": "NOT"},
        {"id": "t4", "text": "Gostei muito da explicação apresentada", "is_offensive": "NOT"},
        {"id": "t5", "text": "Seu idiota, pare de falar besteira", "is_offensive": "OFF"},
        {"id": "t6", "text": "Que comentário imbecil e ofensivo", "is_offensive": "OFF"},
        {"id": "t7", "text": "Você é um babaca sem noção", "is_offensive": "OFF"},
        {"id": "t8", "text": "Cala a boca, seu trouxa", "is_offensive": "OFF"},
    ]
    test = [
        {"id": "e1", "text": "A resposta foi clara e gentil", "is_offensive": "NOT"},
        {"id": "e2", "text": "Muito obrigado pelo suporte", "is_offensive": "NOT"},
        {"id": "e3", "text": "Seu comentário é idiota", "is_offensive": "OFF"},
        {"id": "e4", "text": "Que babaca sem educação", "is_offensive": "OFF"},
    ]
    return train, test


def test_external_benchmark_is_deterministic_and_redacted(tmp_path: Path) -> None:
    train, test = _rows()
    first_manifest, first_result = run_external_benchmark(train, test)
    second_manifest, second_result = run_external_benchmark(train, test)

    assert first_manifest == second_manifest
    assert first_result.metrics_dict() == second_result.metrics_dict()
    assert first_manifest.raw_text_persisted is False
    assert first_manifest.duplicate_ids == 0
    assert first_manifest.cross_split_text_duplicates == 0
    assert len(first_manifest.dataset_sha256) == 64
    assert len(first_result.predictions) == len(test)

    output = tmp_path / "evidence"
    write_evidence_pack(output, first_manifest, first_result)

    expected = {
        "dataset-manifest.json",
        "eval-card.md",
        "evidence-digests.json",
        "experiment.json",
        "metrics.json",
        "predictions.jsonl",
        "report.txt",
    }
    assert {path.name for path in output.iterdir()} == expected

    persisted = "\n".join(path.read_text(encoding="utf-8") for path in output.iterdir())
    for row in train + test:
        assert row["text"] not in persisted

    manifest = json.loads((output / "dataset-manifest.json").read_text(encoding="utf-8"))
    digests = json.loads((output / "evidence-digests.json").read_text(encoding="utf-8"))
    assert manifest["licence"] == "CC BY 4.0"
    assert len(digests["pack_sha256"]) == 64
    assert set(digests["files"]) == expected - {"evidence-digests.json"}


def test_cross_split_text_overlap_fails_closed() -> None:
    train, test = _rows()
    test[0]["text"] = train[0]["text"]

    with pytest.raises(ValueError, match="exact text overlap"):
        run_external_benchmark(train, test)


def test_duplicate_id_fails_closed() -> None:
    train, test = _rows()
    test[0]["id"] = train[0]["id"]

    with pytest.raises(ValueError, match="duplicate ids"):
        run_external_benchmark(train, test)
