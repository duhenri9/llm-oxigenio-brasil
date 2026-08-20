# OLID-BR external benchmark v1

Oxigênio Brasil uses OLID-BR as its first independently sourced PT-BR benchmark gate. This benchmark is deliberately separate from the repository-authored synthetic `ptbr-public-interest-intent` fixture, which remains deterministic regression and failure-control equipment.

## Source identity and reuse terms

- Canonical project: **OLID-BR — Offensive Language Identification Dataset for Brazilian Portuguese**.
- Publisher/maintainer: Douglas Trajano and collaborators.
- Canonical source repository: <https://github.com/DougTrajano/olid-br>.
- Dataset distribution used by this gate: <https://huggingface.co/datasets/dougtrajano/olid-br>.
- Frozen dataset revision: `84b0d7dd4309be677a47c535632a9398ff1897bd`.
- Dataset licence: **Creative Commons Attribution 4.0 International (CC BY 4.0)**, as declared by the canonical OLID-BR repository.
- Source-code licence in the OLID-BR repository is Apache-2.0; this is distinct from the dataset licence.

The benchmark does not assume that public availability implies redistribution permission. The source licence is recorded explicitly and raw OLID-BR rows are not committed to this repository.

## Task and processing contract

The v1 task is binary offensive-language identification using the published `is_offensive` field:

- `OFF` — offensive;
- `NOT` — not offensive.

The official `train` and `test` splits from the frozen source revision are preserved. Oxigênio does not resample or optimise a new split for a more favourable score.

Before training, the adapter validates:

1. non-empty string IDs and texts;
2. the expected binary label vocabulary;
3. unique IDs across the two official splits;
4. exact text-hash overlap across train and test;
5. presence of both expected labels in both splits.

Any violated invariant fails the benchmark instead of silently repairing the source data. The manifest records exact train/test counts, per-split SHA-256 identities and a combined dataset identity bound to the frozen revision.

## Baseline protocol

The first baseline is intentionally simple:

- `TfidfVectorizer`, word 1–2 grams, lower-cased, sub-linear term frequency;
- `LogisticRegression`, `lbfgs`, `max_iter=1000`, `random_state=0`;
- accuracy, macro-F1, confusion matrix and per-label precision/recall/F1/support;
- per-example prediction evidence by source ID and source-text SHA-256.

This gives the project a reproducible baseline before adding larger or model-provider-specific systems.

## Privacy and persistence boundary

OLID-BR contains social-media/offensive-language material. The benchmark may therefore encounter abusive, discriminatory or otherwise sensitive text. For this gate:

- source text is loaded only in memory for vectorisation/evaluation;
- raw source rows are not copied into this repository;
- raw text is not written into the evidence pack;
- per-example evidence stores ID, text SHA-256, expected label, predicted label and correctness only;
- aggregate metrics and dataset identities remain inspectable without redistributing source text.

Hashing source text is an identity mechanism, not anonymisation. A party that already possesses a candidate text could test it against a hash. For that reason, the evidence pack should still be handled as research evidence rather than as a privacy guarantee.

## Evidence pack

`oxigen-olidbr` writes:

- `dataset-manifest.json` — source, revision, licence, counts, split identities and leakage checks;
- `experiment.json` — benchmark/model/source identity;
- `metrics.json` — aggregate and per-label metrics;
- `predictions.jsonl` — IDs/hashes/labels only, no source text;
- `eval-card.md` — operator-readable task, result and limitation summary;
- `report.txt` — compact operator report;
- `evidence-digests.json` — SHA-256 for every evidence file plus pack digest.

## Claim boundary

A score from this gate means only: the declared deterministic baseline was evaluated on the frozen OLID-BR offensive-language task under the documented processing contract.

It is **not** evidence of broad Brazilian Portuguese quality, cultural representativeness, fairness, toxicity safety, instruction following, factuality, production fitness or generalisation to other populations/domains. Those require separate datasets, protocols and evidence gates.

## Attribution

When using or publishing results from this benchmark, retain attribution to the OLID-BR project and its dataset licence. Consult the canonical project for the dataset's preferred academic citation and any updated attribution guidance.
