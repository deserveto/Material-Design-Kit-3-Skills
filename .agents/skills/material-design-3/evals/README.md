# Behavioral evaluation

`cases.json` is a portable behavioral test corpus for this skill. It is intentionally harness-neutral: the same prompts can be run in Codex, OpenCode, or another Agent Skills-compatible coding agent.

`fixtures.json` defines the repository/dependency state that should accompany repeatable cases, and `results.schema.json` defines a stable result record so runs can be compared across harnesses, models, dates, and skill commits.

## Why model runs are separate from unit tests

The Python unit tests verify package structure, eval schema, and deterministic scripts. They cannot prove that a language model will follow design judgment under pressure. A release-quality behavior check therefore needs fresh agent sessions.

## Choose the fixture first

Before running a case, select the fixture listed for that case in `fixtures.json` and reproduce its relevant constraints. The fixture contract matters as much as the prompt: a stable-only Compose case is meaningless if the test repository silently allows alpha dependencies.

Keep fixture state identical between control and skill-enabled runs.

## RED: establish a baseline without the skill

For each selected case:

1. Start a **fresh** Codex or OpenCode session in the matching fixture project.
2. Ensure `material-design-3` is unavailable or disabled.
3. Give only the case `prompt` plus the fixture repository context.
4. Record whether every `required` behavior appears and whether any `forbidden` behavior appears.
5. Keep the output and note the concrete failure/rationalization. Do not edit the skill yet to match a guessed problem.

This is the `without-skill` control.

## GREEN: run the same case with the skill

1. Start another **fresh** session with the same model, fixture, and settings.
2. Make `material-design-3` available through `.agents/skills/material-design-3`.
3. Give the same prompt. Allow normal implicit loading, or explicitly invoke the skill only when testing explicit invocation behavior.
4. Score the same `required` and `forbidden` items.
5. Confirm the result improves because of the skill rather than because the fixture or prompt changed.

This is the `with-skill` run.

## Reproducible result record

Store runs as a JSON array conforming to `results.schema.json`. At minimum each record captures:

- case and fixture IDs;
- harness/version;
- model and reasoning/effort setting;
- date;
- skill commit SHA;
- `without-skill` or `with-skill` condition;
- whether the agent actually loaded the skill;
- required checks passed / total;
- forbidden behaviors observed / total;
- reviewer notes.

For version-sensitive cases, also record whether dependency/API claims were valid for the fixture.

A practical case pass criterion is: all required behaviors present, zero forbidden behaviors, and no Material/platform API claims contradicted by the fixture's pinned dependencies.

## Variance

One run is not enough for behavior-shaping guidance. For important release gates, repeat each high-risk case in multiple fresh contexts (3–5 runs is a useful practical minimum; use more when variance is high). Compare the no-skill control against the skill-enabled runs using identical fixtures and settings.

Do not average away catastrophic failures. Report the count of runs with any BLOCKER-like behavior separately from aggregate pass rates.

## High-risk cases to run first

Prioritize:

- `existing-non-material-system` — prevents unwanted design-system takeover;
- `compose-stability` — prevents silent alpha/experimental adoption;
- `wear-compose-platform-boundary` — prevents mobile/Wear API confusion;
- `expressive-restraint` — catches "AI Material slop";
- `adaptive-list-detail` and `layout-spacing-system` — test layout reasoning rather than styling;
- `interaction-state-contract` — tests focus/loading/error behavior;
- `visual-verification` — tests whether the agent proves its UI work;
- `review-severity` — tests whether review findings are evidence-based rather than aesthetic opinion.

## Current repository verification boundary

This repository's CI validates the deterministic parts of the package and the Agent Skills format. It does **not** claim that Codex, OpenCode, or another model/harness has been exhaustively certified. Record real-model results before promoting a release as behaviorally benchmarked.
