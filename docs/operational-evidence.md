# Operational ML evidence

Oxigênio Brasil separates **pipeline evidence** from **real-world model claims**.

The current operational slice is deliberately small enough to run in CI and inspect end to end. It exists to prove that the repository can execute, compare, package and serve an ML evaluation workflow without presenting a synthetic fixture as market- or research-grade model quality evidence.

## Evidence path

```text
versioned dataset
    ↓
validation + SHA-256
    ↓
three deterministic baselines
    ↓
accuracy + macro F1 + confusion matrices + per-example predictions
    ↓
experiment.json / metrics.json / eval-card.md / report.html
    ↓
evidence-manifest.json with artifact digests
    ↓
CI artifact
```

Run locally:

```bash
python -m pip install -e ".[dev]"
oxigen-evidence \
  --dataset data/benchmarks/ptbr-public-interest-intent-v0.jsonl \
  --source-manifest data/benchmarks/ptbr-public-interest-intent-v0.manifest.json \
  --out-dir artifacts/ptbr-suite
```

The suite compares:

1. a majority-class control;
2. word TF-IDF + logistic regression;
3. character-boundary TF-IDF + logistic regression.

These baselines are intentionally inexpensive and deterministic. Their purpose is to make the evaluation machinery falsifiable and reproducible before more expensive model/provider comparisons are promoted.

## Drift contract

`oxigen-drift` compares the requested dataset split using:

- total variation distance for the label distribution;
- relative change in mean character length;
- relative change in mean whitespace-token count.

The result vocabulary is explicit:

- `PASS` — all monitored metrics remain within configured bounds;
- `DRIFT` — at least one metric exceeds its bound;
- `INDETERMINATE` — the requested reference or candidate split has no examples.

CI executes both a positive control (the frozen dataset compared with itself must `PASS`) and a deliberately shifted negative control (material text-length inflation must produce `DRIFT`). A monitor that cannot detect the negative control is not accepted as evidence.

## API and container contract

The repository ships a small FastAPI surface:

- `GET /health` — liveness;
- `GET /v1/benchmarks` — current benchmark catalog and claim scope;
- `POST /v1/benchmarks/ptbr-intent/run` — execute the deterministic suite over the bundled fixture.

Container run:

```bash
docker build -t oxigenio-evidence .
docker run --rm -p 8000:8000 oxigenio-evidence
```

Interactive OpenAPI documentation is then available from the FastAPI application at `/docs`.

CI must build the image, start the container and verify `/health` before merge. This is an operational packaging check, not a claim that a durable public production deployment already exists.

## Current claim boundary

The bundled `ptbr-public-interest-intent-v0` data is repository-authored and synthetic. It is test equipment for:

- evaluation plumbing;
- reproducibility;
- baseline comparison;
- evidence packaging;
- drift monitoring;
- API/container execution.

It does **not** establish real-world Brazilian Portuguese quality, safety, fairness, regional coverage or production readiness.

## External benchmark promotion gate

A future benchmark may support real PT-BR quality claims only after all of the following are recorded and reviewed:

1. independently sourced dataset;
2. explicit, verified reuse/license terms compatible with the repository and intended use;
3. source URI and immutable source revision/digest where available;
4. documented preprocessing and frozen train/eval/test policy;
5. PII/sensitive-content review;
6. task-specific metrics and baseline rationale;
7. reproducible execution in CI or a separately documented reproducible compute environment;
8. model/provider versions and cost/latency evidence where applicable;
9. error analysis and limitations;
10. a separately versioned claim/evidence contract.

A public dataset being downloadable is not by itself sufficient evidence that redistribution or benchmark promotion is appropriate.
