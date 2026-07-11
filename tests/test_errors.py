# -*- coding: utf-8 -*-

from unittest.mock import patch
import pytest
from pixora import Converter
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
    with pytest.raises(PixoraValidationError):
        Converter(pixel_size=pixel_size)


@pytest.mark.parametrize("pixel_size", ["8", 8.5, None, [], {}, object()])
def test_converter_rejects_invalid_pixel_size_types(pixel_size):
    with pytest.raises(PixoraValidationError):
        Converter(pixel_size=pixel_size)


@pytest.mark.parametrize("image", [None, 1, [], {}, object()])
def test_convert_invalid_input_type(image):
    with pytest.raises(PixoraValidationError):
        Converter().convert(image)


@pytest.mark.parametrize("output", [None, 1, [], {}, object()])
def test_converter_save_invalid_output(output):
    image = Image.new("RGB", (20, 20))

    with pytest.raises(PixoraValidationError):
        Converter().save(image, output)


def test_converter_save_invalid_input():
    with pytest.raises(PixoraValidationError):
        Converter().save(object(), "output.png")


def test_convert_missing_file(tmp_path):
    with pytest.raises(PixoraImageError):
        Converter().convert(tmp_path / "missing.png")


def test_convert_invalid_image_file(tmp_path):
    path = tmp_path / "bad.png"
    path.write_text("not an image")

    with pytest.raises(PixoraImageError):
        Converter().convert(path)


def test_converter_save_propagates_save_error():
    image = Image.new("RGB", (20, 20))

    with patch.object(Image.Image, "save", side_effect=OSError):
        with pytest.raises(PixoraImageError):
            Converter().save(image, "output.png")