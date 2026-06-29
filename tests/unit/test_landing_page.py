from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE_INDEX = ROOT / "site" / "index.html"


def read_index() -> str:
    return SITE_INDEX.read_text(encoding="utf-8")


def test_landing_page_exists() -> None:
    assert SITE_INDEX.exists()


def test_landing_page_has_no_first_party_data_collection_form() -> None:
    html = read_index().casefold()

    assert "<form" not in html
    assert "<input" not in html
    assert "<textarea" not in html
    assert "upload" not in html


def test_landing_page_states_contributions_are_not_automatic_training_data() -> None:
    html = read_index()

    assert "Nenhuma contribuicao sera usada automaticamente para treinamento." in html
    assert "revisao, consentimento, metadados" in html


def test_landing_page_points_contribution_to_github() -> None:
    html = read_index()

    assert "issues/new?template=data_contribution.md" in html
    assert "github.com/duhenri9/llm-oxigenio-brasil" in html
