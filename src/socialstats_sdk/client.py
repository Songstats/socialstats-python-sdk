from __future__ import annotations

import httpx

from .http import DEFAULT_BASE_URL, SocialstatsHTTPClient
from .resources import CreatorsAPI, InfoAPI, PostsAPI


class SocialstatsClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        max_retries: int = 2,
        user_agent: str | None = None,
        httpx_client: httpx.Client | None = None,
    ) -> None:
        self._http = SocialstatsHTTPClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            user_agent=user_agent,
            httpx_client=httpx_client,
        )

        self.info = InfoAPI(self._http)
        self.creators = CreatorsAPI(self._http)
        self.posts = PostsAPI(self._http)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "SocialstatsClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
