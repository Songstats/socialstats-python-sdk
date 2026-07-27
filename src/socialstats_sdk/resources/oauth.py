from __future__ import annotations

from typing import Any
from urllib.parse import quote

from .base import ResourceAPI


class OAuthAPI(ResourceAPI):
    def create(self, *, socialstats_creator_id: str, source_id: str, **params: Any) -> Any:
        if not socialstats_creator_id:
            raise ValueError("socialstats_creator_id is required")
        if not source_id:
            raise ValueError("source_id is required")

        query = {
            "socialstats_creator_id": socialstats_creator_id,
            "source_id": source_id,
            **params,
        }
        return self._post("oauth", params=query)

    def list(self, **params: Any) -> Any:
        return self._get("oauth", params=params)

    def get(self, authorization_id: int | str) -> Any:
        if authorization_id in (None, ""):
            raise ValueError("authorization_id is required")

        return self._get(f"oauth/{quote(str(authorization_id), safe='')}")

    def revoke(self, authorization_id: int | str) -> Any:
        if authorization_id in (None, ""):
            raise ValueError("authorization_id is required")

        return self._delete(f"oauth/{quote(str(authorization_id), safe='')}")

    def attempt_status(self, state_token: str) -> Any:
        if not state_token:
            raise ValueError("state_token is required")

        return self._get(f"oauth-attempts/{quote(state_token, safe='')}")
