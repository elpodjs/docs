---
title: "Elpod Glossary: Pods, Providers, and Dependency Injection"
label: "Glossary"
description: "Precise definitions of Elpod, pods, providers, request scope, constructor injection, Elysia, Bun, Eden Treaty, and architecture checks."
section: operations
order: 40
---

Elpod is an early-stage application framework for structuring modular Elysia services on Bun. This glossary defines the terms used throughout the [documentation](/docs/). If you are new to the framework, follow the [getting started example](/docs/getting-started/) after reading these definitions.

## Framework and runtime

**Elpod** — A decorator-free application structure around Elysia on Bun. It provides explicit constructor dependency injection, feature pods, lifecycle management, and architecture checks while preserving native Elysia routes.

**Bun** — The JavaScript and TypeScript runtime Elpod targets. Elpod's package requires Bun 1.4 or newer. Bun runs the generated server and CLI commands.

**Elysia** — The HTTP framework underneath Elpod. Elysia handles routes, schemas, hooks, plugins, responses, WebSockets, and type inference. Elpod composes these native APIs into a larger application.

**Eden Treaty** — Elysia's type-safe client. Elpod's `ElpodContract<typeof app>` exports route types from pod controllers for a Treaty client; untyped bootstrap or plugin routes do not enter that contract automatically. See [routing and controllers](/docs/routing-and-controllers/).

**OpenAPI** — A description of an HTTP API. Elpod's route inspection and OpenAPI tooling build on routes registered through Elysia; schema quality still depends on the application. See [OpenAPI and routes](/docs/openapi-and-routes/).

## Composition and dependencies

**Application** — The composition value returned by `application({ features, providers, plugins })`. Bootstrap uses it to assemble Elysia routes and the dependency graph.

**Feature boundary** — The ownership line around one business capability, such as users or billing. In Elpod, a pod expresses that boundary in code. It is not a network or security boundary.

**Pod** — An Elpod feature descriptor made with `pod({...})`. It groups one controller, a route prefix, local providers, and optional imports and exports. A pod is an in-process composition boundary, not a process, deployment unit, container, or microservice. `Pod` and `Feature` are aliases in the public API. See [feature pods](/docs/features-and-pods/).

**Controller** — A class whose `routes(app)` method registers native Elysia routes for one pod and returns the Elysia instance. Controllers are resolved from the pod's providers.

**Provider** — A class, value, factory, or async factory registered in Elpod's dependency injection container. Providers supply services or resources to controllers and other providers.

**Dependency injection (DI)** — Supplying collaborators to an object from outside instead of constructing or finding them inside it. Elpod uses explicitly registered providers and declared dependencies. See [dependency injection](/docs/dependency-injection/).

**Constructor injection** — Passing a class's dependencies through its constructor. In Elpod, the class declares the matching runtime tokens with a static `inject` tuple or `needs` alias. No decorator or `reflect-metadata` lookup is needed.

**Dependency graph** — The directed relationships between providers and their dependencies. Elpod validates missing registrations, cycles, and invalid lifetime dependencies before serving requests.

**Inject / needs** — `static readonly inject = [Clock] as const` declares constructor tokens. `needs` is an equivalent alias for classes. Factory helpers keep their separate `inject` argument.

**Imports** — Pods listed as dependencies of another pod. The importing pod can resolve only tokens the imported pod intentionally exports.

**Exports** — Provider tokens a pod makes visible to importing pods. Private providers stay inside their owning pod.

**Uses** — Tokens for application-owned providers a pod consumes. `uses` documents consumption; it does not register a provider. See [provider boundaries](/docs/providers-uses-exports/).

## Lifetimes and operations

**Provider lifetime** — The rule that determines when Elpod creates and reuses a provider. Elpod supports singleton, request, and transient lifetimes.

**Singleton** — The default provider lifetime. One instance is shared in its owning application or feature container until that container is disposed.

**Request scope** — A child dependency injection container for one HTTP request. Request-scoped providers are reused within that request and disposed after the response or stream. Access them from native routes with `injectHandler()`.

**Transient provider** — A provider with `lifetime = "transient"` that creates a fresh instance for each resolution. See [dependency injection](/docs/dependency-injection/).

**Lifecycle** — Startup, initialization, request handling, and disposal of Elpod providers and application resources. Graceful shutdown invokes cleanup rather than abandoning managed resources.

**Architecture audit / seal** — CLI and runtime checks for documented project shape, pod wiring, imports and exports, route boundaries, and the DI graph. These checks cannot prove application security or deployment reliability. See the [CLI reference](/docs/cli/).

For an end-to-end example, create a Bun application with `bun create elpod my-app`, then read [getting started](/docs/getting-started/).
