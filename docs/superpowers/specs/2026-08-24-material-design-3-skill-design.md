# Material Design 3 Agent Skill Design

## Goal

Create a portable, source-grounded Material Design 3 agent skill that Codex and OpenCode can discover from `.agents/skills/material-design-3`, with enough platform-specific guidance and deterministic checks to produce and review robust Material 3 interfaces without turning the skill into a giant prompt.

## Architecture

The repository has one canonical skill. `SKILL.md` contains only trigger conditions, decision rules, workflow, reference routing, verification requirements, and high-value anti-patterns. Detailed Material knowledge lives in focused `references/` files that agents load only when needed. Self-contained Python scripts provide deterministic repository validation and a conservative heuristic web audit. JSON eval cases capture expected agent behavior for generation, migration, adaptive layout, accessibility, theming, and Material 3 Expressive restraint.

Codex and OpenCode both consume the same `.agents/skills/material-design-3` directory. Codex-specific UI metadata lives in `agents/openai.yaml`; OpenCode-specific configuration is an optional example outside the canonical skill. The skill must remain useful without either adapter.

## Design principles

1. **Semantic before visual.** Agents choose Material roles and components by meaning and hierarchy, not by copying reference colors or rounded-card aesthetics.
2. **Inspect before replacing.** Existing design systems, tokens, components, and project conventions are preserved unless the user explicitly asks for migration.
3. **Platform concepts and APIs are separate.** Stable Material concepts must not be conflated with experimental or platform-specific APIs.
4. **Progressive disclosure.** The main skill stays concise; focused references hold the detailed corpus.
5. **Volatile facts are dated.** Version-sensitive platform facts include a `Reviewed` date and primary sources.
6. **Verification is required.** Agents should run existing tests/builds, deterministic checks when applicable, and visual/browser verification when available.
7. **Heuristic audits are not compliance certification.** Static checks report review findings, not proof of Material or accessibility conformance.
8. **Expressive is selective.** M3 Expressive may increase hierarchy and emotional character, but must not sacrifice information architecture, familiarity, accessibility, or task efficiency.

## Canonical skill contents

- `SKILL.md`: trigger, workflow, reference routing, verification contract, anti-patterns.
- `references/foundations.md`: tokens, color, typography, shape, motion, elevation, iconography.
- `references/components.md`: component selection and hierarchy matrix.
- `references/adaptive-accessibility.md`: adaptive layouts, window classes, interaction/accessibility requirements.
- `references/expressive.md`: M3 Expressive techniques, motion, shape library, restraint, API-status policy.
- `references/platform-web.md`: framework-agnostic web/React guidance.
- `references/platform-compose.md`: current Android Compose Material 3 status and mappings.
- `references/platform-flutter.md`: Flutter Material 3 mappings and migration cautions.
- `references/sources.md`: primary sources and review dates.
- `scripts/validate_skill.py`: validates package structure and local invariants.
- `scripts/audit_m3.py`: optional conservative static audit for web UI source.
- `agents/openai.yaml`: Codex/ChatGPT metadata.

## Evaluation strategy

The repo includes behavioral scenarios before the skill is considered releasable. Each case has a prompt, required behaviors, forbidden behaviors, and relevant reference domains. Automated tests validate the eval schema and deterministic scripts. Full model-behavior evaluation requires running the cases in fresh Codex/OpenCode sessions; that is documented separately because this environment does not provide authenticated Codex/OpenCode CLIs.

## Distribution

Version 0.1 is a standalone Agent Skills package, not a harness-specific plugin. Consumers may copy or symlink the canonical skill into a repository or user-level `.agents/skills`. A future plugin may bundle the skill with Figma or other tools, but plugin behavior is intentionally out of scope for v0.1.

## Licensing and attribution

Repository-authored content is MIT licensed. Material Design and Google product names are used descriptively. The project is unofficial and not affiliated with or endorsed by Google. Primary-source URLs are cited; source prose is summarized rather than copied wholesale.
