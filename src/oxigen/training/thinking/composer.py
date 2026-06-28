"""Composicao de prompts curtos com biodiversidade e raciocinio."""

from __future__ import annotations

from .endangered_species import ENDANGERED_SPECIES, EndangeredSpecies, find_species
from .vocabulary import THINKING_PHASES, get_phase_tokens


def compose_thinking_prompt(
    species_name: str,
    phase: str = "observar",
    question: str | None = None,
) -> str:
    """Cria um prompt pequeno e rastreavel para dados sinteticos iniciais."""

    species = find_species(species_name) or ENDANGERED_SPECIES[0]
    tokens = get_phase_tokens(phase)
    base_question = question or "Qual e a menor acao segura para reduzir risco?"

    return "\n".join(
        [
            f"Especie: {species.common_name} ({species.scientific_name})",
            f"Bioma: {species.biome}",
            f"Status ICMBio: {species.icmbio_status}",
            f"Ameacas: {', '.join(species.threats)}",
            f"Fase de raciocinio: {phase}",
            f"Vocabulos: {', '.join(tokens[:6])}",
            f"Pergunta: {base_question}",
            "Responda em portugues brasileiro claro, separando evidencia, incerteza e proxima acao.",
        ],
    )


def compose_species_card(species: EndangeredSpecies) -> dict[str, str]:
    """Transforma uma especie em card simples para dataset ou avaliacao."""

    return {
        "common_name": species.common_name,
        "scientific_name": species.scientific_name,
        "biome": species.biome,
        "icmbio_status": species.icmbio_status,
        "iucn_status": species.iucn_status,
        "threats": ", ".join(species.threats),
        "reasoning_fact": species.reasoning_fact,
    }


def supported_phases() -> tuple[str, ...]:
    """Lista as fases de raciocinio disponiveis."""

    return tuple(THINKING_PHASES)
