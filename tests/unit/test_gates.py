from electrical_engineer.gates.policy import ASK, AUTO, DENY, GateAbort, GateBox, merge_gates


def test_most_restrictive_wins() -> None:
    merged = merge_gates({"sim": "auto"}, {"sim": "deny"})
    assert merged["sim"] == DENY
    merged = merge_gates({"sim": "ask"}, {"sim": "auto"})
    assert merged["sim"] == ASK


def test_third_interrupt_aborts() -> None:
    box = GateBox({"photo": ASK, "matlab": ASK, "compose": ASK})
    box.decide("photo")
    box.decide("matlab")
    try:
        box.decide("compose")
    except GateAbort:
        return
    raise AssertionError("expected abort")


def test_allow_all_skips_ask_not_token() -> None:
    from electrical_engineer.gates.policy import UNCHECKED

    box = GateBox({"photo": ASK}, allow_all=True)
    d = box.decide("photo")
    assert d.policy == AUTO
    assert UNCHECKED == "unchecked"
