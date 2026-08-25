# Behavioral evaluation

`cases.json` is a portable behavioral test corpus for this skill. It is intentionally harness-neutral: the same prompts can be run in Codex, OpenCode, or another Agent Skills-compatible coding agent.

`fixtures.json` defines repository/dependency state and `results.schema.json` defines stable result records.

## Why model runs are separate from unit tests

Unit tests verify package structure, deterministic scripts, and schemas. They cannot prove that a language model will follow design judgment under pressure. Release-quality behavior checking therefore needs **fresh** agent sessions.

## Without the skill

1. Start a fresh Codex, OpenCode, or comparable session in the matching fixture.
2. Ensure `material-design-3` is unavailable or disabled.
3. Give only the case prompt plus fixture context.
4. Score required and forbidden behavior and record the result.

## With the skill

1. Start another fresh session with the same model, fixture, settings, and prompt.
2. Make `material-design-3` available and record whether it actually loaded.
3. Score the same behavior without changing fixture or prompt.

A practical pass is all required behavior, zero forbidden behavior, and no dependency/API claim contradicted by the pinned fixture.

## Variance

For important release gates, repeat high-risk cases in multiple fresh sessions (3–5 runs is a useful practical minimum; use more when variance is high). Do not average away severe failures.

## Result files and provenance

Real result files belong under `evals/results/`; read `results/README.md` before publishing them. Templates, test fixtures, hypothetical tables, or synthetic records are **not** benchmark evidence.

If no real model/harness runs have been performed for a release, state that instead of inventing a matrix.

## Summarizing recorded results

```bash
python evals/summarize_results.py path/to/results.json
python evals/summarize_results.py path/to/results.json --json
```

The summarizer groups by harness, model, and `without-skill` / `with-skill` condition. It aggregates input only; it never invents runs.

## High-risk cases

Prioritize `existing-non-material-system`, `compose-stability`, `wear-compose-platform-boundary`, `expressive-restraint`, `adaptive-list-detail`, `layout-spacing-system`, `interaction-state-contract`, `visual-verification`, and `review-severity`.

## Current verification boundary

CI validates deterministic package behavior and the Agent Skills format. It does **not** certify Codex, OpenCode, or any model/harness as behaviorally compliant. Publish real-model results separately with provenance.
