from __future__ import annotations

from typing import Any

from .base import ResourceAPI, require_any_identifier

_POST_REQUIRED_KEYS = ("socialstats_creator_id", "source_id")
_POST_IDENTIFIER_KEYS = ("post_id", "id_unique", "external_id")


class PostsAPI(ResourceAPI):
    def stats(self, **params: Any) -> Any:
        query = _require_post_params(params)
        return self._get("posts/stats", params=query)

    def historic_stats(self, **params: Any) -> Any:
        query = _require_post_params(params)
        return self._get("posts/historic_stats", params=query)


def _require_post_params(params: dict[str, Any]) -> dict[str, Any]:
    query = dict(params)
    missing = [key for key in _POST_REQUIRED_KEYS if query.get(key) in (None, "")]
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"Missing required parameter(s): {joined}")

    require_any_identifier(query, _POST_IDENTIFIER_KEYS)
    return query
