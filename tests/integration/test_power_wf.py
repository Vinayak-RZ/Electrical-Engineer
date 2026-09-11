from electrical_engineer.catalog import load_recipe


def test_power_recipes_exist() -> None:
    assert load_recipe("solve-power-problem").id == "solve-power-problem"
    assert load_recipe("explain-power").id == "explain-power"
