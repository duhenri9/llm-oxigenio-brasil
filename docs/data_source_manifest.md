# Manifesto De Fontes De Dados

## Status

Nenhuma fonte está aprovada para coleta, treinamento, redistribuição ou publicação.
Este documento define o contrato de avaliação antes de qualquer pipeline de dados.

## Objetivo

Garantir que cada fonte usada pelo projeto Oxigênio Brasil tenha origem, licença,
finalidade, risco e decisão documentados antes de virar amostra, benchmark ou corpus.

## Critérios Obrigatórios

Uma fonte só pode avançar se houver:

- URL, instituição ou responsável verificável;
- licença compatível com o uso proposto;
- finalidade explícita no projeto;
- classificação de risco de PII e dados sensíveis;
- decisão documentada de aceitar, rejeitar ou manter pendente;
- plano de remoção caso a fonte seja contestada.

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

## Decisões Possíveis

- `approved_for_metadata_only`: pode ser catalogada, não coletada.
- `approved_for_eval_sample`: pode gerar amostra pequena de avaliação.
- `approved_for_training_sample`: pode entrar em experimento pequeno.
- `approved_for_corpus`: pode entrar em corpus maior.
- `rejected`: não usar.
- `pending`: aguardar licença, contato, revisão jurídica ou auditoria.

