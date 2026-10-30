# -*- coding: utf-8 -*-
"""pixora random-block algorithm."""

from __future__ import annotations
import random
from PIL import Image
from ..functions import _validate_pixel_size
from ..params import DEFAULT_PIXEL_SIZE
from .base import Algorithm


class RandomBlock(Algorithm):
    """Pixelate an image by replacing each block with a random pixel's color."""

    def __init__(
            self,
            pixel_size: int = DEFAULT_PIXEL_SIZE,
            seed: int = None) -> None:
        """
        Initialize random-block algorithm.

        :param pixel_size: pixel size
        :param seed: optional seed for reproducible random selections
        """
        _validate_pixel_size(pixel_size)
        _validate_seed(seed)

        self._pixel_size = pixel_size
        self._seed = seed

    def apply(self, image: Image.Image) -> Image.Image:
        """
        Apply random-block pixelization.

        :param image: input image
        """
        rng = random.Random(self._seed)

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

                x = rng.randrange(left, right)
                y = rng.randrange(top, bottom)
                color = source[x, y]

                for block_y in range(top, bottom):
                    for block_x in range(left, right):
                        target[block_x, block_y] = color

        return result