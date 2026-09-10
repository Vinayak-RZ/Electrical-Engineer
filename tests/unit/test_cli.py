from electrical_engineer.cli import COMMANDS, build_parser, main


def test_help_lists_commands() -> None:
    text = build_parser().format_help()
    for cmd in COMMANDS:
        assert cmd in text


def test_main_no_args_ok() -> None:
    assert main([]) == 0
