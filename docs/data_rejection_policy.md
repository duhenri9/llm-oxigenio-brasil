# Politica De Rejeicao De Dados

## Principio

Dados entram no projeto apenas por permissao explicita, finalidade clara e risco
controlado. Na duvida, rejeitar.

## Rejeicao Obrigatoria

Rejeitar fontes que contenham:

- dados pessoais sem base legal, consentimento ou necessidade tecnica;
- informacao privada, credenciais, segredos ou dumps internos;
- material com licenca incompatibilidade com treinamento, avaliacao ou redistribuicao;
- conteudo de comunidades indigenas, quilombolas ou tradicionais sem contexto,
  consentimento ou protocolo adequado;
- dados medicos, juridicos, financeiros ou educacionais individualizados;
- conteudo obtido por scraping contra termos de uso;
- conteudo sem autoria, origem ou versao verificavel;
- listas de vazamento, forum privado, grupo fechado ou material pirateado.

## Rejeicao Temporaria

Manter como `pending` quando:

- a licenca existe, mas nao cobre treinamento;
- a fonte e publica, mas nao autoriza redistribuicao;
- a qualidade e util, mas a origem nao esta clara;
- ha risco cultural, regional ou sensivel que exige revisao humana especializada.

## Registro

Toda rejeicao deve registrar:

- fonte;
- motivo;
- evidencia;
- data;
- responsavel;
- possibilidade de reavaliacao.

