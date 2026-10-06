---
title: "CORS and CSRF in Elysia Applications"
label: "CORS and CSRF"
description: "Understand CORS and CSRF as separate controls and configure them at native Elysia HTTP boundaries in an Elpod app."
section: security
order: 40
---

CORS controls browser cross-origin access, while CSRF protects state-changing requests that rely on ambient credentials. Configure these separately at native Elysia boundaries in an Elpod application on Bun.

## The idea

Two guards are often confused. **CORS** asks which browser origins may read a response. **CSRF** asks whether a cookie-backed state change was intentionally made by your application. One is a browser reading rule; the other is a request-intent check.

## How Elpod provides it

**CORS** controls which browser origins may read cross-origin responses. **CSRF** protects cookie-authenticated state changes from unwanted browser requests. They solve different problems.

```ts
import { cors, csrfProtection } from "@elpod/core";

const server = await bootstrap(app, {
  configure: (elysia) => csrfProtection({
    methods: ["POST", "PUT", "PATCH", "DELETE"],
  })(cors({
    origin: ["https://app.example.com"],
    credentials: true,
  })(elysia)),
});
```

Use a narrow explicit origin list for browser applications. If credentials are enabled, never reflect arbitrary origins. CSRF protection belongs on cookie-authenticated mutation routes; bearer APIs generally rely on a different threat model but still need ordinary authorization.

`csrfToken()` creates a token for your application’s token delivery pattern. Follow the module’s native options and test preflight, safe methods, failure status, and proxy behavior.

## Common mistakes

- Treating CORS as authentication.
- Using `*` with credentials.
- Protecting GET reads with a state-changing CSRF policy, or leaving cookie-backed writes unprotected.
- Generating a token but never checking it at the mutation boundary.

## Production notes

Keep origins environment-specific, configure proxies to preserve the intended origin, use TLS, and validate cookies and CSRF tokens server-side. CORS does not stop non-browser clients.

## Related concepts

[Authentication](/docs/security/authentication/) · [Sessions](/docs/security/sessions/) · [Security overview](/docs/security/overview/).
