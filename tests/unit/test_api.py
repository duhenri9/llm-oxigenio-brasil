from __future__ import annotations

from fastapi.testclient import TestClient

from oxigen.api import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "oxigenio-evidence-api"}


def test_benchmark_catalog_preserves_claim_boundary() -> None:
    response = client.get("/v1/benchmarks")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 1
    assert payload[0]["id"] == "ptbr-public-interest-intent-suite"
    assert "synthetic" in payload[0]["dataset_kind"]


def test_benchmark_run_returns_three_baselines() -> None:
    response = client.post("/v1/benchmarks/ptbr-intent/run")

    assert response.status_code == 200
    payload = response.json()
    assert payload["suite"] == "ptbr-public-interest-intent-suite"
    assert len(payload["models"]) == 3
    assert len(payload["dataset_sha256"]) == 64
    assert "not evidence" in payload["claim_boundary"].lower()
