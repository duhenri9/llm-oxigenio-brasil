# Política De Segurança

Este repositório está em fase pre-alpha. Ainda não há modelo treinado, dataset final,
checkpoints, pesos publicados ou infraestrutura de inferência em produção.

## Escopo De Segurança

Relate problemas relacionados a:

- exposição acidental de segredos, tokens, chaves ou credenciais;
- commit de datasets sensíveis, dados pessoais ou dados proprietários;
- falhas em políticas de licença, consentimento ou atribuição de fonte;
- scripts que possam baixar, processar ou publicar dados sem trilha de auditoria;
- vulnerabilidades em código Python, CI, templates ou configuração do projeto.

## Fora Do Escopo Atual

- ataques contra modelo em produção, porque ainda não há modelo publicado;
- jailbreaks de um modelo Oxigênio, porque ainda não há pesos do projeto;
- disponibilidade de serviço, porque ainda não há API pública.

## Como Reportar

Abra uma issue apenas quando o relato não expuser dados sensíveis. Se o relato incluir
segredo, dado pessoal, material privado ou detalhe explorável, envie primeiro por canal
privado ao mantenedor.

Inclua:

- resumo curto;
- arquivo ou fluxo afetado;
- impacto esperado;
- passos mínimos de reprodução;
- recomendação de correção, se houver.

## Regras Para Contribuidores

- Nunca commitar `.env`, tokens, chaves privadas ou credenciais.
- Nunca commitar checkpoints, pesos, datasets brutos ou dumps de usuário.
- Nunca coletar dados em massa antes de existir manifesto de fonte aprovado.
- Nunca publicar exemplos contendo informação pessoal real.
- Tratar toda fonte de dados como rejeitada até passar por licença, consentimento,
  origem, sensibilidade e finalidade.

## Dependências De IA

Dependências pesadas como `torch`, `transformers`, `datasets`, `accelerate`, `trl` e
`axolotl` não devem entrar em dependências runtime sem PR dedicado. Elas podem ser
avaliadas em extras opcionais quando houver escopo técnico, custo e licença claros.

