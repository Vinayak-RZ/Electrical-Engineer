from electrical_engineer.catalog import load_recipe
from electrical_engineer.runner.execute import execute


def test_derive_circuit_yaml_loads() -> None:
    assert load_recipe("derive-circuit").id == "derive-circuit"


def test_derive_voltage_divider(tmp_path) -> None:
    out = execute(
        "derive-circuit",
        run_root=tmp_path,
        problem={"kind": "voltage_divider", "vin": 10, "r1": 1000, "r2": 1000, "expected": 5.0},
    )
    summary = out["summary"]
    assert summary["unchecked"] is False
    assert abs(float(summary["value"]) - 5.0) < 1e-9
