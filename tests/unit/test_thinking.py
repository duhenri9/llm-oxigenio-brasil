from oxigen.training.thinking import (
    ENDANGERED_SPECIES,
    compose_thinking_prompt,
    get_phase_tokens,
)


def test_endangered_species_seed_has_expected_size() -> None:
    assert len(ENDANGERED_SPECIES) == 16


def test_compose_thinking_prompt_includes_species_and_question() -> None:
    prompt = compose_thinking_prompt("Onca-pintada", phase="verificar")

    assert "Onca-pintada" in prompt
    assert "Pergunta:" in prompt
    assert "evidencia" in prompt


def test_get_phase_tokens_returns_phase_vocabulary() -> None:
    tokens = get_phase_tokens("decidir")

    assert "priorizar" in tokens
