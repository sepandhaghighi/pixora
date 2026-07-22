# -*- coding: utf-8 -*-
"""pixora bilinear algorithm."""

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
from ..params import DEFAULT_PIXEL_SIZE
from ..functions import _calculate_pixel_dimensions, _validate_pixel_size
from .base import Algorithm

if TYPE_CHECKING:
    from PIL.Image import Image as PILImage


class Bilinear(Algorithm):
    """
    Pixelate an image using bilinear resampling.

    :param pixel_size: pixel size
    """

    def __init__(
            self,
            pixel_size: int = DEFAULT_PIXEL_SIZE) -> None:
        """
        Initiate bilinear algorithm.

        :param pixel_size: pixel size
        """
        _validate_pixel_size(pixel_size)
        self._pixel_size = pixel_size

    def apply(self, image: PILImage) -> PILImage:
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
            Image.Resampling.BILINEAR,
        )

        image = image.resize(
            (width, height),
            Image.Resampling.NEAREST,
        )

        return image
