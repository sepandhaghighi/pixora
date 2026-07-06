# -*- coding: utf-8 -*-
"""pixora cli."""
from __future__ import annotations
from typing import Optional
import argparse
import sys
from .params import DEFAULT_PIXEL_SIZE
from .converter import pixelize
from .errors import PixoraError


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(prog="pixora", description="Convert images into pixel art.")
    parser.add_argument("input", help="Input image.", )
    parser.add_argument("output", help="Output image.")
    parser.add_argument("-p", "--pixel-size", type=int, default=DEFAULT_PIXEL_SIZE, help="Pixel size (default: {pixel_size}).".format(pixel_size=DEFAULT_PIXEL_SIZE))
    # parser.add_argument( # "-v", # "--version", # action="version", # version=f"%(prog)s {__version__}", #)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """
    CLI entry point.
    
    :param argv: arguments
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        pixelize(args.input, output=args.output, pixel_size=args.pixel_size)
    except PixoraError as exc:
        parser.exit(1, f"Error: {exc}\n")
    except KeyboardInterrupt:
        parser.exit(130)
        return 0


if __name__ == "__main__":
    sys.exit(main())
