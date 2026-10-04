# -*- coding: utf-8 -*-
"""pixora max-block algorithm."""

from __future__ import annotations
from typing import Any, Tuple, Union
from PIL import Image
from ..functions import _validate_pixel_size
from ..params import DEFAULT_PIXEL_SIZE
from .base import Algorithm


class MaxBlock(Algorithm):
    """Pixelate an image by replacing each block with its brightest color."""

    def __init__(
            self,
            pixel_size: int = DEFAULT_PIXEL_SIZE) -> None:
        """
        Initiate max-block algorithm.

        :param pixel_size: pixel size
        """
        _validate_pixel_size(pixel_size)
        self._pixel_size = pixel_size

    @staticmethod
    def _max_block(
            source: Any,
            left: int,
            top: int,
            right: int,
            bottom: int) -> Union[Tuple[int, int, int], Tuple[int, int, int, int]]:
        """
        Calculate the brightest RGB color of a pixel block.

        :param source: source image pixel access
        :param left: left block coordinate
        :param top: top block coordinate
        :param right: right block coordinate
        :param bottom: bottom block coordinate
        """
        brightest = None
        brightest_value = -1

        for y in range(top, bottom):
            for x in range(left, right):
                pixel = source[x, y]
                rgb = pixel[:3]
                brightness = sum(rgb)

                if brightness > brightest_value:
                    brightest = pixel
                    brightest_value = brightness

        return brightest

    def apply(self, image: Image.Image) -> Image.Image:
        """
        Apply max-block pixelization.

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

                color = self._max_block(
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