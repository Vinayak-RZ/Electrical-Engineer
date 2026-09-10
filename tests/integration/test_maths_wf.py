from electrical_engineer.catalog import load_recipe


def test_maths_recipes_exist() -> None:
    assert load_recipe("solve-maths-for-ee").id == "solve-maths-for-ee"
    assert load_recipe("explain-maths-for-ee").id == "explain-maths-for-ee"
