"""Vocabulario inicial de raciocinio derivado de oxigenio, biomas e pesquisa."""

from __future__ import annotations

THINKING_PHASES: dict[str, tuple[str, ...]] = {
    "observar": (
        "observar",
        "respirar",
        "escutar",
        "mapear",
        "notar",
        "descrever",
        "situar",
        "contextualizar",
        "perceber",
        "levantar evidencias",
        "read the ecosystem",
        "trace the signal",
    ),
    "decompor": (
        "decompor",
        "separar camadas",
        "isolar variaveis",
        "distinguir bioma",
        "distinguir ameaca",
        "separar causa e efeito",
        "identificar dependencia",
        "abrir o problema",
        "split the habitat",
        "find the constraint",
    ),
    "relacionar": (
        "conectar",
        "correlacionar",
        "ligar habitat e risco",
        "comparar especies",
        "conectar clima e territorio",
        "cruzar fonte",
        "ver padrao",
        "connect the canopy",
        "link evidence",
    ),
    "decidir": (
        "priorizar",
        "escolher menor acao",
        "reduzir dano",
        "rejeitar excesso",
        "definir criterio",
        "escolher proxima validacao",
        "decidir com incerteza",
        "choose the smallest safe step",
    ),
    "verificar": (
        "testar",
        "validar",
        "checar fonte",
        "medir impacto",
        "procurar contradicao",
        "auditar",
        "revisar licenca",
        "verify the claim",
        "stress the assumption",
    ),
    "regenerar": (
        "regenerar",
        "restaurar",
        "recompor",
        "reflorestar",
        "proteger nascente",
        "abrir corredor",
        "reduzir pressao",
        "restore the system",
        "let the data breathe",
    ),
}


def get_phase_tokens(phase: str) -> tuple[str, ...]:
    """Retorna tokens de uma fase de raciocinio."""

    return THINKING_PHASES[phase]


def all_tokens() -> tuple[str, ...]:
    """Retorna todos os tokens preservando ordem de fases."""

    return tuple(token for tokens in THINKING_PHASES.values() for token in tokens)
