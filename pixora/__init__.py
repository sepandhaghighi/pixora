# -*- coding: utf-8 -*-
"""pixora modules."""
from .params import PIXORA_VERSION
from .algorithms import NearestNeighbor, Lanczos, Bilinear, Bicubic
from .converter import Converter, pixelize
from .errors import PixoraError, PixoraImageError, PixoraValidationError

__version__ = PIXORA_VERSION

__all__ = [
    "Converter",
    "pixelize",
    "PixoraError",
    "PixoraImageError",
    "PixoraValidationError",
    "NearestNeighbor",
    "Lanczos",
    "Bilinear",
    "Bicubic"
]
