from electrical_engineer.catalog import load_recipe


def test_solve_circuit_problem_yaml_loads() -> None:
    recipe = load_recipe("solve-circuit-problem")
    assert recipe.id == "solve-circuit-problem"
    assert "check" in recipe.nodes
