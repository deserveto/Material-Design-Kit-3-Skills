# Material 3 on the web

**Reviewed: 2026-08-25.**

There is no requirement to make web UI look like an Android screenshot. Apply Material semantics through the project's own framework, tokens, components, layout system, and accessibility primitives.

## Material Web library status

The official `@material/web` project continues to receive maintenance releases (snapshot: 2.5.0), but its maintainers have placed the library in **maintenance mode**. New feature/component parity is not guaranteed.

Therefore, do not assume every current Material component has an official web component and do not select `@material/web` automatically for greenfield work. If the maintained component set fits the product it can still be used deliberately; otherwise implement Material semantics through the project's existing accessible primitives/design system.

Consult `assets/platform-capabilities.json` for the reviewed snapshot and re-check upstream before dependency changes.

## Inspect first

Identify the framework/rendering model, existing component library/design system, CSS strategy, theme/token source, icon system, browser/e2e tooling, existing breakpoints/container queries, and dark/light/high-contrast/reduced-motion support.

If the project already has a coherent non-Material design system and the user did not request Material, preserve it.

## Semantic token pattern

When a project needs a new M3 token layer, centralize it:

```css
:root {
  --md-sys-color-primary: ...;
  --md-sys-color-on-primary: ...;
  --md-sys-color-surface: ...;
  --md-sys-color-surface-container: ...;
  --md-sys-shape-corner-small: ...;
  --md-sys-motion-duration-short: ...;
}
```

Do not copy placeholder values into production. Generate/derive real values from the product theme or reuse existing tokens. Read `design-tokens.md` for DTCG/interchange and `color-system.md` for deterministic scheme generation.

## Component implementation

Prefer established accessible primitives and shared components. Material semantics do not require a specific React package. Avoid interactive `<div>`/`<span>` controls when native semantics or established accessible primitives exist.

For search, menus, pickers, sliders, tooltips, and newer Material families, read `components-advanced.md` and check platform capability/dependency status.

## Responsive/adaptive behavior

Use the project's responsive system, CSS grid/flex, container queries, and/or media queries. Do not mechanically copy Android dp values into CSS pixels. Decide from **available space**, not device labels.

## Material Symbols

When using the Material Symbols variable font, request only the glyphs/axes required where feasible and provide accessible names on controls independently from the icon font.

## Verification

Inspect runtime/console errors, relevant widths, overflow/clipping, focus/keyboard operation, supported themes, loading/error/empty states, browser zoom/text scaling/reflow, and reduced-motion behavior.

The dependency-free `scripts/audit_m3.py` surfaces source-review candidates. For a running app, optional `scripts/audit_runtime.mjs` collects rendered axe findings, console/page errors, horizontal overflow, and a basic keyboard focus probe. It loads Playwright and `@axe-core/playwright` only for a real audit; `--help` has no optional dependency requirement.

Source inspection alone is insufficient when rendering tooling is available.
