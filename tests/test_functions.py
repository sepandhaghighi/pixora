# -*- coding: utf-8 -*-

import pytest
from PIL import Image
from pixora import NearestNeighbor, Converter, pixelize


def test_converter_default_pixel_size():
    converter = Converter()
    assert converter._algorithm._pixel_size == 8


@pytest.mark.parametrize("pixel_size", [1, 2, 4, 8, 16, 32])
def test_converter_accepts_valid_pixel_sizes(pixel_size):
    converter = Converter(NearestNeighbor(pixel_size=pixel_size))
    assert converter._algorithm._pixel_size == pixel_size


def test_convert_pillow_image_returns_new_image():
    image = Image.new("RGB", (64, 64), "red")

    result = Converter(NearestNeighbor(pixel_size=8)).convert(image)

    assert isinstance(result, Image.Image)
    assert result is not image
    assert result.size == image.size
    assert result.mode == "RGB"


def test_convert_image_from_file(tmp_path):
    source = tmp_path / "source.png"
    Image.new("RGB", (50, 30), "blue").save(source)

    result = Converter(NearestNeighbor(pixel_size=5)).convert(source)

    assert result.size == (50, 30)
    assert result.mode == "RGBA"


def test_convert_grayscale():
    image = Image.new("RGB", (64, 64), "red")

    result = Converter(
        NearestNeighbor(pixel_size=8)
    ).convert(image, grayscale=True)

    assert isinstance(result, Image.Image)
    assert result.size == image.size
    assert result.mode == "RGBA"


def test_converter_save_creates_output_file(tmp_path):
    image = Image.new("RGB", (40, 40))
    output = tmp_path / "output.png"

    Converter().save(image, output)

    assert output.exists()


def test_converter_save_grayscale(tmp_path):
    image = Image.new("RGB", (40, 40), "red")
    output = tmp_path / "output.png"

    Converter().save(
        image,
        output,
        grayscale=True,
    )

    assert output.exists()

    result = Image.open(output)

    assert result.mode == "RGBA"


def test_pixelize_returns_image():
    image = Image.new("RGB", (60, 60))

    result = pixelize(image)

    assert isinstance(result, Image.Image)
    assert result.size == image.size


def test_pixelize_saves_image(tmp_path):
    image = Image.new("RGB", (30, 30))
    output = tmp_path / "pixelized.png"

    result = pixelize(image, output=output)

    assert output.exists()
    assert isinstance(result, Image.Image)


def test_pixelize_with_file_input(tmp_path):
    source = tmp_path / "input.png"
    Image.new("RGB", (25, 25)).save(source)

    result = pixelize(source)

    assert isinstance(result, Image.Image)
    assert result.size == (25, 25)


def test_pixelize_grayscale():
    image = Image.new("RGB", (60, 60), "red")

    result = pixelize(image, grayscale=True)

    assert isinstance(result, Image.Image)
    assert result.size == image.size
    assert result.mode == "RGBA"
