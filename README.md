# Elpod website

This folder is the complete Elpod website: the GSAP marketing landing at `/` and the documentation at `/docs/`. It builds as a static Astro site and is intentionally self-contained.

```bash
bun install
bun run dev
bun run build
```

The production output is `dist/`. Run `bun run dev`, `bun run build`, `bun run typecheck`, or `bun run preview` from this folder. The sibling `elpod` repository also exposes `landing:*` convenience scripts for working from the Elpod source checkout.

## Documentation source of truth

The website builds documentation only from `src/content/docs/`. Edit the site Markdown and frontmatter there. The sibling `elpode/docs` directory is retained as the library repository’s documentation copy; the website does not import or synchronize it.

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
