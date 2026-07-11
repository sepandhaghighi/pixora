# -*- coding: utf-8 -*-

from unittest.mock import patch
import pytest
from PIL import Image
from pixora import Converter, pixelize
from pixora import PixoraImageError, PixoraValidationError


def test_converter_default_pixel_size():
    converter = Converter()
    assert converter._pixel_size == 8


@pytest.mark.parametrize("pixel_size", [1, 2, 4, 8, 16, 32])
def test_converter_accepts_valid_pixel_sizes(pixel_size):
    converter = Converter(pixel_size=pixel_size)
    assert converter._pixel_size == pixel_size


@pytest.mark.parametrize("pixel_size", [0, -1, -5])
def test_converter_rejects_invalid_pixel_size_values(pixel_size):
    with pytest.raises(PixoraValidationError):
        Converter(pixel_size=pixel_size)


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object()])
def test_converter_rejects_invalid_pixel_size_types(pixel_size):
    with pytest.raises(PixoraValidationError):
        Converter(pixel_size=pixel_size)


def test_convert_pillow_image_returns_new_image():
    image = Image.new("RGB", (64, 64), "red")

    result = Converter(pixel_size=8).convert(image)

    assert isinstance(result, Image.Image)
    assert result is not image
    assert result.size == image.size
    assert result.mode == "RGB"


@pytest.mark.parametrize("image", [None, 1, [], {}, object()])
def test_convert_invalid_input_type(image):
    with pytest.raises(PixoraValidationError):
        Converter().convert(image)


def test_convert_missing_file(tmp_path):
    with pytest.raises(PixoraImageError):
        Converter().convert(tmp_path / "missing.png")


def test_convert_invalid_image_file(tmp_path):
    path = tmp_path / "bad.png"
    path.write_text("not an image")

    with pytest.raises(PixoraImageError):
        Converter().convert(path)


def test_convert_image_from_file(tmp_path):
    source = tmp_path / "source.png"
    Image.new("RGB", (50, 30), "blue").save(source)

    result = Converter(pixel_size=5).convert(source)

    assert result.size == (50, 30)
    assert result.mode == "RGBA"


def test_converter_save_creates_output_file(tmp_path):
    image = Image.new("RGB", (40, 40))
    output = tmp_path / "output.png"

    Converter().save(image, output)

    assert output.exists()


@pytest.mark.parametrize("output", [None, 1, [], {}, object()])
def test_converter_save_invalid_output(output):
    image = Image.new("RGB", (20, 20))

    with pytest.raises(PixoraValidationError):
        Converter().save(image, output)


def test_converter_save_invalid_input():
    with pytest.raises(PixoraValidationError):
        Converter().save(object(), "output.png")


def test_converter_save_propagates_save_error():
    image = Image.new("RGB", (20, 20))

    with patch.object(Image.Image, "save", side_effect=OSError):
        with pytest.raises(PixoraImageError):
            Converter().save(image, "output.png")


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