from electrical_engineer.catalog import load_recipe
from electrical_engineer.nodes import sim as _sim  # noqa: F401
from electrical_engineer.nodes.registry import get
from electrical_engineer.runner.execute import execute
from electrical_engineer.unchecked import UNCHECKED


def test_unconfirmed_spice_rejected(tmp_path) -> None:
    recipe = load_recipe("simulate-after-confirm")
    assert recipe.nodes["spice"].extras.get("require_confirmed") is True
    out = execute("simulate-after-confirm", run_root=tmp_path)
    assert out["summary"]["token"] == UNCHECKED
    spice = (tmp_path / "runs" / out["run_id"] / "nodes" / "spice" / "out.json").read_text()
    assert "unconfirmed" in spice


def test_confirmed_still_honest_without_ngspice(tmp_path) -> None:
    run = tmp_path / "runs" / "pre"
    run.mkdir(parents=True)
    # execute creates its own run id; drop confirmed into that dir after? 
    # instead call run-spice with run_dir that has confirmed.json
    from electrical_engineer.nodes.registry import get

    d = tmp_path / "conf"
    d.mkdir()
    (d / "confirmed.json").write_text('{"confirmed": true}')
    out = get("run-spice")({"id": "sp", "require_confirmed": True, "run_dir": str(d), "repair_max": 0}, {})
    assert "unconfirmed" not in out.get("error", "")
    assert out["ok"] is False  # ngspice still missing
