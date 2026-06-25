from __future__ import annotations

from typing import Any


class SocialstatsError(Exception):
    """Base exception for SDK failures."""


class SocialstatsTransportError(SocialstatsError):
    """Raised for network/transport failures before an HTTP response is received."""


class SocialstatsAPIError(SocialstatsError):
    """Raised when the Socialstats API responds with a non-2xx status code."""

    def __init__(self, message: str, status_code: int, payload: Any = None) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def __str__(self) -> str:
        return f"Socialstats API error ({self.status_code}): {self.message}"
