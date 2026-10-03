# Elpod visual direction

## Product and audience

Elpod gives growing Elysia applications explicit structure on Bun: constructor DI, feature boundaries called pods, provider lifetimes, cross-cutting HTTP boundaries, and architecture checks. Elysia still owns native routing, validation, serialization, WebSockets, and streaming. The audience is experienced TypeScript/backend developers who want a codebase that stays legible as it grows without paying an abstraction tax.

## Visual thesis

**Structure without abstraction tax.** The site should feel like an architectural field guide: precise, quiet, and made from the same visible relationships Elpod creates in code. A recurring boundary/edge language is the signature—framed edges, index markers, and short connector rules that show what belongs together and what is allowed to cross.

## Design language

- **Typography:** Use a warm, editorial serif for product statements and page titles, paired with a compact sans for reading and a restrained monospace for code, labels, paths, and architecture metadata. Type should create a clear ladder: statement → title → section heading → body → metadata → code. Monospace is semantic, never decorative filler.
- **Color:** Keep the near-black ink field and amber Elpod accent, evolve the supporting violet into a muted Elysia signal, and use green/yellow only for meaningful runtime status. Surfaces are ink lifts, not floating cards. No gradients or ambient glow as identity.
- **Geometry:** Mostly square or minimally rounded (2–4px). Borders are architectural rules. Use a single small radius only where a code surface or native control benefits from it. No pill-shaped containers except actual status indicators.
- **Spacing and density:** Generous reading measure and large section breaks, with dense islands for code and navigation. Long content is aligned to a strong left rail; selected diagrams may cross that rail to expose relationships.
- **Layout:** Desktop docs use a persistent, narrow navigation rail and a readable editorial column with a slim metadata rail. Documentation titles stay compact and navigational; the overview alone gets a wider split promise/mental-model composition so its map never collides with the heading. Home then moves through problem → pod boundary → explicit DI → native Elysia → quickstart. Avoid repeating three-card sections.
- **Code and diagrams:** Code blocks are first-class content with filename/context labels, clear line-height, and horizontal overflow on narrow screens. Diagrams use lines, frames, node labels, and whitespace to show composition; never invent dashboards or decorative graphs.
- **Motion:** One subtle load-in and low-key connector/active-line transitions. Motion clarifies relationships and orientation. Respect reduced motion and keep docs content usable without animation.

## Signature elements

1. **Boundary corners:** key conceptual surfaces use small corner marks instead of rounded-card chrome.
2. **Edge annotations:** labels sit on the edge of a rule or frame and name the relationship being shown (`prefix`, `controller`, `exports`, `native`).
3. **Section coordinates:** documentation pages carry a quiet section/order coordinate so navigation feels like an index rather than a generic sidebar.

## Avoid

Generic developer-tool dark mode, purple/blue gradients, glow, glass, endless rounded cards, repetitive card grids, centered hero-only hierarchy, fake product screenshots, excessive pills, meaningless icons, arbitrary labels, and decoration that does not improve comprehension. Technical specificity is part of the brand; copy should remain concrete and honest about what Elpod does not own.

## Responsive behavior

On narrow screens, preserve the order of the reading narrative and the left-edge rules. Collapse the desktop nav into a single browse control, move metadata below titles, reduce diagram density before reducing type, and keep code horizontally scrollable rather than shrinking it into illegibility.

## Open assumptions

- The current amber/violet palette is an existing product cue worth refining rather than replacing.
- The website is a static Astro site and should stay self-contained.
- Current documentation content is authoritative; visual changes should not invent technical claims.
