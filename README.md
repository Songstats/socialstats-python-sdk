# Socialstats Python SDK

Official Python client for the **Socialstats Enterprise API**.

API Base URL: https://api.socialstats.com  
API Key Access: Please contact api@socialstats.com

---

## Automatic Data Access

Regular creator and post analytics automatically use this key's existing channel
connections. Member and entity keys reuse their owning member's active dashboard
connections. Entity keys also accept their agreement's authorization grants; other
Enterprise key types use only their own grants. Public data is returned where
supported when no valid connection exists. Pass `data_access` as `"public"` to exclude connected-account
insights, or omit it for the default `"auto"` behavior.

Dashboard connections returned by `oauth.list` have no grant `id`; disconnect
them in the dashboard. Revoking an entity key's agreement grant does not remove
an independent dashboard connection.

Inspect `data_access_used` (`public` or `authorized`) per source or post.
`is_authorized` and `authorization_status` describe the connection independently
of the selected dataset. Connected-account fields are optional; missing values
are not zero. Facebook posts and Instagram stories require owner channel
authorization. Without it or in public mode, lists omit these posts and post-detail
reads return 403. Public posts from other profiles remain available.

Existing authorized SDK methods remain compatible aliases. New integrations
should use the regular methods shown below. Analytics methods forward `data_access`
without a package upgrade.

## Requirements

- Python >= 3.10

---

## Installation

Install from PyPI:

    pip install socialstats-sdk

For local development:

    pip install -e ".[dev]"

---

## Quick Start

```python
from socialstats_sdk import SocialstatsClient

client = SocialstatsClient(api_key="YOUR_API_KEY")

# API status
status = client.info.status()

# Creator information
creator = client.creators.info(socialstats_creator_id="abcd1234")

# Creator statistics
creator_stats = client.creators.stats(
    socialstats_creator_id="abcd1234",
    source="instagram",
)

# Post statistics
post_stats = client.posts.stats(
    socialstats_creator_id="abcd1234",
    source_id="instagram",
    post_id="1234567890",
)

# Start and poll a creator authorization
authorization = client.oauth.create(
    socialstats_creator_id="abcd1234",
    source_id="youtube",
    return_url="https://customer.example.com/socialstats/oauth-return",
)
authorization_status = client.oauth.attempt_status(authorization["state_token"])
```

---

## Authentication

All requests include your API key in the `apikey` header. The SDK applies its
`base_url`, `timeout`, `api_key`, and `user_agent` settings to each request, including
when you supply an `httpx_client`. Other client settings remain available, and
closing the SDK does not close a client you supplied. Redirects are not followed;
configure the final API base URL.

`max_retries` applies only to GET and HEAD requests. Write requests are attempted
once because a transport failure or server error can occur after a write has
already succeeded. Check the resulting state before retrying a write.

You can request an API key by contacting api@socialstats.com.

We recommend storing your key securely in environment variables:

    export SOCIALSTATS_API_KEY=your_key_here

---

## Available Resource Clients

- `client.info`
- `client.creators`
- `client.posts`
- `client.oauth`

Creator-scoped methods accept `socialstats_creator_id`, `instagram_creator_id`, `facebook_creator_id`, `youtube_creator_id`, or `tiktok_creator_id`. Platform-specific identifiers may be either the platform's internal ID or its username.

Info endpoints:
- `client.info.sources()` -> `/sources`
- `client.info.status()` -> `/status`
- `client.info.uptime_check()` -> `/uptime_check`
- `client.info.definitions()` -> `/definitions`

Creator endpoints:
- `client.creators.info(...)` -> `/creators/info`
- `client.creators.stats(...)` -> `/creators/stats`
- `client.creators.historic_stats(...)` -> `/creators/historic_stats`
- `client.creators.audience(...)` -> `/creators/audience`
- `client.creators.audience_details(country_code=..., ...)` -> `/creators/audience/details`
- `client.creators.activities(...)` -> `/creators/activities`
- `client.creators.content(...)` -> `/creators/content`
- `client.creators.top_posts(...)` -> `/creators/top_posts`
- `client.creators.search(q=..., ...)` -> `/creators/search`
- `client.creators.add_link_request(link=..., ...)` -> `/creators/link_request`
- `client.creators.remove_link_request(link=..., ...)` -> `/creators/link_request`

Post endpoints:
- `client.posts.stats(...)` -> `/posts/{source_id}/stats`
- `client.posts.historic_stats(...)` -> `/posts/{source_id}/historic_stats`

OAuth endpoints:
- `client.oauth.create(...)` -> `POST /oauth`
- `client.oauth.list(...)` -> `GET /oauth`
- `client.oauth.get(...)` -> `GET /oauth/{id}`
- `client.oauth.revoke(...)` -> `DELETE /oauth/{id}`
- `client.oauth.attempt_status(...)` -> `GET /oauth-attempts/{state_token}`

---

## Error Handling

```python
from socialstats_sdk import SocialstatsAPIError, SocialstatsTransportError

try:
    client.creators.info(socialstats_creator_id="invalid")
except SocialstatsAPIError as exc:
    print(f"API error: {exc}")
except SocialstatsTransportError as exc:
    print(f"Transport error: {exc}")
```

---

## Development

To work on the SDK locally:

    git clone https://github.com/songstats/socialstats-python-sdk.git
    cd socialstats-python-sdk
    pip install -e ".[dev]"
    pytest

---

## Versioning

This SDK follows Semantic Versioning (SemVer).

---

## License

MIT
