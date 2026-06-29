# Resumo

Explique a mudanca em poucas linhas.

## Checklist De Seguranca

- [ ] Nao inclui `.env`, token, chave, segredo ou credencial.
- [ ] Nao inclui dataset bruto, checkpoint, peso de modelo ou dump de usuario.
- [ ] Nao inicia coleta massiva, treinamento, inferencia publica ou GPU.
- [ ] Nao adiciona dependencia pesada de ML ao runtime sem justificativa dedicada.
- [ ] Atualiza documentos de governanca quando altera dados, modelo ou avaliacao.

## Validacao

- [ ] `python -m compileall src`
- [ ] `python -m pytest tests/unit/ -v`
- [ ] `python -m ruff check src tests`
- [ ] `python -m ruff format --check src tests`
- [ ] `python -m mypy src`

## Decisoes

Liste decisoes tecnicas relevantes e alternativas rejeitadas.

