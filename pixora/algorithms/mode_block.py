# -*- coding: utf-8 -*-
"""pixora mode-block algorithm."""

from __future__ import annotations
from collections import Counter
from typing import Any
from PIL import Image
from ..functions import _validate_pixel_size
from ..params import DEFAULT_PIXEL_SIZE
from .base import Algorithm


class ModeBlock(Algorithm):
    """
    Pixelate an image by replacing each block with its most frequent color.

    :param pixel_size: pixel size
    """

    def __init__(
            self,
            pixel_size: int = DEFAULT_PIXEL_SIZE) -> None:
        """
        Initiate mode-block algorithm.

        :param pixel_size: pixel size
        """
        _validate_pixel_size(pixel_size)
        self._pixel_size = pixel_size

    @staticmethod
    def _mode_block(
            source: Any,
            left: int,
            top: int,
            right: int,
            bottom: int):
        """
        Calculate the most frequent color of a pixel block.

        :param source: source image pixel access
        :param left: left block coordinate
        :param top: top block coordinate
        :param right: right block coordinate
        :param bottom: bottom block coordinate
        """
        pixels = []

        for y in range(top, bottom):
            for x in range(left, right):
                pixels.append(source[x, y])

        return Counter(pixels).most_common(1)[0][0]

    def apply(self, image: Image.Image) -> Image.Image:
        """
        Apply mode-block pixelization.

        :param image: input image
        """
        width, height = image.size

        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA")

        mode = image.mode
        result = Image.new(mode, (width, height))

        source = image.load()
        target = result.load()

        for top in range(0, height, self._pixel_size):
            for left in range(0, width, self._pixel_size):
                right = min(left + self._pixel_size, width)
                bottom = min(top + self._pixel_size, height)

                color = self._mode_block(
                    source=source,
                    left=left,
                    top=top,
                    right=right,
                    bottom=bottom,
                )

                for y in range(top, bottom):
                    for x in range(left, right):
                        target[x, y] = color

        return result