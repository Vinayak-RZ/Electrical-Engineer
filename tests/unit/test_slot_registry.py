from pathlib import Path


def test_registry_exports() -> None:
    text = Path("ui/src/slots/registry.js").read_text()
    assert "export function register" in text
    assert "export function renderSlot" in text
