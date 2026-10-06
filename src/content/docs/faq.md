---
title: "Elpod FAQ: Bun, Elysia, DI, and Maturity"
label: "FAQ"
description: "Answers to common questions about Elpod, Elysia, Bun, decorator-free dependency injection, pods, compatibility, and working-alpha status."
section: operations
order: 30
---

## The short version

Elpod is an early-stage, decorator-free application framework for modular Elysia services on Bun. It adds explicit constructor dependency injection, feature pods, provider lifetimes, lifecycle management, and architecture checks. Elysia remains the native HTTP and routing layer.

## Does Elpod run on Bun?

Yes. `@elpod/core` is built for Bun ESM and requires Bun 1.4 or newer. Create an application with `bun create elpod my-app`; see [getting started](/docs/getting-started/).

## Does Elpod support dependency injection without decorators or reflect-metadata?

Yes. Classes declare constructor dependencies with a static `inject` tuple or its `needs` alias. Providers are registered explicitly, and Elpod validates the dependency graph. See [dependency injection](/docs/dependency-injection/).

## Does Elpod preserve Elysia type inference and Eden Treaty?

Elpod controllers register native Elysia routes. `ElpodContract<typeof app>` composes the pod route types for Eden Treaty clients. Routes added through untyped bootstrap configuration or native plugins are runtime routes outside that contract. See [routing and controllers](/docs/routing-and-controllers/).

## Is Elpod a replacement for Elysia?

No. Elysia remains the router, HTTP server, schema system, and native plugin surface. Elpod adds composition, DI scopes, lifecycle, cross-cutting boundaries, and architecture checks.

## Why no decorators?

Explicit static `inject` tuples and `routes(app)` are easy to read, typecheck, test, and run in Bun without reflection or a transform.

For class dependencies, `needs` is also supported as a readable alias. `inject` remains the generator’s canonical spelling.

## What is a pod compared with a module?

A pod is Elpod’s feature descriptor: name, prefix, controller, providers, and dependency boundaries. It is an in-process composition value, not a process or deployment unit.

## How do features share a service?

Put shared infrastructure in application `providers` and list its token in `uses`. For a genuine feature dependency, `exports` the provider from one pod and `imports` that pod from the other.

## Does Elpod provide a database, broker, or ORM?

No. It provides small lifecycle and orchestration contracts. Driver, ORM, broker, durability, and deployment choices remain application-owned.

## Is `MemoryCache` or `InMemoryJobQueue` production-ready?

They are useful for local and single-process workloads. They do not coordinate replicas or survive restarts. Use shared adapters for distributed guarantees.

## How is Elpod different from Nest?

Elpod intentionally keeps Elysia’s native APIs and uses explicit values and constructors. It does not add decorators, metadata-driven modules, or a parallel controller/router abstraction. NestJS has a more mature ecosystem and broader established integrations. Read the [Elpod and NestJS comparison](/docs/compare/elpod-vs-nestjs/) for trade-offs.

## Can I add Elpod to an existing Elysia application?

You can move native routes into pod controllers and keep using Elysia hooks, plugins, and schemas. This requires deliberate migration of composition and route types; Elpod is not a drop-in wrapper around every existing application. See [routing](/docs/routing-and-controllers/) and [plugins](/docs/plugins/).

## Can I use Prisma or Drizzle? Does Elpod include an ORM?

Elpod does not include an ORM. Register your chosen client through a provider and own its connection, transaction, migration, and disposal policy. See [database and migrations](/docs/database-and-migrations/).

## Does Elpod include authentication?

Elpod includes authentication boundary helpers, but your application chooses and configures its identity provider, credential validation, and storage. See [authentication](/docs/security/authentication/) and [sessions](/docs/security/sessions/).

## Can I return a `Response`?

Yes. Native `Response` objects retain their status, headers, body, and streaming lifecycle.

## What does the architecture seal guarantee?

It checks the documented project shape, wiring, imports/exports, route registrar boundary, and DI graph. It does not prove business behavior, security, availability, or deployment correctness.

## Is the alpha API stable?

No. Pin versions, read the changelog, and run `elpod audit` and `elpod doctor` in CI.
