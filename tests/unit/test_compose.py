from electrical_engineer.compose.graph import ComposeError, compose


def test_over_cap_rejects() -> None:
    nodes = {f"n{i}": {"activity": "solve-explain"} for i in range(17)}
    try:
        compose({"nodes": nodes, "edges": []})
    except ComposeError as exc:
        assert "16" in str(exc)
    else:
        raise AssertionError("expected cap")
