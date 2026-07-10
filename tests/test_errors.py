# -*- coding: utf-8 -*-

import pytest
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