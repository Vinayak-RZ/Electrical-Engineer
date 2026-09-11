from electrical_engineer.router.hybrid import UNMATCHED, route


def test_explicit_skips_classify() -> None:
    r = route("solve-circuit-problem", [("unmatched-cosolver", 0.99)])
    assert r.kind == "explicit"
    assert r.recipe_id == "solve-circuit-problem"


def test_close_scores_ask() -> None:
    r = route(None, [("solve-circuit-problem", 0.40), ("explain-circuits", 0.30)])
    assert r.kind == "ask"
    assert r.recipe_id is None


def test_unmatched_fallback() -> None:
    r = route(None, [])
    assert r.recipe_id == UNMATCHED
    r = route(None, [("solve-circuit-problem", 0.0)])
    assert r.kind == "unmatched"
