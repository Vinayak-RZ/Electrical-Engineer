from electrical_engineer.catalog import load_recipe


def test_measurements_recipes_exist() -> None:
    assert load_recipe("solve-measurements-problem").id == "solve-measurements-problem"
    assert load_recipe("explain-measurements").id == "explain-measurements"
