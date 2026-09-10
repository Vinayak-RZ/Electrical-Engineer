import electrical_engineer.local_llm.client as client


def test_skip_if_missing(monkeypatch) -> None:
    monkeypatch.delenv("EE_LOCAL_LLM_URL", raising=False)
    out = client.complete("hello")
    assert out["skipped"] is True
    assert out["byok"] is False
    assert "unset" in out["reason"]
