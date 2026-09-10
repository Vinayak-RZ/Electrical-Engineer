from pathlib import Path


def test_css_vars_match_design() -> None:
    css = Path("ui/src/tokens.css").read_text()
    assert "--ee-color-canvas: #ffffff" in css
    assert "--ee-color-ink: #0a0b0d" in css
    assert "--ee-color-primary: #0052ff" in css
    assert "Inter" in css
