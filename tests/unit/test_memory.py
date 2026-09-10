from pathlib import Path

from electrical_engineer.memory.store import CAP, excerpt, write_capped


def test_over_cap_summarises(tmp_path: Path) -> None:
    p = tmp_path / "facts.md"
    huge = "x" * (CAP + 100)
    out = write_capped(p, huge)
    assert len(out.encode()) <= CAP
    assert "summarised" in out
    assert excerpt(p) == out[:800]
