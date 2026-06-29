# Design System v0.1

## Direção

Nome de trabalho: **Brazilian Research Interface**.

A LP deve parecer uma superfície editorial-científica brasileira: clara como
produto, rigorosa como pesquisa, brasileira no repertório e sem copiar linguagem
visual de marcas existentes.

## Princípios

- Brasil como critério, não ornamento.
- Pesquisa antes de marketing.
- Governança visível, não escondida em rodapé.
- Futuro sem neon, biomas sem folclore, rede sem blockchain.
- Artefatos visuais devem explicar método, não decorar.
- Nada de chat, upload, formulário próprio, login ou coleta de prompts na LP v0.

## Tokens

### Cor

| Token | Uso |
| --- | --- |
| `--ink` | texto principal, fundos institucionais |
| `--paper` | fundo editorial quente |
| `--paper-strong` | áreas de leitura e superfícies de specimen |
| `--forest` | governança, território, profundidade |
| `--leaf` | biomas, continuidade, redes vivas |
| `--river` | fonte, fluxo de dados, avaliação |
| `--clay` | tensão, território, alerta |
| `--gold` | evidência, destaque, chamada editorial |

### Tipografia

- Interface: sans moderna de sistema.
- Títulos: peso alto, ritmo editorial, sem efeito futurista.
- Evidência técnica: labels pequenos, uppercase controlado e números tabulares.
- Futuro: indicado por estrutura e contraste, não por fonte sci-fi.

### Espaçamento

- Seções usam respiro amplo.
- Superfícies de leitura usam bordas finas e grid.
- Componentes de decisão devem ter densidade maior que marketing cards.

## Componentes

### Hero

Apresenta o projeto como iniciativa para construir fundação auditável. O hero deve
mostrar território + rede + método, não promessa de modelo pronto. Também deve
ter uma frase em linguagem simples para explicar a intenção a visitantes não técnicos.

### StatusBand

Mostra o estado real: pre-alpha, sem modelo treinado, sem corpus aprovado e
governança em construção.

### DomainSpecimen

Substitui card genérico. Cada domínio deve parecer um registro editorial-científico
com índice, taxonomia, critério de avaliação e risco de segurança.

### EvidencePanel

Resume como o projeto ganha credibilidade: dados com trilha, avaliação antes de
claim e segurança por desenho.

### TrustSystem

Diagrama visual proprietário do fluxo mínimo:

```txt
Fonte -> Licença -> Metadados -> Rejeição -> Avaliação -> Modelo
```

Ele deve comunicar que a LP não coleta dados automaticamente e que o treinamento
só acontece depois de revisão.

### TimeContrast

Contraste editorial entre 2026 e 2051. Não é roadmap, promessa climática ou
claim de impacto; é uma pergunta de governança sobre que conhecimento o Brasil
quer preservar, auditar e tornar acessível.

### ContributionNotice

Convite para comunidade via GitHub. Deve manter a frase de segurança:
nenhuma contribuição será usada automaticamente para treinamento. Também deve
dar exemplos concretos de participação futura, como sugerir fontes, revisar
perguntas, apontar riscos e avaliar clareza em português brasileiro.

### SupportModal

CTA institucional de apoio financeiro. Deve abrir apenas por ação do usuário e
explicar que apoiar o projeto não compra acesso, prioridade, influência sobre
dados ou promessa de resultado.

Permitido:

- link para GitHub Sponsors;
- link para `SUPPORT.md`;
- link para relatório financeiro;
- apoio institucional sem formulário próprio.

Proibido:

- popup automático;
- sistema de pagamento embutido;
- script externo de pagamento;
- PIX direto na LP;
- linguagem de vaquinha ou promessa de retorno.

### RoadmapStep

Passos técnicos pequenos, auditáveis e sem promessa de escala prematura.

## Proibições

- Não usar `o2-zuca` em comunicação pública.
- Não usar `Oxi` como marca pública.
- Não mencionar nomes de modelos específicos na LP v0.
- Não transformar contribuições em dataset automaticamente.
- Não adicionar formulário próprio, chat, upload ou login.
- Não expor chave PIX pessoal na LP.
- Não adicionar Stripe, checkout, tracking ou analytics.
