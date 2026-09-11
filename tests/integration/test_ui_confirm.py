from fastapi.testclient import TestClient

from electrical_engineer.ui_server.app import create_app


def test_confirm_does_not_simulate() -> None:
    client = TestClient(create_app())
    r = client.post("/api/runs/x/confirm")
    assert r.json()["confirmed"] is True
    assert r.json()["simulate"] is False


def test_confirm_writes_flag(tmp_path) -> None:
    client = TestClient(create_app(tmp_path))
    client.post("/api/runs/x/confirm")
    flag = (tmp_path / "runs" / "x" / "confirmed.json").read_text()
    assert '"simulate": false' in flag
    assert "run-spice" not in flag
