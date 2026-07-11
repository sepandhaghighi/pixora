# -*- coding: utf-8 -*-

from unittest.mock import patch
import pytest
from pixora.cli import (
    _build_parser,
    _print_pixora_info,
    _resolve_argument,
    main,
)
from pixora import PixoraError


def test_build_parser():
    parser = _build_parser()
    assert parser.prog == "pixora"


def test_resolve_argument_prefers_positional():
    parser = _build_parser()

    assert _resolve_argument(parser, "positional.png", "optional.png", "input") == "positional.png"


def test_resolve_argument_uses_optional():
    parser = _build_parser()

    assert _resolve_argument(parser, None, "optional.png", "input") == "optional.png"


def test_resolve_argument_missing():
    parser = _build_parser()

    with pytest.raises(SystemExit):
        _resolve_argument(parser, None, None, "input")


@patch("pixora.cli.tprint")
@patch("builtins.print")
def test_print_pixora_info(mock_print, mock_tprint):
    _print_pixora_info()

    assert mock_tprint.call_count == 2
    mock_print.assert_called_once()


@patch("pixora.cli.pixelize")
def test_main_success(mock_pixelize):
    main(["input.png", "output.png"])

    mock_pixelize.assert_called_once_with(
        "input.png",
        output="output.png",
        pixel_size=8,
    )


@patch("pixora.cli.pixelize")
def test_main_with_pixel_size(mock_pixelize):
    main(["input.png", "output.png", "--pixel-size", "16"])

    mock_pixelize.assert_called_once_with(
        "input.png",
        output="output.png",
        pixel_size=16,
    )


@patch("pixora.cli.pixelize", side_effect=PixoraError("failure"))
def test_main_handles_pixora_error(_):
    with pytest.raises(SystemExit) as exc:
        main(["input.png", "output.png"])

    assert exc.value.code == 1


@patch("pixora.cli.pixelize", side_effect=KeyboardInterrupt)
def test_main_handles_keyboard_interrupt(_):
    with pytest.raises(SystemExit) as exc:
        main(["input.png", "output.png"])

    assert exc.value.code == 130


@patch("pixora.cli.pixelize", side_effect=EOFError)
def test_main_handles_eof(_):
    with pytest.raises(SystemExit) as exc:
        main(["input.png", "output.png"])

    assert exc.value.code == 130


@patch("pixora.cli._print_pixora_info")
def test_main_info(mock_info):
    main(["--info"])

    mock_info.assert_called_once()


def test_main_missing_arguments():
    with pytest.raises(SystemExit):
        main([])


def test_main_missing_output():
    with pytest.raises(SystemExit):
        main(["input.png"])