# Contribuindo

Obrigado por considerar contribuir com o LLM Oxigênio Brasil.

Este projeto é Portuguese-first. Issues, PRs, comentários de código, docstrings e commits devem priorizar português claro. Inglês técnico é bem-vindo quando ajudar precisão, especialmente em nomes de papers, bibliotecas e termos estabelecidos.

## Antes De Escrever Código

Use este filtro:

1. Isso precisa existir agora?
2. Já existe algo parecido no repo?
3. Uma documentação ou checklist resolve?
4. A biblioteca padrão resolve?
5. Uma dependência já instalada resolve?
6. A solução pode ser menor?
7. Isso preserva segurança, validação, ownership, acessibilidade e dados?

Se a resposta não for clara, abra uma issue ou proposta curta antes de implementar.

## North Star

Leia antes de propor mudanças grandes:

- [`docs/research_north_star.md`](docs/research_north_star.md)
- [`docs/dev_senior_onboarding.md`](docs/dev_senior_onboarding.md)

## Dados

Qualquer contribuição de dados deve indicar:

- origem;
- licença;
- data de coleta;
- idioma/dialeto;
- critérios de filtragem;
- riscos conhecidos;
- se contém dados pessoais ou sensíveis;
- se envolve conhecimento tradicional, indígena, quilombola ou territorial.

FineWeb, Dolma, OLMo e pipelines similares servem como referências de transparência, metadados e filtros, não como autorização para copiar dados sem revisar licença e contexto.

## Commits

Prefira mensagens curtas em português:

```txt
docs: adiciona norte de pesquisa
feat: adiciona vocábulos de raciocínio
fix: corrige composição de exemplo
```

## PRs

Todo PR deve explicar:

- o que mudou;
- por que precisa existir;
- como foi validado;
- riscos;
- o que ficou fora de escopo.

## Código

- Escreva funções pequenas.
- Use tipos quando ajudarem leitura.
- Evite dependência nova sem justificativa.
- Não comite datasets grandes, modelos, checkpoints ou `.env`.
- Não inclua segredos, tokens, chaves privadas ou dados reais sensíveis.
