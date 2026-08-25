# Material Design 3 Skill v0.4.0 Design

## Purpose

v0.4.0 turns the repository from a primarily prose-driven Material 3 reasoning skill into a more deterministic engineering framework. The existing progressive-disclosure structure remains canonical; the release adds machine-readable platform capability data, deeper implementation contracts, stronger verification, and maintenance data that agents can query instead of guessing.

## Scope

The release adds six connected capabilities:

1. **Platform capability matrix** — a machine-readable snapshot of Material implementation status across Compose Material3, Wear Compose Material3, Flutter Material, Material Web, and Android Views/MDC.
2. **Deeper design/component contracts** — focused references for design intent, search/pickers/data-entry edge cases, and platform availability reasoning without bloating `SKILL.md`.
3. **Token/color interoperability** — DTCG 2025.10 guidance plus Material Color Utilities guidance for deterministic scheme generation and cross-platform semantic token mapping.
4. **Runtime verification** — keep the dependency-free Python static audit, but add an optional Playwright + axe runtime audit for rendered pages. The optional audit must not add runtime dependencies to projects that only install the skill.
5. **Granular source freshness** — track review dates per volatile source family rather than only a single global date.
6. **Behavior benchmark tooling** — make eval results easy to record and summarize without fabricating model/harness results that have not actually been run.

## Non-goals

- Do not replace the existing `SKILL.md` progressive-disclosure architecture.
- Do not make Material Web the recommended greenfield web component stack; its official library remains in maintenance mode even though releases continue.
- Do not present Android Views/MDC as the preferred new Android implementation; it is a maintenance/migration profile after the 2026 Compose-first shift.
- Do not silently require alpha/experimental Compose APIs.
- Do not claim WCAG or Material certification from heuristic tooling.
- Do not fabricate multi-model benchmark numbers.
- Do not add Figma/plugin packaging in this release.

## Current upstream snapshot

Reviewed 2026-08-25 from primary upstream sources:

- Compose Material3 stable `1.4.0`, alpha `1.5.0-alpha26`; Material3 Adaptive stable `1.3.0`.
- Wear Compose stable `1.6.2`; current release page exposes `1.7.0-beta01`.
- Flutter documentation reflects `3.44.7`; Material 3 has been the default since Flutter `3.16`.
- Material Web latest release is `2.5.0` (2026-07-14) but the project remains in maintenance mode.
- Material Components for Android / Views latest release is `1.14.0` (2026-05-13) and the repository is explicitly in maintenance mode; new projects should prefer Compose.
- DTCG `2025.10` is the first stable Design Tokens Community Group format.
- Material Color Utilities supports HCT, tonal palettes, dynamic schemes, scheme variants, light/dark mode, and contrast levels.

## Architecture

### 1. Capability matrix

Create `assets/platform-capabilities.json` with:

- a top-level schema/version/reviewed date;
- platform metadata including library status and version snapshot;
- component capability records;
- status values constrained to `stable`, `experimental`, `maintenance`, `partial`, `unavailable`, or `platform-native`;
- notes that distinguish design guidance from exact API availability.

The matrix is a decision aid, not an exhaustive API reference. Agents must still inspect a target project's pinned dependency before changing code.

### 2. Focused references

Add:

- `references/design-intent.md` — task/product personality, hierarchy, density, brand, adaptive needs, and Expressive intensity before visual treatment.
- `references/design-tokens.md` — semantic token layering, DTCG interchange, mapping into existing project token vocabularies, and when not to create a parallel token system.
- `references/color-system.md` — Material Color Utilities/HCT workflow, scheme variants, contrast levels, brand fallback, and platform translation boundaries.
- `references/platform-android-views.md` — maintenance-mode guidance and migration posture for MDC-Android.
- `references/accessibility-web.md` — WCAG 2.2 / ARIA-oriented web checks to complement platform-neutral accessibility guidance.
- `references/components-advanced.md` — focused contracts for search, pickers, menus, sliders, tooltips, data-heavy controls, and platform availability checks.

Update `SKILL.md` routing so these references are loaded only when applicable.

### 3. Runtime audit

Add `scripts/audit_runtime.mjs` as an optional executable:

- `--help` must work without Playwright/axe installed;
- dependencies are dynamically imported only for an actual audit;
- when dependencies are missing, exit with code `2` and give exact install guidance;
- audit one or more paths against a supplied base URL;
- collect axe violations, console errors, horizontal overflow, and basic focusability evidence;
- support JSON and human-readable output;
- clearly state that results are heuristic evidence, not certification.

Do not modify the repository into a Node package solely for this script.

### 4. Static audit improvements

Keep `audit_m3.py` dependency-free but reduce noisy guidance:

- fixed pixel font size should be a lower-confidence review signal, not described as an accessibility violation;
- add checks for viewport zoom disabling and `text-size-adjust: none` because those more directly threaten text scaling;
- include rule counts in JSON output for easier CI ingestion.

### 5. Granular source snapshots

Create `assets/source-snapshots.json` containing source families with `reviewed`, `url`, `kind`, and optional version/status facts.

Update `check_source_freshness.py` so:

- the existing `SKILL.md material-reviewed` behavior remains supported;
- granular source snapshots are checked by default when the asset exists;
- output identifies exactly which source families are stale;
- `--json` emits machine-readable freshness information;
- deterministic `--as-of` behavior remains available for tests.

No live scraping is required for the default CI check because upstream HTML changes would make normal verification brittle.

### 6. Behavioral benchmark tooling

Add:

- `evals/results/README.md` describing how real results are stored;
- `evals/summarize_results.py` that validates a result array against the practical contract and summarizes by harness/model/condition;
- tests for summary math and malformed records.

The repository must explicitly state that no result is a real benchmark unless it was produced by a recorded fresh-session run.

## Validation

v0.4.0 is complete when:

1. new deterministic tests fail on v0.3.0 behavior and pass after implementation;
2. `python -m unittest discover -s tests -v` passes;
3. `python .agents/skills/material-design-3/scripts/validate_skill.py` passes;
4. `skills-ref validate .agents/skills/material-design-3` passes in CI;
5. `node --check scripts/audit_runtime.mjs` and `audit_runtime.mjs --help` pass when Node is available;
6. source freshness checks pass for the 2026-08-25 snapshot;
7. repository documentation and changelog describe the new boundaries accurately.
