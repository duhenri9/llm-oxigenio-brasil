# Politica De PII E Dados Sensiveis

## Objetivo

Evitar que o Oxigenio Brasil colete, treine, publique ou redistribua dado pessoal,
dado sensivel ou material que exponha pessoas, comunidades ou instituicoes.

## Definicoes Operacionais

PII inclui qualquer dado que identifique ou possa identificar uma pessoa:

- nome completo combinado com contexto;
- CPF, RG, telefone, email, endereco, IP ou identificador unico;
- dados escolares, financeiros, juridicos, medicos ou trabalhistas;
- imagens, audio ou transcricoes identificaveis;
- historico de conversas privadas.

Dados sensiveis incluem:

- saude;
- origem racial ou etnica;
- religiao;
- opiniao politica;
- filiacao sindical;
- vida sexual;
- biometria;
- dados de criancas e adolescentes;
- conhecimento tradicional ou local que exija consentimento contextual.

## Regra De Uso

- Nao usar PII real para treinamento.
- Nao publicar exemplos com PII real.
- Nao depender de remocao automatica como unica camada de seguranca.
- Nao aceitar datasets de terceiros sem licenca e prova de origem.
- Nao incluir dados de comunidades vulneraveis sem revisao humana e protocolo.

## Acoes Futuras

Antes do data pipeline, criar validadores para:

- padroes de CPF, CNPJ, telefone, email e endereco;
- nomes combinados com dados de contato;
- texto com alto risco medico, financeiro, juridico ou educacional individualizado;
- amostras que exigem rejeicao manual.

