---
name: product-art-direction
description: Define a product-specific visual identity before frontend implementation so websites feel intentional, recognizable, and unlike generic AI-made SaaS pages.
---

# Product Art Direction

Act as the art-direction layer before frontend implementation begins. Use this skill when a product needs a visual point of view, when a website risks looking like a template, or when a frontend request has not yet established how the product should feel.

The core principle is:

> Derive the design language from the product, not from popular UI trends.

This skill primarily defines the visual direction. It should not jump straight to React, CSS, components, or implementation details. Its job is to answer:

- What should this product feel like?
- Why should it feel that way?
- What makes its visual identity recognizable?
- What should it deliberately avoid?

## Start with the product

Before choosing a style, understand:

- what the product does and what it helps people accomplish;
- who the target audience is, including their context, expertise, urgency, and expectations;
- what the product should make people feel and do;
- what category conventions help comprehension and which have become visual clichés;
- what content, brand assets, technical constraints, and responsive contexts are already in scope.

If important context is missing, state the assumptions that shape the direction instead of silently defaulting to a fashionable interface.

## Choose one strong visual thesis

Turn the product understanding into a concise visual thesis: a memorable statement about the product's character, atmosphere, and visual tension. It should be specific enough to guide decisions and distinctive enough to separate the product from its category.

The thesis may be expressed through a visual metaphor, such as a field notebook, instrument panel, editorial archive, workshop bench, civic noticeboard, or another metaphor earned by the product. Do not choose a metaphor merely because it looks interesting. Explain the connection between the metaphor and the product's purpose, audience, or behavior.

Prefer fewer, stronger visual ideas. Decoration must support product meaning, hierarchy, orientation, or emotion; remove decoration that has no job.

## Define the design language

Document decisions for each of these dimensions. Describe the behavior and rationale, not just a list of fashionable ingredients.

- **Typography direction:** voice, type roles, contrast between families or weights, measure, line-height, numeral treatment, and how type participates in hierarchy and layout architecture.
- **Spacing and density:** the intended rhythm, breathing room, information density, and where compression or expansion communicates importance.
- **Geometry:** the philosophy for corners, borders, dividers, surfaces, shapes, and container edges. Decide whether the product is precise, soft, tactile, engineered, raw, or another coherent direction. Avoid arbitrary radii.
- **Color behavior:** semantic roles, dominant and supporting tones, contrast, accent frequency, state colors, light/dark behavior, and how color should guide attention rather than decorate empty space.
- **Layout principles:** focal hierarchy, alignment logic, content width, asymmetry or symmetry, navigation behavior, editorial pacing, and how the composition should change across screen sizes.
- **Imagery and illustration:** subject matter, framing, crop logic, texture, art treatment, source constraints, and how imagery earns its place. Maintain a consistent treatment across assets.
- **Motion behavior:** what moves, what stays still, timing, transition character, feedback, loading behavior, and how reduced-motion preferences are respected.
- **Signature visual elements:** one to three recognizable devices—such as a specific rule, crop, typographic gesture, diagram language, material cue, or navigation behavior—that make the product identifiable without becoming a gimmick.

Treat typography as part of the architecture, whitespace as structure, and hierarchy as the foundation that styling serves.

## Explicitly reject generic patterns

Before implementation, name the category clichés and patterns that the product should avoid. Unless the product has a clear reason to use them, strongly discourage:

- excessive cards or wrapping every concept in a card;
- excessive pills, badges, and rounded controls;
- gratuitous gradients;
- purple/blue glow aesthetics by default;
- glassmorphism without a product-specific reason;
- repetitive section layouts that make every page feel interchangeable;
- excessive centered content and permanently centered hero copy;
- arbitrary typography sizes or decorative type scales;
- arbitrary border radii, random shadows, and inconsistent surface treatments;
- meaningless icons used to fill space;
- fake dashboards or fabricated data used as decoration;
- generic developer-tool aesthetics when the product does not call for them;
- generic SaaS landing-page structure: announcement bar, centered headline, three feature cards, logo strip, testimonial cards, pricing grid, and undifferentiated CTA sections.

Avoiding a cliché does not mean banning it mechanically. If a pattern is necessary, document the product reason, constrain its use, and make it serve the established thesis.

## Use this workflow

Follow this sequence before beginning frontend implementation:

1. Understand the product.
2. Understand the audience.
3. Define the desired feeling and user response.
4. Identify visual clichés in the product category.
5. Decide what should be avoided.
6. Choose one strong visual thesis and, where useful, a grounded visual metaphor.
7. Define typography.
8. Define color behavior.
9. Define geometry and border-radius philosophy.
10. Define spacing and density.
11. Define layout behavior and responsive hierarchy.
12. Define imagery, illustration, and motion.
13. Define recognizable signature elements.
14. Document the direction.
15. Only then begin frontend implementation.

Responsive design should adapt hierarchy, content priority, density, and composition—not merely shrink a desktop layout. System-level consistency matters, but every section should not be forced into the same layout pattern.

## Keep a persistent source of truth

Maintain a project-level `DESIGN.md` as the persistent visual source of truth whenever the project permits it. Read an existing `DESIGN.md` before proposing changes. If it does not exist and the user has authorized project documentation, create it before implementation and record:

- product identity, audience, and desired emotional response;
- visual thesis and visual metaphor;
- typography, color, geometry, spacing, density, and layout rules;
- imagery and motion direction;
- signature elements;
- explicit anti-patterns and category clichés to avoid;
- open questions, assumptions, and examples of the direction in use.

Keep the document concise enough to consult during implementation. Update it when a foundational direction changes so later screens do not drift into a collection of local stylistic decisions.

## Document and review the direction

Before writing frontend code, produce a practical art-direction brief with a short rationale for each major decision and a clear list of rejected defaults. The brief should be concrete enough that another implementer can make consistent decisions without guessing.

Review the rendered result—not only the source code—as the final truth. Inspect representative viewport sizes, real content lengths, empty/loading/error/success states, and dense areas. Look for weak hierarchy, accidental sameness, decoration without purpose, inaccessible contrast, layout collapse, and places where the concept harms comprehension. Revise the direction or implementation when the rendered output no longer expresses the thesis.
