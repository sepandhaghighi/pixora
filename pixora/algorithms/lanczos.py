# -*- coding: utf-8 -*-
"""pixora lanczos algorithm."""

from __future__ import annotations
from PIL import Image
from ..params import DEFAULT_PIXEL_SIZE
from ..functions import _calculate_pixel_dimensions, _validate_pixel_size
from .base import Algorithm


class Lanczos(Algorithm):
    """
    Pixelate an image using Lanczos resampling.

    :param pixel_size: pixel size
    """

    def __init__(
            self,
            pixel_size: int = DEFAULT_PIXEL_SIZE) -> None:
        """
        Initiate Lanczos algorithm.

        :param pixel_size: pixel size
        """
        _validate_pixel_size(pixel_size)
        self._pixel_size = pixel_size

    def apply(self, image: Image.Image) -> Image.Image:
        """
        Apply the algorithm.

        :param image: input image
        """
        width, height = image.size

        small_width, small_height = _calculate_pixel_dimensions(
            width=width,
            height=height,
            pixel_size=self._pixel_size,
        )

        image = image.resize(
            (small_width, small_height),
            Image.Resampling.LANCZOS,
        )

        image = image.resize(
            (width, height),
            Image.Resampling.NEAREST,
        )

        return image
