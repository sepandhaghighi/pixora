# -*- coding: utf-8 -*-
"""pixora params."""
from enum import Enum

PIXORA_VERSION = "0.1"

PIXORA_OVERVIEW = '''TODO'''

DEFAULT_PIXEL_SIZE = 8

PIXEL_SIZE_TYPE_ERROR = "Pixel size must be an integer."
PIXEL_SIZE_VALUE_ERROR = "Pixel size must be greater than zero."

IMAGE_SAVE_ERROR = "Failed to save image: {path}"
IMAGE_TYPE_ERROR = "Expected a PIL.Image.Image instance."
IMAGE_INPUT_TYPE_ERROR = "Image must be a str, pathlib.Path, or PIL.Image.Image."

PATH_TYPE_ERROR = "Expected a str or pathlib.Path."
IMAGE_NOT_FOUND_ERROR = "Image not found: {path}"
UNSUPPORTED_IMAGE_ERROR = "Unsupported image: {}"

EXIT_MESSAGE = "See you. Bye!"
