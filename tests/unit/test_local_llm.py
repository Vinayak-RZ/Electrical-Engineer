from electrical_engineer.local_llm import client


def test_skip_if_missing(monkeypatch) -> None:
    monkeypatch.delenv("EE_LOCAL_LLM_URL", raising=False)
    out = client.complete("hello")
    assert out["skipped"] is True
    assert out["byok"] is False
    assert "unset" in out["reason"]


def test_no_http_when_unset(monkeypatch) -> None:
    monkeypatch.delenv("EE_LOCAL_LLM_URL", raising=False)

    def boom(*_a, **_k):
        raise AssertionError("httpx must not be called")

    monkeypatch.setattr(client.httpx, "post", boom)
    from electrical_engineer.local_llm.hooks import classify_scores, solve_explain_hook

    assert classify_scores("find vout") is None
    assert solve_explain_hook("explain kvl")["skipped"] is True
