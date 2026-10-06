# Elpod documentation website

Elpod is an early-stage, decorator-free application framework for modular Elysia services on Bun. It adds explicit constructor dependency injection, feature pods, lifecycle management, and architecture checks while preserving native Elysia routes.

[Read the documentation](https://elpod.vercel.app/docs/) · [Core framework](https://github.com/elpodjs/core) · [CLI](https://github.com/elpodjs/cli) · [Starter](https://github.com/elpodjs/create-elpod)

This folder is the complete Elpod website: the GSAP marketing landing at `/` and the documentation at `/docs/`. It builds as a static Astro site and is intentionally self-contained.

```bash
bun install
bun run dev
bun run build
python3 scripts/seo-audit.py
```

The production output is `dist/`. Run `bun run dev`, `bun run build`, `bun run typecheck`, or `bun run preview` from this folder. The sibling `core` repository also exposes `landing:*` convenience scripts for working from the Elpod source checkout.

The [technical SEO audit](./SEO-AUDIT.md) records crawlability, metadata, crawler policy, and deployment checks. The [search intent matrix](./SEARCH-INTENT-MATRIX.md) maps developer questions to documentation pages. `public/llms.txt` is a compact agent-facing index; the generated HTML remains the canonical content.

## Documentation source of truth

The website builds documentation only from `src/content/docs/`. Edit the site Markdown and frontmatter there. The sibling `core/docs` directory is retained as the library repository’s documentation copy; the website does not import or synchronize it.

The content collection is defined in `src/content.config.ts`. Every page needs a title, sidebar label, description, section, and order. Relative documentation links should use canonical web paths such as `/docs/getting-started/`.

## Separate repository plan

This folder is its own repository (for example, `elpod-website`). It must remain copyable as one unit: site builds do not import library source, sibling Markdown, or anything outside this folder at runtime.

## Design and animation map

- `src/styles/tokens.css` is the shared blueprint palette and typography contract for the landing and future docs.
- `src/styles/docs.css` extends that system for prose, navigation, callouts, tables, and highlighted code.
- `SceneRequestLifecycle` pins one master timeline: request → scope → injection → response → disposal.
- `ScenePodCutaway` draws a feature boundary and reveals its prefix, controller, providers, and exports.
- `SceneExplicitDI` highlights the declaration, constructor parameter, and one-to-one dependency edge.
- `SceneNativeElysia` keeps the native Elysia band fixed while Elpod composition fades around it.
- `SceneLaunchChecklist` animates only verified CLI and runtime capabilities.

GSAP is dynamically imported by `src/scripts/landing-animations.ts`, registered with the free ScrollTrigger plugin, and cleaned up through `gsap.context()`. Reduced-motion users get readable final states without pinning or scrubbed timelines. No GSAP Club plugins are used.

Documentation pages do not load GSAP. Astro handles the content collection, static routes, Shiki code highlighting, canonical metadata, and sitemap generation.
