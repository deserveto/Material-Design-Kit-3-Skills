---
name: material-design-3
description: Use when creating, implementing, migrating, or reviewing interfaces that are explicitly intended to follow Material Design 3, Material You, or Material 3 Expressive.
license: MIT
metadata:
  version: "0.2.0"
  material-reviewed: "2026-08-24"
---

# Material Design 3

## Core principle

Material 3 is semantic and token-driven, not a preset visual style. Choose hierarchy and components from user intent, then express them through the project's existing theme and implementation stack.

Use this skill only when Material 3/Material You/M3 Expressive is requested or already established. Do not force Material into another design system without explicit migration intent.

## Workflow

1. Inspect project instructions, dependencies, theme/tokens, shared components, layout conventions, and relevant screens before editing.
2. Classify the task: new M3 UI, existing-M3 extension, legacy/M2 migration, review/audit, or Expressive enhancement.
3. Identify the platform. Never translate one platform's Material API literally into another.
4. Load only the relevant references below. When creating or changing typography or shape values, read the dedicated typography or shape reference before choosing values.
5. Establish information/action hierarchy before color, shape, or motion. Reuse existing semantic tokens and components.
6. Implement applicable interaction states and adaptive behavior from available window space, not device labels.
7. Verify accessibility: semantics/names, keyboard/focus, target size, non-color cues, text scaling/reflow, contrast, reduced motion, and localization.
8. Run project verification and inspect the rendered UI when browser, preview, emulator, screenshot, or equivalent tooling exists.

## Reference routing

| Need | Read |
|---|---|
| Tokens, color, motion, elevation, icons | [foundations](references/foundations.md) |
| Typography roles, baseline scale, font mapping | [typography](references/typography.md) |
| Shape scale, corner values, Expressive polygons | [shape](references/shape.md) |
| Component choice and prominence | [components](references/components.md) |
| Adaptive layout and accessibility | [adaptive/accessibility](references/adaptive-accessibility.md) |
| M3 Expressive and restraint | [Expressive](references/expressive.md) |
| HTML/CSS/JS, React, Next.js, web | [web](references/platform-web.md) |
| Android Jetpack Compose | [Compose](references/platform-compose.md) |
| Flutter | [Flutter](references/platform-flutter.md) |
| Volatile facts / primary sources | [sources](references/sources.md) |

## Decision rules

- Prefer semantic roles (`primary`, `onPrimary`, `surfaceContainer`) over raw component colors.
- Choose buttons, chips, navigation, sheets, dialogs, cards, and selection controls by interaction semantics and prominence, not appearance.
- Treat dynamic color as a product-controlled theme mode, not mandatory brand replacement.
- Use M3 Expressive selectively for meaningful hierarchy; keep repeated utility interactions efficient and familiar.
- Never assume an official Material concept has a stable API everywhere. Check the pinned dependency and dated platform reference; never silently upgrade to alpha/experimental libraries.
- Preserve project architecture. Material adoption does not justify unrelated rewrites.

## Verification

Before completion, run relevant tests/type checks/lint/build; use `scripts/audit_m3.py` for a conservative web-source review when useful; render relevant states and widths when tooling exists; verify keyboard/focus/accessibility and supported themes; report experimental API adoption explicitly.

The audit is heuristic. A clean result is **not** Material or accessibility certification.

## Common mistakes

Avoid reference-purple-as-brand, card-wrapping every section, arbitrary radii, equal prominence for every action, chips/FABs used as generic buttons, shadow-heavy hierarchy, stretched phone navigation on wide screens, tiny icon hit targets, color-only state, excessive expressive motion/shapes, local duplicate theme values, and silent experimental dependency upgrades.
