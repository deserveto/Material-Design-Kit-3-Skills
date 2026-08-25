# Material Design 3 Skill v0.4.0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the Material Design 3 Agent Skill into a more deterministic, platform-aware, verifiable engineering framework without abandoning progressive disclosure or adding mandatory heavy dependencies.

**Architecture:** Keep `SKILL.md` as the lightweight router. Put durable prose in focused references, deterministic platform/source facts in JSON assets, static checks in dependency-free Python, optional rendered checks in a dynamically-loaded Node script, and behavioral benchmark aggregation in the eval package. Existing validation remains the release gate.

**Tech Stack:** Markdown/YAML Agent Skill package, JSON assets, Python 3.11 standard library, optional Node.js + Playwright + `@axe-core/playwright`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-25-material-design-3-v040-design.md`

## Global Constraints

- Preserve the canonical skill path `.agents/skills/material-design-3`.
- Preserve progressive disclosure; do not move all reference content into `SKILL.md`.
- Do not introduce mandatory Node/npm dependencies for normal skill installation.
- Do not recommend Material Web or Android Views as preferred greenfield stacks while their official libraries are in maintenance mode.
- Do not silently adopt alpha/experimental Compose APIs.
- Do not claim Material/WCAG certification from heuristic audits.
- Do not fabricate model benchmark results.
- Source snapshot review date for this release is `2026-08-25`.

---

### Task 1: Add v0.4.0 contract tests

**Files:**
- Create: `tests/test_v040_features.py`
- Modify later: files named by subsequent tasks

**Interfaces:**
- Consumes: current v0.3.0 repository layout
- Produces: deterministic expectations for all new v0.4.0 files, data shapes, CLI behaviors, and routing

- [ ] **Step 1: Write failing tests**

Add tests asserting:

```python
self.assertIn('version: "0.4.0"', skill_text)
self.assertTrue((SKILL / "assets/platform-capabilities.json").is_file())
self.assertTrue((SKILL / "assets/source-snapshots.json").is_file())
self.assertTrue((SKILL / "references/design-intent.md").is_file())
self.assertTrue((SKILL / "references/design-tokens.md").is_file())
self.assertTrue((SKILL / "references/color-system.md").is_file())
self.assertTrue((SKILL / "references/platform-android-views.md").is_file())
self.assertTrue((SKILL / "references/accessibility-web.md").is_file())
self.assertTrue((SKILL / "references/components-advanced.md").is_file())
```

Also assert platform metadata/version snapshots, source snapshot validation, runtime-audit `--help`, static-audit new rules/counts, and benchmark summary behavior.

- [ ] **Step 2: Commit the tests without implementation**

Commit message:

```text
test: define v0.4.0 engineering framework contracts
```

- [ ] **Step 3: Verify RED in GitHub Actions**

Expected: repository tests fail because v0.4.0 files/routing do not yet exist.

---

### Task 2: Add deterministic capability/source data and focused references

**Files:**
- Create: `.agents/skills/material-design-3/assets/platform-capabilities.json`
- Create: `.agents/skills/material-design-3/assets/source-snapshots.json`
- Create: `.agents/skills/material-design-3/references/design-intent.md`
- Create: `.agents/skills/material-design-3/references/design-tokens.md`
- Create: `.agents/skills/material-design-3/references/color-system.md`
- Create: `.agents/skills/material-design-3/references/platform-android-views.md`
- Create: `.agents/skills/material-design-3/references/accessibility-web.md`
- Create: `.agents/skills/material-design-3/references/components-advanced.md`
- Modify: `.agents/skills/material-design-3/references/sources.md`
- Modify: `.agents/skills/material-design-3/SKILL.md`

**Interfaces:**
- Consumes: official source snapshot recorded in the spec
- Produces: machine-readable platform/source facts and on-demand reference routing

- [ ] **Step 1: Implement capability JSON**

Use top-level shape:

```json
{
  "schema_version": 1,
  "reviewed": "2026-08-25",
  "statuses": ["stable", "experimental", "maintenance", "partial", "unavailable", "platform-native"],
  "platforms": {},
  "components": {}
}
```

Record current platform snapshots and representative components including buttons, search, navigation, text fields, selection, sliders, dialogs/sheets, progress, carousel, and Expressive shapes/motion.

- [ ] **Step 2: Implement source snapshot JSON**

Each record must include:

```json
{
  "id": "compose-material3-releases",
  "kind": "platform-release",
  "url": "https://developer.android.com/jetpack/androidx/releases/compose-material3",
  "reviewed": "2026-08-25"
}
```

Optional facts may include stable/preview versions or maintenance state.

- [ ] **Step 3: Add focused references**

Keep each reference decision-oriented and explicitly state platform/version boundaries.

- [ ] **Step 4: Route references from `SKILL.md` and set version `0.4.0`**

Add routing rows for design intent, tokens, color generation, advanced components, web accessibility, Android Views, and capability/source data.

- [ ] **Step 5: Run relevant repository tests in CI after commit**

Expected: file/routing/data tests pass; audit/tool tests may remain red until later tasks.

---

### Task 3: Strengthen static audit and granular freshness

**Files:**
- Modify: `.agents/skills/material-design-3/scripts/audit_m3.py`
- Modify: `.agents/skills/material-design-3/scripts/check_source_freshness.py`
- Modify: `tests/test_audit_m3.py`
- Modify: `tests/test_source_freshness.py`
- Modify: `tests/test_v040_features.py`

**Interfaces:**
- Produces: `audit_m3.py --json` with `rule_counts`; new rules `m3.a11y.viewport-zoom-disabled` and `m3.a11y.text-size-adjust-disabled`; freshness JSON with per-source stale records

- [ ] **Step 1: Add failing tests for static audit**

Tests must prove these snippets are detected:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
```

```css
html { text-size-adjust: none; }
```

JSON output must contain `rule_counts`.

- [ ] **Step 2: Implement minimal static-audit changes**

Keep the existing fixed-pixel-font-size rule but change its message to describe token/scaling review rather than implying a direct accessibility failure.

- [ ] **Step 3: Add failing tests for per-source freshness**

Given a temporary `source-snapshots.json`, assert stale source IDs are named and JSON output is deterministic under `--as-of`.

- [ ] **Step 4: Implement granular freshness while preserving old CLI compatibility**

Default to the asset adjacent to the skill when present; retain `material-reviewed` as package-level metadata.

- [ ] **Step 5: Verify focused tests and full Python suite in CI**

---

### Task 4: Add optional rendered runtime audit

**Files:**
- Create: `.agents/skills/material-design-3/scripts/audit_runtime.mjs`
- Modify: `tests/test_v040_features.py`
- Modify: `.agents/skills/material-design-3/references/platform-web.md`
- Modify: `.agents/skills/material-design-3/references/accessibility-web.md`

**Interfaces:**
- CLI: `node audit_runtime.mjs --base-url http://localhost:3000 --paths /,/settings [--json]`
- Exit codes: `0` audit completed; `1` findings in `--strict`; `2` invalid arguments/missing optional dependencies/runtime setup error

- [ ] **Step 1: Add failing tests for script presence/help contract**

When Node is available:

```python
subprocess.run(["node", str(RUNTIME_AUDIT), "--help"], ...)
```

must return `0` without Playwright installed and mention `--base-url`, `--paths`, `--json`, and `--strict`.

- [ ] **Step 2: Implement argument parsing before dynamic imports**

- [ ] **Step 3: Dynamically load `playwright` and `@axe-core/playwright` only for real audits**

Missing dependency error must recommend:

```text
npm install --save-dev playwright @axe-core/playwright
```

- [ ] **Step 4: Implement rendered checks**

For each URL/viewport capture:

- axe violations;
- page/console errors;
- horizontal overflow;
- at least one keyboard Tab probe and active-element evidence;
- findings grouped by path/viewport.

- [ ] **Step 5: Document runtime verification usage and limitations**

- [ ] **Step 6: Verify Node syntax/help plus full Python suite in CI**

---

### Task 5: Add behavioral benchmark result tooling

**Files:**
- Create: `.agents/skills/material-design-3/evals/results/README.md`
- Create: `.agents/skills/material-design-3/evals/summarize_results.py`
- Modify: `.agents/skills/material-design-3/evals/README.md`
- Modify: `tests/test_eval_schema.py`
- Modify: `tests/test_v040_features.py`

**Interfaces:**
- CLI: `python evals/summarize_results.py <results.json> [--json]`
- Produces groups by `(harness, model, condition)` with run count, required-pass rate, forbidden-observation rate, and catastrophic-failure count

- [ ] **Step 1: Add failing summary tests**

Use a temporary result array with both `without-skill` and `with-skill` records and assert exact aggregate counts/rates.

- [ ] **Step 2: Implement standard-library-only summarizer**

Reject missing required numeric fields and impossible totals with exit code `2`.

- [ ] **Step 3: Document result provenance**

State clearly that examples/templates are not benchmark claims; only recorded fresh-session runs count as results.

- [ ] **Step 4: Verify focused eval tests and full suite**

---

### Task 6: Release docs, validation, and final verification

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Modify: `.github/workflows/verify.yml` if needed for Node syntax/help validation
- Modify: repository tests only when required to validate documented behavior

**Interfaces:**
- Produces: accurate v0.4.0 user-facing documentation and green CI

- [ ] **Step 1: Update README feature/structure/validation sections**

Document capability matrix, DTCG/color guidance, Android Views maintenance profile, optional runtime audit, granular freshness, and benchmark summary tooling.

- [ ] **Step 2: Add `0.4.0 - 2026-08-25` changelog section**

- [ ] **Step 3: Ensure CI runs**

```text
python -m unittest discover -s tests -v
python .agents/skills/material-design-3/scripts/validate_skill.py
skills-ref validate .agents/skills/material-design-3
node --check .agents/skills/material-design-3/scripts/audit_runtime.mjs
node .agents/skills/material-design-3/scripts/audit_runtime.mjs --help
python .agents/skills/material-design-3/scripts/check_source_freshness.py --max-age-days 45
```

- [ ] **Step 4: Run final verification on the head commit**

Require green GitHub Actions/status checks before calling the implementation complete.

- [ ] **Step 5: Review branch diff against `main`**

Confirm no unrelated files changed, no fabricated benchmark results were added, and the branch remains fast-forwardable from its original base.
