from pathlib import Path


def test_no_wan_bind_in_product() -> None:
    for path in Path("src").rglob("*.py"):
        text = path.read_text()
        if "0.0.0.0" in text:
            raise AssertionError(path)


def test_no_cordis_dep() -> None:
    blob = Path("pyproject.toml").read_text()
    assert "cordis" not in blob.lower()
    assert "deepseek" not in blob.lower()


def test_css_tokens_not_raw_sprawl() -> None:
    css = Path("ui/src/tokens.css").read_text()
    assert "--ee-color-primary" in css
    jsx = Path("ui/src/slots/root.jsx").read_text()
    assert "#0052ff" not in jsx
