---
title: "Elpod vs NestJS: Bun and Elysia Architecture Trade-offs"
label: "Elpod vs NestJS"
description: "A fair comparison of NestJS and Elpod for modular TypeScript backends, including decorators, dependency injection, routing, ecosystem, and maturity."
section: foundations
order: 110
---

NestJS and Elpod both help teams organize modular TypeScript backends, but they target different foundations. NestJS is a mature application framework with established conventions and a broad integration ecosystem. Elpod is an early-stage, smaller application layer designed for Bun and native Elysia routes.

## Compare the trade-offs

| Concern | NestJS | Elpod |
| --- | --- | --- |
| Primary HTTP model | Nest controllers and framework integrations | Native Elysia routes in pod controllers |
| Dependency injection | Container-based constructor injection, commonly declared with decorators | Explicit static token tuples and constructor injection without decorators or reflection |
| Feature composition | Nest modules and providers | Elpod pods with providers, imports, and exports |
| Runtime orientation | Broad Node.js ecosystem | Bun-first, Elysia-based |
| Maturity | Established framework and integrations | Working alpha; APIs can change |

NestJS's modules, dependency injection, testing utilities, and integrations are useful when a team values its established ecosystem. Its official [provider documentation](https://docs.nestjs.com/providers) explains its common decorator-based pattern. Elpod suits a team that has chosen Bun and Elysia and wants visible dependency graphs without replacing Elysia's route API.

## How constructor dependencies differ

In Elpod, a service declares the exact runtime tokens that match its constructor parameters:

```ts
class InvoiceRepository {
  find(id: string) { return { id }; }
}

class InvoiceService {
  static readonly inject = [InvoiceRepository] as const;
  constructor(private readonly invoices: InvoiceRepository) {}
  find(id: string) { return this.invoices.find(id); }
}
```

Register both classes in a pod's `providers` list. NestJS commonly uses `@Injectable()` and module provider registrations for the same broad purpose. Elpod does not attempt to translate Nest decorators or modules automatically.

## Migration and decision points

Moving from NestJS means redesigning modules as pods, HTTP endpoints as native Elysia routes, and injected dependencies as explicit provider tokens. Existing Nest guards, pipes, interceptors, and integrations require deliberate equivalents or application-owned adapters. There is no drop-in migration path.

If an existing NestJS codebase depends heavily on its ecosystem, staying on NestJS may be simpler. If a new Bun service already uses Elysia and needs stronger structure, evaluate Elpod with a small feature first. Read [dependency injection](/docs/dependency-injection/), [feature pods](/docs/features-and-pods/), [routing](/docs/routing-and-controllers/), and [Elpod vs plain Elysia](/docs/compare/elpod-vs-elysia/).
