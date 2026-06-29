# Política De Seleção De Modelo Base

## Status

Nenhum modelo base foi escolhido de forma irreversível. Nenhum peso foi baixado,
treinado, convertido ou publicado por este repositório.

## Enquadramento Correto

Enquanto o projeto usar modelos base estrangeiros, a descrição técnica correta é:

```txt
LLM aberto, Portuguese-first, adaptado e avaliado para o contexto brasileiro.
```

Evitar claim técnico de "100% brasileiro" até existir base, corpus, treino,
avaliação e licença que sustentem essa afirmação.

## Hipótese Inicial

`Qwen3-8B` é a hipótese inicial para modelo aluno em experimentos pequenos,
porque oferece bom equilíbrio entre tamanho, custo de teste, ecossistema aberto
e viabilidade para SFT/LoRA.

`Qwen3-14B` pode ser avaliado se houver ganho claro e custo controlado.

## Papel Do Ecossistema GLM

`GLM-4.5` ou variantes da família GLM podem ser avaliados como:

- teacher para gerar ou revisar amostras;
- judge auxiliar em avaliação;
- baseline comparativo;
- ferramenta de orquestração técnica.

Eles não devem ser adotados como primeiro modelo aluno sem matriz de custo,
licença, hardware, qualidade PT-BR e risco operacional.

## Comparativos

Gemma, Llama, Mistral e outros modelos podem ser avaliados quando:

- a licença permitir o uso pretendido;
- o custo for compatível;
- houver benchmark PT-BR;
- o resultado for documentado em eval card.

## Critérios De Decisão

Cada candidato deve ser avaliado por:

- licença;
- custo de inferência e treino;
- suporte a português brasileiro;
- janela de contexto;
- maturidade de tooling;
- compatibilidade com TRL, Axolotl, vLLM ou equivalente;
- qualidade em domínios brasileiros críticos;
- risco de lock-in;
- facilidade de reprodução por comunidade aberta.

## Fontes De Referência

- Qwen3-8B: https://huggingface.co/Qwen/Qwen3-8B
- GLM-4.5: https://huggingface.co/zai-org/GLM-4.5
- TRL: https://huggingface.co/docs/trl/index

