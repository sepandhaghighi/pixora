# -*- coding: utf-8 -*-

from unittest.mock import patch
import pytest
from pixora import NearestNeighbor, Lanczos, Bilinear, Bicubic
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


def test_resolve_argument_prefers_optional():
    parser = _build_parser()

    assert _resolve_argument(parser, "positional.png", "optional.png", "input") == "optional.png"


def test_resolve_argument_uses_optional():
    parser = _build_parser()

    assert _resolve_argument(parser, None, "optional.png", "input") == "optional.png"


def test_resolve_argument_uses_positional():
    parser = _build_parser()

    assert _resolve_argument(parser, "positional.png", None, "input") == "positional.png"


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
@pytest.mark.parametrize(
    "arguments,algorithm,pixel_size,grayscale",
    [
        (
            ["input.png", "output.png"],
            NearestNeighbor,
            8,
            False,
        ),
        (
            ["input.png", "output.png", "--pixel-size", "16"],
            NearestNeighbor,
            16,
            False,
        ),
        (
            ["input.png", "output.png", "--algorithm", "lanczos"],
            Lanczos,
            8,
            False,
        ),
        (
            ["input.png", "output.png", "--algorithm", "lanczos", "--pixel-size", "16"],
            Lanczos,
            16,
            False,
        ),
        (
            ["input.png", "output.png", "--algorithm", "bilinear"],
            Bilinear,
            8,
            False,
        ),
        (
            ["input.png", "output.png", "--algorithm", "bilinear", "--pixel-size", "16"],
            Bilinear,
            16,
            False,
        ),
        (
            ["input.png", "output.png", "--algorithm", "bicubic"],
            Bicubic,
            8,
            False,
        ),
        (
            ["input.png", "output.png", "--algorithm", "bicubic", "--pixel-size", "16"],
            Bicubic,
            16,
            False,
        ),
        (
            ["input.png", "output.png", "--grayscale"],
            NearestNeighbor,
            8,
            True,
        ),
    ],
)
def test_main_algorithm(
        mock_pixelize,
        arguments,
        algorithm,
        pixel_size,
        grayscale):
    main(arguments)

    mock_pixelize.assert_called_once()

    args, kwargs = mock_pixelize.call_args

    assert args == ("input.png",)
    assert kwargs["output"] == "output.png"
    assert kwargs["grayscale"] is grayscale

    result_algorithm = kwargs["algorithm"]

    assert isinstance(result_algorithm, algorithm)
    assert result_algorithm._pixel_size == pixel_size


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
