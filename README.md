# LLM Oxigenio Brasil

Modelo aberto, Portuguese-first, pensado para pesquisa aplicada em linguagem, biodiversidade, educacao, cultura brasileira e soberania tecnica.

## Norte

O objetivo do projeto e construir uma base transparente para experimentar modelos de linguagem em portugues brasileiro, com criterios claros de dados, avaliacao, seguranca e governanca.

O documento principal do projeto e:

- [`docs/research_north_star.md`](docs/research_north_star.md)

Para retomada tecnica por Tech Lead ou Dev Senior, leia tambem:

- [`HANDOFF.md`](HANDOFF.md)

## Principios

- Portugues brasileiro primeiro.
- Transparencia de dados e metodologia.
- Respeito a comunidades, povos indigenas, quilombolas, biomas e conhecimento local.
- Menos codigo antes da necessidade.
- Avaliacao antes de claims publicos.
- Nenhum dado sensivel ou privado em datasets publicos.

## Estrutura Inicial

```txt
docs/
  research_north_star.md
  dev_senior_onboarding.md
src/oxigen/
  training/thinking/
    endangered_species.py
    vocabulary.py
    composer.py
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
python -m pytest
```

## Apoie O Projeto

Custos futuros incluem curadoria de dados, armazenamento, avaliacao, treinamento, inferencia e documentacao publica.

Veja [`SUPPORT.md`](SUPPORT.md).

## Status

Projeto em fase inicial. Ainda nao ha modelo treinado, dataset final, pesos publicados ou benchmark oficial.

## Contato

- GitHub: https://github.com/duhenri9/llm-oxigenio-brasil
