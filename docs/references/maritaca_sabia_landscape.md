# Landscape Técnico Brasileiro: Maritaca/Sabiá

## Status

Este documento registra Maritaca/Sabiá como referência externa de maturidade
técnica para o Oxigênio Brasil. Ele não autoriza treino, coleta de corpus,
scraping, uso de pesos, criação de dataset ou claim público novo.

O uso correto neste projeto é:

```txt
Landscape técnico brasileiro: Maritaca/Sabiá como referência externa de
maturidade, avaliação e pipeline de dados.
```

Oxigênio Brasil não tenta copiar Sabiá. A tese própria do projeto é construir
uma fundação aberta, auditável e complementar para domínios brasileiros críticos.

## O Que É Maritaca/Sabiá

Maritaca AI é um ator brasileiro relevante no ecossistema de LLMs em português.
A família Sabiá serve como sinal de maturidade técnica em adaptação para
português brasileiro, continued pretraining, avaliação local e especialização
por domínio.

Para o Oxigênio Brasil, o ecossistema deve ser separado em partes distintas:

| Parte | Como tratar no Oxigênio Brasil |
| --- | --- |
| Modelos fechados ou acessados por API | Podem ser avaliados como baseline, teacher ou judge quando custo, licença, versão, data e finalidade estiverem registrados. Não devem virar dependência central. |
| Papers e technical reports | Referências metodológicas para leitura crítica. Não são plano operacional automático. |
| Benchmarks abertos | Fontes de inspiração para estrutura, rubricas e avaliação. Reuso depende de licença, escopo e redistribuição. |
| API client público | Ferramenta possível para experimentos controlados. Não implica adoção de modelo fechado. |
| Metodologia de dados | Referência para filtros, metadados, classificação e avaliação de qualidade, sem copiar volume ou corpus. |

## O Que Pode Inspirar

- Continued pretraining em português como caminho técnico relevante, somente
  depois de pipeline auditável, benchmark e revisão de licença.
- ClassiCC-PT como referência metodológica para construir corpus em português
  com filtros específicos por idioma, qualidade, educação, STEM e toxicidade.
- Avaliação com exames, rubricas e tarefas brasileiras, desde que as fontes
  sejam públicas, verificáveis e licenciadas para o uso pretendido.
- Avaliação estruturada com LLM-as-judge, rubricas oficiais, checklists manuais
  e revisão humana.
- Registro de versão, data, custo, licença e finalidade quando modelos externos
  forem usados como teacher, judge ou baseline.

Frase de orientação:

```txt
O ecossistema Maritaca/Sabiá mostra que adaptação ao português brasileiro,
avaliação local e dados específicos por idioma são tecnicamente relevantes.
O Oxigênio Brasil adota essa lição como referência, mas segue uma direção
própria: abertura, auditabilidade, limites explícitos e foco em domínios
brasileiros ainda pouco cobertos.
```

## O Que Não Copiar

- Modelo fechado, pesos indisponíveis ou dependência operacional de API externa.
- Dependência prematura de infraestrutura pesada, TPU/JAX ou stack específica.
- Claims comerciais ou comparativos públicos sem avaliação própria.
- Foco excessivo em direito como se representasse todo o contexto brasileiro.
- Metas de volume grande nesta fase.
- Uso de dados, benchmarks ou questões sem licença e redistribuição claras.
- Treino de classificadores novos antes de avaliar classificadores existentes,
  heurísticas simples e amostras pequenas.

## Benchmarks Como Referência

### OAB-Bench

OAB-Bench pode inspirar avaliação jurídica estruturada com questões de escrita,
rubricas oficiais e avaliação por judge. Para o Oxigênio Brasil, a lição central
é a estrutura de rubrica e revisão, não a transformação do projeto em benchmark
jurídico.

### Magis-Bench

Magis-Bench pode inspirar tarefas discursivas de alta exigência, avaliação por
critérios oficiais e tratamento cuidadoso de respostas longas. O uso direto
depende de licença, escopo e risco de orientar indevidamente em domínio jurídico.

### MARCA

MARCA pode inspirar benchmarks agentic/search em português, especialmente quando
a tarefa envolve múltiplas entidades, verificação manual e checklists. O ponto
mais útil para o Oxigênio Brasil é medir rastreabilidade e completude, não apenas
acerto final.

### BRACEval

BRACEval deve ficar como referência candidata apenas se houver documentação,
licença e acesso suficientes. Sem isso, não deve ser incorporado a benchmark
interno nem citado como dependência.

## Gaps Onde Oxigênio Brasil Pode Diferenciar

- Biomas, clima e biodiversidade.
- Educação cívica.
- Educação financeira responsável.
- Segurança digital e golpes.
- Conhecimento regional e cultura.
- Direitos, limites e Constituição brasileira em linguagem cidadã.
- Governança de dados com origem, licença, PII, rejeição e metadados auditáveis.

## Regras Operacionais

- Não publicar claim comparativo contra Maritaca ou Sabiá.
- Não usar nomes de modelo, como `Oxigênio-1`, sem artefato real, model card,
  eval card, licença e benchmark mínimo.
- Não criar dataset, baixar pesos, fazer scraping ou iniciar treino a partir
  deste documento.
- Não adicionar dependência pesada por causa deste landscape.
- Não alterar a landing page pública com claims comparativos.
- Todo experimento futuro com modelo externo deve registrar modelo, provedor,
  versão, data, custo, licença, finalidade, prompt set e limitações.

## Referências Primárias

- ClassiCC-PT / corpus português: https://arxiv.org/abs/2509.08824
- Sabiá-4 Technical Report: https://arxiv.org/abs/2603.10213
- OAB-Bench: https://github.com/maritaca-ai/oab-bench
- Magis-Bench: https://github.com/maritaca-ai/magis-bench
- MARCA: https://github.com/maritaca-ai/MARCA
- Maritalk API client: https://github.com/maritaca-ai/maritalk-api
