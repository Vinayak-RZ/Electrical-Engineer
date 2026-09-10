from fastapi.testclient import TestClient

from electrical_engineer.ui_server.app import create_app


def test_artifact_svg() -> None:
    client = TestClient(create_app())
    r = client.get("/api/runs/x/artifact.svg")
    assert r.status_code == 200
    assert "svg" in r.headers.get("content-type", "")
