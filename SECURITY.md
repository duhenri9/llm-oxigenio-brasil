# Politica De Seguranca

Este repositorio esta em fase pre-alpha. Ainda nao ha modelo treinado, dataset final,
checkpoints, pesos publicados ou infraestrutura de inferencia em producao.

## Escopo De Seguranca

Relate problemas relacionados a:

- exposicao acidental de segredos, tokens, chaves ou credenciais;
- commit de datasets sensiveis, dados pessoais ou dados proprietarios;
- falhas em politicas de licenca, consentimento ou atribuicao de fonte;
- scripts que possam baixar, processar ou publicar dados sem trilha de auditoria;
- vulnerabilidades em codigo Python, CI, templates ou configuracao do projeto.

## Fora Do Escopo Atual

- ataques contra modelo em producao, porque ainda nao ha modelo publicado;
- jailbreaks de um modelo Oxigenio, porque ainda nao ha pesos do projeto;
- disponibilidade de servico, porque ainda nao ha API publica.

## Como Reportar

Abra uma issue apenas quando o relato nao expuser dados sensiveis. Se o relato incluir
segredo, dado pessoal, material privado ou detalhe exploravel, envie primeiro por canal
privado ao mantenedor.

Inclua:

- resumo curto;
- arquivo ou fluxo afetado;
- impacto esperado;
- passos minimos de reproducao;
- recomendacao de correcao, se houver.

## Regras Para Contribuidores

- Nunca commitar `.env`, tokens, chaves privadas ou credenciais.
- Nunca commitar checkpoints, pesos, datasets brutos ou dumps de usuario.
- Nunca coletar dados em massa antes de existir manifesto de fonte aprovado.
- Nunca publicar exemplos contendo informacao pessoal real.
- Tratar toda fonte de dados como rejeitada ate passar por licenca, consentimento,
  origem, sensibilidade e finalidade.

## Dependencias De IA

Dependencias pesadas como `torch`, `transformers`, `datasets`, `accelerate`, `trl` e
`axolotl` nao devem entrar em dependencias runtime sem PR dedicado. Elas podem ser
avaliadas em extras opcionais quando houver escopo tecnico, custo e licenca claros.

