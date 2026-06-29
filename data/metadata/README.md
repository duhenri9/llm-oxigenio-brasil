# Metadata De Dados

Este diretorio e reservado para metadados auditaveis de fontes, amostras e artefatos
de dados. Ele nao deve conter dados brutos, dados pessoais, dumps, checkpoints ou
arquivos grandes.

## Estado Atual

Nenhum corpus foi coletado. Nenhuma fonte esta aprovada para treinamento.

## Esquema Minimo Futuro

Cada fonte aprovada devera registrar:

- `source_id`: identificador estavel;
- `name`: nome da fonte;
- `url`: origem publica ou contrato interno;
- `owner`: instituicao, autor ou mantenedor;
- `license`: licenca verificavel;
- `collection_method`: API, download oficial, convenio ou outro metodo;
- `allowed_use`: pesquisa, avaliacao, treinamento, redistribuicao ou proibido;
- `language`: idioma principal;
- `domain`: dominio brasileiro relacionado;
- `pii_risk`: baixo, medio, alto ou proibido;
- `sensitive_risk`: baixo, medio, alto ou proibido;
- `version_date`: data da versao avaliada;
- `auditor`: responsavel pela revisao;
- `decision`: aprovado, rejeitado ou pendente.

## Regra Principal

Todo dado com metadado incompleto deve ser tratado como rejeitado ate prova em contrario.

