# Contribuindo

Obrigado por considerar contribuir com o LLM Oxigenio Brasil.

Este projeto e Portuguese-first. Issues, PRs, comentarios de codigo, docstrings e commits devem priorizar portugues claro. Ingles tecnico e bem-vindo quando ajudar precisao, especialmente em nomes de papers, bibliotecas e termos estabelecidos.

## Antes De Escrever Codigo

Use este filtro:

1. Isso precisa existir agora?
2. Ja existe algo parecido no repo?
3. Uma documentacao ou checklist resolve?
4. A biblioteca padrao resolve?
5. Uma dependencia ja instalada resolve?
6. A solucao pode ser menor?
7. Isso preserva seguranca, validacao, ownership, acessibilidade e dados?

Se a resposta nao for clara, abra uma issue ou proposta curta antes de implementar.

## North Star

Leia antes de propor mudancas grandes:

- [`docs/research_north_star.md`](docs/research_north_star.md)
- [`docs/dev_senior_onboarding.md`](docs/dev_senior_onboarding.md)

## Dados

Qualquer contribuicao de dados deve indicar:

- origem;
- licenca;
- data de coleta;
- idioma/dialeto;
- criterios de filtragem;
- riscos conhecidos;
- se contem dados pessoais ou sensiveis;
- se envolve conhecimento tradicional, indigena, quilombola ou territorial.

FineWeb, Dolma, OLMo e pipelines similares servem como referencias de transparencia, metadados e filtros, nao como autorizacao para copiar dados sem revisar licenca e contexto.

## Commits

Prefira mensagens curtas em portugues:

```txt
docs: adiciona norte de pesquisa
feat: adiciona vocabulos de raciocinio
fix: corrige composicao de exemplo
```

## PRs

Todo PR deve explicar:

- o que mudou;
- por que precisa existir;
- como foi validado;
- riscos;
- o que ficou fora de escopo.

## Codigo

- Escreva funcoes pequenas.
- Use tipos quando ajudarem leitura.
- Evite dependencia nova sem justificativa.
- Nao comite datasets grandes, modelos, checkpoints ou `.env`.
- Nao inclua segredos, tokens, chaves privadas ou dados reais sensiveis.
