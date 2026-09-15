# -*- coding: utf-8 -*-
"""pixora algorithms."""

from .base import Algorithm
from .nearest_neighbor import NearestNeighbor
from .lanczos import Lanczos
from .bilinear import Bilinear
from .bicubic import Bicubic
from .mean_block import MeanBlock
from .mode_block import ModeBlock

__all__ = [
    "Algorithm",
    "NearestNeighbor",
    "Lanczos",
    "Bilinear",
    "Bicubic",
    "MeanBlock",
    "ModeBlock"
]
