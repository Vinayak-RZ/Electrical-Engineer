from pathlib import Path


def test_spike_results_pick_bm25() -> None:
    text = Path("research/notes/rag-spike-results-2026-09.md").read_text()
    assert "**bm25**" in text
    assert "empty" in text.lower()
    assert "LightRAG" in text
    assert "commercial" in Path("research/notes/rag-spike-2026-09.md").read_text().lower()
