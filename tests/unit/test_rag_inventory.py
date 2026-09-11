from electrical_engineer.cli import main
from electrical_engineer.rag.inventory import load_inventory


def test_rag_list_cli(capsys, tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / "workflows").mkdir()
    (tmp_path / "note.md").write_text("owned chapter")
    assert main(["rag", "add", str(tmp_path / "note.md"), "--book-id", "own-01", "--licence-tag", "CC-BY"]) == 0
    assert main(["rag", "list"]) == 0
    out = capsys.readouterr().out
    assert "note.md" in out
    items = load_inventory(tmp_path)
    assert items[0]["book_id"] == "own-01"
    assert items[0]["licence_tag"] == "CC-BY"
    assert items[0]["untrusted"] is True
