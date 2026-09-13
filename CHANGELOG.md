# Changelog

All notable changes to this project are documented in this file.

## Unreleased

### Fixed

- Route public post statistics through the source-specific API paths instead of nonexistent generic post endpoints.
- Apply SDK authentication, base URL, timeout, and user agent to injected HTTPX clients without changing or closing the supplied client.
- Disable redirects so the API key is not forwarded to a redirected endpoint.
- Retry only GET and HEAD requests; ambiguous write failures are surfaced after one attempt.

## [0.2.0] - 2026-09-08

### Added

- OAuth authorization lifecycle resource coverage
- Authorized creator and post resource methods
- Platform-specific creator ID and username selectors

## [0.1.0] - 2026-06-25

### Added

- Initial standalone Python SDK repo for Socialstats Enterprise API (`/enterprise/v1`)
- Full documented resource coverage:
  - `info`
  - `creators`
  - `posts`
- Shared HTTP client with:
  - `apikey` header auth
  - JSON response decoding
  - retry/backoff on transport errors and retryable status codes
- Structured exception types for API and transport failures
- Route coverage audit doc mapping Rails routes and Socialstats OpenAPI paths to SDK methods
- Test suite covering route mapping, header auth, validation, and error handling
