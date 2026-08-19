# Executable PT-BR ML Benchmark

This repository now includes one deliberately narrow, reproducible machine-learning vertical slice.

The goal is not to claim that Oxigênio Brasil has trained a production language model. The goal is to make the project's data and evaluation discipline executable: a versioned dataset, explicit splits, a deterministic baseline, inspectable metrics, machine-readable evidence, tests and CI.

## What runs

The benchmark classifies short Brazilian Portuguese public-interest queries into six repository-defined domains:

- biodiversidade
- cidadania
- cultura_regional
- educacao_civica
- financas
- seguranca_digital

The current fixture is repository-authored and synthetic. It contains 48 records: 36 frozen training examples and 12 frozen evaluation examples.

## Run locally

```bash
python -m pip install -e ".[dev]"
python -m oxigen.benchmarks.ptbr_intent \
  --dataset data/benchmarks/ptbr-public-interest-intent-v0.jsonl \
  --out artifacts/ptbr-public-interest-intent-v0.json
```

Or use the installed CLI:

```bash
oxigen-benchmark
```

The output records:

- exact benchmark name and version;
- SHA-256 of the dataset bytes;
- model family and configuration;
- train/eval counts;
- ordered label set;
- accuracy and macro F1;
- confusion matrix;
- one inspectable prediction record per evaluation example;
- an explicit claim boundary.

## Why the dataset is synthetic

This first slice is test equipment for the ML pipeline itself. Using repository-authored data keeps provenance and licensing unambiguous while the project establishes the execution contract.

A strong metric on this fixture must **not** be interpreted as real-world PT-BR quality. The fixture is small, authored by the repository, does not represent natural traffic and does not establish regional, demographic, dialect, robustness, factuality or safety coverage.

The manifest is stored at:

`data/benchmarks/ptbr-public-interest-intent-v0.manifest.json`

## Promotion rule for future benchmarks

A future external/public dataset should not replace this benchmark silently. It should be added as a separately versioned adapter with:

1. source and license recorded before ingestion;
2. immutable or content-addressed dataset identity;
3. documented preprocessing;
4. contamination/leakage checks appropriate to the dataset;
5. frozen evaluation split or a reproducible split rule;
6. baseline configuration recorded exactly;
7. metrics and per-example evidence where licensing permits;
8. known limitations and excluded claims;
9. CI or a reproducible execution path;
10. an eval card tied to the exact evidence artifact.

## Next technical gate

The next meaningful promotion is not a larger synthetic score. It is one independently sourced, legally reusable PT-BR benchmark with a documented adapter, provenance, baseline comparison and repeatable evidence artifact.
