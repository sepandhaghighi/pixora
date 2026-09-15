# -*- coding: utf-8 -*-
"""pixora cli."""
from __future__ import annotations
from typing import Optional, List
import argparse
from art import tprint
from .algorithms import Algorithm, NearestNeighbor, Lanczos, Bilinear, Bicubic, MeanBlock, ModeBlock
from .params import DEFAULT_PIXEL_SIZE, EXIT_MESSAGE
from .params import PIXORA_VERSION, PIXORA_OVERVIEW
from .converter import pixelize
from .errors import PixoraError

ALGORITHMS = {
    "nearest-neighbor": NearestNeighbor,
    "lanczos": Lanczos,
    "bilinear": Bilinear,
    "bicubic": Bicubic,
    "mean-block": MeanBlock,
    "mode-block": ModeBlock,
}


def _print_pixora_info() -> None:
    """Print Pixora info."""
    tprint("Pixora")
    tprint("V:" + PIXORA_VERSION)
    print(PIXORA_OVERVIEW)


def _build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(prog="pixora", description="Convert images into pixel art.")
    parser.add_argument("input", nargs="?", metavar="INPUT", help="Input image.")
    parser.add_argument("output", nargs="?", metavar="OUTPUT", help="Output image.")
    parser.add_argument("-i", "--input", dest="input_opt", metavar="INPUT", help="Input image.")
    parser.add_argument("-o", "--output", dest="output_opt", metavar="OUTPUT", help="Output image.")
    parser.add_argument(
        "-p",
        "--pixel-size",
        type=int,
        default=DEFAULT_PIXEL_SIZE,
        help="Pixel size (default: {pixel_size}).".format(
            pixel_size=DEFAULT_PIXEL_SIZE))
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str.lower,
        choices=sorted(ALGORITHMS),
        default="nearest-neighbor",
        help="Pixelization algorithm (default: nearest-neighbor).")
    parser.add_argument("--grayscale", action="store_true", help="Convert the result to grayscale.")
    parser.add_argument("-v", "--version", action="version", version=PIXORA_VERSION)
    parser.add_argument("--info", action="store_true", help="Print info.")
    return parser


def _resolve_argument(
    parser: argparse.ArgumentParser,
    positional: Optional[str],
    optional: Optional[str],
    name: str,
) -> str:
    """
    Resolve positional/optional CLI arguments.

    :param parser: argument parser
    :param positional: positional argument
    :param optional: optional argument
    :param name: argument name
    """
    value = optional or positional
    if value is None:
        parser.error(f"{name} is required.")
    return value


def _create_algorithm(name: str, pixel_size: int) -> Algorithm:
    """
    Create a pixelization algorithm.

    :param name: algorithm name
    :param pixel_size: pixel size
    """
    algorithm_class = ALGORITHMS[name]
    return algorithm_class(pixel_size=pixel_size)


def main(argv: Optional[List[str]] = None) -> None:
    """
    CLI entry point.

    :param argv: arguments
    """
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.info:
        _print_pixora_info()
        return
    input_image = _resolve_argument(parser, args.input, args.input_opt, "input")
    output_image = _resolve_argument(parser, args.output, args.output_opt, "output")
    try:
        algorithm = _create_algorithm(name=args.algorithm, pixel_size=args.pixel_size)
        pixelize(input_image, output=output_image, algorithm=algorithm, grayscale=args.grayscale)
    except PixoraError as exc:
        parser.exit(1, f"Error: {exc}\n")
    except (KeyboardInterrupt, EOFError):
        parser.exit(130, f"{EXIT_MESSAGE}\n")
