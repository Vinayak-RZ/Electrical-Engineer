from electrical_engineer.runner.fsm import parse_recipe, ready_ids, run_fsm, RunnerError


def _echo(_spec: dict, inputs: dict) -> dict:
    return {"ok": True, "seen": sorted(inputs)}


def test_ready_order_sorted() -> None:
    recipe = parse_recipe(
        {
            "id": "t",
            "nodes": {
                "b": {"activity": "echo", "needs": ["a"]},
                "c": {"activity": "echo", "needs": ["a"]},
                "a": {"activity": "echo"},
            },
        }
    )
    assert ready_ids(recipe, {}) == ["a"]
    assert ready_ids(recipe, {"a": {}}) == ["b", "c"]


def test_run_diamond() -> None:
    recipe = parse_recipe(
        {
            "id": "diamond",
            "nodes": {
                "a": {"activity": "echo"},
                "b": {"activity": "echo", "needs": ["a"]},
                "c": {"activity": "echo", "needs": ["a"]},
                "d": {"activity": "echo", "needs": ["b", "c"]},
            },
        }
    )
    out = run_fsm(recipe, {"echo": _echo})
    assert set(out) == {"a", "b", "c", "d"}
    assert out["d"]["seen"] == ["b", "c"]


def test_cycle_rejected() -> None:
    try:
        parse_recipe(
            {
                "id": "loop",
                "nodes": {
                    "a": {"activity": "echo", "needs": ["b"]},
                    "b": {"activity": "echo", "needs": ["a"]},
                },
            }
        )
    except RunnerError as exc:
        assert "cycle" in str(exc)
    else:
        raise AssertionError("expected cycle")
