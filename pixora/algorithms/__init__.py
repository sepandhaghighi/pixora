# -*- coding: utf-8 -*-
"""pixora algorithms."""

from .base import Algorithm
from .nearest_neighbor import NearestNeighbor
from .lanczos import Lanczos
from .bilinear import Bilinear
from .bicubic import Bicubic
from .mean_block import MeanBlock
from .mode_block import ModeBlock
from .median_block import MedianBlock
from .max_block import MaxBlock
from .min_block import MinBlock

__all__ = [
    "Algorithm",
    "NearestNeighbor",
    "Lanczos",
    "Bilinear",
    "Bicubic",
    "MeanBlock",
    "ModeBlock",
    "MedianBlock",
    "MaxBlock",
    "MinBlock",
]
