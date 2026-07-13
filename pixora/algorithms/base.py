# -*- coding: utf-8 -*-
"""pixora base algorithm."""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any
from ..errors import PixoraValidationError
from ..params import ALGORITHM_TYPE_ERROR
if TYPE_CHECKING:
    from PIL.Image import Image as PILImage


class Algorithm(ABC):
    """Base class for all Pixora algorithms."""

    @abstractmethod
    def apply(self, image: PILImage) -> PILImage:
        """
        Apply the algorithm.

        :param image: input image
        """


def _validate_algorithm(algorithm: Any) -> None:
    """
    Validate an algorithm.

    :param algorithm: conversion algorithm
    """
    if not isinstance(algorithm, Algorithm):
        raise PixoraValidationError(ALGORITHM_TYPE_ERROR)
