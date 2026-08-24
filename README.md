# Material Design Kit 3 Skills

A portable Agent Skills implementation of **Material Design 3**, **Material You**, and **Material 3 Expressive** guidance for coding agents.

The project is built around one canonical skill:

```text
.agents/skills/material-design-3/
```

That location is intentionally shared by **Codex** and **OpenCode**, so the Material knowledge does not fork into harness-specific prompts.

> **Status:** v0.1.0. The Material/platform research snapshot was reviewed on 2026-08-24. Version-sensitive implementation facts should be re-checked against the primary sources before dependency changes.

## What this skill is trying to solve

Most "Material Design" prompts teach an agent a look: purple, round cards, large radii, and shadows. This project instead teaches the agent to reason through:

- semantic design tokens and color roles;
- typography, shape, motion, elevation, and Material Symbols;
- component choice by interaction semantics and hierarchy;
- adaptive layouts rather than stretched phone screens;
- accessibility and complete interaction states;
- Material 3 Expressive with restraint;
- platform-specific implementation differences;
- stable versus alpha/experimental APIs;
- deterministic and visual verification.

It is an **unofficial** community project and is not affiliated with or endorsed by Google.

## Repository structure

```text
.agents/skills/material-design-3/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── evals/
│   ├── README.md
│   └── cases.json
├── references/
│   ├── adaptive-accessibility.md
│   ├── components.md
│   ├── expressive.md
│   ├── foundations.md
│   ├── platform-compose.md
│   ├── platform-flutter.md
│   ├── platform-web.md
│   └── sources.md
└── scripts/
    ├── audit_m3.py
    └── validate_skill.py

adapters/
├── codex/
│   └── AGENTS.md.example
└── opencode/
    ├── AGENTS.md.example
    └── opencode.jsonc.example
```

`SKILL.md` stays intentionally small. Detailed knowledge is loaded from focused references only when the task needs it.

## Install in a repository

Copy the canonical skill into the target repository:

```bash
mkdir -p .agents/skills
cp -R /path/to/Material-Design-Kit-3-Skills/.agents/skills/material-design-3 .agents/skills/
```

Then optionally adapt one of the small `AGENTS.md.example` files into the target repository's own instructions.

### Codex

Codex scans `.agents/skills` in the current repository hierarchy. After installation, invoke explicitly with `$material-design-3`, use `/skills`, or let Codex select it when the task matches the skill description.

For a user-global installation, place the skill at:

```text
~/.agents/skills/material-design-3/
```

The bundled `agents/openai.yaml` adds Codex/ChatGPT-facing metadata without adding external tool dependencies.

### OpenCode

OpenCode also discovers the agent-compatible path:

```text
.agents/skills/material-design-3/SKILL.md
```

A user-global copy can live at:

```text
~/.agents/skills/material-design-3/
```

OpenCode can load it through its native skill mechanism. `adapters/opencode/opencode.jsonc.example` shows an optional permission entry that explicitly allows this skill.

## Validate the skill package

No third-party Python dependencies are required.

```bash
python .agents/skills/material-design-3/scripts/validate_skill.py
```

The validator checks the Agent Skills naming/frontmatter contract, progressive-disclosure line limit, and referenced local files.

Run the repository test suite:

```bash
python -m unittest discover -s tests -v
```

## Heuristic web audit

For a web project, the skill includes a conservative review helper:

```bash
python .agents/skills/material-design-3/scripts/audit_m3.py src
```

Machine-readable output:

```bash
python .agents/skills/material-design-3/scripts/audit_m3.py --json src
```

The current rules review a few high-signal problems such as raw component colors, `transition: all`, and generic React `div`/`span` click targets. Theme custom-property declarations and common generated/dependency directories are excluded.

**A clean audit is not Material Design or accessibility certification.** It is only an agent/reviewer aid.

## Behavioral evals

`.agents/skills/material-design-3/evals/cases.json` contains scenarios for:

- new M3 UI creation;
- preserving a non-Material existing system;
- M2/legacy migration;
- semantic color roles;
- adaptive list-detail layouts;
- touch targets and icon semantics;
- Material 3 Expressive restraint;
- Compose stable/experimental API boundaries;
- Flutter migration;
- visual verification.

See the eval README for the control-vs-skill procedure. The important part is running the same case in fresh sessions **without the skill** and **with the skill**, not simply checking that a prompt "sounds good."

## Current platform snapshot

The reference corpus records volatile implementation facts separately from stable Material concepts. At the 2026-08-24 review:

- Google's Material site presents M3 Expressive as the current Material 3 evolution and advertises an updated Figma M3 Design Kit.
- AndroidX Compose Material3 lists 1.4.0 stable and 1.5.0-alpha26 alpha; newer Expressive APIs such as `MotionScheme` and `MaterialShapes` need version/status checks before adoption.
- Flutter has used Material 3 by default since Flutter 3.16, but migration can still require component changes rather than a theme flag alone.

Primary sources and review dates live in `references/sources.md`.

## Design philosophy

The skill follows this order:

```text
user task
  -> existing product/design system
  -> information hierarchy
  -> Material component semantics
  -> semantic theme roles
  -> platform implementation
  -> interaction + adaptive + accessibility states
  -> deterministic verification
  -> rendered verification
```

That is intentionally different from "make it look Material."

## Roadmap

Possible later work, after the standalone skill proves itself through real-model evals:

- broader static audit rules with explicit false-positive controls;
- fixture repositories and automated Codex/OpenCode behavior matrices;
- Figma-assisted workflows;
- plugin packaging for wider distribution;
- additional platform profiles where there is a maintained Material implementation.

The canonical Material knowledge should remain in the Agent Skill even if plugins are added later.

## License

MIT for repository-authored content. Material Design, Material You, Material Symbols, Android, Flutter, Google, and related names/trademarks belong to their respective owners. External source material remains under its original terms.
