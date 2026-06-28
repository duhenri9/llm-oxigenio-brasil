# Handoff Tecnico -- LLM Oxigenio Brasil

**Para:** Tech Lead / Dev Senior  
**De:** Eduardo Henrique Ananias  
**Status:** pre-alpha, fundacao inicial publicada  
**Repositorio:** https://github.com/duhenri9/llm-oxigenio-brasil  
**Commit base deste handoff:** `ec714fb5fcc7799151bb9e39ff61837ee5531245`

Este documento e o ponto de retomada do projeto. Ele separa o que ja existe no repositorio do que esta planejado para proximos PRs.

## 1. Visao Executiva

LLM Oxigenio Brasil e um projeto de pesquisa aberta, Portuguese-first, para construir uma base tecnica de LLMs voltada a portugues brasileiro, biodiversidade, educacao, cultura, dados brasileiros e governanca responsavel.

O projeto nao e:

- wrapper sobre ChatGPT;
- RAG simples;
- campanha de marketing sem avaliacao;
- promessa de modelo treinado antes de dados, pipeline e benchmarks.

O projeto e:

- uma base de pesquisa aberta;
- um repositorio de metodologia;
- uma trilha para curadoria de dados;
- uma fundacao para continued pre-training, SFT e avaliacao futura;
- um experimento de soberania tecnica Portuguese-first.

Decisoes atuais:

| Dimensao | Decisao |
| --- | --- |
| Nome do projeto | LLM Oxigenio Brasil |
| Slug do repositorio | `llm-oxigenio-brasil` |
| Pacote Python | `oxigen` |
| Autor | Eduardo |
| Idioma | Portugues brasileiro primeiro, ingles tecnico quando necessario |
| Licenca do codigo | Apache-2.0 |
| Status de modelo | Nenhum peso treinado ou publicado ainda |
| Status de dados | Nenhum corpus coletado ainda |
| Proximo modulo tecnico | `data_pipeline/` |

## 2. Estado Atual Do Repositorio

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

O que esta funcional:

- pacote Python `oxigen`;
- modulo `training.thinking`;
- catalogo inicial com 16 especies brasileiras ameacadas;
- vocabulario inicial de fases de raciocinio;
- composer de prompts rastreaveis;
- smoke tests basicos;
- documentacao de contribuicao, conduta, suporte e north star.

O que ainda nao existe:

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
| Inferencia | A definir entre vLLM / llama.cpp / ONNX | Pendente |
| Avaliacao | A definir | Pendente |

Principio de engenharia:

```txt
Antes de adicionar dependencia, modulo ou abstracao, provar que precisa existir agora.
```

## 4. Modulo `thinking/`

O modulo `src/oxigen/training/thinking/` e a primeira semente operacional do projeto.

Arquivos:

- `endangered_species.py`: 16 especies brasileiras ameacadas com bioma, status, ameacas e fato de raciocinio.
- `vocabulary.py`: fases de raciocinio e tokens em portugues/ingles tecnico.
- `composer.py`: cria prompts curtos combinando especie, fase e pergunta.

Uso atual:

```python
from oxigen.training.thinking import compose_thinking_prompt

prompt = compose_thinking_prompt("Onca-pintada", phase="verificar")
```

Objetivo:

- gerar dados sinteticos pequenos e rastreaveis;
- testar linguagem Portuguese-first;
- conectar biodiversidade brasileira a tarefas de raciocinio;
- servir como insumo futuro para SFT ou avaliacao, sem fingir que ja e dataset final.

Limite:

- este modulo nao e corpus;
- nao substitui curadoria de dados;
- nao deve ser usado para claims de desempenho.

## 5. North Star De Pesquisa

Documento principal:

- `docs/research_north_star.md`

Ele define:

- tese;
- metas iniciais;
- instituicoes de referencia;
- pipeline de pesquisa;
- politica de dados;
- constituicao do modelo;
- red-team brasileiro;
- avaliacao;
- referencias bibliograficas.

Decisao importante:

```txt
O proximo passo tecnico real e implementar data_pipeline/,
mas somente depois de fechar manifestos de fonte, metadados,
regras de rejeicao e politicas de dados sensiveis.
```

## 6. Pipeline De Treinamento Planejado

Fase 0: Fundacao.

- Status: em andamento.
- Feito: repo inicial, docs, pacote Python, thinking seed.
- Falta: data pipeline, CI, security policy, model/inference stubs, metadata schema.

Fase 1: Data pipeline.

- coletores por fonte;
- manifestos de licenca;
- deduplicacao;
- filtros de qualidade;
- identificacao PT-BR;
- metadados;
- contagem de tokens.

Fase 2: Continued pre-training.

- somente depois de corpus auditavel;
- base model ainda nao decidido em codigo;
- Qwen 2.5 7B pode ser candidato, nao decisao implementada.

Fase 3: SFT.

- pares instrucao-resposta curados;
- TRL/Axolotl a avaliar;
- injecao de raciocinio apenas se validada.

Fase 4: Alinhamento.

- DPO/RLAIF se houver dados de preferencia;
- constituicao brasileira;
- red-team brasileiro.

Fase 5: Serving e avaliacao continua.

- vLLM/ONNX/llama.cpp a avaliar;
- benchmark e arena brasileira apenas depois de baseline mensuravel.

## 7. Corpus Planejado

Nenhum dado foi coletado ainda.

Fontes candidatas:

| Dominio | Fonte candidata | Status |
| --- | --- | --- |
| Legislacao | Planalto, Senado | Nao coletado |
| Jurisprudencia | STF e bases publicas | Nao coletado |
| Demografia | IBGE | Nao coletado |
| Economia | IPEA | Nao coletado |
| Ambiente | INPE | Nao coletado |
| Educacao | MEC/INEP | Nao coletado |
| Conhecimento geral | Wikipedia PT-BR | Nao coletado |
| Dominio publico | Biblioteca Nacional / Dominio Publico | Nao coletado |
| Web | CommonCrawl filtrado | Nao coletado |

Antes de coletar:

- revisar licenca;
- documentar fonte;
- definir campos de metadados;
- definir criterio de rejeicao;
- registrar riscos de PII e dados sensiveis.

## 8. Licencas

Codigo:

- Apache-2.0, em `LICENSE`.

Pesos de modelo:

- nenhum peso publicado ainda;
- `MODEL_LICENSE` ainda nao existe;
- recomendacao futura: RAIL brasileira, com restricoes alinhadas a leis brasileiras e direitos humanos.

Nao criar `MODEL_LICENSE` sem revisao juridica minima.

## 9. Suporte Financeiro

Arquivos existentes:

- `.github/FUNDING.yml`;
- `SUPPORT.md`.

Canais atuais:

- GitHub Sponsors: depende de habilitacao da conta/repo;
- link custom para `SUPPORT.md`;
- PIX registrado no suporte: `11950377457`.

Pendencias:

- habilitar GitHub Sponsors;
- revisar se PIX deve permanecer publico;
- criar links Apoia.se/PicPay, se forem usados;
- publicar relatorio financeiro quando houver financiamento real.

## 10. Padroes De Engenharia

Non-negotiable:

- portugues primeiro;
- sem dados sensiveis;
- sem `.env`;
- sem checkpoints ou datasets grandes no git;
- sem dependencia nova sem justificativa;
- sem claims de modelo sem avaliacao;
- sem scraping sem licenca/contexto;
- testes para qualquer modulo operacional;
- documentar fonte e rejeicao de dados.

Commits:

```txt
docs: adiciona norte de pesquisa
feat: adiciona coletor inicial
fix: corrige validacao de metadados
```

## 11. Proximos Passos Priorizados

Esta semana:

1. Criar `SECURITY.md`.
2. Criar `.github/workflows/ci.yml`.
3. Criar issue templates.
4. Criar `data/metadata/README.md` com schema.
5. Criar branch `feat/data-pipeline`.

Primeiro mes:

1. Implementar `src/oxigen/data_pipeline/`.
2. Definir manifesto de fontes.
3. Criar filtros basicos.
4. Processar amostra pequena, nao corpus completo.
5. Criar relatorio de qualidade da amostra.

Trimestre:

1. Avaliar baseline de modelo candidato.
2. Definir benchmarks PT-BR.
3. Criar red-team brasileiro inicial.
4. Decidir infraestrutura de treinamento.

## 12. Pendencias Manuais Do Eduardo

- [ ] Habilitar GitHub Sponsors.
- [ ] Confirmar se o PIX `11950377457` deve ficar publico.
- [ ] Criar Apoia.se, se for usado.
- [ ] Criar PicPay, se for usado.
- [ ] Criar email de contato do projeto.
- [ ] Ativar Discussions no GitHub.
- [ ] Configurar branch protection em `main`.
- [ ] Adicionar topics no repo: `llm`, `portuguese`, `brazil`, `open-source`, `machine-learning`, `nlp`, `amazonia`, `education`.

## 13. Referencia Rapida

| Arquivo | Prioridade | Motivo |
| --- | --- | --- |
| `README.md` | Alta | Visao publica e setup |
| `HANDOFF.md` | Alta | Estado real e proximos passos |
| `docs/research_north_star.md` | Alta | Norte tecnico e cientifico |
| `docs/dev_senior_onboarding.md` | Alta | Fluxo para Dev Senior |
| `CONTRIBUTING.md` | Alta | Padroes de contribuicao |
| `CODE_OF_CONDUCT.md` | Media | Conduta e etica de dados |
| `SUPPORT.md` | Media | Funding e transparencia |
| `src/oxigen/training/thinking/*` | Media | Primeira semente operacional |
| `pyproject.toml` | Alta | Metadados e deps de dev |

## 14. Nota Sobre O Handoff Original

O rascunho externo de handoff descrevia uma versao mais completa do repositorio, com CI, model stubs, inference, evaluation, data metadata e licenca de modelo. Esses itens ainda nao existem neste repo no momento deste handoff.

Este arquivo prevalece como estado real do repositorio atual.
