# Política De PII E Dados Sensíveis

## Objetivo

Evitar que o Oxigênio Brasil colete, treine, publique ou redistribua dado pessoal,
dado sensível ou material que exponha pessoas, comunidades ou instituições.

## Definições Operacionais

PII inclui qualquer dado que identifique ou possa identificar uma pessoa:

- nome completo combinado com contexto;
- CPF, RG, telefone, email, endereço, IP ou identificador unico;
- dados escolares, financeiros, jurídicos, médicos ou trabalhistas;
- imagens, áudio ou transcrições identificáveis;
- historico de conversas privadas.

Dados sensíveis incluem:

- saúde;
- origem racial ou étnica;
- religiao;
- opinião política;
- filiação sindical;
- vida sexual;
- biometria;
- dados de crianças e adolescentes;
- conhecimento tradicional ou local que exija consentimento contextual.

## Regra De Uso

- Não usar PII real para treinamento.
- Não publicar exemplos com PII real.
- Não depender de remoção automática como unica camada de segurança.
- Não aceitar datasets de terceiros sem licença e prova de origem.
- Não incluir dados de comunidades vulneráveis sem revisão humana e protocolo.

## Ações Futuras

Antes do data pipeline, criar validadores para:

- padrões de CPF, CNPJ, telefone, email e endereço;
- nomes combinados com dados de contato;
- texto com alto risco médico, financeiro, jurídico ou educacional individualizado;
- amostras que exigem rejeição manual.

