# Handoff Técnico -- LLM Oxigênio Brasil

**Para:** Tech Lead / Dev Senior
**De:** Eduardo Henrique Ananias
**Status:** pre-alpha, fundação inicial publicada
**Repositório:** https://github.com/duhenri9/llm-oxigenio-brasil
**Commit base deste handoff:** `ec714fb5fcc7799151bb9e39ff61837ee5531245`

Este documento é o ponto de retomada do projeto. Ele separa o que já existe no repositório do que está planejado para próximos PRs.

## 1. Visão Executiva

LLM Oxigênio Brasil é um projeto de pesquisa aberta, Portuguese-first, para construir uma base técnica de LLMs voltada a português brasileiro, biodiversidade, educação, cultura, dados brasileiros e governança responsável.

O projeto não é:

- wrapper sobre ChatGPT;
- RAG simples;
- campanha de marketing sem avaliação;
- promessa de modelo treinado antes de dados, pipeline e benchmarks.

O projeto é:

- uma base de pesquisa aberta;
- um repositório de metodologia;
- uma trilha para curadoria de dados;
- uma fundação para continued pre-training, SFT e avaliação futura;
- um experimento de soberania técnica Portuguese-first.

Decisões atuais:

| Dimensão | Decisão |
| --- | --- |
| Nome do projeto | LLM Oxigênio Brasil |
| Slug do repositório | `llm-oxigenio-brasil` |
| Pacote Python | `oxigen` |
| Autor | Eduardo |
| Idioma | Português brasileiro primeiro, inglês técnico quando necessário |
| Licença do código | Apache-2.0 |
| Status de modelo | Nenhum peso treinado ou publicado ainda |
| Status de dados | Nenhum corpus coletado ainda |
| Próximo módulo técnico | `data_pipeline/` |

## 2. Estado Atual Do Repositório

Estado real no commit inicial:

```txt
llm-oxigenio-brasil/
|-- .github/
|   |-- FUNDING.yml
|-- .gitignore
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
|-- README.md
|-- SUPPORT.md
|-- HANDOFF.md
|-- docs/
|   |-- dev_senior_onboarding.md
|   |-- research_north_star.md
|-- pyproject.toml
|-- src/
|   |-- oxigen/
|       |-- __init__.py
|       |-- training/
|           |-- __init__.py
|           |-- thinking/
|               |-- __init__.py
|               |-- composer.py
|               |-- endangered_species.py
|               |-- vocabulary.py
|-- tests/
    |-- test_thinking.py
```

O que está funcional:

- pacote Python `oxigen`;
- módulo `training.thinking`;
- catálogo inicial com 16 espécies brasileiras ameaçadas;
- vocabulário inicial de fases de raciocínio;
- composer de prompts rastreáveis;
- smoke tests básicos;
- documentação de contribuição, conduta, suporte e north star.

O que ainda não existe:

- `src/oxigen/data_pipeline/`;
- `src/oxigen/model.py`;
- `src/oxigen/inference/`;
- `src/oxigen/evaluation/`;
- `configs/`;
- `data/metadata/`;
- `.github/workflows/ci.yml`;
- issue templates;
- `MODEL_LICENSE`;
- `SECURITY.md`;
- benchmark suite;
- corpus coletado;
- pesos de modelo.

## 3. Arquitetura Atual

Stack atual:

| Camada | Tecnologia | Status |
| --- | --- | --- |
| Linguagem | Python 3.11+ | Definido |
| Empacotamento | setuptools | Implementado |
| Testes | pytest | Declarado em `.[dev]`; teste simples criado |
| Lint | ruff | Declarado em `.[dev]` |
| Dados | A definir | Pendente |
| Treinamento | A definir entre Axolotl / TRL / HuggingFace | Pendente |
| Inferência | A definir entre vLLM / llama.cpp / ONNX | Pendente |
| Avaliação | A definir | Pendente |

Princípio de engenharia:

```txt
Antes de adicionar dependência, módulo ou abstração, provar que precisa existir agora.
```

## 4. Módulo `thinking/`

O módulo `src/oxigen/training/thinking/` é a primeira semente operacional do projeto.

Arquivos:

- `endangered_species.py`: 16 espécies brasileiras ameaçadas com bioma, status, ameaças e fato de raciocínio.
- `vocabulary.py`: fases de raciocínio e tokens em português/inglês técnico.
- `composer.py`: cria prompts curtos combinando espécie, fase e pergunta.

Uso atual:

```python
from oxigen.training.thinking import compose_thinking_prompt

prompt = compose_thinking_prompt("Onca-pintada", phase="verificar")
```

Objetivo:

- gerar dados sintéticos pequenos e rastreáveis;
- testar linguagem Portuguese-first;
- conectar biodiversidade brasileira a tarefas de raciocínio;
- servir como insumo futuro para SFT ou avaliação, sem fingir que já é dataset final.

Limite:

- este módulo não é corpus;
- não substitui curadoria de dados;
- não deve ser usado para claims de desempenho.

## 5. North Star De Pesquisa

Documento principal:

- `docs/research_north_star.md`

Ele define:

- tese;
- metas iniciais;
- instituições de referência;
- pipeline de pesquisa;
- política de dados;
- constituição do modelo;
- red-team brasileiro;
- avaliação;
- referências bibliográficas.

Decisão importante:

```txt
O próximo passo técnico real é implementar data_pipeline/,
mas somente depois de fechar manifestos de fonte, metadados,
regras de rejeição e políticas de dados sensíveis.
```

## 6. Pipeline De Treinamento Planejado

Fase 0: Fundação.

- Status: em andamento.
- Feito: repo inicial, docs, pacote Python, thinking seed.
- Falta: data pipeline, CI, security policy, model/inference stubs, metadata schema.

Fase 1: Data pipeline.

- coletores por fonte;
- manifestos de licença;
- deduplicação;
- filtros de qualidade;
- identificação PT-BR;
- metadados;
- contagem de tokens.

Fase 2: Continued pre-training.

- somente depois de corpus auditável;
- base model ainda não decidido em código;
- Qwen 2.5 7B pode ser candidato, não decisão implementada.

Fase 3: SFT.

- pares instrução-resposta curados;
- TRL/Axolotl a avaliar;
- injeção de raciocínio apenas se validada.

Fase 4: Alinhamento.

- DPO/RLAIF se houver dados de preferência;
- constituição brasileira;
- red-team brasileiro.

Fase 5: Serving e avaliação contínua.

- vLLM/ONNX/llama.cpp a avaliar;
- benchmark e arena brasileira apenas depois de baseline mensurável.

## 7. Corpus Planejado

Nenhum dado foi coletado ainda.

Fontes candidatas:

| Domínio | Fonte candidata | Status |
| --- | --- | --- |
| Legislação | Planalto, Senado | Não coletado |
| Jurisprudência | STF e bases públicas | Não coletado |
| Demografia | IBGE | Não coletado |
| Economia | IPEA | Não coletado |
| Ambiente | INPE | Não coletado |
| Educação | MEC/INEP | Não coletado |
| Conhecimento geral | Wikipedia PT-BR | Não coletado |
| Domínio público | Biblioteca Nacional / Domínio Público | Não coletado |
| Web | CommonCrawl filtrado | Não coletado |

Antes de coletar:

- revisar licença;
- documentar fonte;
- definir campos de metadados;
- definir critério de rejeição;
- registrar riscos de PII e dados sensíveis.

## 8. Licenças

Código:

- Apache-2.0, em `LICENSE`.

Pesos de modelo:

- nenhum peso publicado ainda;
- `MODEL_LICENSE` ainda não existe;
- recomendação futura: RAIL brasileira, com restrições alinhadas a leis brasileiras e direitos humanos.

Não criar `MODEL_LICENSE` sem revisão jurídica mínima.

## 9. Suporte Financeiro

Arquivos existentes:

- `.github/FUNDING.yml`;
- `SUPPORT.md`.

Canais atuais:

- GitHub Sponsors: depende de habilitação da conta/repo;
- link custom para `SUPPORT.md`;
- PIX registrado no suporte: `11950377457`.

Pendências:

- habilitar GitHub Sponsors;
- revisar se PIX deve permanecer público;
- criar links Apoia.se/PicPay, se forem usados;
- publicar relatório financeiro quando houver financiamento real.

## 10. Padrões De Engenharia

Non-negotiable:

- português primeiro;
- sem dados sensíveis;
- sem `.env`;
- sem checkpoints ou datasets grandes no git;
- sem dependência nova sem justificativa;
- sem claims de modelo sem avaliação;
- sem scraping sem licença/contexto;
- testes para qualquer módulo operacional;
- documentar fonte e rejeição de dados.

Commits:

```txt
docs: adiciona norte de pesquisa
feat: adiciona coletor inicial
fix: corrige validação de metadados
```

## 11. Próximos Passos Priorizados

Esta semana:

1. Criar `SECURITY.md`.
2. Criar `.github/workflows/ci.yml`.
3. Criar issue templates.
4. Criar `data/metadata/README.md` com schema.
5. Criar branch `feat/data-pipeline`.

Primeiro mês:

1. Implementar `src/oxigen/data_pipeline/`.
2. Definir manifesto de fontes.
3. Criar filtros básicos.
4. Processar amostra pequena, não corpus completo.
5. Criar relatório de qualidade da amostra.

Trimestre:

1. Avaliar baseline de modelo candidato.
2. Definir benchmarks PT-BR.
3. Criar red-team brasileiro inicial.
4. Decidir infraestrutura de treinamento.

## 12. Pendências Manuais Do Eduardo

- [ ] Habilitar GitHub Sponsors.
- [ ] Confirmar se o PIX `11950377457` deve ficar público.
- [ ] Criar Apoia.se, se for usado.
- [ ] Criar PicPay, se for usado.
- [ ] Criar email de contato do projeto.
- [ ] Ativar Discussions no GitHub.
- [ ] Configurar branch protection em `main`.
- [ ] Adicionar topics no repo: `llm`, `portuguese`, `brazil`, `open-source`, `machine-learning`, `nlp`, `amazonia`, `education`.

## 13. Referência Rápida

| Arquivo | Prioridade | Motivo |
| --- | --- | --- |
| `README.md` | Alta | Visão pública e setup |
| `HANDOFF.md` | Alta | Estado real e próximos passos |
| `docs/research_north_star.md` | Alta | Norte técnico e científico |
| `docs/dev_senior_onboarding.md` | Alta | Fluxo para Dev Senior |
| `CONTRIBUTING.md` | Alta | Padrões de contribuição |
| `CODE_OF_CONDUCT.md` | Média | Conduta e ética de dados |
| `SUPPORT.md` | Média | Funding e transparência |
| `src/oxigen/training/thinking/*` | Média | Primeira semente operacional |
| `pyproject.toml` | Alta | Metadados e deps de dev |

## 14. Nota Sobre O Handoff Original

O rascunho externo de handoff descrevia uma versão mais completa do repositório, com CI, model stubs, inference, evaluation, data metadata e licença de modelo. Esses itens ainda não existem neste repo no momento deste handoff.

Este arquivo prevalece como estado real do repositório atual.

## 15. Atualização -- Fundação Auditável V1

Esta atualização registra a direção aprovada para a primeira branch de governança
do projeto. O objetivo não é treinar modelo, baixar corpus ou provisionar GPU.
O objetivo é deixar o projeto auditável antes de qualquer implementação pesada.

Arquivos de referência adicionados nesta etapa:

- `SECURITY.md`;
- `.github/workflows/ci.yml`;
- `.github/ISSUE_TEMPLATE/*`;
- `.github/PULL_REQUEST_TEMPLATE.md`;
- `data/metadata/README.md`;
- `docs/brazilian_domain_strategy.md`;
- `docs/data_source_manifest.md`;
- `docs/data_rejection_policy.md`;
- `docs/pii_sensitive_data_policy.md`;
- `docs/model_selection_policy.md`;
- `docs/model_card_template.md`;
- `docs/eval_card_template.md`;
- `docs/benchmark_plan_ptbr.md`;
- `docs/financial_report.md`.

Decisões técnicas:

- `Qwen3-8B` fica como hipótese inicial de modelo aluno, não como decisão irreversível.
- `GLM-4.5` pode ser teacher, judge ou baseline, não primeiro aluno por padrão.
- Dependências pesadas de ML ficam fora do runtime até haver PR próprio.
- Custos de GPU são estimativas, não cotações ou garantia.
- O projeto deve se apresentar como open-source, Portuguese-first, adaptado e avaliado
  para o contexto brasileiro até haver base técnica para claim mais forte.

Próximo passo recomendado:

```txt
Versão 2 -- Data Pipeline Auditável
```

Ela deve criar amostras pequenas, manifestos preenchidos, validadores de metadados e
filtros de PII. Ainda não deve iniciar treino, corpus grande ou publicação de pesos.

## Naming Guidance

- Projeto público: `Oxigênio Brasil`.
- Primeiro modelo futuro, se e quando houver base técnica para publicação: `Oxigênio-1`.
- Codename interno permitido: `Oxi`.
- Evitar nomes informais como `o2-zuca` em README, LP, docs públicos, model cards,
  eval cards e releases.

A nomenclatura de modelo só deve ser usada publicamente quando houver artefato real,
model card, eval card, licença e benchmark mínimo.

## 16. Atualização -- Landing Page V0

A LP pública inicial vive em `site/` como site estático, sem framework e sem
dependências de runtime.

Escopo:

- apresentar o Oxigênio Brasil como iniciativa open-source, Portuguese-first;
- comunicar domínios brasileiros críticos;
- explicar governança antes de treinamento;
- abrir contribuição futura por GitHub;
- preparar deploy por GitHub Pages via `.github/workflows/pages.yml`.

Fora do escopo:

- conversa integrada;
- coleta de prompts ou respostas;
- formulário próprio;
- login;
- upload de arquivos;
- uso automático de contribuições para treinamento;
- Vercel.

A página deve manter o aviso público de que nenhuma contribuição será usada
automaticamente para treinamento e que todo dado precisa passar por revisão,
consentimento, metadados, filtros de qualidade e política de dados sensíveis.

Conceito narrativo registrado:

- `2026`: o Brasil real de hoje, com desafios concretos de informação,
  biomas, cidadania, cultura e segurança digital;
- `2051`: horizonte de 25 anos para imaginar informação confiável em português
  como infraestrutura, sem prometer que o modelo resolverá esse futuro;
- regra editorial: usar o contraste como reflexão, não como hype, promessa verde
  ou claim de impacto.
