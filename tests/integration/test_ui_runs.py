from fastapi.testclient import TestClient

from electrical_engineer.ui_server.app import create_app


def test_run_list_and_detail(tmp_path) -> None:
    runs = tmp_path / "runs" / "abcd-1"
    runs.mkdir(parents=True)
    (runs / "summary.json").write_text('{"recipe_id":"x","unchecked":true}')
    client = TestClient(create_app(tmp_path))
    listed = client.get("/api/runs").json()["runs"]
    assert "abcd-1" in listed
    detail = client.get("/api/runs/abcd-1")
    assert detail.status_code == 200
    assert "unchecked" in detail.json()["summary"]
