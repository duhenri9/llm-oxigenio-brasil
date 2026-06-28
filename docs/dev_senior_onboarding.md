# Onboarding Para Dev Senior

Este documento traduz a disciplina usada no E-merge.ia Workspace para o LLM Oxigenio Brasil.

## Regra Principal

Antes de implementar, passar por tres filtros:

1. Filtro de Impacto: que camada muda?
2. Ponytail Audit: isso precisa existir agora?
3. North Star: isso aproxima o projeto de pesquisa aberta, segura e Portuguese-first?

## Fluxo De Trabalho

1. Ler `docs/research_north_star.md`.
2. Classificar a entrada: dados, treinamento, avaliacao, inferencia, governanca, funding ou documentacao.
3. Escrever escopo curto.
4. Separar dentro e fora do escopo.
5. Implementar o menor passo verificavel.
6. Rodar validacoes.
7. Devolver veredito, evidencias, riscos e proximo passo.

## Guardrails

- Nao adicionar dependencia sem necessidade.
- Nao comitar dataset grande.
- Nao comitar checkpoint/modelo.
- Nao publicar dados sensiveis.
- Nao prometer benchmark sem avaliacao.
- Nao usar conhecimento tradicional sem revisar contexto e consentimento.
- Nao misturar pesquisa, fundraising e claims comerciais sem transparencia.

## Primeiros PRs Recomendados

PR1:

- fechar base documental;
- compilar pacote;
- validar modulo `thinking`;
- revisar funding antes de campanha publica.

PR2:

- criar `data_pipeline/` com manifestos, licencas e filtros;
- definir formato de metadados inspirado em Dolma/OLMo;
- documentar rejeicoes de dados.

PR3:

- criar avaliacao inicial PT-BR;
- mapear Assin2, HateBR e benchmarks linguisticos;
- definir metricas antes de treinamento.
