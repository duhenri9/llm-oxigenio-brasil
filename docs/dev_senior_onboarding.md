# Onboarding Para Dev Senior

Este documento traduz a disciplina usada no E-merge.ia Workspace para o LLM Oxigênio Brasil.

## Regra Principal

Antes de implementar, passar por três filtros:

1. Filtro de Impacto: que camada muda?
2. Ponytail Audit: isso precisa existir agora?
3. North Star: isso aproxima o projeto de pesquisa aberta, segura e Portuguese-first?

## Fluxo De Trabalho

1. Ler `docs/research_north_star.md`.
2. Classificar a entrada: dados, treinamento, avaliação, inferência, governança, funding ou documentação.
3. Escrever escopo curto.
4. Separar dentro e fora do escopo.
5. Implementar o menor passo verificável.
6. Rodar validações.
7. Devolver veredito, evidências, riscos e próximo passo.

## Guardrails

- Não adicionar dependência sem necessidade.
- Não comitar dataset grande.
- Não comitar checkpoint/modelo.
- Não publicar dados sensíveis.
- Não prometer benchmark sem avaliação.
- Não usar conhecimento tradicional sem revisar contexto e consentimento.
- Não misturar pesquisa, fundraising e claims comerciais sem transparência.

## Primeiros PRs Recomendados

PR1:

- fechar base documental;
- compilar pacote;
- validar módulo `thinking`;
- revisar funding antes de campanha pública.

PR2:

- criar `data_pipeline/` com manifestos, licenças e filtros;
- definir formato de metadados inspirado em Dolma/OLMo;
- documentar rejeições de dados.

PR3:

- criar avaliação inicial PT-BR;
- mapear Assin2, HateBR e benchmarks linguísticos;
- definir métricas antes de treinamento.
