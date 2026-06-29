# Landing Page V0

Site estático da LP pública inicial do Oxigênio Brasil.

## Design System

Leia [`DESIGN_SYSTEM.md`](DESIGN_SYSTEM.md) antes de alterar layout, tokens,
componentes ou direção visual da LP.

## Escopo

- apresenta a tese pública do projeto;
- traduz a tese para visitantes que não conhecem IA, LLM ou open-source;
- mostra domínios brasileiros críticos;
- explica governança antes de treinamento;
- direciona contribuições para GitHub;
- inclui CTA institucional de apoio por modal acionado pelo usuário;
- não coleta conversas;
- não possui formulário próprio;
- não possui login;
- não usa contribuições automaticamente para treino.
- não embute pagamento, PIX, tracking ou analytics.

## Rodar Localmente

Abrir `site/index.html` diretamente no navegador ou servir estaticamente:

```bash
python -m http.server 8000 --directory site
```
