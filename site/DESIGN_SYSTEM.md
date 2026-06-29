# Design System v0.1

## Direcao

Nome de trabalho: **Brazilian Research Interface**.

A LP deve parecer uma superficie editorial-cientifica brasileira: clara como
produto, rigorosa como pesquisa, brasileira no repertorio e sem copiar linguagem
visual de marcas existentes.

## Principios

- Brasil como criterio, nao ornamento.
- Pesquisa antes de marketing.
- Governanca visivel, nao escondida em rodape.
- Futuro sem neon, biomas sem folclore, rede sem blockchain.
- Artefatos visuais devem explicar metodo, nao decorar.
- Nada de chat, upload, formulario proprio, login ou coleta de prompts na LP v0.

## Tokens

### Cor

| Token | Uso |
| --- | --- |
| `--ink` | texto principal, fundos institucionais |
| `--paper` | fundo editorial quente |
| `--paper-strong` | areas de leitura e superficies de specimen |
| `--forest` | governanca, territorio, profundidade |
| `--leaf` | biomas, continuidade, redes vivas |
| `--river` | fonte, fluxo de dados, avaliacao |
| `--clay` | tensao, territorio, alerta |
| `--gold` | evidencia, destaque, chamada editorial |

### Tipografia

- Interface: sans moderna de sistema.
- Titulos: peso alto, ritmo editorial, sem efeito futurista.
- Evidencia tecnica: labels pequenos, uppercase controlado e numeros tabulares.
- Futuro: indicado por estrutura e contraste, nao por fonte sci-fi.

### Espacamento

- Secoes usam respiro amplo.
- Superficies de leitura usam bordas finas e grid.
- Componentes de decisao devem ter densidade maior que marketing cards.

## Componentes

### Hero

Apresenta o projeto como iniciativa para construir fundacao auditavel. O hero deve
mostrar territorio + rede + metodo, nao promessa de modelo pronto.

### StatusBand

Mostra o estado real: pre-alpha, sem modelo treinado, sem corpus aprovado e
governanca em construcao.

### DomainSpecimen

Substitui card generico. Cada dominio deve parecer um registro editorial-cientifico
com indice, taxonomia, criterio de avaliacao e risco de seguranca.

### EvidencePanel

Resume como o projeto ganha credibilidade: dados com trilha, avaliacao antes de
claim e seguranca por desenho.

### TrustSystem

Diagrama visual proprietario do fluxo minimo:

```txt
Fonte -> Licenca -> Metadados -> Rejeicao -> Avaliacao -> Modelo
```

Ele deve comunicar que a LP nao coleta dados automaticamente e que o treinamento
so acontece depois de revisao.

### TimeContrast

Contraste editorial entre 2026 e 2051. Nao e roadmap, promessa climatica ou
claim de impacto; e uma pergunta de governanca.

### ContributionNotice

Convite para comunidade via GitHub. Deve manter a frase de seguranca:
nenhuma contribuicao sera usada automaticamente para treinamento.

### SupportModal

CTA institucional de apoio financeiro. Deve abrir apenas por acao do usuario e
explicar que apoiar o projeto nao compra acesso, prioridade, influencia sobre
dados ou promessa de resultado.

Permitido:

- link para GitHub Sponsors;
- link para `SUPPORT.md`;
- link para relatorio financeiro;
- apoio institucional sem formulario proprio.

Proibido:

- popup automatico;
- sistema de pagamento embutido;
- script externo de pagamento;
- PIX direto na LP;
- linguagem de vaquinha ou promessa de retorno.

### RoadmapStep

Passos tecnicos pequenos, auditaveis e sem promessa de escala prematura.

## Proibicoes

- Nao usar `o2-zuca` em comunicacao publica.
- Nao usar `Oxi` como marca publica.
- Nao mencionar nomes de modelos especificos na LP v0.
- Nao transformar contribuições em dataset automaticamente.
- Nao adicionar formulario proprio, chat, upload ou login.
- Nao expor chave PIX pessoal na LP.
- Nao adicionar Stripe, checkout, tracking ou analytics.
