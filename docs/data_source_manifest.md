# Manifesto De Fontes De Dados

## Status

Nenhuma fonte esta aprovada para coleta, treinamento, redistribuicao ou publicacao.
Este documento define o contrato de avaliacao antes de qualquer pipeline de dados.

## Objetivo

Garantir que cada fonte usada pelo projeto Oxigenio Brasil tenha origem, licenca,
finalidade, risco e decisao documentados antes de virar amostra, benchmark ou corpus.

## Criterios Obrigatorios

Uma fonte so pode avancar se houver:

- URL, instituicao ou responsavel verificavel;
- licenca compativel com o uso proposto;
- finalidade explicita no projeto;
- classificacao de risco de PII e dados sensiveis;
- decisao documentada de aceitar, rejeitar ou manter pendente;
- plano de remocao caso a fonte seja contestada.

## Template De Entrada

```yaml
source_id:
name:
url:
owner:
license:
license_evidence:
collection_method:
allowed_use:
domain:
language:
pii_risk:
sensitive_risk:
copyright_risk:
indigenous_or_traditional_knowledge_risk:
redistribution_allowed:
training_allowed:
evaluation_allowed:
notes:
decision:
auditor:
decision_date:
```

## Decisoes Possiveis

- `approved_for_metadata_only`: pode ser catalogada, nao coletada.
- `approved_for_eval_sample`: pode gerar amostra pequena de avaliacao.
- `approved_for_training_sample`: pode entrar em experimento pequeno.
- `approved_for_corpus`: pode entrar em corpus maior.
- `rejected`: nao usar.
- `pending`: aguardar licenca, contato, revisao juridica ou auditoria.

