# -*- coding: utf-8 -*-
"""pixora params."""
PIXORA_VERSION = "0.1"

PIXORA_OVERVIEW = '''Pixora is a lightweight Python library and command-line tool for converting ordinary images into retro-style pixel art.
Built on top of Pillow, it provides a simple API for pixelizing images with customizable pixel sizes while supporting both file paths
and in-memory objects. Whether you are creating game assets, generating pixelated avatars, or adding a nostalgic visual effect to your images,
Pixora offers a fast, and easy-to-use solution for both scripts and terminal workflows.'''

DEFAULT_PIXEL_SIZE = 8

PIXEL_SIZE_TYPE_ERROR = "Pixel size must be an integer."
PIXEL_SIZE_VALUE_ERROR = "Pixel size must be greater than zero."

IMAGE_SAVE_ERROR = "Failed to save image: {path}"
IMAGE_TYPE_ERROR = "Expected a PIL.Image.Image instance."
IMAGE_INPUT_TYPE_ERROR = "Image must be a str, pathlib.Path, or PIL.Image.Image."

ALGORITHM_TYPE_ERROR = "Expected an instance of pixora.algorithms.Algorithm."

PATH_TYPE_ERROR = "Expected a str or pathlib.Path."
IMAGE_NOT_FOUND_ERROR = "Image not found: {path}"
UNSUPPORTED_IMAGE_ERROR = "Unsupported image: {path}"

EXIT_MESSAGE = "See you. Bye!"
