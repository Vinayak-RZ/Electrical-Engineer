from electrical_engineer.vision.fixtures import load_fixture


def test_fixture_path_no_vlm() -> None:
    data = load_fixture()
    assert data["vlm"] is False
    assert "R1" in data["cir"]
    assert data["low_confidence"] is True
