from __future__ import annotations

import httpx
import pytest
import respx

from socialstats_sdk import SocialstatsAPIError, SocialstatsClient


@respx.mock
def test_info_status_sends_apikey_header() -> None:
    route = respx.get("https://api.socialstats.com/enterprise/v1/status").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SocialstatsClient(api_key="test_key")
    data = client.info.status()

    assert data["result"] == "success"
    assert route.called
    assert route.calls.last.request.headers["apikey"] == "test_key"


@respx.mock
def test_info_sources_definitions_and_uptime_routes() -> None:
    sources = respx.get("https://api.socialstats.com/enterprise/v1/sources").mock(
        return_value=httpx.Response(200, json={"result": "success", "sources": []})
    )
    definitions = respx.get("https://api.socialstats.com/enterprise/v1/definitions").mock(
        return_value=httpx.Response(200, json={"result": "success", "definitions": {}})
    )
    uptime = respx.get("https://api.socialstats.com/enterprise/v1/uptime_check").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SocialstatsClient(api_key="test_key")
    client.info.sources()
    client.info.definitions()
    client.info.uptime_check()

    assert sources.called
    assert definitions.called
    assert uptime.called


@respx.mock
def test_creators_info_hits_expected_route_and_params() -> None:
    route = respx.get("https://api.socialstats.com/enterprise/v1/creators/info").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SocialstatsClient(api_key="test_key")
    client.creators.info(socialstats_creator_id="abcd1234", with_links=True)

    request = route.calls.last.request
    assert request.url.params["socialstats_creator_id"] == "abcd1234"
    assert request.url.params["with_links"] == "true"


@respx.mock
def test_creators_top_posts_is_mapped() -> None:
    route = respx.get("https://api.socialstats.com/enterprise/v1/creators/top_posts").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SocialstatsClient(api_key="test_key")
    client.creators.top_posts(
        socialstats_creator_id="creator1",
        source="instagram",
        metric="views",
        scope="total",
    )

    request = route.calls.last.request
    assert request.url.params["socialstats_creator_id"] == "creator1"
    assert request.url.params["source"] == "instagram"
    assert request.url.params["metric"] == "views"
    assert request.url.params["scope"] == "total"


@respx.mock
def test_posts_stats_hits_expected_route_and_params() -> None:
    route = respx.get("https://api.socialstats.com/enterprise/v1/posts/stats").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SocialstatsClient(api_key="test_key")
    client.posts.stats(
        socialstats_creator_id="abcd1234",
        source_id="instagram",
        post_id="17900000000000000",
    )

    request = route.calls.last.request
    assert request.url.params["socialstats_creator_id"] == "abcd1234"
    assert request.url.params["source_id"] == "instagram"
    assert request.url.params["post_id"] == "17900000000000000"


@respx.mock
def test_api_error_raises_socialstats_api_error() -> None:
    respx.get("https://api.socialstats.com/enterprise/v1/status").mock(
        return_value=httpx.Response(401, json={"result": "error", "message": "Invalid Api Key"})
    )

    client = SocialstatsClient(api_key="bad_key")

    with pytest.raises(SocialstatsAPIError) as exc:
        client.info.status()

    assert exc.value.status_code == 401
    assert "Invalid Api Key" in str(exc.value)


def test_creator_identifier_validation() -> None:
    client = SocialstatsClient(api_key="test_key")

    with pytest.raises(ValueError):
        client.creators.info()


def test_post_required_param_validation() -> None:
    client = SocialstatsClient(api_key="test_key")

    with pytest.raises(ValueError):
        client.posts.stats(socialstats_creator_id="abcd1234", source_id="instagram")


@respx.mock
def test_creators_search_route() -> None:
    route = respx.get("https://api.socialstats.com/enterprise/v1/creators/search").mock(
        return_value=httpx.Response(200, json={"result": "success", "results": []})
    )

    client = SocialstatsClient(api_key="test_key")
    client.creators.search(q="don diablo", limit=10)

    request = route.calls.last.request
    assert request.url.params["q"] == "don diablo"
    assert request.url.params["limit"] == "10"
