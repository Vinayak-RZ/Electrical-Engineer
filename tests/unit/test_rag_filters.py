from electrical_engineer.rag.inventory import add_doc
from electrical_engineer.rag.retrieve import retrieve


def test_empty_retrieval_visible(tmp_path) -> None:
    (tmp_path / "workflows").mkdir()
    out = retrieve({"book_id": "missing"}, cwd=tmp_path)
    assert out["empty"] is True
    assert out["passages"] == []


def test_filters_book_and_chapter(tmp_path) -> None:
    (tmp_path / "workflows").mkdir()
    rag = tmp_path / ".electrical-engineer" / "rag"
    rag.mkdir(parents=True)
    chapter = rag / "ch1.md"
    chapter.write_text("KVL around a loop.")
    add_doc("ch1.md", tags={"book_id": "own", "chapter_id": "1", "domain_tag": "circuits"}, cwd=tmp_path)
    hit = retrieve({"book_id": "own", "chapter_id": "1"}, cwd=tmp_path)
    assert hit["empty"] is False
    assert hit["passages"][0]["book_id"] == "own"
    miss = retrieve({"book_id": "own", "chapter_id": "99"}, cwd=tmp_path)
    assert miss["empty"] is True
