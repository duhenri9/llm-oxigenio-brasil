# Estratégia De Domínios Brasileiros Críticos

## 1. Propósito

Oxigênio Brasil deve ser avaliado onde um modelo Portuguese-first precisa ser útil
para a vida cotidiana no Brasil. A estratégia não transforma o projeto em modelo
especialista. Ela define domínios onde dados, avaliação e segurança precisam ser
tratados com mais rigor.

## 2. O Que Esta Estratégia É

- um mapa de governança;
- uma referência para coleta futura;
- uma base para benchmark PT-BR;
- uma forma de evitar claims genéricos sem prova.

## 3. O Que Esta Estratégia Não É

- autorização para scraping;
- dataset aprovado;
- promessa de treinamento;
- garantia de resposta correta em domínio sensível;
- claim de modelo especialista.

## 4. Biomas, Clima E Biodiversidade

Objetivo: responder sobre Amazônia, Cerrado, Caatinga, Mata Atlântica, Pantanal,
Pampa, litoral, espécies, clima e conservação com cuidado factual.

Fontes futuras devem priorizar instituições públicas, bases acadêmicas, órgãos de
pesquisa e materiais com licença clara. O modelo deve reconhecer incerteza, contexto
regional e diferença entre evidência científica, política pública e opinião.

## 5. Cidadania, Estado E Direito Público

Objetivo: explicar direitos, serviços públicos, deveres cívicos e caminhos oficiais
sem simular advogado, órgão público ou decisão jurídica.

O modelo deve orientar busca por fontes oficiais e evitar aconselhamento jurídico
individualizado.

## 6. Educação Cívica

Objetivo: apoiar compreensão de instituições, democracia, Constituição, políticas
públicas, orçamento e participação social.

A avaliação deve medir neutralidade, clareza, rastreabilidade e capacidade de separar
fato, processo institucional e opinião.

## 7. Educação Financeira Responsável

Objetivo: explicar conceitos de juros, dívida, orçamento, crédito, golpes financeiros
e planejamento básico sem recomendar investimento personalizado.

O modelo deve recusar promessas de ganho, simulações enganosas e orientações que
coloquem usuário vulnerável em risco.

## 8. Segurança Digital E Golpes

Objetivo: ajudar usuários a reconhecer phishing, fraude, engenharia social, golpes de
PIX, clonagem, falsos suportes e riscos comuns no Brasil.

O modelo deve priorizar prevenção, canais oficiais e passos seguros. Não deve ensinar
execução de golpe, evasão, invasão ou coleta de credenciais.

## 9. Conhecimento Regional E Cultura

Objetivo: respeitar diversidade regional, linguagem local, cultura popular, história,
culinária, geografia, manifestações culturais e contextos territoriais.

O projeto deve evitar apropriar conhecimento tradicional ou local sem fonte, contexto
e consentimento quando aplicável.

## 10. Estratégia De Dados

Antes de coletar qualquer amostra:

- registrar fonte no manifesto;
- avaliar licença;
- classificar risco de PII;
- classificar risco cultural e sensível;
- decidir se a fonte serve para metadata, avaliação, treinamento pequeno ou corpus;
- registrar rejeições.

## 11. Estratégia De Avaliação

Cada domínio deve ter perguntas com:

- resposta verificável;
- fonte pública;
- critério de correção;
- caso de incerteza;
- caso de recusa segura;
- revisão humana quando o risco for alto.

## 12. Estratégia De Segurança

Domínios brasileiros críticos exigem red-team específico para:

- alucinação com fonte falsa;
- conselho jurídico, médico ou financeiro indevido;
- desinformação eleitoral ou institucional;
- viés regional;
- exposição de PII;
- golpes digitais;
- uso indevido de conhecimento tradicional.

## 13. Próxima Versão

A próxima etapa não é treinamento. A próxima etapa é `data_pipeline/` pequeno,
auditável, com manifestos, filtros e amostras mínimas aprovadas.

