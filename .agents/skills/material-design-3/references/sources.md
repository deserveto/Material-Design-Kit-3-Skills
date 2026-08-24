# Primary sources and review log

**Material knowledge review date: 2026-08-24.** Prefer these primary sources when a fact may have changed. Do not treat this file as a substitute for re-checking live API documentation before a version-sensitive dependency change.

## Agent Skills and harness compatibility

- Agent Skills specification: https://agentskills.io/specification
  - Reviewed 2026-08-24.
  - Canonical format: skill directory with `SKILL.md`; optional `scripts/`, `references/`, and `assets/`; progressive disclosure; name/description constraints.
  - Official validation command: `skills-ref validate <skill-dir>`.
- Agent Skills `skills-ref`: https://github.com/agentskills/agentskills/tree/main/skills-ref
  - Reviewed 2026-08-24.
  - Reference validator currently requires Python 3.11+ and exposes the `skills-ref` CLI.
  - CI pins the source commit used for validation so a moving upstream `main` branch cannot silently change release results.
- Codex skill documentation: https://developers.openai.com/codex/skills
  - Reviewed 2026-08-24.
  - Codex scans repository/user `.agents/skills`; optional `agents/openai.yaml` provides Codex/ChatGPT metadata.
- OpenCode skills: https://opencode.ai/docs/skills
  - Reviewed 2026-08-24.
  - OpenCode supports project/user `.agents/skills` as an agent-compatible skill source in addition to OpenCode-native paths.

## Material Design

- Material Design 3 home / current announcements: https://m3.material.io/
  - Reviewed 2026-08-24.
  - Current site describes M3 Expressive and the updated Figma M3 Design Kit.
- Material 3 in Compose: https://developer.android.com/develop/ui/compose/designsystems/material3
  - Reviewed 2026-08-24.
  - Covers Material 3 / M3 Expressive implementation concepts, theming, dynamic color, typography, shapes, and experimental API caveats.
- Compose `Typography`: https://developer.android.com/reference/kotlin/androidx/compose/material3/Typography
  - Reviewed 2026-08-24.
  - Current 1.5 alpha API exposes emphasized counterparts for the baseline roles; treat version-specific additions separately from the baseline type scale.
- Compose `Shapes`: https://developer.android.com/reference/kotlin/androidx/compose/material3/Shapes
  - Reviewed 2026-08-24.
  - Current 1.5.0-alpha26 constructor adds `largeIncreased`, `extraLargeIncreased`, and `extraExtraLarge`.
- Compose `ShapeDefaults`: https://developer.android.com/reference/kotlin/androidx/compose/material3/ShapeDefaults
  - Reviewed 2026-08-24.
  - Tracks default semantic shape slots and the newer 1.5 alpha additions.
- Compose Material3 releases: https://developer.android.com/jetpack/androidx/releases/compose-material3
  - Reviewed 2026-08-24.
  - Snapshot at review: stable 1.4.0, alpha 1.5.0-alpha26.
  - The release page explicitly directs Wear OS developers to the Wear Compose Material3 library.
- `MotionScheme`: https://developer.android.com/reference/kotlin/androidx/compose/material3/MotionScheme
  - Reviewed 2026-08-24.
  - Added in 1.5.0-alpha26; standard/expressive and effects/spatial motion specs.
- `MaterialShapes`: https://developer.android.com/reference/kotlin/androidx/compose/material3/MaterialShapes
  - Reviewed 2026-08-24.
  - Current API marked `ExperimentalMaterial3ExpressiveApi` and exposes 35 predefined shapes.
- Window size classes: https://developer.android.com/develop/ui/views/layout/use-window-size-classes
  - Reviewed 2026-08-24.
  - Current width classes: compact <600dp, medium 600–839, expanded 840–1199, large 1200–1599, extra-large >=1600.
- Canonical adaptive layouts: https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts
  - Reviewed 2026-08-24.
  - Current guidance covers list-detail, feed, and supporting-pane composition driven by available space.
- Material Symbols: https://developers.google.com/fonts/docs/material_symbols
  - Reviewed 2026-08-24.
  - Documents 2,500+ symbols and variable axes including FILL, wght, GRAD, and opsz.
- Flutter Material 3: https://docs.flutter.dev/ui/design/material
  - Reviewed 2026-08-24.
  - Current docs describe Material 3 as default and cover adaptive/expressive direction.
- Flutter Material 3 default/migration: https://docs.flutter.dev/release/breaking-changes/material-3-default
  - Reviewed 2026-08-24.
  - Material 3 default since Flutter 3.16 and migration caveats.

## Wear OS Material 3

- Wear Compose releases: https://developer.android.com/jetpack/androidx/releases/wear-compose
  - Reviewed 2026-08-24.
  - Snapshot at review: stable 1.6.2; alpha 1.7.0-alpha07.
  - Wear Compose Material3 is the recommended Wear Material implementation; the 1.5 stable generation introduced Wear Material 3 Expressive support.
- Wear Compose Material3 API: https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary
  - Reviewed 2026-08-24.
  - Provides Wear-specific theming, components, motion, and typography.
- Wear Compose guidance: https://developer.android.com/training/wearables/compose
  - Reviewed 2026-08-24.
  - Recommends Wear-specific Material/Material3 APIs rather than mobile Material libraries and covers Wear dependency differences.
- Wear Material 2.5 to Material 3 migration: https://developer.android.com/training/wearables/compose/migrate-to-material3
  - Reviewed 2026-08-24.
  - Recommends phased migration and Wear-specific component mappings; mixed M2.5/M3 should not be the long-term state.
- Android's Wear Compose M3 agent skill: https://developer.android.com/agents/skills/wear/wear-compose-m3/skill
  - Reviewed 2026-08-24.
  - Useful primary implementation guidance for current Wear component and migration behavior.

## Research background for M3 Expressive

- Google Design, M3 Expressive research: https://design.google/library/expressive-material-design-google-research
  - Use for the research rationale behind expressive color, shape, size, motion, containment, hierarchy, and usability findings.

## Source policy

When updating this skill:

1. prefer Material/Google/Android/Flutter/Agent Skills/OpenAI/OpenCode primary documentation;
2. record the review date for volatile facts;
3. distinguish a design-system concept from a platform API;
4. label stable/alpha/beta/experimental APIs accurately and separately per platform;
5. summarize guidance rather than copying large passages;
6. pin external validation dependencies used in CI where practical;
7. update the changelog when a platform-status claim changes.
