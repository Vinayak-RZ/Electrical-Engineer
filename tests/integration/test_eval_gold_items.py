from pathlib import Path


def test_circuits_and_unmatched_gold_exist() -> None:
    c = Path("eval/gold/circuits/divider-dc-01")
    u = Path("eval/gold/unmatched/open-ended-01")
    assert (c / "task.md").is_file()
    assert (c / "expect.json").is_file()
    assert (u / "task.md").is_file()
    assert (u / "expect.json").is_file()
    assert "solve-circuit-problem" in (c / "expect.json").read_text()
    assert "unchecked" in (u / "expect.json").read_text()
