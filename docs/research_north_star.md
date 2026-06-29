# Research North Star

Este é o documento central do LLM Oxigênio Brasil.

Ele define o que o projeto quer aprender, quais referências técnicas orientam as decisões e quais limites não devem ser cruzados.

## Tese

O Brasil precisa de pesquisa aberta em LLMs que trate português brasileiro, biodiversidade, cultura, educação, legislação e conhecimento local como centro do problema, não como nota de rodapé multilingue.

O projeto não começa prometendo "o melhor modelo brasileiro". Ele começa criando uma base verificável:

- dados com origem e licença;
- filtros documentados;
- avaliação multidimensional;
- alinhamento com direitos e contexto brasileiro;
- treinamento incremental;
- transparência suficiente para auditoria.

## Metas Iniciais

- Criar pipeline de dados Portuguese-first.
- Justificar um alvo inicial de até 50B tokens com qualidade maior que volume.
- Preparar continued pre-training e SFT.
- Usar avaliação PT-BR antes de claims públicos.
- Construir vocábulos e tarefas de raciocínio inspirados no tema oxigênio, biodiversidade e Brasil.

## Instituições E Contribuições Aplicadas

| Instituição | O que traz para o Oxigênio Brasil |
| --- | --- |
| Meta FAIR | Arquitetura LLaMA, continued pre-training, filtros de dados e eficiência. |
| Google DeepMind | Leis de escalonamento Chinchilla e critério qualidade > escala via Gemma. |
| Stanford HAI | Alpaca/Self-Instruct e HELM para avaliação multidimensional. |
| UC Berkeley | Chatbot Arena, Vicuna e vLLM para avaliação humana e inferência. |
| Allen AI | OLMo e Dolma como referência de transparência e metadados de dados. |
| Anthropic | Constitutional AI e red-teaming com categorias brasileiras. |
| HuggingFace | TRL, DPO e FineWeb como referência de ferramentas e filtros. |
| Mistral AI | Modelos pequenos eficientes e contexto longo com atenção otimizada. |
| UW / Stanford | Chain-of-Thought, RLHF e Self-Instruct. |
| Tsinghua | Treinamento multilingue com proporção controlada de inglês técnico. |
| USP NILC | Assin2, HateBR e recursos linguísticos PT-BR. |
| INPE | Dados ambientais, Amazônia, clima, queimadas e sensoriamento remoto. |
| MIT, Princeton, ETH, CMU, KAIST, UFMG, UNICAMP, UFRJ | Referências complementares em avaliação, sistemas, linguística, ética e ciência aberta. |

## Pipeline De Pesquisa

```txt
Fontes e licenças
  -> filtros de qualidade e segurança
  -> metadados por documento
  -> deduplicação
  -> mistura Portuguese-first + inglês técnico controlado
  -> continued pre-training
  -> SFT
  -> DPO/RLAIF quando houver dados suficientes
  -> avaliação PT-BR
  -> red-teaming brasileiro
  -> publicação auditável
```

## Dados

Todo dado precisa responder:

- de onde veio;
- qual licença permite uso;
- se contém PII;
- se contém discurso de ódio, violência ou dados sensíveis;
- se envolve conhecimento tradicional, indígena, quilombola ou territorial;
- qual filtro foi aplicado;
- qual proporção entra no mix final.

## Constituição Do Modelo

Constitutional AI inspira o método, mas a constituição do projeto deve ser brasileira.

Fontes normativas iniciais:

- Constituição Federal de 1988;
- LGPD;
- Convenção 169 da OIT;
- Artigo 231 da CF sobre povos indígenas;
- princípios de segurança, transparência e não exploração.

## Red-Team Brasileiro

Categorias iniciais:

1. dados pessoais e doxxing;
2. racismo, xenofobia e ódio regional;
3. ataques a povos indígenas, quilombolas e comunidades tradicionais;
4. desinformação sobre saúde e meio ambiente;
5. garimpo ilegal, madeira ilegal e dano ambiental;
6. fraude financeira e golpe;
7. violência política;
8. sexualização, exploração ou assédio.

## Avaliação

Não publicar claim sem avaliação.

Camadas:

- capacidade linguística PT-BR;
- raciocínio;
- segurança;
- conhecimento regional;
- robustez contra prompt injection;
- vieses;
- custo/inferência;
- utilidade humana.

Benchmarks candidatos:

- Assin2;
- HateBR;
- tarefas de QA ambiental;
- avaliação humana estilo Arena;
- HELM-like cards para transparência.

## Referências Bibliográficas

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

## Decisão Atual

O próximo passo técnico real é implementar `data_pipeline/`, mas somente depois de fechar:

- manifestos de fonte;
- esquema de metadados;
- regras de rejeição;
- validação local;
- políticas de dados sensíveis.
