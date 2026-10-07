# Elpod visual direction

## Product and audience

Elpod gives growing Elysia applications explicit structure on Bun: constructor DI, feature boundaries called pods, provider lifetimes, cross-cutting HTTP boundaries, and architecture checks. Elysia still owns native routing, validation, serialization, WebSockets, and streaming. The audience is experienced TypeScript/backend developers who want a codebase that stays legible as it grows without paying an abstraction tax.

## Visual thesis

**Friendly structure, clearly drawn.** The site should feel like an architectural field guide made by the character in the Elpod logo: approachable in color and shape, precise in its diagrams and code. Framed boundaries, index markers, and connector rules still show what belongs together and what may cross an edge.

## Design language

- **Typography:** Use a confident, rounded sans for product statements, page titles, and reading, with restrained monospace for code, labels, paths, and architecture metadata. Type should create a clear ladder: statement → title → section heading → body → metadata → code. Monospace is semantic, never decorative filler.
- **Color:** Both the landing page and documentation take their color from the supplied logo: warm cream, deep cocoa, and soft coral. Light is the default on every page; an explicit dark option uses cocoa surfaces, cream text, and lighter coral. The choice persists across both surfaces. Code examples stay dark in both modes for stable syntax contrast.
- **Geometry:** Softly rounded controls and panels echo the Elpod mark. Precise rules inside diagrams and navigation still make technical relationships easy to trace.
- **Spacing and density:** Generous reading measure and large section breaks, with dense islands for code and navigation. Long content is aligned to a strong left rail; selected diagrams may cross that rail to expose relationships.
- **Layout:** The landing page pairs a direct product statement with a logo-led composition illustration, then moves through pod boundaries, explicit DI, native Elysia, and preflight checks. Desktop docs use a persistent, narrow navigation rail and a readable column. The docs overview has a wider split hero with the real Elpod mark and a compact composition map. On mobile, these split compositions stack and navigation becomes a browse control.
- **Code and diagrams:** Code blocks are first-class content with filename/context labels, clear line-height, and horizontal overflow on narrow screens. Diagrams use lines, frames, node labels, and whitespace to show composition; never invent dashboards or decorative graphs.
- **Motion:** One subtle load-in and low-key connector/active-line transitions. Motion clarifies relationships and orientation. Respect reduced motion and keep docs content usable without animation.

## Signature elements

1. **Soft boundary frames:** key conceptual surfaces use rounded frames while the rules inside remain precise.
2. **Edge annotations:** labels sit on the edge of a rule or frame and name the relationship being shown (`prefix`, `controller`, `exports`, `native`).
3. **The real mark:** the landing illustration and documentation overview feature the supplied Elpod character, and the header swaps between the supplied light and dark wordmarks with the reader's theme choice.

## Avoid

Generic developer-tool dark mode, purple/blue gradients, glow, glass, endless rounded cards, repetitive card grids, centered hero-only hierarchy, fake product screenshots, excessive pills, meaningless icons, arbitrary labels, and decoration that does not improve comprehension. Technical specificity is part of the brand; copy should remain concrete and honest about what Elpod does not own.

## Responsive behavior

On narrow screens, preserve the order of the reading narrative and the left-edge rules. Collapse the desktop nav into a single browse control, move metadata below titles, reduce diagram density before reducing type, and keep code horizontally scrollable rather than shrinking it into illegibility.

## Open assumptions

- The existing logo files in `public/` are the authoritative brand assets.
- The website is a static Astro site and should stay self-contained.
- Current documentation content is authoritative; visual changes should not invent technical claims.
