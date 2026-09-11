from pathlib import Path

from electrical_engineer.catalog import load_recipe
from electrical_engineer.runner.execute import execute


def test_solve_circuit_problem_yaml_loads() -> None:
    recipe = load_recipe("solve-circuit-problem")
    assert recipe.id == "solve-circuit-problem"
    assert "check" in recipe.nodes


def test_solve_circuit_run_dir(tmp_path) -> None:
    out = execute(
        "solve-circuit-problem",
        run_root=tmp_path,
        problem={"kind": "voltage_divider", "vin": 10, "r1": 1000, "r2": 1000, "expected": 5.0},
    )
    summary_path = Path(out["run_dir"]) / "summary.json"
    assert summary_path.is_file()
    assert out["summary"]["recipe_id"] == "solve-circuit-problem"
    assert out["summary"]["unchecked"] is False
    assert abs(float(out["summary"]["value"]) - 5.0) < 1e-9
    assert (tmp_path / "runs" / out["run_id"]).is_dir()


def test_cli_run_solve_circuit_problem(capsys) -> None:
    from electrical_engineer.cli import main

    assert main(["run", "solve-circuit-problem"]) == 0
    assert "solve-circuit-problem" in capsys.readouterr().out
