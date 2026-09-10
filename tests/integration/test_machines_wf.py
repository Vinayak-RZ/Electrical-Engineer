from electrical_engineer.catalog import load_recipe


def test_machines_recipes_exist() -> None:
    assert load_recipe("solve-machines-problem").id == "solve-machines-problem"
    assert load_recipe("explain-machines").id == "explain-machines"
