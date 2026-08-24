# Material Design 3 Agent Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a portable Material Design 3 Agent Skill for Codex and OpenCode with focused references, deterministic validation, behavioral eval fixtures, and CI.

**Architecture:** One canonical `.agents/skills/material-design-3` package follows the Agent Skills standard. A concise `SKILL.md` routes agents to focused references; standard-library Python scripts provide validation and optional heuristic auditing; adapters stay thin and outside the canonical knowledge source.

**Tech Stack:** Markdown, YAML, JSON, Python 3.10+ standard library, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-24-material-design-3-skill-design.md`

## Global Constraints

- Canonical discovery path: `.agents/skills/material-design-3/SKILL.md`.
- Skill name must be exactly `material-design-3` and satisfy the Agent Skills name grammar.
- `SKILL.md` must stay under 500 lines and use progressive disclosure.
- No runtime Python dependencies beyond the standard library.
- Version-sensitive platform claims must be dated and sourced in `references/sources.md`.
- Static auditing must describe itself as heuristic, never certification.
- Material 3 Expressive experimental APIs must be identified as experimental where applicable.

---

### Task 1: Define eval and validation contracts

**Files:**
- Create: `tests/test_validate_skill.py`
- Create: `tests/test_eval_schema.py`
- Create: `.agents/skills/material-design-3/evals/cases.json`
- Create: `.agents/skills/material-design-3/scripts/validate_skill.py`

**Interfaces:**
- `validate_skill.py [skill_dir]` returns exit code 0 only when structural invariants pass.
- Eval cases are a JSON array with `id`, `prompt`, `required`, `forbidden`, and `references`.

- [ ] Write failing unit tests for the missing validator and eval contract.
- [ ] Run `python -m unittest discover -s tests -v` and confirm failure is caused by missing implementation/files.
- [ ] Implement the minimal validator and eval fixtures.
- [ ] Run the tests and confirm they pass.

### Task 2: Author the canonical skill and focused references

**Files:**
- Create: `.agents/skills/material-design-3/SKILL.md`
- Create: `.agents/skills/material-design-3/references/foundations.md`
- Create: `.agents/skills/material-design-3/references/components.md`
- Create: `.agents/skills/material-design-3/references/adaptive-accessibility.md`
- Create: `.agents/skills/material-design-3/references/expressive.md`
- Create: `.agents/skills/material-design-3/references/platform-web.md`
- Create: `.agents/skills/material-design-3/references/platform-compose.md`
- Create: `.agents/skills/material-design-3/references/platform-flutter.md`
- Create: `.agents/skills/material-design-3/references/sources.md`

**Interfaces:**
- `SKILL.md` references each file directly using one-level relative paths.
- References label stable concepts separately from version-sensitive platform APIs.

- [ ] Extend validator tests to require the canonical references and required SKILL sections.
- [ ] Run tests and confirm the new assertions fail.
- [ ] Write the skill and references from primary-source-grounded synthesis.
- [ ] Run tests and `validate_skill.py` until green.

### Task 3: Add conservative web audit tooling

**Files:**
- Create: `tests/test_audit_m3.py`
- Create: `.agents/skills/material-design-3/scripts/audit_m3.py`

**Interfaces:**
- `audit_m3.py [paths...] [--json]` emits findings with `rule`, `severity`, `path`, `line`, and `message`.
- Exit 0 means the audit ran successfully; findings are review items, not a build failure by default.

- [ ] Write failing tests for raw component colors, `transition: all`, non-semantic click targets, exclusions, and JSON output.
- [ ] Run targeted tests and confirm failure.
- [ ] Implement minimal standard-library scanner.
- [ ] Run all tests and confirm green.

### Task 4: Add harness adapters and repository documentation

**Files:**
- Create: `.agents/skills/material-design-3/agents/openai.yaml`
- Create: `adapters/codex/AGENTS.md.example`
- Create: `adapters/opencode/AGENTS.md.example`
- Create: `adapters/opencode/opencode.jsonc.example`
- Create: `.agents/skills/material-design-3/evals/README.md`
- Create: `README.md`
- Create: `LICENSE`
- Create: `CHANGELOG.md`

**Interfaces:**
- README documents repo-local and user-global installation for Codex/OpenCode.
- OpenCode example allows `material-design-3` skill loading without duplicating skill content.

- [ ] Extend validation tests for metadata and documentation links.
- [ ] Run tests and confirm missing-artifact failures.
- [ ] Add adapters/documentation/license/changelog.
- [ ] Run tests and validator.

### Task 5: Add CI and perform release verification

**Files:**
- Create: `.github/workflows/verify.yml`

**Interfaces:**
- CI runs Python unit tests, skill validator, and JSON compilation checks on pushes and pull requests.

- [ ] Add workflow after local commands are known-green.
- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Run `.agents/skills/material-design-3/scripts/validate_skill.py`.
- [ ] Run `python -m compileall .agents/skills/material-design-3/scripts tests`.
- [ ] Search tracked files for placeholders and accidental generated artifacts.
- [ ] Review `git diff --check` and repository tree.
