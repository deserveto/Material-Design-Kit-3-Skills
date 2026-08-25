# Primary sources and review log

**Material knowledge review date: 2026-08-25.** Prefer primary sources when a fact may have changed. Machine-readable review dates/facts are also recorded in `../assets/source-snapshots.json`.

Do not treat this file or the capability matrix as a substitute for re-checking live API documentation before a version-sensitive dependency change.

## Agent Skills and harness compatibility

- Agent Skills specification: https://agentskills.io/specification — reviewed 2026-08-25; canonical skill structure and `skills-ref validate`.
- Agent Skills `skills-ref`: https://github.com/agentskills/agentskills/tree/main/skills-ref — reviewed 2026-08-25.
- Codex skill documentation: https://developers.openai.com/codex/skills — reviewed 2026-08-25.
- OpenCode skills: https://opencode.ai/docs/skills — reviewed 2026-08-25.

## Material Design and Android Compose

- Material Design 3: https://m3.material.io/ — reviewed 2026-08-25; current direction is M3 Expressive.
- Compose Material3 releases: https://developer.android.com/jetpack/androidx/releases/compose-material3 — snapshot stable **1.4.0**, alpha **1.5.0-alpha26**.
- Compose Material3 Adaptive: https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive — snapshot stable **1.3.0**.
- Compose Typography: https://developer.android.com/reference/kotlin/androidx/compose/material3/Typography — reviewed 2026-08-25.
- Compose Shapes: https://developer.android.com/reference/kotlin/androidx/compose/material3/Shapes — reviewed 2026-08-25.
- MotionScheme: https://developer.android.com/reference/kotlin/androidx/compose/material3/MotionScheme — reviewed 2026-08-25; current snapshot places it in the 1.5 alpha line.
- MaterialShapes: https://developer.android.com/reference/kotlin/androidx/compose/material3/MaterialShapes — reviewed 2026-08-25; experimental Expressive API.
- Canonical adaptive layouts: https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts — reviewed 2026-08-25.

## Wear OS Material 3

- Wear Compose releases: https://developer.android.com/jetpack/androidx/releases/wear-compose — snapshot stable **1.6.2**, beta **1.7.0-beta01**.
- Wear Compose Material3 API: https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary — reviewed 2026-08-25.
- Wear Compose guidance: https://developer.android.com/training/wearables/compose — reviewed 2026-08-25.

## Flutter

- Flutter Material 3: https://docs.flutter.dev/ui/design/material — reviewed 2026-08-25; docs reflect Flutter **3.44.7**, Material 3 default since **3.16**.
- Material 3 default/migration: https://docs.flutter.dev/release/breaking-changes/material-3-default — reviewed 2026-08-25.

## Material Web

- Material Web releases: https://github.com/material-components/material-web/releases — latest snapshot **2.5.0** (2026-07-14), including Expressive token versions.
- Maintenance announcement: https://github.com/material-components/material-web/discussions/5642 — reviewed 2026-08-25; official library remains in **maintenance mode**, not deprecated.

## Android Views / MDC-Android

- Repository/status: https://github.com/material-components/material-components-android — reviewed 2026-08-25; Views library explicitly in **maintenance mode** after the 2026 Compose-first shift.
- Releases: https://github.com/material-components/material-components-android/releases — latest snapshot **1.14.0** (2026-05-13), including Material3Expressive themes/styles.

## Tokens and color tooling

- DTCG 2025.10: https://www.designtokens.org/TR/2025.10/format/ — first stable Design Tokens Community Group format, published 2025-10-28.
- Material Color Utilities: https://github.com/material-foundation/material-color-utilities — HCT, tonal palettes, dynamic schemes, variants, and contrast-aware generation.
- Dynamic color scheme guide: https://github.com/material-foundation/material-color-utilities/blob/main/dev_guide/creating_color_scheme.md — source color + variant + light/dark + contrast level.

## Accessibility

- WCAG 2.2: https://www.w3.org/TR/WCAG22/ — reviewed 2026-08-25.
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/ — reviewed 2026-08-25.

## Research background for M3 Expressive

- Google Design research: https://design.google/library/expressive-material-design-google-research

## Source policy

1. Prefer primary documentation.
2. Record per-source review dates in `assets/source-snapshots.json`.
3. Distinguish design-system concepts from platform APIs.
4. Label stable/preview/experimental/maintenance state separately per platform.
5. Summarize rather than copy large passages.
6. Pin external validation dependencies in CI where practical.
7. Update the capability matrix and changelog when platform status changes.
8. Never update a review date unless the source was actually re-checked.
