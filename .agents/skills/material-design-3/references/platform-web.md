# Material 3 on the web

There is no requirement to make web UI look like an Android screenshot. Apply Material semantics through the project's own framework, tokens, components, layout system, and accessibility primitives.

## Inspect first

Before implementing, identify:

- framework and rendering model (React, Next.js, Vue, Svelte, vanilla, etc.);
- existing component library/design system;
- CSS strategy (CSS modules, Tailwind, CSS-in-JS, plain CSS, etc.);
- theme/token source;
- icon system;
- browser/e2e tooling;
- existing breakpoints/container queries;
- dark/light/high-contrast/reduced-motion support.

If the project already has a coherent non-Material design system and the user did not request Material, preserve it.

## Semantic CSS token pattern

When a project needs a new M3 token layer, centralize it. Example naming:

```css
:root {
  --md-sys-color-primary: ...;
  --md-sys-color-on-primary: ...;
  --md-sys-color-surface: ...;
  --md-sys-color-on-surface: ...;
  --md-sys-color-surface-container: ...;
  --md-sys-shape-corner-small: ...;
  --md-sys-motion-duration-short: ...;
}
```

Do not copy placeholder ellipses or reference-theme values into production. Generate/derive real values from the product theme or reuse existing tokens.

Components consume tokens rather than raw theme values:

```css
.buttonFilled {
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
}
```

If the project already uses a different token naming system, map Material semantics into that system rather than adding a parallel vocabulary unnecessarily.

## Component implementation

Prefer the project's established accessible primitives and shared components. Material semantics do not require a specific React package.

Avoid building interactive controls from generic `<div>`/`<span>` elements when native semantics or established accessible primitives exist. If a non-native control is unavoidable, implement its complete keyboard/focus/state contract.

## Responsive/adaptive behavior

Use the project's responsive system, CSS grid/flex, container queries, and/or media queries to realize adaptive Material patterns. Do not mechanically copy Android dp values into CSS pixels. Preserve the principle: decide from **available space**, not device labels.

## Material Symbols

When using the Material Symbols variable font, request only the glyphs/axes required where feasible. Set font loading to avoid exposing ligature text during load. Provide accessible names on controls independently from the icon font.

## Visual verification

For UI changes, use available browser tooling (for example Playwright, project-specific browser tests, local preview, or screenshots) to inspect:

- runtime/console errors;
- layout at relevant widths;
- overflow/clipping;
- focus states and keyboard operation;
- supported theme modes;
- loading/error/empty states;
- reduced-motion behavior if motion was added.

Source inspection alone is insufficient when rendering tooling is available.
