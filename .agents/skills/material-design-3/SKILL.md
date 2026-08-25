---
name: material-design-3
description: Use when creating, implementing, migrating, auditing, or reviewing Material Design 3 (Material 3 / M3), Material You, M3 Expressive, Compose Material3, Wear Compose Material 3, Flutter Material 3, Material Web, or existing Android Views Material interfaces.
license: MIT
metadata:
  version: "0.4.0"
  material-reviewed: "2026-08-25"
---

# Material Design 3

## Core principle

Material 3 is semantic and token-driven, not a preset visual style. Choose hierarchy and components from user intent, then express them through the project's existing theme and implementation stack.

Use this skill only when Material 3/Material You/M3 Expressive is requested or already established. Do not force Material into another design system without explicit migration intent.

## Workflow

1. Inspect project instructions, dependencies, theme/tokens, shared components, layout conventions, relevant screens, and available verification tooling before editing.
2. Classify the task: new M3 UI, existing-M3 extension, legacy/M2 migration, review/audit, Expressive enhancement, Wear-specific work, or maintenance/migration of Android Views.
3. For meaningful new/redesign work, establish design intent: primary task, hierarchy, density, personality, brand constraints, adaptive needs, and Expressive intensity.
4. Identify the platform and pinned versions. Never translate one platform's Material API literally into another; Wear Compose is distinct from mobile Compose Material3.
5. Load only the relevant references below. Use the capability/source assets for reviewed machine-readable facts, then re-check live primary documentation before a version-sensitive dependency change.
6. Establish information/action hierarchy and structural regions before color, shape, or motion. Reuse existing semantic tokens and components.
7. Implement applicable interaction states and adaptive composition from available space, not device labels.
8. Verify accessibility: semantics/names/states, keyboard/rotary focus, target size, non-color cues, text scaling/reflow, contrast, reduced motion, and localization.
9. Run project verification and inspect rendered UI at relevant states and widths/sizes when browser, preview, emulator, screenshot, or equivalent tooling exists.

## Reference routing

| Need | Read |
|---|---|
| Product/task personality, density, hierarchy, Expressive intensity | [design intent](references/design-intent.md) |
| Tokens, color, motion, elevation, icons | [foundations](references/foundations.md) |
| DTCG/interchange token architecture and cross-platform mapping | [design tokens](references/design-tokens.md) |
| HCT, Material Color Utilities, dynamic/brand scheme generation | [color system](references/color-system.md) |
| Typography roles, baseline scale, font mapping | [typography](references/typography.md) |
| Shape scale, corner values, Expressive polygons | [shape](references/shape.md) |
| Layout regions, spacing, insets, content widths | [layout/spacing](references/layout-spacing.md) |
| Component overview / decision questions | [components](references/components.md) |
| Buttons, icon actions, FABs, destructive/action prominence | [action components](references/components-actions.md) |
| Navigation bar/rail/drawer, tabs, app bars | [navigation components](references/components-navigation.md) |
| Fields, switches, checkbox/radio, chips, segmented controls | [input/selection components](references/components-input-selection.md) |
| Cards/lists, dialogs/sheets, Snackbar, progress, containment | [feedback/containment components](references/components-feedback-containment.md) |
| Search, pickers, menus, sliders, tooltips, newer component availability | [advanced components](references/components-advanced.md) |
| Hover/focus/pressed/selected/loading/error behavior | [interaction states](references/interaction-states.md) |
| Adaptive patterns and accessibility | [adaptive/accessibility](references/adaptive-accessibility.md) |
| Web-specific WCAG/ARIA checks and runtime verification | [web accessibility](references/accessibility-web.md) |
| M2/legacy migration | [migration](references/migration.md) |
| Structured Material review/audit severity | [review rubric](references/review-rubric.md) |
| M3 Expressive and restraint | [Expressive](references/expressive.md) |
| HTML/CSS/JS, React, Next.js, web | [web](references/platform-web.md) |
| Android Jetpack Compose (mobile/tablet/desktop Android) | [Compose](references/platform-compose.md) |
| Wear OS Compose Material 3 | [Wear](references/platform-wear.md) |
| Flutter | [Flutter](references/platform-flutter.md) |
| Existing Android XML/Views maintenance and Compose migration | [Android Views](references/platform-android-views.md) |
| Volatile facts / primary sources | [sources](references/sources.md) |

## Machine-readable decision data

Use these when deterministic lookup is more useful than prose:

- `assets/platform-capabilities.json` — reviewed platform/library status plus representative component capability boundaries.
- `assets/source-snapshots.json` — granular review dates and recorded volatile source facts.
- `assets/typography-baseline.json`, `assets/shape-baseline.json`, `assets/component-prominence.json`, and `assets/interaction-states.json` — stable decision/reference data.

The capability matrix is a decision aid, not an exhaustive API reference. Inspect the project's pinned dependency and re-check primary docs before dependency changes.

## Decision rules

- Prefer semantic roles (`primary`, `onPrimary`, `surfaceContainer`) over raw component colors.
- Choose buttons, chips, navigation, sheets, dialogs, cards, and selection controls by interaction semantics and prominence, not appearance.
- Derive a small design-intent model before substantial new/Expressive UI so styling serves the task rather than novelty.
- Use a coherent spacing/layout system and component defaults rather than screenshot-specific local values.
- A component is incomplete until applicable focus/pressed/selected/disabled/loading/error behavior is implemented and testable.
- Treat dynamic color as a product-controlled theme mode, not mandatory brand replacement.
- Prefer deterministic color/token generation and mapping over guessed local values when a new scheme is required.
- Use M3 Expressive selectively for meaningful hierarchy; keep repeated utility interactions efficient and familiar.
- Never assume an official Material concept has a stable API everywhere. Check the pinned dependency, capability matrix, and dated platform reference; never silently upgrade to alpha/experimental libraries.
- Treat Material Web and Android Views maintenance status as engineering constraints, not as evidence that Material design guidance itself is deprecated.
- Preserve project architecture. Material adoption does not justify unrelated rewrites.
- For migrations, change semantics/component models in phases; do not declare a color/radius reskin a complete M3 migration.
- For reviews, report evidence and impact using `review-rubric.md`; do not invent a universal Material score.

## Verification

Before completion:

1. run relevant tests/type checks/lint/build;
2. use `scripts/audit_m3.py` for a conservative dependency-free web-source review when useful;
3. when a running web app and optional dependencies are available, use `scripts/audit_runtime.mjs` for rendered axe/console/overflow/focus evidence;
4. render relevant states and widths/sizes when tooling exists;
5. verify keyboard/focus/accessibility and supported themes;
6. report experimental API adoption explicitly.

`audit_m3.py --strict` and `audit_runtime.mjs --strict` are review gates, not certification. A clean result is **not** Material or accessibility certification.

For source maintenance, `scripts/check_source_freshness.py` checks package and granular source-review dates. For behavioral eval result files, `evals/summarize_results.py` aggregates recorded runs but never creates benchmark evidence.

For skill-package changes, run the bundled validator/tests and the official Agent Skills `skills-ref validate` check used by CI.

## Common mistakes

Avoid reference-purple-as-brand, card-wrapping every section, arbitrary radii or spacing, equal prominence for every action, chips/FABs used as generic buttons, shadow-heavy hierarchy, stretched phone navigation on wide screens, tiny icon hit targets, removed focus outlines, disabled browser zoom, color-only state, fixed layouts that block text reflow, excessive expressive motion/shapes, mobile Compose components in Wear UI, new greenfield Android Views when Compose is viable, assuming Material Web has full future component parity, cosmetic-only M2 migrations, local duplicate theme values, guessed color schemes when a deterministic token pipeline is available, and silent experimental dependency upgrades.
