from pathlib import Path


def test_host_docs_exist() -> None:
    base = Path("docs/hosts")
    for name in ("README.md", "cursor.md", "claude-code.md", "openai.md"):
        text = (base / name).read_text()
        assert "electrical-engineer mcp" in text or "stdio" in text.lower()
