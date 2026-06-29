import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE_INDEX = ROOT / "site" / "index.html"
SITE_SCRIPT = ROOT / "site" / "main.js"
SITE_DESIGN_SYSTEM = ROOT / "site" / "DESIGN_SYSTEM.md"


def read_index() -> str:
    return SITE_INDEX.read_text(encoding="utf-8")


def read_script() -> str:
    return SITE_SCRIPT.read_text(encoding="utf-8")


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def test_landing_page_exists() -> None:
    assert SITE_INDEX.exists()


def test_design_system_exists() -> None:
    assert SITE_DESIGN_SYSTEM.exists()


def test_landing_page_has_no_first_party_data_collection_form() -> None:
    html = read_index().casefold()

    assert "<form" not in html
    assert "<input" not in html
    assert "<textarea" not in html
    assert "upload" not in html


def test_landing_page_has_no_embedded_payment_or_tracking() -> None:
    combined = f"{read_index()}\n{read_script()}".casefold()

    assert "stripe" not in combined
    assert "checkout" not in combined
    assert "paypal" not in combined
    assert "mercadopago" not in combined
    assert "picpay" not in combined
    assert "analytics" not in combined
    assert "gtag" not in combined
    assert "11950377457" not in combined


def test_landing_page_states_contributions_are_not_automatic_training_data() -> None:
    html = read_index()

    assert "Nenhuma contribuição será usada automaticamente para treinamento." in html
    assert "revisão, consentimento, metadados" in html


def test_landing_page_points_contribution_to_github() -> None:
    html = read_index()

    assert "issues/new?template=data_contribution.md" in html
    assert "github.com/duhenri9/llm-oxigenio-brasil" in html


def test_landing_page_has_2026_2051_narrative_without_future_promise() -> None:
    html = read_index()
    normalized = normalize_whitespace(html)

    assert "2026" in html
    assert "2051" in html
    assert "O Brasil que temos" in html
    assert "O Brasil que podemos ter" in html
    assert "que conhecimento o Brasil quer preservar, auditar e tornar acessível" in normalized
    assert "não promete chegar a 2051" in html


def test_landing_page_explains_project_in_plain_language() -> None:
    html = normalize_whitespace(read_index())

    assert "Em termos simples" in html
    assert "futuros modelos de IA entendam melhor o português brasileiro" in html
    assert "Portuguese-first significa começar pelo português brasileiro" in html
    assert "Modelos de linguagem são sistemas de IA capazes de ler" in html


def test_landing_page_makes_future_contribution_concrete() -> None:
    html = normalize_whitespace(read_index())

    assert "Você poderá contribuir sugerindo fontes públicas" in html
    assert "revisando perguntas" in html
    assert "apontando riscos" in html
    assert "avaliar se o modelo fala português brasileiro com clareza" in html


def test_landing_page_keeps_model_names_out_of_public_copy() -> None:
    html = read_index()

    assert "Qwen" not in html
    assert "GLM" not in html
    assert "Oxigenio-1" not in html
    assert "Oxigênio-1" not in html


def test_landing_page_keeps_internal_or_informal_names_out_of_public_copy() -> None:
    html = read_index()

    assert "o2-zuca" not in html.casefold()
    assert re.search(r"\bOxi\b", html) is None
    assert "O2" not in html


def test_landing_page_has_trust_system_flow() -> None:
    html = read_index()

    assert "Sistema de confiança" in html
    assert "Fonte" in html
    assert "Licença" in html
    assert "Metadados" in html
    assert "Rejeição" in html
    assert "Avaliação" in html
    assert "somente depois de evidência" in html


def test_landing_page_has_public_commitments_from_research_foundation() -> None:
    html = normalize_whitespace(read_index())

    assert "Compromissos públicos" in html
    assert "O Oxigênio Brasil não começa pelo modelo" in html
    assert "Sem fonte, sem dado." in html
    assert "Sem benchmark, sem promessa." in html
    assert "Sem revisão, sem treino." in html
    assert "Sem esconder falhas." in html
    assert "Dados não entram por volume" in html
    assert "risco, finalidade e decisão documentada" in html
    assert "amostras precisam passar por revisão humana e segurança contextual" in html
    assert "golpes digitais, desinformação, dados pessoais e comunidades vulneráveis" in html
    assert "como documenta esses erros" in html


def test_landing_page_has_user_triggered_support_modal() -> None:
    html = read_index()
    script = read_script()

    assert "Apoiar o Oxigênio Brasil" in html
    assert "Apoiar pesquisa aberta" in html
    assert "SUPPORT.md" in html
    assert "github.com/sponsors/duhenri9" in html
    assert re.search(r"<dialog[^>]*\sopen\b", html, re.IGNORECASE | re.DOTALL) is None
    assert "data-support-open" in html
    assert "showModal()" in script
