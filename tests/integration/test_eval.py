from electrical_engineer.cli import main
from electrical_engineer.eval_runner.score import iter_items


def test_eval_pack_circuits_cli(capsys, tmp_path, monkeypatch) -> None:
    monkeypatch.chdir("/workspace")
    code = main(["eval", "--pack", "circuits"])
    out = capsys.readouterr().out
    assert "divider-dc-01" in out
    assert code in {0, 1}
    items = iter_items("circuits")
    assert items
