# LLM Oxigenio Brasil

**Oxigenio Brasil** e uma iniciativa open-source, Portuguese-first, para construir
uma fundacao auditavel de pesquisa, avaliacao e adaptacao de modelos de linguagem
ao contexto brasileiro.

O projeto ainda nao tem modelo treinado. Ele organiza primeiro os criterios de
dados, governanca, seguranca, avaliacao e contribuicao responsavel.

## Norte

O objetivo do projeto e construir uma base transparente para experimentar modelos
de linguagem em portugues brasileiro, com criterios claros de dados, avaliacao,
seguranca e governanca.

Documentos principais:

- [`docs/research_north_star.md`](docs/research_north_star.md)
- [`docs/brazilian_domain_strategy.md`](docs/brazilian_domain_strategy.md)
- [`HANDOFF.md`](HANDOFF.md)

## Status

Projeto em fase inicial. Ainda nao ha modelo treinado, dataset final, pesos
publicados, corpus coletado, benchmark oficial ou GPU provisionada.

## Principios

- Portugues brasileiro primeiro.
- Transparencia de dados e metodologia.
- Respeito a comunidades, povos indigenas, quilombolas, biomas e conhecimento local.
- Menos codigo antes da necessidade.
- Avaliacao antes de claims publicos.
- Nenhum dado sensivel ou privado em datasets publicos.
- Nenhum claim de "100% brasileiro" antes de base, dados, treino, avaliacao e licenca sustentarem isso.

## Dominios Brasileiros Criticos

| Dominio | Por que importa |
| --- | --- |
| Biomas, Clima e Biodiversidade | Conecta ciencia, territorio, conservacao e vida cotidiana. |
| Cidadania, Estado e Direito Publico | Ajuda a navegar servicos, direitos e deveres sem substituir fonte oficial. |
| Educacao Civica | Explica instituicoes, democracia, politicas publicas e participacao social. |
| Educacao Financeira Responsavel | Reduz risco de divida, golpe e promessa financeira enganosa. |
| Seguranca Digital e Golpes | Ajuda usuarios a reconhecer fraude, phishing e engenharia social. |
| Conhecimento Regional e Cultura | Valoriza diversidade brasileira com cuidado contra generalizacao e apropriacao. |

Leia a estrategia completa em
[`docs/brazilian_domain_strategy.md`](docs/brazilian_domain_strategy.md).

## Governanca

- [`SECURITY.md`](SECURITY.md)
- [`docs/data_source_manifest.md`](docs/data_source_manifest.md)
- [`docs/data_rejection_policy.md`](docs/data_rejection_policy.md)
- [`docs/pii_sensitive_data_policy.md`](docs/pii_sensitive_data_policy.md)
- [`docs/model_selection_policy.md`](docs/model_selection_policy.md)
- [`docs/model_card_template.md`](docs/model_card_template.md)
- [`docs/eval_card_template.md`](docs/eval_card_template.md)
- [`docs/benchmark_plan_ptbr.md`](docs/benchmark_plan_ptbr.md)
- [`docs/financial_report.md`](docs/financial_report.md)
- [`data/metadata/README.md`](data/metadata/README.md)

## Estrutura Inicial

```txt
docs/
  research_north_star.md
  brazilian_domain_strategy.md
  data_source_manifest.md
  benchmark_plan_ptbr.md
data/
  metadata/
src/oxigen/
  training/thinking/
    endangered_species.py
    vocabulary.py
    composer.py
tests/
  unit/
```

## Instalar Para Desenvolvimento

```bash
git clone https://github.com/duhenri9/llm-oxigenio-brasil.git
cd llm-oxigenio-brasil
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Validacao Local

```bash
python -m compileall src
python -m pytest tests/unit/ -v
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src
```

## Modelo Base

Nenhum modelo base foi escolhido de forma irreversivel. A escolha de modelo aluno
sera definida por benchmark, custo, licenca, tooling e qualidade em PT-BR. Modelos
externos poderao ser usados como referencia, judge ou baseline, sem decisao
irreversivel nesta fase.

Veja [`docs/model_selection_policy.md`](docs/model_selection_policy.md).

## Apoie O Projeto

Custos futuros incluem curadoria de dados, armazenamento, avaliacao, treinamento,
inferencia e documentacao publica. Valores citados no projeto sao estimativas,
nao cotacoes firmes ou garantia de execucao.

Veja [`SUPPORT.md`](SUPPORT.md).

## Contato

- GitHub: https://github.com/duhenri9/llm-oxigenio-brasil
