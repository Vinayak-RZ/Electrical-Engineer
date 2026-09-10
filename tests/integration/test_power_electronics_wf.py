from electrical_engineer.catalog import load_recipe


def test_power_electronics_recipes_exist() -> None:
    assert load_recipe("solve-power-electronics-problem").id == "solve-power-electronics-problem"
    assert load_recipe("explain-power-electronics").id == "explain-power-electronics"
