# Elpod technical SEO and AI retrieval audit

Audited 6 October 2026. Canonical site: `https://elpod.vercel.app/`. The local production build was inspected after the changes in this repository; live HTTP checks describe the previously deployed site until these changes are deployed.

## What was checked

| Area | Result | Evidence / action |
| --- | --- | --- |
| Raw HTML | Pass | Astro emits static HTML. The built dependency injection page has its article text and five code blocks in the response body. The site audit counted 66 raw HTML code blocks across 34 pages. Important documentation does not require client-side JavaScript. |
| Indexability | Pass locally | No `noindex` directives. All 34 HTML pages appear in `sitemap-0.xml` and receive one canonical URL. `robots.txt` allows public pages. |
| Titles and descriptions | Pass locally | Every built page has a unique title, description, Open Graph title/description, and Twitter card fields. Technical subjects lead documentation titles and H1s. |
| Headings and semantics | Pass locally | One H1 per page; docs use `<main>`, `<article>`, navigation landmarks, and a visible breadcrumb. Compare pages use semantic tables. |
| Structured data | Syntax pass | Homepage: `WebSite`, `Organization`, `SoftwareApplication`, and `SoftwareSourceCode`. Documentation: `BreadcrumbList` plus `TechArticle`, `CollectionPage`, or `WebPage` as appropriate. The local audit parses every JSON-LD block and checks type presence. Rich-result eligibility was not tested or promised. |
| Internal discovery | Pass locally | All local links resolve to built files; no generated page lacks inbound HTML links. Sidebar, related-concept links, pager, glossary, and comparison links expose the topic graph. |
| URL architecture | Pass with redirect pending | Documentation uses nested topic URLs and trailing-slash canonicals. There is no paginated collection. A nonexistent live documentation URL returned HTTP 404. |
| Sitemap and robots | Pass locally | `sitemap-index.xml` references the generated URL sitemap; `robots.txt` references the index. |
| Live status | Partial before deployment | Live homepage, dependency injection page, `robots.txt`, and sitemap index returned HTTP 200. Live `llms.txt` still returned 404. Both `/docs/dependency-injection` and `/docs/dependency-injection/` returned 200, creating duplicate URL forms. `vercel.json` now requests a 308 redirect to the trailing-slash form; verify after deployment. |
| Mobile | Pass for sampled pages | At a 390px viewport, the homepage and NestJS comparison rendered without horizontal document overflow. The docs navigation collapses into a mobile disclosure. This was a visual sample, not a full device matrix. |
| Performance risks | Review after deployment | Documentation pages do not load GSAP. Homepage animation bundle is about 118 kB before gzip, dynamically imported; large public image files are unused by the sampled pages. Run field Core Web Vitals and Lighthouse after deployment. |
| GitHub cross-links | Improved locally | Website, core, CLI, and starter READMEs now define the framework and link to canonical docs and neighboring repositories. Package descriptions and homepage URLs were updated locally. |

Run the repeatable local audit after `bun run build`:

```bash
python3 scripts/seo-audit.py
```

The audit catches missing or duplicate metadata, H1s, invalid JSON-LD syntax, broken local links, orphan HTML pages, missing sitemap entries, and thin raw HTML. It cannot prove a search engine will index or cite a page.

## Crawler policy

The site is a public open-source documentation site, with no private URL paths or subscriber content. `public/robots.txt` deliberately uses one `User-agent: *` group with `Allow: /` and a sitemap link. No crawler-specific group is blocked. This permits compliant search crawlers such as Googlebot and Bingbot and compatible AI search crawlers such as OAI-SearchBot, Claude-SearchBot, and PerplexityBot. It also permits the documented model-development crawlers GPTBot and ClaudeBot under the same public-content policy. A user-initiated fetcher may treat robots rules differently. Allowing a crawler is access permission, not a promise of indexing, training inclusion, citation, or recommendation.

The crawler identifiers and purposes were checked against [Google Search Central](https://developers.google.com/search/docs/crawling-indexing/googlebot), [Bing Webmaster Tools](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), [OpenAI's crawler reference](https://developers.openai.com/api/docs/bots), [Anthropic's crawler guidance](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), and [Perplexity's crawler reference](https://docs.perplexity.ai/docs/resources/perplexity-crawlers). Revisit this policy if content rights or access requirements change. Robots rules are not an access-control mechanism.

`llms.txt` is a compact agent-facing map, not an official ranking signal or substitute for HTML. `FAQPage` markup was omitted: the FAQ is useful as ordinary HTML, and Google's FAQ rich results are currently limited to well-known authoritative health and government sites ([Google Search Central](https://developers.google.com/search/blog/2023/08/howto-faq-changes)).

## Retrieval spot checks

Read only the built HTML of `/`, `/docs/`, `/docs/dependency-injection/`, `/docs/features-and-pods/`, and both comparison pages. Each identifies Elpod's relationship to Bun and Elysia, links to the canonical site or source, and exposes the working-alpha status in text. The dependency injection article explains static constructor tokens, lifetimes, and request scope; the pod article defines a feature boundary; the comparisons distinguish plain Elysia and NestJS with trade-offs. Installation is in `/docs/getting-started/` and the `llms.txt` map.

## Follow-up after deployment

1. Verify no-slash URLs return 308 to slash URLs and that canonical URLs match the final destination. Vercel documents `trailingSlash: true` as a 308 redirect in its [project configuration reference](https://vercel.com/docs/project-configuration/vercel-json).
2. Inspect Google Search Console and Bing Webmaster Tools for discovered URLs, crawl errors, and indexing decisions. The local build cannot determine index status.
3. Measure field Core Web Vitals and mobile performance on the deployed site. Review the landing animation bundle and actual image usage if LCP or INP is poor.
4. Keep package versions, docs, README claims, and `llms.txt` aligned as the working alpha changes.

## GitHub settings to apply in the organization

Local README and `package.json` edits are ready in the adjacent `core`, `cli`, and `create-elpod` repositories. GitHub organization/repository descriptions and topics are account settings, and this environment has no `gh` CLI or authenticated GitHub settings connector. Suggested settings:

- Organization description: `Decorator-free application structure for modular Elysia services on Bun. Explicit DI, feature pods, native routes.`
- Organization website: `https://elpod.vercel.app/`
- Core repository description: `Decorator-free application framework for Elysia on Bun: explicit constructor DI, feature pods, native routes.`
- Docs repository description: `Documentation and website for Elpod, an application framework for modular Elysia services on Bun.`
- Core topics: `bun`, `elysia`, `typescript`, `dependency-injection`, `constructor-injection`, `modular-architecture`, `backend-framework`.
- Docs topics: `bun`, `elysia`, `typescript`, `documentation`, `dependency-injection`.

No organization profile README was available in the local checkouts. Create a dedicated `.github` organization repository only if the team wants to maintain that additional surface.
