# Enterprise Routes Audit (Socialstats Rails -> Python SDK)

Audited against:

- `/Users/Oskar/1001tl/docs/socialstats_openapi.yaml`
- `/Users/Oskar/1001tl/config/routes.rb`
- `/Users/Oskar/1001tl/app/controllers/enterprise/v1/creators_controller.rb`
- `/Users/Oskar/1001tl/app/controllers/enterprise/v1/info_controller.rb`
- `/Users/Oskar/1001tl/app/controllers/enterprise/v1/enterprise_base_controller.rb`

Authentication observed in Rails and OpenAPI: `apikey` request header.

## `/enterprise/v1/info`

| HTTP | Route           | SDK Method                   | Source |
| ---- | --------------- | ---------------------------- | ------ |
| GET  | `/sources`      | `client.info.sources()`      | OpenAPI + Rails |
| GET  | `/status`       | `client.info.status()`       | OpenAPI + Rails |
| GET  | `/uptime_check` | `client.info.uptime_check()` | Rails route |
| GET  | `/definitions`  | `client.info.definitions()`  | OpenAPI + Rails |

## `/enterprise/v1/creators`

| HTTP   | Route                 | SDK Method                                             | Source |
| ------ | --------------------- | ------------------------------------------------------ | ------ |
| GET    | `/info`               | `client.creators.info(...)`                            | OpenAPI + Rails |
| GET    | `/stats`              | `client.creators.stats(...)`                           | OpenAPI + Rails |
| GET    | `/historic_stats`     | `client.creators.historic_stats(...)`                  | OpenAPI + Rails |
| GET    | `/audience`           | `client.creators.audience(...)`                        | OpenAPI + Rails |
| GET    | `/audience/details`   | `client.creators.audience_details(country_code=..., ...)` | OpenAPI + Rails |
| GET    | `/activities`         | `client.creators.activities(...)`                      | OpenAPI + Rails |
| GET    | `/content`            | `client.creators.content(...)`                         | OpenAPI + Rails |
| GET    | `/top_posts`          | `client.creators.top_posts(...)`                       | OpenAPI + Rails |
| GET    | `/search`             | `client.creators.search(q=..., ...)`                   | OpenAPI + Rails |
| POST   | `/link_request`       | `client.creators.add_link_request(link=..., ...)`      | OpenAPI + Rails |
| DELETE | `/link_request`       | `client.creators.remove_link_request(link=..., ...)`   | OpenAPI + Rails |

Creator endpoints require one creator identifier (`socialstats_creator_id`, `instagram_creator_id`, `facebook_creator_id`, `youtube_creator_id`, or `tiktok_creator_id`), except `search`, which requires `q`.

## `/enterprise/v1/posts`

| HTTP | Route             | SDK Method                       | Source |
| ---- | ----------------- | -------------------------------- | ------ |
| GET  | `/:source_id/stats`          | `client.posts.stats(...)`        | OpenAPI + Rails |
| GET  | `/:source_id/historic_stats` | `client.posts.historic_stats(...)` | OpenAPI + Rails |

Post endpoints require one creator identifier, `source_id`, and one post identifier: `post_id`, `id_unique`, or `external_id`.

## `/enterprise/v1/oauth`

| HTTP   | Route                          | SDK Method                         | Source |
| ------ | ------------------------------ | ---------------------------------- | ------ |
| POST   | `/oauth`                       | `client.oauth.create(...)`         | OpenAPI + Rails |
| GET    | `/oauth`                       | `client.oauth.list(...)`           | OpenAPI + Rails |
| GET    | `/oauth/:id`                   | `client.oauth.get(...)`            | OpenAPI + Rails |
| DELETE | `/oauth/:id`                   | `client.oauth.revoke(...)`         | OpenAPI + Rails |
| GET    | `/oauth-attempts/:state_token` | `client.oauth.attempt_status(...)` | OpenAPI + Rails |

Regular analytics use automatic channel access; the retained legacy methods are compatibility aliases. Pass `data_access=public` for public data only.
