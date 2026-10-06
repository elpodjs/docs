---
title: "Elpod vs Plain Elysia: When to Add Application Structure"
label: "Elpod vs Elysia"
description: "Compare plain Elysia with Elpod's optional structure for Bun backends: explicit DI, feature pods, lifecycle ownership, and architecture checks."
section: foundations
order: 100
---

Plain Elysia is a direct, typed HTTP framework for Bun. It is a strong choice when an application is small enough for its team to manage routes, dependencies, and service boundaries with local conventions. Elpod adds an opinionated application structure when those conventions need to be shared and checked across a larger codebase. Elpod still uses Elysia for HTTP.

## The architectural difference

| Decision | Plain Elysia | Elpod on Elysia |
| --- | --- | --- |
| HTTP routes | Register native Elysia routes directly | Register the same native routes in pod controllers |
| Dependencies | Application chooses its own construction pattern | Explicit constructor tokens and provider graph |
| Feature boundaries | Application conventions | Pods with providers, imports, and exports |
| Lifecycle | Application manages resources | Provider initialization and disposal contracts |
| Architecture checks | Team tooling | Elpod CLI audit, doctor, and seal |

Both approaches can use Elysia schemas, plugins, hooks, WebSockets, and Eden Treaty. Elpod's `ElpodContract` collects typed routes registered in pod controllers; routes added through untyped bootstrap callbacks or plugins need separate type handling.

## A native route inside an Elpod pod

```ts
import { application, pod, type ElpodElysia } from "@elpod/core";

class OrdersService {
  list() { return [{ id: "order-1" }]; }
}

class OrdersController {
  static readonly inject = [OrdersService] as const;
  constructor(private readonly orders: OrdersService) {}

  routes(app: ElpodElysia) {
    return app.get("/", () => this.orders.list());
  }
}

const orders = pod({
  name: "orders",
  prefix: "/orders",
  controller: OrdersController,
  providers: [OrdersService],
});

export const app = application({ features: [orders] });
```

The route is still `GET /orders/` in Elysia. The pod states which feature owns it and which providers its controller can receive.

## When each fits

Choose plain Elysia when minimal surface area matters more than built-in architecture checks and the dependency graph is still easy to see. Choose Elpod when multiple features need explicit ownership, test overrides, provider lifetimes, and a shared project structure. Elpod is a working alpha, so pin versions and verify upgrades before using it for a critical service.

Continue with [feature pods](/docs/features-and-pods/), [dependency injection](/docs/dependency-injection/), [routing and controllers](/docs/routing-and-controllers/), or [getting started](/docs/getting-started/).
