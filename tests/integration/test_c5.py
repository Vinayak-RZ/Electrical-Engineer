from electrical_engineer.catalog import load_recipe
from electrical_engineer.runner.execute import execute


def test_c5_confirm_required_no_silent_sim(tmp_path) -> None:
    recipe = load_recipe("control-diagram-to-model")
    acts = {n.activity for n in recipe.nodes.values()}
    assert "confirm-topology" in acts
    assert "run-python-control" not in acts
    assert "run-spice" not in acts
    out = execute("control-diagram-to-model", run_root=tmp_path)
    confirm = (tmp_path / "runs" / out["run_id"] / "nodes" / "confirm" / "out.json").read_text()
    assert '"simulate": false' in confirm
    assert '"confirmed": false' in confirm
