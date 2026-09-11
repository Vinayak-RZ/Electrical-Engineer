from electrical_engineer.nodes import photo as _photo  # noqa: F401
from electrical_engineer.nodes.registry import names


def test_photo_ports_registered() -> None:
    for name in (
        "detect-components",
        "connect-wires",
        "ocr-labels",
        "draft-netlist",
        "confirm-topology",
    ):
        assert name in names()
