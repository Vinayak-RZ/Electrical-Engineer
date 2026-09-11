from pathlib import Path


def test_extensive_paths_exist() -> None:
    text = Path("docs/EXTENSIVE.md").read_text()
    for p in (
        "src/electrical_engineer/cli.py",
        "src/electrical_engineer/runner/execute.py",
        "ui/src/tokens.css",
        "docs/planning/T1_TRIALS.md",
        "eval/gold/",
        "assets/electrical-engineer-logo.svg",
        "docs/media/ui-empty.png",
    ):
        assert p in text
        if not p.endswith("/"):
            assert Path(p).exists()
    readme = Path("README.md").read_text()
    assert readme.count("docs/EXTENSIVE.md") >= 1
    assert "unchecked" in readme
    assert "PyPI" in readme  # named as not shipped
    assert "assets/electrical-engineer-logo.svg" in readme
    for rel in (
        "docs/media/ui-empty.png",
        "docs/media/ui-checked-run.png",
        "docs/media/ui-unchecked-confirm.png",
    ):
        assert rel in readme
        assert Path(rel).is_file()
        assert Path(rel).stat().st_size > 1000
