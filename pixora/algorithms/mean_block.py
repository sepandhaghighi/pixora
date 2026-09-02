# -*- coding: utf-8 -*-
"""pixora mean-block algorithm."""

from __future__ import annotations

from PIL import Image

from ..functions import _validate_pixel_size
from ..params import DEFAULT_PIXEL_SIZE
from .base import Algorithm


class MeanBlock(Algorithm):
    """
    Pixelate an image by replacing each block with its mean RGB color.

    :param pixel_size: pixel size
    """

    def __init__(
            self,
            pixel_size: int = DEFAULT_PIXEL_SIZE) -> None:
        """
        Initiate mean-block algorithm.

        :param pixel_size: pixel size
        """
        _validate_pixel_size(pixel_size)
        self._pixel_size = pixel_size
    
    @staticmethod
    def _mean_block(
            source,
            left: int,
            top: int,
            right: int,
            bottom: int,
            mode: str):
        """
        Calculate the mean color of a pixel block.

        :param source: source image pixel access
        :param left: left block coordinate
        :param top: top block coordinate
        :param right: right block coordinate
        :param bottom: bottom block coordinate
        :param mode: image mode
        """
        red = green = blue = alpha = 0
        count = (right - left) * (bottom - top)

        for y in range(top, bottom):
            for x in range(left, right):
                pixel = source[x, y]

                if mode == "RGBA":
                    r, g, b, a = pixel
                    alpha += a
                else:
                    r, g, b = pixel

                red += r
                green += g
                blue += b

        if mode == "RGBA":
            return (red // count, green // count, blue // count, alpha // count)

        return (red // count, green // count, blue // count)

    def apply(self, image: Image.Image) -> Image.Image:
        """
        Apply mean-block pixelization.

        :param image: input image
        """
        width, height = image.size
        mode = image.mode

        if mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA")
            mode = "RGBA"

        result = Image.new(mode, (width, height))

        source = image.load()
        target = result.load()

        for top in range(0, height, self._pixel_size):
            for left in range(0, width, self._pixel_size):
                right = min(left + self._pixel_size, width)
                bottom = min(top + self._pixel_size, height)

                color = self._mean_block(
                    source,
                    left,
                    top,
                    right,
                    bottom,
                    mode,
                )

                for y in range(top, bottom):
                    for x in range(left, right):
                        target[x, y] = color

        return result
