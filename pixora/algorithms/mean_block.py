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

    def apply(self, image: Image.Image) -> Image.Image:
        """
        Apply mean-block pixelization.

        :param image: input image
        """
        image = image.convert("RGBA")
        width, height = image.size
        result = Image.new("RGBA", (width, height))

        source = image.load()
        target = result.load()

        for top in range(0, height, self._pixel_size):
            for left in range(0, width, self._pixel_size):
                right = min(left + self._pixel_size, width)
                bottom = min(top + self._pixel_size, height)

                red = green = blue = alpha = 0
                count = 0

                for y in range(top, bottom):
                    for x in range(left, right):
                        r, g, b, a = source[x, y]
                        red += r
                        green += g
                        blue += b
                        alpha += a
                        count += 1

                color = (
                    red // count,
                    green // count,
                    blue // count,
                    alpha // count,
                )

                for y in range(top, bottom):
                    for x in range(left, right):
                        target[x, y] = color

        return result