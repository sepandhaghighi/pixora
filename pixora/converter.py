"""Image conversion utilities."""

from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING, Union, Optional
from PIL import Image
from .algorithms import Algorithm
from .algorithms import NearestNeighbor
from .algorithms.base import _validate_algorithm
from .functions import ImageInput, _load_image, _save_image
from .functions import _validate_path, _validate_image_input
if TYPE_CHECKING:
    from PIL.Image import Image as PILImage


class Converter:
    """
    Convert images into pixel art using nearest-neighbor scaling.

    Parameters
    ----------
    pixel_size : int, default=8
    Size of the generated pixels.
    """

    def __init__(self, algorithm: Optional[Algorithm] = None) -> None:
        """
        Initiate converter.

        :param algorithm: conversion algorithm
        """
        if algorithm is None:
            algorithm = NearestNeighbor()
        _validate_algorithm(algorithm)
        self._algorithm = algorithm

    def convert(self, image: ImageInput) -> PILImage:
        """
        Convert an image.

        :param image: input image
        """
        _validate_image_input(image)
        img = _load_image(image)
        return self._algorithm.apply(img)

    def save(self, image: ImageInput, output: Union[str, Path]) -> None:
        """
        Convert an image and save the result.

        :param image: input image
        :param output: file path
        """
        _validate_image_input(image)
        _validate_path(output)
        result = self.convert(image)
        _save_image(result, output)


def pixelize(
        image: ImageInput,
        *,
        output: Optional[Union[str, Path]] = None,
        algorithm: Optional[Algorithm] = None) -> PILImage:
    """
    Convert an image into pixel art.

    :param image: input image
    :param output: output file path
    :param algorithm: conversion algorithm
    """
    converter = Converter(algorithm=algorithm)
    result = converter.convert(image)
    if output is not None:
        _save_image(result, output)
    return result
