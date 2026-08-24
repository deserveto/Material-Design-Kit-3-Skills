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
  <img alt="version" src="https://img.shields.io/badge/version-v0.3.0-7c3aed?style=for-the-badge" />
  <img alt="skill" src="https://img.shields.io/badge/skill-material--design--3-0f766e?style=for-the-badge" />
  <img alt="license" src="https://img.shields.io/badge/license-MIT-111827?style=for-the-badge" />
</p>

<p align="center">
  <a href="#quick-install">Quick install</a>
  ·
  <a href="#what-you-get">What you get</a>
  ·
  <a href="#usage">Usage</a>
  ·
  <a href="#validation-and-audit">Validation</a>
  ·
  <a href="#repository-structure">Structure</a>
</p>

---

## Why this exists

Most "Material Design" prompts teach a **look**:

- purple everywhere,
- round cards,
- oversized radii,
- lots of shadows.

This repository teaches an agent a **system** instead:

- semantic design tokens and color roles;
- typography, shape, layout/spacing, motion, elevation, and Material Symbols;
- component choice by interaction semantics and hierarchy;
- complete focus/pressed/selected/loading/error state contracts;
- adaptive layouts rather than stretched phone screens;
- accessibility and rendered verification;
- Material 3 Expressive with restraint;
- Web, mobile Compose, Wear Compose, and Flutter platform boundaries;
- phased Material 2/legacy migration;
- evidence-based review severity;
- stable versus alpha/experimental API boundaries;
- deterministic behavioral eval contracts and maintenance checks.

It is an **unofficial community project** and is **not affiliated with or endorsed by Google**.

---

## Quick install

The easiest path is through the shared **`skills` CLI** ecosystem.

### Install for the current project

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3
```

### Install for Codex

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3 \
  --agent codex \
  --yes
```

### Install for OpenCode

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3 \
  --agent opencode \
  --yes
```

### Install globally

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3 \
  --global \
  --yes
```

### Install for multiple agents

```bash
npx skills add deserveto/Material-Design-Kit-3-Skills@material-design-3 \
  --agent codex \
  --agent opencode \
  --yes
```

> The canonical skill name is **`material-design-3`**.

---

## Demo workflow

<p align="center">
  <img src="assets/demo-flow.svg" alt="Install, use, and verify workflow for the Material Design 3 Skill" width="100%" />
</p>

### Typical flow

1. Install the skill with `npx skills add ...`
2. Ask your coding agent to build, migrate, or review an interface using Material 3
3. Let the skill route the agent to only the references it needs:
   - foundations / typography / shape,
   - layout and spacing,
   - specific component families,
   - interaction states,
   - adaptive/accessibility,
   - migration or review rubric,
   - Expressive,
   - Web / Compose / Wear / Flutter
4. Run project verification plus the included Material audit helper when useful
5. Review the rendered result and relevant states, not just the source code

---

## What you get

| Area | What it gives the agent |
|---|---|
| **Core skill** | Lean `SKILL.md` with progressive-disclosure routing |
| **Foundations** | Semantic tokens, color, motion, elevation, and icons |
| **Typography guide** | Full 15-role baseline scale, custom-font mapping, scaling, and platform translation |
| **Shape guide** | Corner scale, Compose baseline values, newer alpha slots, and all 35 experimental MaterialShapes |
| **Layout + spacing** | Structural regions, spacing systems, insets, readable width, and adaptive composition |
| **Component decision guides** | Separate action, navigation, input/selection, and feedback/containment rules |
| **Interaction states** | Focus, pressed, selected, disabled, loading, error, async recovery, and reduced-motion contracts |
| **Adaptive + accessibility** | Window-size thinking, navigation adaptation, keyboard/focus, touch targets, contrast, scaling |
| **Migration guide** | Phased Material 2/legacy → M3 migration instead of cosmetic reskinning |
| **Review rubric** | BLOCKER/HIGH/MEDIUM/LOW findings with evidence, impact, recommendation, verification |
| **Expressive** | Material 3 Expressive guidance with clear restraint rules |
| **Platform profiles** | Web, Android Compose, Wear Compose Material 3, and Flutter implementation guidance |
| **Machine-readable assets** | Typography, shape, action-prominence, and interaction-state data for deterministic tooling |
| **Validator** | Checks the skill package contract and reference integrity |
| **Audit helper** | Conservative static review for common web-side M3 issues with optional strict mode |
| **Behavioral evals** | Cases, fixture contracts, and a stable result schema for control-vs-skill runs |
| **Freshness guard** | Monthly CI check that flags Material source research when its review date becomes stale |

---

## Usage

### When to use this skill

Use it when a task is explicitly about:

- creating a new Material 3 / M3 UI,
- extending an existing Material 3 application,
- migrating from Material 2 / legacy patterns,
- reviewing a UI for Material 3 alignment,
- applying Material 3 Expressive carefully,
- implementing M3 on Web, Android Compose, Wear OS Compose, or Flutter.

### What the skill will deliberately avoid

This skill tries to stop agents from doing things like:

- forcing Material into a repo that uses another design system,
- translating Compose APIs literally into web code,
- using mobile Compose Material3 as the primary Wear OS component library,
- hard-coding reference purple everywhere,
- inventing random radii and spacing per component,
- wrapping every section in cards,
- overusing FABs, chips, shadows, or Expressive shapes,
- removing keyboard focus outlines without a replacement,
- stretching phone navigation patterns onto wide layouts,
- calling a color/radius reskin a complete M2→M3 migration,
- silently using experimental APIs as if they were stable.

---

## Validation and audit

### Validate the skill package

```bash
python .agents/skills/material-design-3/scripts/validate_skill.py
```

CI also runs the official Agent Skills reference validator:

```bash
skills-ref validate .agents/skills/material-design-3
```

### Run the repository test suite

```bash
python -m unittest discover -s tests -v
```

### Run the heuristic Material audit for a web project

```bash
python .agents/skills/material-design-3/scripts/audit_m3.py src
```

### JSON output

```bash
python .agents/skills/material-design-3/scripts/audit_m3.py --json src
```

### Strict CI/review mode

```bash
python .agents/skills/material-design-3/scripts/audit_m3.py --strict src
```

`--strict` returns exit code `1` when any heuristic finding exists. It is opt-in because findings are review candidates, not automatic proof of a defect.

### Check source-review freshness

```bash
python .agents/skills/material-design-3/scripts/check_source_freshness.py --max-age-days 45
```

> A clean audit is **not** Material compliance or accessibility certification. It is a conservative reviewer/agent aid.

---

## Behavioral evals

The repository includes a harness-neutral eval corpus for fresh-session testing with and without the skill.

Covered scenarios include:

- new M3 UI generation,
- preserving non-Material existing systems,
- M2/legacy phased migration,
- semantic color role usage,
- adaptive list-detail and layout/spacing behavior,
- touch target, focus, loading/error, and icon semantics,
- Material 3 Expressive restraint,
- Compose stable vs experimental API boundaries,
- Wear Compose vs mobile Compose platform boundaries,
- Flutter migration,
- evidence-based review severity,
- visual verification behavior.

`fixtures.json` defines repeatable environment contracts and `results.schema.json` defines how to record harness/model/commit/control-vs-skill results.

See:

```text
.agents/skills/material-design-3/evals/
```

---

## Current platform snapshot

At the current research snapshot (**reviewed 2026-08-24**):

- Google's Material site presents **M3 Expressive** as the current evolution of Material 3.
- AndroidX Compose Material3 is **1.4.0 stable** with a separate **1.5.0-alpha26** line containing newer Expressive APIs.
- Wear Compose is **1.6.2 stable** and its Wear-specific Material3 library already supports Material 3 Expressive; Wear must not be treated as mobile Compose Material3.
- Flutter has used Material 3 by default since Flutter 3.16, but migration can still require real component changes.
- Agent Skills defines progressive disclosure and recommends `skills-ref validate` for format validation.

Version-sensitive facts are recorded separately from stable concepts so the agent does not confuse:

```text
official Material guidance
!=
stable API everywhere
!=
the same API on every platform
```

Primary sources and review dates are pinned in:

```text
.agents/skills/material-design-3/references/sources.md
```

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
│   └── results.schema.json
├── references/
│   ├── adaptive-accessibility.md
│   ├── components.md
│   ├── components-actions.md
│   ├── components-navigation.md
│   ├── components-input-selection.md
│   ├── components-feedback-containment.md
│   ├── expressive.md
│   ├── foundations.md
│   ├── interaction-states.md
│   ├── layout-spacing.md
│   ├── migration.md
│   ├── review-rubric.md
│   ├── typography.md
│   ├── shape.md
│   ├── platform-compose.md
│   ├── platform-wear.md
│   ├── platform-flutter.md
│   ├── platform-web.md
│   └── sources.md
├── assets/
│   ├── typography-baseline.json
│   ├── shape-baseline.json
│   ├── component-prominence.json
│   └── interaction-states.json
└── scripts/
    ├── audit_m3.py
    ├── check_source_freshness.py
    └── validate_skill.py

adapters/
├── codex/
│   └── AGENTS.md.example
└── opencode/
    ├── AGENTS.md.example
    └── opencode.jsonc.example

tests/
.github/workflows/
docs/
assets/
```

---

## Manual install fallback

If you do not want to use `npx skills`, you can still copy the skill manually:

```bash
mkdir -p .agents/skills
cp -R /path/to/Material-Design-Kit-3-Skills/.agents/skills/material-design-3 .agents/skills/
```

For user-global installation, place it in:

```text
~/.agents/skills/material-design-3/
```

---

## Roadmap

Possible later work:

- SARIF output and additional audit rules with tighter false-positive controls;
- real fixture repositories plus published multi-model behavior matrices;
- richer rendered demo examples and golden comparisons;
- Figma-assisted workflows;
- plugin packaging for wider distribution;
- additional platform profiles where Material implementations are maintained.

The canonical Material knowledge should remain in the **Agent Skill**, even if plugins are added later.

---

## License

This repository is released under the **MIT License** for repository-authored content.

Material Design, Material You, Material Symbols, Android, Flutter, Google, and related names/trademarks belong to their respective owners. External source material remains under its original terms.
