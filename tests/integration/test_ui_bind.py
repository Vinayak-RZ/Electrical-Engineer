from fastapi.testclient import TestClient

from electrical_engineer.ui_server.app import (
    BIND_HOST,
    create_app,
    should_open_browser,
    ui_page_url,
)


def test_bind_is_loopback() -> None:
    assert BIND_HOST == "127.0.0.1"
    client = TestClient(create_app())
    r = client.get("/api/health")
    assert r.json()["bind"] == "127.0.0.1"


def test_no_browser_flag(monkeypatch) -> None:
    monkeypatch.setenv("EE_NO_BROWSER", "1")
    assert should_open_browser() is False


def test_ui_page_url_includes_run_query() -> None:
    assert ui_page_url() == "http://127.0.0.1:8765/"
    assert ui_page_url("brpx-1") == "http://127.0.0.1:8765/?run=brpx-1"
