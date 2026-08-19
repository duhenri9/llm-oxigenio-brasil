"""Small operational API for inspecting and executing Oxigênio benchmark evidence."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from oxigen.benchmarks.suite import SUITE_NAME, SUITE_VERSION, run_suite

DATASET_PATH = Path(
    os.environ.get(
        "OXIGEN_DATASET_PATH",
        "data/benchmarks/ptbr-public-interest-intent-v0.jsonl",
    )
)

app = FastAPI(
    title="Oxigênio Brasil Evidence API",
    description=(
        "Operational surface for reproducible PT-BR benchmark evidence. "
        "The bundled benchmark fixture is synthetic and does not establish "
        "real-world model quality."
    ),
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    service: str


class BenchmarkDescriptor(BaseModel):
    id: str
    version: str
    dataset_kind: str
    claim_scope: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="oxigenio-evidence-api")


@app.get("/v1/benchmarks", response_model=list[BenchmarkDescriptor])
def benchmarks() -> list[BenchmarkDescriptor]:
    return [
        BenchmarkDescriptor(
            id=SUITE_NAME,
            version=SUITE_VERSION,
            dataset_kind="repository-authored synthetic fixture",
            claim_scope="evaluation-pipeline and reproducibility evidence only",
        )
    ]


@app.post("/v1/benchmarks/ptbr-intent/run")
def run_ptbr_intent() -> dict[str, Any]:
    """Execute the deterministic benchmark suite against the bundled frozen fixture."""

    return run_suite(DATASET_PATH).to_dict()
