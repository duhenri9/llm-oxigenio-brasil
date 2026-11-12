# Vercel Retirement Record — oxigenio-brasil

**Data:** 12/11/2026 · **Owner:** WM3 / fundador · **Status:** PREPARED / NOT DELETED.  
**Política:** WM3 Blueprint, `WM3-GOV-VERCEL-RETIRE-2026-11-12`.  
**Autorização:** política de remover projetos não prioritários APROVADA; exclusão individual pela interface da Vercel ainda não confirmada.

## Prova de fonte versionada

- Projeto Vercel: `oxigenio-brasil` (`prj_64YIQHqwFIIVyg0j62dzq80lULFM`), equipe `eduardo-henrique-ananias-projects`.
- Deployment production READY consultado: `dpl_97Kx3kkup2jP5pPdBtw16ieEGC2d`.
- GitHub source: https://github.com/duhenri9/llm-oxigenio-brasil
- **SHA exato do deploy de produção:** `b15dd0a2b9333e548d05e0fcd7145d84bcbf2eac` (objeto de commit confirmado no GitHub).
- **Ref de preservação criada:** `archive/vercel-production-2026-11-12` apontando para esse SHA; caso a main evolua, usar esta ref para reproduzir a versão publicada.
- Domínios de projeto: `oxigenio-brasil.vercel.app` e URLs padrão de branch/equipe `*.vercel.app`. **Nenhum domínio personalizado identificado** em preflight.
- Variáveis de ambiente listadas pela API Vercel: **nenhuma**. Valores secretos não foram consultados.

## Decisão e escopo

**Categoria:** CANDIDATE_GITHUB_CONFIRMED; não integra o foco comercial Recupera Lead/ProofLayer vigente.  
**Justificativa:** projeto de portfólio/experimental fora da prioridade comercial; verificar se serve de demonstração/recrutamento.  
**Preservado:** Git source e assets versionados, scripts, documentação, arquivo de licença que estiver versionado, SHA completo de produção.  
**NÃO garantido por Git:** env externo, Vercel deployment history, storage, logs, DNS, domínio, banco, pagamentos, sessões, analytics, links de terceiros ou dados operacionais; ausência de env não é prova de que tudo está contido em Git.

## Gates finais antes de deletar

- [ ] Confirmar que nenhum cliente, teste pago, candidatura, parceiro, campanha, webhook/callback ou domínio externo ainda exige a URL.
- [ ] Verificar conteúdo persistido em providers externos/Blob e não haver dados de usuário que precisem ser exportados ou mantidos.
- [ ] Confirmar build e forma de reconstrução: checkout de `archive/vercel-production-2026-11-12`; instalar dependências conforme lockfile; configurar somente segredos legítimos em vault de nova plataforma; testes/build/QA antes de redeploy.
- [ ] Concluir revisão da PR de documentação e conferir `production` alias vigente.
- [ ] Titular confirmar exclusão no painel Vercel e registrar data.
- [ ] Reconsultar ID do projeto, aliases, DNS/consumidores depois da exclusão. Só então mudar o status para `DELETED_CONFIRMED`.

## Ponto de exclusão — confirmação manual obrigatória

**Vercel:** https://vercel.com/d?to=%2Feduardo-henrique-ananias-projects%2Foxigenio-brasil%2Fsettings%2Fgeneral%23delete-project&title=Review+in+Vercel

A integração Vercel disponibiliza a tela de exclusão, **não executa a exclusão** por ferramenta. Nenhum pagamento, domínio, URL ou execução do produto é modificado por esta PR.

## Restauração deliberada

Para reimplantar: recuperar o código com `git checkout archive/vercel-production-2026-11-12` (ou SHA `b15dd0a2b9333e548d05e0fcd7145d84bcbf2eac`); validar requisitos de runtime do README/package; configurar autenticação/DB/variáveis em gerenciador seguro conforme necessidade; testar a build e ambiente antes de apontar domínios. A URL `vercel.app` anterior e histórico da Vercel não são garantidos.

**Receipt:** CODIFIED SOURCE = CONFIRMED · LOCAL ENV NAMES = NONE · CUSTOM DOMAIN = NONE DETECTED · BUSINESS/EXTERNAL CONSUMERS = UNKNOWN · VERCEL DELETE = NOT PERFORMED.
