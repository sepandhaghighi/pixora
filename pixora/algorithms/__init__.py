# -*- coding: utf-8 -*-
"""pixora algorithms."""

from .base import Algorithm
from .nearest_neighbor import NearestNeighbor
from .lanczos import Lanczos

__all__ = [
    "Algorithm",
    "NearestNeighbor",
    "Lanczos"
]
