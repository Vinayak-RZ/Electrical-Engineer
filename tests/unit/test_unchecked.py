from electrical_engineer.unchecked import UNCHECKED

SYNONYMS = ("unverified", "not simulated", "approx")


def requires_unchecked(text: str, summary: dict) -> bool:
    return UNCHECKED in text and summary.get("unchecked") is True


def test_exact_token_required() -> None:
    assert requires_unchecked("answer unchecked V=3", {"unchecked": True})


def test_synonym_fails() -> None:
    for s in SYNONYMS:
        assert not requires_unchecked(f"answer {s}", {"unchecked": False})
        assert UNCHECKED not in s
