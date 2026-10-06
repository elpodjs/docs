---
title: "Rate Limiting for Elpod Applications"
label: "Rate limiting"
description: "Apply rate limits at Elysia boundaries and use a distributed store when multiple Bun processes must share counters."
section: security
order: 50
---

Rate limiting protects an Elysia endpoint from excessive traffic in an Elpod application on Bun. Use local counters only for local or single-process needs; distributed deployments need shared counters.

## The idea

Rate limiting is crowd control. It protects expensive work and gives honest clients a predictable “try again later” answer. It is not a complete defense against a large network attack.

## How Elpod provides it

`rateLimit()` applies a bounded request decision through a `RateLimitStore`. `MemoryRateLimitStore` is suitable for one process and tests.

```ts
import { MemoryRateLimitStore, rateLimit } from "@elpod/core";

const limiter = rateLimit({
  store: new MemoryRateLimitStore(),
  limit: 100,
  windowMs: 60_000,
  key: (request) => request.headers.get("x-api-key") ?? "anonymous",
});

const server = await bootstrap(app, {
  configure: (elysia) => limiter(elysia),
});
```

Use different keys and limits for login, expensive endpoints, public traffic, and trusted service calls. Decide whether the key is a verified principal, tenant, API key, or carefully normalized client address.

## Common mistakes

- Trusting an arbitrary forwarded IP header without a trusted proxy boundary.
- Using one global limit for all routes and tenants.
- Treating a process-local counter as a cluster-wide limit.
- Returning a generic error without `Retry-After` or useful client guidance when your contract needs it.

## Production notes

Implement a shared atomic store for replicas, define fail-open versus fail-closed behavior, and monitor rejected requests. Rate limiting is not DDoS protection; keep edge/network controls in place.

## Related concepts

[Cache and locks](/docs/cache-and-locks/) · [Brute force protection](/docs/security/brute-force-and-signed-urls/) · [Security overview](/docs/security/overview/).
