# Politica De Selecao De Modelo Base

## Status

Nenhum modelo base foi escolhido de forma irreversivel. Nenhum peso foi baixado,
treinado, convertido ou publicado por este repositorio.

## Enquadramento Correto

Enquanto o projeto usar modelos base estrangeiros, a descricao tecnica correta e:

```txt
LLM aberto, Portuguese-first, adaptado e avaliado para o contexto brasileiro.
```

Evitar claim tecnico de "100% brasileiro" ate existir base, corpus, treino,
avaliacao e licenca que sustentem essa afirmacao.

## Hipotese Inicial

`Qwen3-8B` e a hipotese inicial para modelo aluno em experimentos pequenos,
porque oferece bom equilibrio entre tamanho, custo de teste, ecossistema aberto
e viabilidade para SFT/LoRA.

`Qwen3-14B` pode ser avaliado se houver ganho claro e custo controlado.

## Papel Do Ecossistema GLM

`GLM-4.5` ou variantes da familia GLM podem ser avaliados como:

- teacher para gerar ou revisar amostras;
- judge auxiliar em avaliacao;
- baseline comparativo;
- ferramenta de orquestracao tecnica.

Eles nao devem ser adotados como primeiro modelo aluno sem matriz de custo,
licenca, hardware, qualidade PT-BR e risco operacional.

## Comparativos

Gemma, Llama, Mistral e outros modelos podem ser avaliados quando:

- a licenca permitir o uso pretendido;
- o custo for compativel;
- houver benchmark PT-BR;
- o resultado for documentado em eval card.

## Criterios De Decisao

Cada candidato deve ser avaliado por:

- licenca;
- custo de inferencia e treino;
- suporte a portugues brasileiro;
- janela de contexto;
- maturidade de tooling;
- compatibilidade com TRL, Axolotl, vLLM ou equivalente;
- qualidade em dominios brasileiros criticos;
- risco de lock-in;
- facilidade de reproducao por comunidade aberta.

## Fontes De Referencia

- Qwen3-8B: https://huggingface.co/Qwen/Qwen3-8B
- GLM-4.5: https://huggingface.co/zai-org/GLM-4.5
- TRL: https://huggingface.co/docs/trl/index

