""" Image conversion utilities. """
from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING, Union, Optional
from PIL import Image
from .params import DEFAULT_PIXEL_SIZE
from .functions import ImageInput, _load_image, _save_image
from .functions import calculate_pixel_dimensions
from .functions import _validate_pixel_size, validate_path, _validate_image_input
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

    def __init__(self, pixel_size: int = DEFAULT_PIXEL_SIZE) -> None:
        _validate_pixel_size(pixel_size)
        self.pixel_size = pixel_size

    def convert(self, image: ImageInput) -> PILImage:
        """
        Convert an image into pixel art.

        :param image: input image
        """
        _validate_image_input(image)
        img = _load_image(image)
        width, height = img.size
        small_width, small_height = calculate_pixel_dimensions(width=width, height=height, pixel_size=self.pixel_size, )
        img = img.resize((small_width, small_height), Image.Resampling.NEAREST, )
        img = img.resize((width, height), Image.Resampling.NEAREST, )
        return img

    def save(self, image: ImageInput, output: Union[str, Path]) -> Path:
        """
        Convert an image and save the result.

        :param image: input image
        :param output: file path
        """
        _validate_image_input(image)
        validate_path(output)
        result = self.convert(image)
        return _save_image(result, output)


def pixelize(image: ImageInput, *, output: Optional[Union[str, Path]]
             = None, pixel_size: int = DEFAULT_PIXEL_SIZE) -> PILImage:
    """
    Convert an image into pixel art.

    :param image: input image
    :param output: output file path
    :param pixel_size: pixel size
    """
    converter = Converter(pixel_size=pixel_size)
    result = converter.convert(image)
    if output is not None:
        _save_image(result, output)
    return result
