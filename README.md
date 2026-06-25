# Socialstats Python SDK

Official Python client for the **Socialstats Enterprise API**.

API Base URL: https://api.socialstats.com  
API Key Access: Please contact api@socialstats.com

---

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
```

---

## Authentication

All requests include your API key in the `apikey` header.

You can request an API key by contacting api@socialstats.com.

We recommend storing your key securely in environment variables:

    export SOCIALSTATS_API_KEY=your_key_here

---

## Available Resource Clients

- `client.info`
- `client.creators`
- `client.posts`

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
- `client.posts.stats(...)` -> `/posts/stats`
- `client.posts.historic_stats(...)` -> `/posts/historic_stats`

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
