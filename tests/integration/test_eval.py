from electrical_engineer.cli import main
from electrical_engineer.eval_runner.score import iter_items


def test_eval_pack_circuits_cli(capsys) -> None:
    """CI cwd is the checkout, not a Cloud Agent /workspace path."""
    code = main(["eval", "--pack", "circuits"])
    out = capsys.readouterr().out
    assert "divider-dc-01" in out
    assert code == 0
    assert iter_items("circuits")
