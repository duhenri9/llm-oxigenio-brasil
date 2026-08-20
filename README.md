# Oxigênio Brasil

**Portuguese-first open research for auditable data, evaluation and adaptation of language models to Brazilian contexts.**

Oxigênio Brasil is an open-source research initiative focused on Brazilian Portuguese, data governance, model evaluation and responsible adaptation. The project does **not** claim to have trained a Brazilian foundation model yet. Its current public standard is narrower: make assumptions, datasets, evaluation paths and limitations inspectable before larger model claims are made.

> **Current executable milestone:** the repository ships a deterministic PT-BR ML evaluation stack with a versioned synthetic regression suite plus a separately gated, independently sourced OLID-BR benchmark pinned to an explicit dataset revision and licence. CI also exercises machine-readable evidence, drift controls, a small FastAPI surface and a containerised runtime.

## Em português

O **Oxigênio Brasil** é uma iniciativa open-source, Portuguese-first, para construir uma fundação auditável de pesquisa, avaliação e adaptação de modelos de linguagem ao contexto brasileiro.

O projeto ainda não possui um modelo fundacional próprio treinado. Em vez de antecipar esse claim, organiza e executa primeiro critérios de dados, governança, segurança, avaliação e contribuição responsável.

## Veja a esteira executável

Requisitos: Python 3.11+.

```bash
git clone https://github.com/duhenri9/llm-oxigenio-brasil.git
cd llm-oxigenio-brasil
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
oxigen-evidence --out-dir artifacts/ptbr-suite
```

O evidence pack registra:

```text
artifacts/ptbr-suite/
  dataset-manifest.json
  eval-card.md
  evidence-manifest.json
  experiment.json
  metrics.json
  report.html
```

A suíte compara um majority-class control, word TF-IDF + logistic regression e character-boundary TF-IDF + logistic regression sobre o mesmo split congelado. O manifesto final contém SHA-256 dos artefatos para tornar a execução inspecionável.

O benchmark original e estreito continua disponível:

```bash
oxigen-benchmark
```

**Limite do claim:** o dataset v0 é pequeno, sintético e escrito no próprio repositório. Ele serve para provar a esteira reprodutível de ML, avaliação, packaging e monitoramento; suas métricas **não** são evidência de qualidade real de um modelo PT-BR em produção.

Detalhes:

- [`docs/ptbr_public_interest_benchmark.md`](docs/ptbr_public_interest_benchmark.md)
- [`docs/operational-evidence.md`](docs/operational-evidence.md)

## Benchmark externo versionado — OLID-BR

O primeiro gate independente usa **OLID-BR**, um dataset de identificação de linguagem ofensiva em português brasileiro. A integração fixa uma revisão exata da fonte, registra explicitamente a licença **CC BY 4.0**, preserva os splits oficiais `train`/`test` e falha em caso de IDs duplicados ou sobreposição exata de texto entre os splits.

```bash
oxigen-olidbr --out-dir artifacts/olidbr-v1
```

O baseline é deliberadamente simples: word TF-IDF + logistic regression. O evidence pack registra provenance, revisão, licença, SHA-256 dos splits, métricas agregadas e evidência por exemplo usando ID e hash do texto. **O texto bruto do OLID-BR é usado apenas em memória durante a avaliação e não é persistido nos artefatos gerados pelo benchmark.**

Esse resultado responde apenas à tarefa congelada de linguagem ofensiva do OLID-BR. Ele não sustenta claims de cobertura cultural ampla, fairness, segurança, factualidade, representatividade nacional ou qualidade geral de um modelo em português brasileiro.

Detalhes:

- [`docs/olid_br_external_benchmark.md`](docs/olid_br_external_benchmark.md)

## Drift com negative control

O monitor de drift tem semântica explícita `PASS | DRIFT | INDETERMINATE` e compara distribuição de labels, tamanho médio em caracteres e contagem média de tokens.

```bash
oxigen-drift \
  --reference data/benchmarks/ptbr-public-interest-intent-v0.jsonl \
  --candidate data/benchmarks/ptbr-public-interest-intent-v0.jsonl \
  --expect PASS
```

O CI também constrói deliberadamente um dataset deslocado e exige que o monitor retorne `DRIFT`. Um detector que não captura o negative control não é aceito como evidência.

## API e container

```bash
docker build -t oxigenio-evidence .
docker run --rm -p 8000:8000 oxigenio-evidence
```

Superfícies atuais:

- `GET /health`
- `GET /v1/benchmarks`
- `POST /v1/benchmarks/ptbr-intent/run`
- documentação OpenAPI em `/docs`

O CI constrói o container, inicia a API e verifica o health endpoint antes de aceitar a mudança. Isso prova packaging e execução operacional; **não** é um claim de que já exista um serviço público de produção com SLA.

## Norte

O objetivo é construir uma base transparente para experimentar modelos em português brasileiro com critérios claros de dados, avaliação, segurança e governança.

Documentos principais:

- [`docs/research_north_star.md`](docs/research_north_star.md)
- [`docs/roadmap.md`](docs/roadmap.md)
- [`docs/brazilian_domain_strategy.md`](docs/brazilian_domain_strategy.md)
- [`docs/ptbr_public_interest_benchmark.md`](docs/ptbr_public_interest_benchmark.md)
- [`docs/olid_br_external_benchmark.md`](docs/olid_br_external_benchmark.md)
- [`docs/operational-evidence.md`](docs/operational-evidence.md)
- [`docs/references/maritaca_sabia_landscape.md`](docs/references/maritaca_sabia_landscape.md)
- [`HANDOFF.md`](HANDOFF.md)

Landing page pública:

- [`site/index.html`](site/index.html)

## Estado atual

### Executável hoje

- pacote Python instalável em modo de desenvolvimento;
- testes unitários, Ruff e MyPy em CI;
- benchmark determinístico de classificação de texto PT-BR;
- três baselines comparáveis sobre split sintético congelado;
- dataset sintético versionado com manifesto de provenance e limites de uso;
- benchmark externo OLID-BR com fonte/revisão/licença explícitas e splits oficiais preservados;
- evidence pack externo sem persistência do texto bruto da fonte;
- evidence pack sintético com experiment record, métricas, eval card, HTML report e digests;
- monitor de drift com positive e negative controls;
- API FastAPI pequena e documentada;
- imagem Docker construída e smoke-tested em CI;
- componentes experimentais em `src/oxigen/`.

### Ainda não existe — e não é reivindicado

- modelo fundacional Oxigênio treinado;
- dataset nacional final;
- pesos de modelo publicados;
- corpus de treinamento consolidado;
- benchmark oficial representativo do Brasil real ou de múltiplos domínios brasileiros;
- deploy público durável com SLA;
- GPU ou infraestrutura de treinamento comprometida;
- claim de segurança, factualidade, fairness ou cobertura cultural ampla.

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
  monitoring/
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
oxigen-benchmark
oxigen-evidence --out-dir artifacts/ptbr-suite
oxigen-olidbr --out-dir artifacts/olidbr-v1
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
