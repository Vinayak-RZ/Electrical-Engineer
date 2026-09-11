from fastapi.testclient import TestClient

from electrical_engineer.ui_server.app import create_app


def test_artifact_svg() -> None:
    client = TestClient(create_app())
    r = client.get("/api/runs/x/artifact.svg")
    assert r.status_code == 200
    assert "svg" in r.headers.get("content-type", "")


def test_artifact_falls_back_to_first_svg(tmp_path) -> None:
    d = tmp_path / "runs" / "c1"
    d.mkdir(parents=True)
    (d / "bode.svg").write_text("<svg xmlns='http://www.w3.org/2000/svg'></svg>")
    r = TestClient(create_app(tmp_path)).get("/api/runs/c1/artifact.svg")
    assert r.status_code == 200
    assert "svg" in r.text.lower()
