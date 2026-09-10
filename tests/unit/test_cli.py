from electrical_engineer.cli import COMMANDS, build_parser, main


def test_help_lists_commands() -> None:
    text = build_parser().format_help()
    for cmd in COMMANDS:
        assert cmd in text


def test_version_flag() -> None:
    try:
        main(["--version"])
    except SystemExit as exc:
        assert exc.code == 0
    else:
        raise AssertionError("expected SystemExit")
