# Roadmap Técnico

## Escopo

Este roadmap organiza próximos passos técnicos sem transformar referências
externas em execução prematura. Ele não autoriza treino, coleta de corpus,
scraping, publicação de pesos ou claims públicos de desempenho.

## V1 -- Fundação Auditável

Status: em andamento.

- Documentar tese, domínios brasileiros críticos e limites do projeto.
- Registrar políticas de fonte, licença, PII, rejeição e metadados.
- Manter a landing page como apresentação segura, sem coleta de prompts, upload,
  login ou claims de modelo.

## V2 -- Data Pipeline Auditável

- Começar pequeno, com amostras verificáveis e reproduzíveis.
- Criar manifesto preenchido por fonte antes de qualquer coleta.
- Registrar licença, origem, risco de PII, risco cultural/sensível, rejeição,
  metadados e finalidade da amostra.
- Usar ClassiCC-PT como referência metodológica, não como alvo de volume.
- Não estabelecer volume grande como meta operacional nesta fase.
- Priorizar validadores locais, relatórios de qualidade e exemplos auditáveis.

## V3 -- Benchmark PT-BR v0

- Começar com poucas questões por domínio.
- Usar fontes públicas verificáveis e critérios de correção explícitos.
- Incluir revisão humana antes de qualquer ranking público.
- Inspirar-se em OAB-Bench, Magis-Bench e MARCA para rubricas, checklists e
  avaliação estruturada.
- Priorizar gaps do Oxigênio Brasil: biomas, cidadania, educação cívica,
  educação financeira responsável, segurança digital, cultura regional e
  direitos em linguagem cidadã.
- Registrar falhas em eval cards e failure cards, não apenas acertos.

## V4 -- Teacher/Judge Bake-off

- Avaliar modelos externos como baseline, teacher ou judge quando licença, custo
  e disponibilidade permitirem.
- Considerar Sabiá via API, GLM, Qwen, Llama, Mistral, Gemma e outros candidatos
  sem criar dependência central de modelo fechado.
- Registrar modelo, provedor, versão, data, custo, licença, finalidade, prompt
  set e limitações de cada uso.
- Comparar qualidade em português brasileiro, rastreabilidade, segurança,
  calibração de incerteza e domínios brasileiros críticos.

## V5 -- SFT/LoRA Pequeno

- Executar apenas depois de pipeline auditável, benchmark v0, eval card, failure
  cards e revisão de licença.
- Usar amostras pequenas e rastreáveis antes de qualquer escala.
- Manter model card e eval card como pré-requisitos para publicação.
- Evitar nomes públicos de modelo até haver artefato técnico real.

## Fora De Escopo Agora

- Treino de modelo.
- Download de pesos.
- Dataset real ou corpus grande.
- Scraping.
- Dependências pesadas de ML.
- Claims comparativos na landing page pública.
