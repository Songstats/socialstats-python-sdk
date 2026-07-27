from __future__ import annotations

from typing import Any

from .base import CREATOR_IDENTIFIER_KEYS, ResourceAPI, require_any_identifier


class CreatorsAPI(ResourceAPI):
    def info(self, **params: Any) -> Any:
        return self._get("creators/info", params=self._with_identifier(params))

    def stats(self, **params: Any) -> Any:
        return self._get("creators/stats", params=self._with_identifier(params))

    def historic_stats(self, **params: Any) -> Any:
        return self._get("creators/historic_stats", params=self._with_identifier(params))

    def audience(self, **params: Any) -> Any:
        return self._get("creators/audience", params=self._with_identifier(params))

    def audience_details(self, *, country_code: str, **params: Any) -> Any:
        if not country_code:
            raise ValueError("country_code is required")

        query = self._with_identifier(params)
        query["country_code"] = country_code
        return self._get("creators/audience/details", params=query)

    def activities(self, **params: Any) -> Any:
        return self._get("creators/activities", params=self._with_identifier(params))

    def content(self, **params: Any) -> Any:
        return self._get("creators/content", params=self._with_identifier(params))

    def authorized_stats(self, **params: Any) -> Any:
        return self._get("creators/authorized/stats", params=self._with_identifier(params))

    def authorized_historic_stats(self, **params: Any) -> Any:
        return self._get("creators/authorized/historic_stats", params=self._with_identifier(params))

    def authorized_audience(self, **params: Any) -> Any:
        return self._get("creators/authorized/audience", params=self._with_identifier(params))

    def authorized_content(self, **params: Any) -> Any:
        return self._get("creators/authorized/content", params=self._with_identifier(params))

    def top_posts(self, **params: Any) -> Any:
        return self._get("creators/top_posts", params=self._with_identifier(params))

    def search(self, *, q: str, **params: Any) -> Any:
        if not q:
            raise ValueError("q is required")

        query = {"q": q}
        query.update(params)
        return self._get("creators/search", params=query)

    def add_link_request(self, *, link: str, **params: Any) -> Any:
        if not link:
            raise ValueError("link is required")

        query = self._with_identifier(params)
        query["link"] = link
        return self._post("creators/link_request", params=query)

    def remove_link_request(self, *, link: str, **params: Any) -> Any:
        if not link:
            raise ValueError("link is required")

        query = self._with_identifier(params)
        query["link"] = link
        return self._delete("creators/link_request", params=query)

    def _with_identifier(self, params: dict[str, Any]) -> dict[str, Any]:
        query = dict(params)
        require_any_identifier(query, CREATOR_IDENTIFIER_KEYS)
        return query
