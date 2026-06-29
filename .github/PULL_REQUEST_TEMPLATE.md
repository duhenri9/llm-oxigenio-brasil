# Resumo

Explique a mudança em poucas linhas.

## Checklist De Segurança

- [ ] Não inclui `.env`, token, chave, segredo ou credencial.
- [ ] Não inclui dataset bruto, checkpoint, peso de modelo ou dump de usuário.
- [ ] Não inicia coleta massiva, treinamento, inferência pública ou GPU.
- [ ] Não adiciona dependência pesada de ML ao runtime sem justificativa dedicada.
- [ ] Atualiza documentos de governança quando altera dados, modelo ou avaliação.

## Validação

- [ ] `python -m compileall src`
- [ ] `python -m pytest tests/unit/ -v`
- [ ] `python -m ruff check src tests`
- [ ] `python -m ruff format --check src tests`
- [ ] `python -m mypy src`

## Decisões

Liste decisões técnicas relevantes e alternativas rejeitadas.

