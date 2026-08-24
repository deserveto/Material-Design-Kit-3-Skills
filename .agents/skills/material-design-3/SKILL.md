---
name: material-design-3
description: Use when creating, implementing, migrating, auditing, or reviewing Material Design 3 (Material 3 / M3), Material You, M3 Expressive, Compose Material3, Wear Compose Material 3, Flutter Material 3, or Material UI design-system interfaces.
license: MIT
metadata:
  version: "0.3.0"
  material-reviewed: "2026-08-24"
---

# Material Design 3

## Core principle

Material 3 is semantic and token-driven, not a preset visual style. Choose hierarchy and components from user intent, then express them through the project's existing theme and implementation stack.

Use this skill only when Material 3/Material You/M3 Expressive is requested or already established. Do not force Material into another design system without explicit migration intent.

## Workflow

1. Inspect project instructions, dependencies, theme/tokens, shared components, layout conventions, relevant screens, and available verification tooling before editing.
2. Classify the task: new M3 UI, existing-M3 extension, legacy/M2 migration, review/audit, Expressive enhancement, or Wear-specific implementation.
3. Identify the platform and pinned versions. Never translate one platform's Material API literally into another; Wear Compose is distinct from mobile Compose Material3.
4. Load only the relevant references below. When changing typography, shape, layout/spacing, interaction states, migration behavior, or review criteria, read the dedicated reference before choosing values or APIs.
5. Establish information/action hierarchy and structural regions before color, shape, or motion. Reuse existing semantic tokens and components.
6. Implement applicable interaction states and adaptive composition from available space, not device labels.
7. Verify accessibility: semantics/names/states, keyboard/rotary focus, target size, non-color cues, text scaling/reflow, contrast, reduced motion, and localization.
8. Run project verification and inspect rendered UI at relevant states and widths/sizes when browser, preview, emulator, screenshot, or equivalent tooling exists.

## Reference routing

| Need | Read |
|---|---|
| Tokens, color, motion, elevation, icons | [foundations](references/foundations.md) |
| Typography roles, baseline scale, font mapping | [typography](references/typography.md) |
| Shape scale, corner values, Expressive polygons | [shape](references/shape.md) |
| Layout regions, spacing, insets, content widths | [layout/spacing](references/layout-spacing.md) |
| Component overview / decision questions | [components](references/components.md) |
| Buttons, icon actions, FABs, destructive/action prominence | [action components](references/components-actions.md) |
| Navigation bar/rail/drawer, tabs, app bars | [navigation components](references/components-navigation.md) |
| Fields, switches, checkbox/radio, chips, segmented controls | [input/selection components](references/components-input-selection.md) |
| Cards/lists, dialogs/sheets, Snackbar, progress, containment | [feedback/containment components](references/components-feedback-containment.md) |
| Hover/focus/pressed/selected/loading/error behavior | [interaction states](references/interaction-states.md) |
| Adaptive patterns and accessibility | [adaptive/accessibility](references/adaptive-accessibility.md) |
| M2/legacy migration | [migration](references/migration.md) |
| Structured Material review/audit severity | [review rubric](references/review-rubric.md) |
| M3 Expressive and restraint | [Expressive](references/expressive.md) |
| HTML/CSS/JS, React, Next.js, web | [web](references/platform-web.md) |
| Android Jetpack Compose (mobile/tablet/desktop Android) | [Compose](references/platform-compose.md) |
| Wear OS Compose Material 3 | [Wear](references/platform-wear.md) |
| Flutter | [Flutter](references/platform-flutter.md) |
| Volatile facts / primary sources | [sources](references/sources.md) |

## Decision rules

- Prefer semantic roles (`primary`, `onPrimary`, `surfaceContainer`) over raw component colors.
- Choose buttons, chips, navigation, sheets, dialogs, cards, and selection controls by interaction semantics and prominence, not appearance.
- Use a coherent spacing/layout system and component defaults rather than screenshot-specific local values.
- A component is incomplete until applicable focus/pressed/selected/disabled/loading/error behavior is implemented and testable.
- Treat dynamic color as a product-controlled theme mode, not mandatory brand replacement.
- Use M3 Expressive selectively for meaningful hierarchy; keep repeated utility interactions efficient and familiar.
- Never assume an official Material concept has a stable API everywhere. Check the pinned dependency and dated platform reference; never silently upgrade to alpha/experimental libraries.
- Preserve project architecture. Material adoption does not justify unrelated rewrites.
- For migrations, change semantics/component models in phases; do not declare a color/radius reskin a complete M3 migration.
- For reviews, report evidence and impact using `review-rubric.md`; do not invent a universal Material score.

## Verification

Before completion, run relevant tests/type checks/lint/build; use `scripts/audit_m3.py` for a conservative web-source review when useful; render relevant states and widths/sizes when tooling exists; verify keyboard/focus/accessibility and supported themes; report experimental API adoption explicitly.

Use `scripts/audit_m3.py --strict` only when the project intentionally wants heuristic findings to produce a non-zero exit code. The audit is heuristic: a clean result is **not** Material or accessibility certification.

For skill-package changes, run the bundled validator/tests and the official Agent Skills `skills-ref validate` check used by CI.

## Common mistakes

Avoid reference-purple-as-brand, card-wrapping every section, arbitrary radii or spacing, equal prominence for every action, chips/FABs used as generic buttons, shadow-heavy hierarchy, stretched phone navigation on wide screens, tiny icon hit targets, removed focus outlines, color-only state, fixed web typography that blocks scaling, excessive expressive motion/shapes, mobile Compose components in Wear UI, cosmetic-only M2 migrations, local duplicate theme values, and silent experimental dependency upgrades.
