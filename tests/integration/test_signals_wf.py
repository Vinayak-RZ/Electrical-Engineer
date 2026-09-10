from electrical_engineer.catalog import load_recipe


def test_signals_recipes_exist() -> None:
    assert load_recipe("solve-signals-problem").id == "solve-signals-problem"
    assert load_recipe("explain-signals").id == "explain-signals"
