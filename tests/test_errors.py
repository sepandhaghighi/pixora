# -*- coding: utf-8 -*-

from unittest.mock import patch
import pytest
from PIL import Image
from pixora import NearestNeighbor, Bilinear, Bicubic, Lanczos, Box
from pixora import MeanBlock, ModeBlock, MedianBlock, MaxBlock, MinBlock, Converter
from pixora import PixoraError, PixoraImageError, PixoraValidationError


def test_error_inheritance():
    assert issubclass(PixoraError, Exception)
    assert issubclass(PixoraImageError, PixoraError)
    assert issubclass(PixoraValidationError, PixoraError)
    assert issubclass(PixoraValidationError, ValueError)


@pytest.mark.parametrize(
    "exception",
    [
        PixoraError("error"),
        PixoraImageError("image"),
        PixoraValidationError("validation"),
    ],
)
def test_exceptions_can_be_raised(exception):
    with pytest.raises(type(exception)):
        raise exception


def test_validation_error_is_caught_as_value_error():
    with pytest.raises(ValueError):
        raise PixoraValidationError("invalid")


@pytest.mark.parametrize("pixel_size", [0, -1, -5])
def test_converter_rejects_invalid_pixel_size_values(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be greater than zero."):
        Converter(NearestNeighbor(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types1(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(NearestNeighbor(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types2(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(Bilinear(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types3(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(Bicubic(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types4(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(Lanczos(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types5(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(MeanBlock(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types6(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(ModeBlock(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types7(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(MedianBlock(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types8(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(MaxBlock(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types9(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(MinBlock(pixel_size=pixel_size))


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object(), True, False])
def test_converter_rejects_invalid_pixel_size_types10(pixel_size):
    with pytest.raises(PixoraValidationError, match="Pixel size must be an integer."):
        Converter(Box(pixel_size=pixel_size))


@pytest.mark.parametrize("image", [None, 1, [], {}, object()])
def test_convert_invalid_input_type(image):
    with pytest.raises(PixoraValidationError, match="Image must be a str, pathlib.Path, or PIL.Image.Image."):
        Converter().convert(image)


@pytest.mark.parametrize("output", [None, 1, [], {}, object()])
def test_converter_save_invalid_output(output):
    image = Image.new("RGB", (20, 20))

    with pytest.raises(PixoraValidationError, match="Expected a str or pathlib.Path."):
        Converter().save(image, output)


def test_converter_save_invalid_input():
    with pytest.raises(PixoraValidationError, match="Image must be a str, pathlib.Path, or PIL.Image.Image."):
        Converter().save(object(), "output.png")


def test_convert_missing_file(tmp_path):
    with pytest.raises(PixoraImageError, match=r"Image not found:"):
        Converter().convert(tmp_path / "missing.png")


def test_convert_invalid_image_file(tmp_path):
    path = tmp_path / "bad.png"
    path.write_text("not an image")

    with pytest.raises(PixoraImageError, match=r"Unsupported image:"):
        Converter().convert(path)


def test_converter_save_propagates_save_error():
    image = Image.new("RGB", (20, 20))

    with patch.object(Image.Image, "save", side_effect=OSError):
        with pytest.raises(PixoraImageError, match=r"Failed to save image:"):
            Converter().save(image, "output.png")


def test_converter_invalid_algorithm():
    with pytest.raises(PixoraValidationError, match="Expected an instance of pixora.algorithms.Algorithm."):
        Converter(algorithm="nearest")
