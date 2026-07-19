# -*- coding: utf-8 -*-

from PIL import Image
import pytest

from pixora import NearestNeighbor, Lanczos


@pytest.mark.parametrize(
    "algorithm",
    [
        NearestNeighbor(pixel_size=8),
        Lanczos(pixel_size=8),
    ],
)
def test_algorithms_apply_returns_new_image(algorithm):
    """
    Test algorithms return a new Pillow image.

    :param algorithm: pixelization algorithm
    """
    image = Image.new("RGB", (64, 64), "red")

    result = algorithm.apply(image)

    assert isinstance(result, Image.Image)
    assert result is not image
    assert result.size == image.size
    assert result.mode == "RGB"


@pytest.mark.parametrize(
    "algorithm",
    [
        NearestNeighbor(pixel_size=1),
        NearestNeighbor(pixel_size=8),
        NearestNeighbor(pixel_size=32),
        Lanczos(pixel_size=1),
        Lanczos(pixel_size=8),
        Lanczos(pixel_size=32),
    ],
)
def test_algorithms_preserve_image_size(algorithm):
    """
    Test algorithms preserve image size.

    :param algorithm: pixelization algorithm
    """
    image = Image.new("RGB", (100, 80), "blue")

    result = algorithm.apply(image)

    assert result.size == image.size


@pytest.mark.parametrize(
    "algorithm,pixel_size",
    [
        (NearestNeighbor(pixel_size=4), 4),
        (NearestNeighbor(pixel_size=16), 16),
        (Lanczos(pixel_size=4), 4),
        (Lanczos(pixel_size=16), 16),
    ],
)
def test_algorithms_store_pixel_size(algorithm, pixel_size):
    """
    Test algorithms store pixel size.

    :param algorithm: pixelization algorithm
    :param pixel_size: expected pixel size
    """
    assert algorithm._pixel_size == pixel_size
