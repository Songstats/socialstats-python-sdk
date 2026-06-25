# Changelog

All notable changes to this project are documented in this file.

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
