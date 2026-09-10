from electrical_engineer.catalog import load_recipe


def test_em_recipes_exist() -> None:
    assert load_recipe("solve-em-problem").id == "solve-em-problem"
    assert load_recipe("explain-em").id == "explain-em"
