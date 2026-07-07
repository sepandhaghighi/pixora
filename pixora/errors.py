# -*- coding: utf-8 -*-
"""pixora errors."""


class PixoraError(Exception):
    """Base exception for all Pixora errors."""


class PixoraImageError(PixoraError):
    """Raised when an image cannot be loaded, processed, or saved."""


class PixoraValidationError(PixoraError, ValueError):
    """Raised when an invalid argument or configuration is supplied."""
