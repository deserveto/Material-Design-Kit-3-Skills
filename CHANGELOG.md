# Changelog

All notable changes to this project are documented here.

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
