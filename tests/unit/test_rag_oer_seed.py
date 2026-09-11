from pathlib import Path

from electrical_engineer.rag.retrieve import retrieve


def test_perturbed_ohms_query_hits_chapter_2() -> None:
    out = retrieve(
        {"book_id": "kuphaldt-dc"},
        query="How voltage, current, and resistance relate Ohm's law",
        cwd=Path("."),
    )
    assert out["empty"] is False
    assert out["passages"][0]["chapter_id"] == "2"
    assert out["passages"][0]["book_id"] == "kuphaldt-dc"


def test_kvl_query_hits_chapter_6() -> None:
    out = retrieve(
        {"book_id": "kuphaldt-dc"},
        query="Kirchhoff's Voltage Law KVL voltage divider circuits",
        cwd=Path("."),
    )
    assert out["empty"] is False
    assert out["passages"][0]["chapter_id"] == "6"


def test_wrong_chapter_filter_is_empty() -> None:
    out = retrieve(
        {"book_id": "kuphaldt-dc", "chapter_id": "99"},
        query="Ohm's law",
        cwd=Path("."),
    )
    assert out["empty"] is True
