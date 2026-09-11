from electrical_engineer.catalog import load_recipe


def test_electronics_recipes_exist() -> None:
    assert load_recipe("solve-electronics-problem").id == "solve-electronics-problem"
    assert load_recipe("explain-electronics").id == "explain-electronics"
