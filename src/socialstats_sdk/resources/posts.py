from __future__ import annotations

from typing import Any
from urllib.parse import quote

from .base import CREATOR_IDENTIFIER_KEYS, ResourceAPI, require_any_identifier

_POST_IDENTIFIER_KEYS = ("post_id", "id_unique", "external_id")


class PostsAPI(ResourceAPI):
    def stats(self, **params: Any) -> Any:
        query = _require_post_params(params)
        return self._get("posts/stats", params=query)

    def historic_stats(self, **params: Any) -> Any:
        query = _require_post_params(params)
        return self._get("posts/historic_stats", params=query)

    def authorized_stats(self, **params: Any) -> Any:
        query = _require_post_params(params)
        source_id = quote(str(query["source_id"]), safe="")
        return self._get(f"posts/authorized/{source_id}/stats", params=query)

    def authorized_historic_stats(self, **params: Any) -> Any:
        query = _require_post_params(params)
        source_id = quote(str(query["source_id"]), safe="")
        return self._get(f"posts/authorized/{source_id}/historic_stats", params=query)


def _require_post_params(params: dict[str, Any]) -> dict[str, Any]:
    query = dict(params)
    if query.get("source_id") in (None, ""):
        raise ValueError("source_id is required")

    require_any_identifier(query, CREATOR_IDENTIFIER_KEYS)
    require_any_identifier(query, _POST_IDENTIFIER_KEYS)
    return query
