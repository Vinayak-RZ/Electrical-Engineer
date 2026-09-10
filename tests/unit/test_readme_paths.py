from pathlib import Path


def test_extensive_paths_exist() -> None:
    text = Path("docs/EXTENSIVE.md").read_text()
    for p in (
        "src/electrical_engineer/cli.py",
        "src/electrical_engineer/runner/execute.py",
        "ui/src/tokens.css",
        "docs/planning/T1_TRIALS.md",
        "eval/gold/",
    ):
        assert p in text
        if not p.endswith("/"):
            assert Path(p).exists()
    assert Path("README.md").read_text().count("docs/EXTENSIVE.md") >= 1
    assert "unchecked" in Path("README.md").read_text()
    assert "PyPI" in Path("README.md").read_text()  # named as not shipped
