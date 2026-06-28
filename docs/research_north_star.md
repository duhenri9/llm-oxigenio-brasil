# Research North Star

Este e o documento central do LLM Oxigenio Brasil.

Ele define o que o projeto quer aprender, quais referencias tecnicas orientam as decisoes e quais limites nao devem ser cruzados.

## Tese

O Brasil precisa de pesquisa aberta em LLMs que trate portugues brasileiro, biodiversidade, cultura, educacao, legislacao e conhecimento local como centro do problema, nao como nota de rodape multilingue.

O projeto nao comeca prometendo "o melhor modelo brasileiro". Ele comeca criando uma base verificavel:

- dados com origem e licenca;
- filtros documentados;
- avaliacao multidimensional;
- alinhamento com direitos e contexto brasileiro;
- treinamento incremental;
- transparencia suficiente para auditoria.

## Metas Iniciais

- Criar pipeline de dados Portuguese-first.
- Justificar um alvo inicial de ate 50B tokens com qualidade maior que volume.
- Preparar continued pre-training e SFT.
- Usar avaliacao PT-BR antes de claims publicos.
- Construir vocabulos e tarefas de raciocinio inspirados no tema oxigenio, biodiversidade e Brasil.

## Instituicoes E Contribuicoes Aplicadas

| Instituicao | O que traz para o Oxigenio Brasil |
| --- | --- |
| Meta FAIR | Arquitetura LLaMA, continued pre-training, filtros de dados e eficiencia. |
| Google DeepMind | Leis de escalonamento Chinchilla e criterio qualidade > escala via Gemma. |
| Stanford HAI | Alpaca/Self-Instruct e HELM para avaliacao multidimensional. |
| UC Berkeley | Chatbot Arena, Vicuna e vLLM para avaliacao humana e inferencia. |
| Allen AI | OLMo e Dolma como referencia de transparencia e metadados de dados. |
| Anthropic | Constitutional AI e red-teaming com categorias brasileiras. |
| HuggingFace | TRL, DPO e FineWeb como referencia de ferramentas e filtros. |
| Mistral AI | Modelos pequenos eficientes e contexto longo com atencao otimizada. |
| UW / Stanford | Chain-of-Thought, RLHF e Self-Instruct. |
| Tsinghua | Treinamento multilingue com proporcao controlada de ingles tecnico. |
| USP NILC | Assin2, HateBR e recursos linguisticos PT-BR. |
| INPE | Dados ambientais, Amazonia, clima, queimadas e sensoriamento remoto. |
| MIT, Princeton, ETH, CMU, KAIST, UFMG, UNICAMP, UFRJ | Referencias complementares em avaliacao, sistemas, linguistica, etica e ciencia aberta. |

## Pipeline De Pesquisa

```txt
Fontes e licencas
  -> filtros de qualidade e seguranca
  -> metadados por documento
  -> deduplicacao
  -> mistura Portuguese-first + ingles tecnico controlado
  -> continued pre-training
  -> SFT
  -> DPO/RLAIF quando houver dados suficientes
  -> avaliacao PT-BR
  -> red-teaming brasileiro
  -> publicacao auditavel
```

## Dados

Todo dado precisa responder:

- de onde veio;
- qual licenca permite uso;
- se contem PII;
- se contem discurso de odio, violencia ou dados sensiveis;
- se envolve conhecimento tradicional, indigena, quilombola ou territorial;
- qual filtro foi aplicado;
- qual proporcao entra no mix final.

## Constituicao Do Modelo

Constitutional AI inspira o metodo, mas a constituicao do projeto deve ser brasileira.

Fontes normativas iniciais:

- Constituicao Federal de 1988;
- LGPD;
- Convencao 169 da OIT;
- Artigo 231 da CF sobre povos indigenas;
- principios de seguranca, transparencia e nao exploracao.

## Red-Team Brasileiro

Categorias iniciais:

1. dados pessoais e doxxing;
2. racismo, xenofobia e odio regional;
3. ataques a povos indigenas, quilombolas e comunidades tradicionais;
4. desinformacao sobre saude e meio ambiente;
5. garimpo ilegal, madeira ilegal e dano ambiental;
6. fraude financeira e golpe;
7. violencia politica;
8. sexualizacao, exploracao ou assedio.

## Avaliacao

Nao publicar claim sem avaliacao.

Camadas:

- capacidade linguistica PT-BR;
- raciocinio;
- seguranca;
- conhecimento regional;
- robustez contra prompt injection;
- vieses;
- custo/inferencia;
- utilidade humana.

Benchmarks candidatos:

- Assin2;
- HateBR;
- tarefas de QA ambiental;
- avaliacao humana estilo Arena;
- HELM-like cards para transparencia.

## Referencias Bibliograficas

1. Touvron et al. LLaMA: Open and Efficient Foundation Language Models. 2023.
2. Touvron et al. Llama 2: Open Foundation and Fine-Tuned Chat Models. 2023.
3. Hoffmann et al. Training Compute-Optimal Large Language Models. 2022.
4. Team et al. Gemma: Open Models Based on Gemini Research and Technology. 2024.
5. Taori et al. Alpaca: A Strong, Replicable Instruction-Following Model. 2023.
6. Liang et al. Holistic Evaluation of Language Models. 2022.
7. Chiang et al. Vicuna: An Open-Source Chatbot Impressing GPT-4. 2023.
8. Zheng et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. 2023.
9. Kwon et al. Efficient Memory Management for Large Language Model Serving with PagedAttention. 2023.
10. Groeneveld et al. OLMo: Accelerating the Science of Language Models. 2024.
11. Soldaini et al. Dolma: An Open Corpus of Three Trillion Tokens. 2024.
12. Bai et al. Constitutional AI: Harmlessness from AI Feedback. 2022.
13. Ganguli et al. Red Teaming Language Models to Reduce Harms. 2022.
14. von Werra et al. TRL: Transformer Reinforcement Learning. 2020.
15. Rafailov et al. Direct Preference Optimization. 2023.
16. Penedo et al. The FineWeb Datasets. 2024.
17. Jiang et al. Mistral 7B. 2023.
18. Beltagy et al. Longformer: The Long-Document Transformer. 2020.
19. Wei et al. Chain-of-Thought Prompting Elicits Reasoning. 2022.
20. Ouyang et al. Training Language Models to Follow Instructions with Human Feedback. 2022.
21. Wang et al. Self-Instruct. 2022.
22. Zhao et al. A Survey of Large Language Models. 2023.
23. Real, Fonseca and Oliveira. ASSIN 2 Shared Task. 2020.
24. Vargas et al. HateBR: A Large Expert Annotated Corpus of Brazilian Instagram Comments. 2022.

## Decisao Atual

O proximo passo tecnico real e implementar `data_pipeline/`, mas somente depois de fechar:

- manifestos de fonte;
- esquema de metadados;
- regras de rejeicao;
- validacao local;
- politicas de dados sensiveis.
