<p align="center">
  <img src="assets/banner.svg" alt="Material Design 3 Skill banner" width="100%" />
</p>

<h1 align="center">Material Design 3 Skill</h1>

<p align="center">
  A portable <strong>Agent Skill</strong> for <strong>Material Design 3</strong>, <strong>Material You</strong>, and <strong>Material 3 Expressive</strong>.
  <br />
  Built for coding agents such as <strong>Codex</strong> and <strong>OpenCode</strong>, with one canonical skill source under <code>.agents/skills/</code>.
</p>

<p align="center">
  <a href="https://github.com/deserveto/Material-Design-Kit-3-Skills"><img alt="repo" src="https://img.shields.io/badge/repo-Material--Design--Kit--3--Skills-1f6feb?style=for-the-badge" /></a>
  <img alt="version" src="https://img.shields.io/badge/version-v0.4.0-7c3aed?style=for-the-badge" />
  <img alt="skill" src="https://img.shields.io/badge/skill-material--design--3-0f766e?style=for-the-badge" />
  <img alt="license" src="https://img.shields.io/badge/license-MIT-111827?style=for-the-badge" />
</p>

<p align="center">
  <a href="#quick-install">Quick install</a>
  ·
  <a href="#what-you-get">What you get</a>
  ·
  <a href="#validation-and-audit">Validation</a>
  ·
  <a href="#behavioral-evals">Evals</a>
  ·
  <a href="#repository-structure">Structure</a>
</p>

---

## Why this exists

Most "Material Design" prompts teach a **look**: purple everywhere, round cards, oversized radii, and lots of shadows.

This repository teaches an agent a **system** instead:

- semantic design tokens and color roles;
- design intent before styling;
- deterministic color-scheme and token interoperability guidance;
- typography, shape, layout/spacing, motion, elevation, and Material Symbols;
- component choice by interaction semantics and hierarchy;
- complete focus/pressed/selected/loading/error contracts;
- adaptive layouts rather than stretched phone screens;
- WCAG/ARIA-aware web accessibility and rendered verification;
- Material 3 Expressive with restraint;
- Web, Compose, Wear Compose, Flutter, and existing Android Views boundaries;
- phased Material 2/legacy migration;
- evidence-based review severity;
- stable vs preview/experimental/maintenance API boundaries;
- machine-readable platform/source snapshots;
- deterministic scripts plus behavioral eval contracts.

It is an **unofficial community project** and is **not affiliated with or endorsed by Google**.

---

## Quick install

### Current project

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3
```

### Codex

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3 \
  --agent codex \
  --yes
```

### OpenCode

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3 \
  --agent opencode \
  --yes
```

### Global

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3 \
  --global \
  --yes
```

> The canonical skill name is **`material-design-3`**.

---

## Demo workflow

<p align="center">
  <img src="assets/demo-flow.svg" alt="Install, use, and verify workflow for the Material Design 3 Skill" width="100%" />
</p>

A typical run is:

1. Install the skill.
2. Ask the agent to build, migrate, or review Material 3 UI.
3. The skill inspects the existing stack/theme/components before choosing implementation primitives.
4. For substantial new/redesign work it derives a small design-intent model before styling.
5. It loads only the relevant references and machine-readable capability/source data.
6. It implements semantic tokens, appropriate components, complete states, accessibility, and adaptive behavior.
7. It runs project verification plus the bundled static/runtime checks when useful.
8. It inspects the rendered result rather than declaring visual correctness from source alone.

---

## What you get

| Area | What it gives the agent |
|---|---|
| **Core skill** | Lean `SKILL.md` with progressive-disclosure routing |
| **Design intent** | Primary-task, hierarchy, density, brand, adaptive, and Expressive-intensity reasoning |
| **Foundations** | Semantic tokens, color, motion, elevation, and icons |
| **Token interoperability** | DTCG 2025.10-oriented interchange guidance and mapping into existing project token systems |
| **Color system** | Material Color Utilities / HCT workflow for deterministic scheme generation instead of guessed hex values |
| **Typography guide** | Full 15-role baseline scale, custom-font mapping, scaling, and platform translation |
| **Shape guide** | Corner scale, Compose baseline values, newer slots, and all 35 experimental MaterialShapes |
| **Layout + spacing** | Structural regions, spacing systems, insets, readable width, and adaptive composition |
| **Component guides** | Action, navigation, input/selection, containment, plus advanced search/picker/menu/slider contracts |
| **Interaction states** | Focus, pressed, selected, disabled, loading, error, async recovery, and reduced-motion contracts |
| **Adaptive + accessibility** | Window-space thinking, navigation adaptation, keyboard/focus, targets, contrast, scaling |
| **Web accessibility** | WCAG 2.2 / ARIA-oriented implementation and verification checks |
| **Migration guide** | Phased Material 2/legacy → M3 migration instead of cosmetic reskinning |
| **Review rubric** | BLOCKER/HIGH/MEDIUM/LOW findings with evidence, impact, recommendation, verification |
| **Expressive** | Material 3 Expressive guidance with clear restraint rules |
| **Platform profiles** | Web, Android Compose, Wear Compose Material 3, Flutter, and Android Views maintenance/migration |
| **Capability matrix** | `platform-capabilities.json` for reviewed platform/component availability and stability boundaries |
| **Source snapshots** | `source-snapshots.json` with granular source-family review dates and volatile facts |
| **Static audit** | Dependency-free source review with optional strict mode and machine-readable rule counts |
| **Runtime audit** | Optional Playwright + axe rendered checks without making Node dependencies mandatory for skill installation |
| **Behavioral evals** | Cases, fixture contracts, result schema, provenance rules, and deterministic result summarization |
| **Freshness guard** | Package-level and per-source staleness detection |

---

## Usage

Use the skill when a task is explicitly about creating/extending Material 3 UI, migrating from Material 2 or legacy Material, reviewing Material alignment, applying M3 Expressive, maintaining/migrating an existing Views-based Android Material app, or implementing Material semantics on Web, Compose, Wear Compose, or Flutter.

The skill deliberately avoids forcing Material into unrelated design systems, treating Material as “purple rounded cards,” copying APIs across platforms, silently upgrading to experimental libraries, treating Material Web maintenance mode as full future parity, recommending Android Views as the default greenfield Android stack, and inventing behavioral benchmark numbers.

### Machine-readable lookup

For platform/version-sensitive work, the agent can consult:

```text
.agents/skills/material-design-3/assets/platform-capabilities.json
.agents/skills/material-design-3/assets/source-snapshots.json
```

These are **reviewed snapshots**, not replacements for checking the target project's pinned dependencies and live upstream docs before a version-sensitive dependency change.

---

## Validation and audit

### Validate the skill package

```bash
python .agents/skills/material-design-3/scripts/validate_skill.py
skills-ref validate .agents/skills/material-design-3
```

### Run the repository test suite

```bash
python -m unittest discover -s tests -v
```

### Static Material/web audit

```bash
python .agents/skills/material-design-3/scripts/audit_m3.py src
python .agents/skills/material-design-3/scripts/audit_m3.py --json src
python .agents/skills/material-design-3/scripts/audit_m3.py --strict src
```

The static audit remains intentionally conservative. v0.4.0 adds stronger signals for disabled viewport zoom and disabled text-size adjustment, while keeping fixed-pixel typography as a review candidate rather than calling it an accessibility failure by itself.

### Optional rendered runtime audit

`audit_runtime.mjs --help` has no optional dependency requirement. To actually audit a running web app, install the runtime tools in the **target project**:

```bash
npm install --save-dev playwright @axe-core/playwright
```

Then run:

```bash
node .agents/skills/material-design-3/scripts/audit_runtime.mjs \
  --base-url http://localhost:3000 \
  --paths /,/settings
```

JSON/strict modes are also supported:

```bash
node .agents/skills/material-design-3/scripts/audit_runtime.mjs \
  --base-url http://localhost:3000 \
  --paths /,/settings \
  --json \
  --strict
```

It collects axe violations, browser/page errors, horizontal overflow, and a basic keyboard-focus probe at narrow and wide viewports by default.

> A clean static or runtime audit is **not** Material, WCAG, or accessibility certification.

### Check research freshness

```bash
python .agents/skills/material-design-3/scripts/check_source_freshness.py --max-age-days 45
python .agents/skills/material-design-3/scripts/check_source_freshness.py --max-age-days 45 --json
```

v0.4.0 checks both the package review date and granular source-family dates from `source-snapshots.json`.

---

## Behavioral evals

The repository includes a harness-neutral corpus for fresh-session control-vs-skill testing.

Real result files belong in:

```text
.agents/skills/material-design-3/evals/results/
```

Do **not** commit synthetic examples as benchmark evidence. A result only counts as a benchmark run when it came from a documented fresh session with provenance.

Summarize a recorded result set with:

```bash
python .agents/skills/material-design-3/evals/summarize_results.py results.json
python .agents/skills/material-design-3/evals/summarize_results.py results.json --json
```

The summarizer groups by harness/model/condition and reports required-behavior pass rate, forbidden-behavior observation rate, run count, and catastrophic-failure count when recorded. It does not execute models or create evidence.

---

## Current platform snapshot

At the current research snapshot (**reviewed 2026-08-25**):

- Material 3 Expressive remains the current Material direction.
- AndroidX Compose Material3 is **1.4.0 stable** with **1.5.0-alpha26** as the current alpha snapshot; Material3 Adaptive is **1.3.0 stable**.
- Wear Compose is **1.6.2 stable** with **1.7.0-beta01** as the current preview snapshot; Wear uses its own Material3 APIs.
- Flutter documentation reflects **3.44.7** and Material 3 has been the default since Flutter 3.16.
- Material Web has a **2.5.0** release but remains in official **maintenance mode**.
- Material Components for Android Views is at **1.14.0** and is in **maintenance mode**; new Android Material work should prefer Compose when viable.
- DTCG **2025.10** is the first stable Design Tokens Community Group interchange format.

Version-sensitive facts are recorded separately from stable concepts so the agent does not confuse:

```text
official Material guidance
!= stable API everywhere
!= the same API on every platform
!= an actively expanding component library everywhere
```

Primary sources are tracked in `references/sources.md` and `assets/source-snapshots.json`.

---

## Repository structure

```text
.agents/skills/material-design-3/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── evals/
│   ├── README.md
│   ├── cases.json
│   ├── fixtures.json
│   ├── results.schema.json
│   ├── summarize_results.py
│   └── results/
│       └── README.md
├── references/
│   ├── design-intent.md
│   ├── design-tokens.md
│   ├── color-system.md
│   ├── foundations.md
│   ├── typography.md
│   ├── shape.md
│   ├── layout-spacing.md
│   ├── components*.md
│   ├── interaction-states.md
│   ├── adaptive-accessibility.md
│   ├── accessibility-web.md
│   ├── expressive.md
│   ├── migration.md
│   ├── review-rubric.md
│   ├── platform-web.md
│   ├── platform-compose.md
│   ├── platform-wear.md
│   ├── platform-flutter.md
│   ├── platform-android-views.md
│   └── sources.md
├── assets/
│   ├── platform-capabilities.json
│   ├── source-snapshots.json
│   ├── typography-baseline.json
│   ├── shape-baseline.json
│   ├── component-prominence.json
│   └── interaction-states.json
└── scripts/
    ├── audit_m3.py
    ├── audit_runtime.mjs
    ├── check_source_freshness.py
    └── validate_skill.py

adapters/
tests/
.github/workflows/
docs/
assets/
```

---

## Manual install fallback

```bash
mkdir -p .agents/skills
cp -R /path/to/Material-Design-Kit-3-Skills/.agents/skills/material-design-3 .agents/skills/
```

For user-global installation, place it in `~/.agents/skills/material-design-3/`.

---

## Roadmap

Possible later work includes SARIF output, real fixture repositories plus published multi-model behavior matrices, richer rendered/golden comparisons, Figma-assisted workflows, plugin packaging, and additional maintained platform profiles.

The canonical Material knowledge should remain in the **Agent Skill**, even if plugins are added later.

---

## License

This repository is released under the **MIT License** for repository-authored content.

Material Design, Material You, Material Symbols, Android, Flutter, Google, and related names/trademarks belong to their respective owners. External source material remains under its original terms.
