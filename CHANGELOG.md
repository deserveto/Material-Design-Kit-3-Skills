# Changelog

All notable changes to this project are documented here.

## 0.4.0 - 2026-08-25

- Added a reviewed machine-readable `platform-capabilities.json` matrix spanning Compose Material3, Wear Compose Material3, Flutter, Material Web, and Android Views/MDC with representative component stability/availability boundaries.
- Added granular `source-snapshots.json` tracking for platform releases/status, Material guidance, Agent Skills, WCAG/ARIA, DTCG 2025.10, and Material Color Utilities.
- Added design-intent guidance so substantial UI work establishes task hierarchy, density, brand constraints, adaptive needs, and Expressive intensity before styling.
- Added DTCG-oriented design-token interoperability guidance plus Material Color Utilities/HCT color-system guidance for deterministic scheme generation instead of guessed local colors.
- Added focused advanced component contracts for search, menus, pickers, sliders, tooltips, loading/progress, and version-sensitive API selection.
- Added a web accessibility profile grounded in WCAG 2.2 / ARIA patterns and an Android Views maintenance/migration profile reflecting the 2026 Compose-first shift.
- Updated platform snapshots: Compose Material3 1.4.0 stable / 1.5.0-alpha26 preview, Material3 Adaptive 1.3.0 stable, Wear Compose 1.6.2 stable / 1.7.0-beta01 preview, Flutter docs 3.44.7, Material Web 2.5.0 maintenance mode, and MDC-Android 1.14.0 maintenance mode.
- Expanded `audit_m3.py` with disabled browser-zoom and text-size-adjust checks, machine-readable rule counts, and lower-noise fixed-pixel typography wording while preserving dependency-free operation.
- Added optional `audit_runtime.mjs` with dynamically loaded Playwright + axe checks for rendered accessibility violations, page/console errors, overflow, and basic keyboard-focus evidence; normal skill installation remains dependency-free.
- Expanded `check_source_freshness.py` to report per-source staleness and JSON output while preserving package-level review-date behavior.
- Added behavioral result provenance rules, `evals/results/`, optional catastrophic-failure recording, and `summarize_results.py` for deterministic aggregation without fabricating benchmark runs.
- Added v0.4.0 regression tests and CI checks for the new assets, runtime-audit syntax/help, freshness tooling, and existing official Agent Skills validation.

## 0.3.0 - 2026-08-24

- Added dedicated layout/spacing and interaction-state guides covering structural regions, adaptive composition, insets, focus, pressed/selected/disabled/loading/error states, async recovery, and reduced motion.
- Added a Wear OS Compose Material 3 platform profile with a dated 1.6.2 stable / 1.7.0-alpha07 snapshot, Wear-specific component boundaries, round-screen/rotary/ambient guidance, and migration rules.
- Added a phased Material 2/legacy migration guide and evidence-based Material review rubric with BLOCKER/HIGH/MEDIUM/LOW severity definitions.
- Split component decision guidance into focused action, navigation, input/selection, and feedback/containment references while keeping the core skill progressively disclosed.
- Added machine-readable action-prominence and interaction-state assets for deterministic tooling.
- Expanded `audit_m3.py` with focus-outline removal, hard-coded pixel radius, and fixed-pixel font-size review rules plus opt-in `--strict` exit behavior.
- Expanded behavioral evals with layout/spacing, interaction-state, Wear-platform, phased-migration, and review-severity cases; added portable fixture contracts and a reproducible result JSON Schema.
- Added official Agent Skills `skills-ref` validation in CI, pinned to a reviewed upstream commit.
- Expanded skill activation keywords for M3, Compose Material3, Wear Compose Material 3, and Flutter Material 3 without broad generic UI triggers.
- Added a monthly source-review freshness workflow and deterministic `check_source_freshness.py` maintenance guard.
- Refreshed README/source documentation and primary-source tracking for adaptive layouts, Wear Compose, and Agent Skills validation.

## 0.2.0 - 2026-08-24

- Added a dedicated Material 3 typography reference with the full 15-role baseline size/line-height scale, semantic role guidance, custom-font mapping, accessibility, and Web/Compose/Flutter translation rules.
- Added a dedicated shape reference covering the Compose baseline 4/8/12/16/24dp example, square/full endpoints, newer 1.5 alpha shape slots, all 35 experimental `MaterialShapes`, morphing guidance, and platform boundaries.
- Added machine-readable typography and shape baseline JSON assets for future deterministic tooling.
- Added regression evals for typography hierarchy, web type-scale translation, coherent shape systems, and experimental Expressive-shape stability.

## 0.1.0 - 2026-08-24

- Added the portable `.agents/skills/material-design-3` skill for Codex and OpenCode.
- Added focused Material 3 foundation, component, adaptive/accessibility, Expressive, web, Compose, and Flutter references.
- Added dated primary-source tracking for volatile platform facts.
- Added a deterministic skill validator and conservative web-source audit tool.
- Added behavioral eval cases and a fresh-session control-vs-skill evaluation procedure.
- Added thin Codex/OpenCode adapter examples and Codex metadata.
