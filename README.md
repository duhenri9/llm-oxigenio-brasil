# Oxigênio Brasil

**Portuguese-first open research for auditable data, evaluation and adaptation of language models to Brazilian contexts.**

Oxigênio Brasil is an open-source research initiative focused on Brazilian Portuguese, data governance, model evaluation and responsible adaptation. The project does **not** claim to have trained a Brazilian foundation model yet. Its current public standard is narrower: make assumptions, datasets, evaluation paths and limitations inspectable before larger model claims are made.

> **Current executable milestone:** the repository now ships a deterministic PT-BR machine-learning benchmark vertical slice with a versioned synthetic dataset, frozen train/eval splits, a TF-IDF + logistic-regression baseline, metrics, per-example predictions, dataset SHA-256 evidence, tests and CI.

## Em português

O **Oxigênio Brasil** é uma iniciativa open-source, Portuguese-first, para construir uma fundação auditável de pesquisa, avaliação e adaptação de modelos de linguagem ao contexto brasileiro.

O projeto ainda não possui um modelo fundacional próprio treinado. Em vez de antecipar esse claim, organiza e executa primeiro critérios de dados, governança, segurança, avaliação e contribuição responsável.

## Veja uma execução de ML real

Requisitos: Python 3.11+.

```bash
git clone https://github.com/duhenri9/llm-oxigenio-brasil.git
cd llm-oxigenio-brasil
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m oxigen.benchmarks.ptbr_intent
```

A execução produz um artefato JSON inspecionável em:

```text
artifacts/ptbr-public-interest-intent-v0.json
```

Esse artefato registra a identidade exata do benchmark, SHA-256 do dataset, configuração do baseline, métricas, matriz de confusão e previsões individuais da avaliação.

**Limite do claim:** o dataset v0 é pequeno, sintético e escrito no próprio repositório. Ele serve para provar a esteira reprodutível de ML e avaliação; suas métricas **não** são evidência de qualidade real de um modelo PT-BR em produção.

Detalhes: [`docs/ptbr_public_interest_benchmark.md`](docs/ptbr_public_interest_benchmark.md).

## Norte

O objetivo é construir uma base transparente para experimentar modelos em português brasileiro com critérios claros de dados, avaliação, segurança e governança.

Documentos principais:

- [`docs/research_north_star.md`](docs/research_north_star.md)
- [`docs/roadmap.md`](docs/roadmap.md)
- [`docs/brazilian_domain_strategy.md`](docs/brazilian_domain_strategy.md)
- [`docs/ptbr_public_interest_benchmark.md`](docs/ptbr_public_interest_benchmark.md)
- [`docs/references/maritaca_sabia_landscape.md`](docs/references/maritaca_sabia_landscape.md)
- [`HANDOFF.md`](HANDOFF.md)

Landing page pública:

- [`site/index.html`](site/index.html)

## Estado atual

### Executável hoje

- pacote Python instalável em modo de desenvolvimento;
- testes unitários, Ruff e MyPy em CI;
- benchmark determinístico de classificação de texto PT-BR;
- dataset sintético versionado com manifesto de provenance e limites de uso;
- geração de evidência JSON reproduzível;
- componentes experimentais em `src/oxigen/`.

### Ainda não existe — e não é reivindicado

- modelo fundacional Oxigênio treinado;
- dataset nacional final;
- pesos de modelo publicados;
- corpus de treinamento consolidado;
- benchmark oficial representativo do Brasil real;
- GPU ou infraestrutura de treinamento comprometida;
- claim de segurança, factualidade ou cobertura cultural ampla.

## Princípios

- Português brasileiro primeiro.
- Evidência executável antes de claims públicos.
- Transparência de dados e metodologia.
- Respeito a comunidades, povos indígenas, quilombolas, biomas e conhecimento local.
- Avaliação antes de escala.
- Nenhum dado sensível ou privado em datasets públicos.
- Nenhum claim de "100% brasileiro" antes de base, dados, treino, avaliação e licença sustentarem isso.

## Domínios brasileiros críticos

| Domínio | Por que importa |
| --- | --- |
| Biomas, Clima e Biodiversidade | Conecta ciência, território, conservação e vida cotidiana. |
| Cidadania, Estado e Direito Público | Ajuda a navegar serviços, direitos e deveres sem substituir fonte oficial. |
| Educação Cívica | Explica instituições, democracia, políticas públicas e participação social. |
| Educação Financeira Responsável | Reduz risco de dívida, golpe e promessa financeira enganosa. |
| Segurança Digital e Golpes | Ajuda usuários a reconhecer fraude, phishing e engenharia social. |
| Conhecimento Regional e Cultura | Valoriza diversidade brasileira com cuidado contra generalização e apropriação. |

Leia [`docs/brazilian_domain_strategy.md`](docs/brazilian_domain_strategy.md).

## Governança e avaliação

- [`SECURITY.md`](SECURITY.md)
- [`docs/data_source_manifest.md`](docs/data_source_manifest.md)
- [`docs/data_rejection_policy.md`](docs/data_rejection_policy.md)
- [`docs/pii_sensitive_data_policy.md`](docs/pii_sensitive_data_policy.md)
- [`docs/model_selection_policy.md`](docs/model_selection_policy.md)
- [`docs/model_card_template.md`](docs/model_card_template.md)
- [`docs/eval_card_template.md`](docs/eval_card_template.md)
- [`docs/benchmark_plan_ptbr.md`](docs/benchmark_plan_ptbr.md)
- [`docs/roadmap.md`](docs/roadmap.md)
- [`data/benchmarks/ptbr-public-interest-intent-v0.manifest.json`](data/benchmarks/ptbr-public-interest-intent-v0.manifest.json)

## Estrutura

```text
data/
  benchmarks/
  metadata/
docs/
site/
src/oxigen/
  benchmarks/
  training/
tests/
  unit/
```

## Validação local

```bash
python -m compileall src
python -m pytest tests/unit/ -v
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src
python -m oxigen.benchmarks.ptbr_intent
```

## Modelo base

Nenhum modelo base foi escolhido de forma irreversível. A escolha de futuros modelos será definida por benchmark, custo, licença, tooling e qualidade em PT-BR. Modelos externos podem atuar como referência, judge ou baseline sem se tornarem automaticamente o produto do projeto.

Veja [`docs/model_selection_policy.md`](docs/model_selection_policy.md).

## Naming

O nome público do projeto é **Oxigênio Brasil**. Nomes de modelos, como um futuro `Oxigênio-1`, só devem ser usados quando houver artefato técnico, model card, eval card, licença e avaliação mínima que sustentem o nome.

## Contribuição

Comece por [`CONTRIBUTING.md`](CONTRIBUTING.md). Para benchmarks novos, preserve provenance, licença, split reproduzível, baseline exato, limitações e evidência executável.

## Apoie o projeto

Custos futuros incluem curadoria de dados, armazenamento, avaliação, treinamento, inferência e documentação pública. Valores citados no projeto são estimativas, não cotações firmes ou garantia de execução.

Veja [`SUPPORT.md`](SUPPORT.md).

## Contato

GitHub: https://github.com/duhenri9/llm-oxigenio-brasil
