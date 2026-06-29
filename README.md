# LLM Oxigênio Brasil

**Oxigênio Brasil** é uma iniciativa open-source, Portuguese-first, para construir
uma fundação auditável de pesquisa, avaliação e adaptação de modelos de linguagem
ao contexto brasileiro.

O projeto ainda não tem modelo treinado. Ele organiza primeiro os critérios de
dados, governança, segurança, avaliação e contribuição responsável.

## Norte

O objetivo do projeto é construir uma base transparente para experimentar modelos
de linguagem em português brasileiro, com critérios claros de dados, avaliação,
segurança e governança.

Documentos principais:

- [`docs/research_north_star.md`](docs/research_north_star.md)
- [`docs/brazilian_domain_strategy.md`](docs/brazilian_domain_strategy.md)
- [`HANDOFF.md`](HANDOFF.md)

Landing page pública inicial:

- [`site/index.html`](site/index.html)

## Status

Projeto em fase inicial. Ainda não há modelo treinado, dataset final, pesos
publicados, corpus coletado, benchmark oficial ou GPU provisionada.

## Princípios

- Português brasileiro primeiro.
- Transparência de dados e metodologia.
- Respeito a comunidades, povos indígenas, quilombolas, biomas e conhecimento local.
- Menos código antes da necessidade.
- Avaliação antes de claims públicos.
- Nenhum dado sensível ou privado em datasets públicos.
- Nenhum claim de "100% brasileiro" antes de base, dados, treino, avaliação e licença sustentarem isso.

## Domínios Brasileiros Críticos

| Domínio | Por que importa |
| --- | --- |
| Biomas, Clima e Biodiversidade | Conecta ciência, território, conservação e vida cotidiana. |
| Cidadania, Estado e Direito Público | Ajuda a navegar serviços, direitos e deveres sem substituir fonte oficial. |
| Educação Cívica | Explica instituições, democracia, políticas públicas e participação social. |
| Educação Financeira Responsável | Reduz risco de dívida, golpe e promessa financeira enganosa. |
| Segurança Digital e Golpes | Ajuda usuários a reconhecer fraude, phishing e engenharia social. |
| Conhecimento Regional e Cultura | Valoriza diversidade brasileira com cuidado contra generalização e apropriação. |

Leia a estratégia completa em
[`docs/brazilian_domain_strategy.md`](docs/brazilian_domain_strategy.md).

## Governança

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
site/
  index.html
  styles.css
  main.js
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

## Validação Local

```bash
python -m compileall src
python -m pytest tests/unit/ -v
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src
```

## Modelo Base

Nenhum modelo base foi escolhido de forma irreversível. A escolha de modelo aluno
será definida por benchmark, custo, licença, tooling e qualidade em PT-BR. Modelos
externos poderão ser usados como referência, judge ou baseline, sem decisão
irreversível nesta fase.

Veja [`docs/model_selection_policy.md`](docs/model_selection_policy.md).

## Naming

O nome público do projeto é `Oxigênio Brasil`. Nomes de modelos, como um futuro
`Oxigênio-1`, só devem ser usados quando houver artefato técnico, model card,
eval card, licença e avaliação mínima.

## LP Pública

A LP v0 é estática, editorial e segura por desenho. Ela abre portas para
contribuição futura via GitHub, mas não possui conversa integrada, formulário
próprio, login, upload, coleta de prompts ou uso automático de contribuições para
treinamento.

Para visualizar localmente:

```bash
python -m http.server 8000 --directory site
```

## Apoie O Projeto

Custos futuros incluem curadoria de dados, armazenamento, avaliação, treinamento,
inferência e documentação pública. Valores citados no projeto são estimativas,
não cotações firmes ou garantia de execução.

Veja [`SUPPORT.md`](SUPPORT.md).

## Contato

- GitHub: https://github.com/duhenri9/llm-oxigenio-brasil
