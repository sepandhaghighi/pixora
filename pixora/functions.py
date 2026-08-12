# -*- coding: utf-8 -*-
"""pixora functions."""

from __future__ import annotations
from typing import Tuple, Union, Any
from pathlib import Path
from PIL import Image
from .params import PIXEL_SIZE_TYPE_ERROR, PIXEL_SIZE_VALUE_ERROR
from .params import IMAGE_TYPE_ERROR, IMAGE_INPUT_TYPE_ERROR, IMAGE_SAVE_ERROR
from .params import PATH_TYPE_ERROR, IMAGE_NOT_FOUND_ERROR, UNSUPPORTED_IMAGE_ERROR
from .errors import PixoraImageError, PixoraValidationError

ImageInput = Union[str, Path, Image.Image]


def _load_image(image: ImageInput) -> Image.Image:
    """
    Load an image.

    :param image: input image
    """
    if isinstance(image, Image.Image):
        _validate_image(image)
        return image.copy()
    path = _normalize_path(image)
    if not path.exists():
        raise PixoraImageError(IMAGE_NOT_FOUND_ERROR.format(path=path))
    try:
        with Image.open(path) as img:
            return img.convert("RGBA")
    except OSError as exc:
        raise PixoraImageError(UNSUPPORTED_IMAGE_ERROR.format(path=path)) from exc


def _save_image(image: Image.Image, output: Union[str, Path]) -> None:
    """
    Save an image.

    :param image: input image
    :param output: output file path
    """
    _validate_image(image)
    output = _normalize_path(output)
    if output.parent:
        output.parent.mkdir(parents=True, exist_ok=True)
    try:
        image.save(output)
    except Exception as exc:
        raise PixoraImageError(IMAGE_SAVE_ERROR.format(path=output)) from exc


def _validate_pixel_size(pixel_size: Any) -> None:
    """
    Validate a pixel size.

    :param pixel_size: pixel size
    """
    if not isinstance(pixel_size, int) or isinstance(pixel_size, bool):
        raise PixoraValidationError(PIXEL_SIZE_TYPE_ERROR)
    if pixel_size <= 0:
        raise PixoraValidationError(PIXEL_SIZE_VALUE_ERROR)


def _validate_image(image: Any) -> None:
    """
    Validate a Pillow image.

    :param image: input image
    """
    if not isinstance(image, Image.Image):
        raise PixoraValidationError(IMAGE_TYPE_ERROR)


def _validate_image_input(image: Any):
    """
    Validate image input.

    :param image: image
    """
    if not isinstance(image, (str, Path, Image.Image)):
        raise PixoraValidationError(IMAGE_INPUT_TYPE_ERROR)


def _validate_path(path: Any):
    """
    Validate a path.

    :param path: file path
    """
    if not isinstance(path, (str, Path)):
        raise PixoraValidationError(PATH_TYPE_ERROR)


def _normalize_path(path: Union[str, Path]) -> Path:
    """
    Convert a path-like object to a Path.

    :param path: file path
    """
    _validate_path(path)
    return Path(path).expanduser()


def _calculate_pixel_dimensions(width: int, height: int, pixel_size: int) -> Tuple[int, int]:
    """
    Calculate the temporary downscaled dimensions.

    :param width: image width
    :param height: image height
    :param pixel_size: pixel size
    """
    _validate_pixel_size(pixel_size)
    return max(1, width // pixel_size), max(1, height // pixel_size)
