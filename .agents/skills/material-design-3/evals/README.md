# Behavioral evaluation

`cases.json` is a portable behavioral test corpus for this skill. It is intentionally harness-neutral: the same prompts can be run in Codex, OpenCode, or another Agent Skills-compatible coding agent.

## Why model runs are separate from unit tests

The Python unit tests verify package structure, eval schema, and deterministic scripts. They cannot prove that a language model will follow design judgment under pressure. A release-quality behavior check therefore needs fresh agent sessions.

## RED: establish a baseline without the skill

For each selected case:

1. Start a **fresh** Codex or OpenCode session in a fixture project that matches the prompt.
2. Ensure `material-design-3` is unavailable or disabled.
3. Give only the case `prompt` plus the fixture repository context.
4. Record whether every `required` behavior appears and whether any `forbidden` behavior appears.
5. Keep the output and note the concrete failure/rationalization. Do not edit the skill yet to match a guessed problem.

This is the "without the skill" control.

## GREEN: run the same case with the skill

1. Start another **fresh** session with the same model, fixture, and settings.
2. Make `material-design-3` available through `.agents/skills/material-design-3`.
3. Give the same prompt. Allow normal implicit loading, or explicitly invoke the skill only when testing explicit invocation behavior.
4. Score the same `required` and `forbidden` items.
5. Confirm the result improves because of the skill rather than because the fixture or prompt changed.

This is the "with the skill" run.

## Recommended scoring

For each case, store:

- harness and version;
- model and reasoning/effort setting;
- date;
- skill commit SHA;
- required checks passed / total;
- forbidden behaviors observed / total;
- whether the agent actually loaded the skill;
- concise reviewer notes.

A practical pass criterion is: all required behaviors present, zero forbidden behaviors, and no Material/platform API claims contradicted by the fixture's pinned dependencies.

## Variance

One run is not enough for behavior-shaping guidance. For important release gates, repeat each high-risk case in multiple fresh contexts (3–5 runs is a useful practical minimum; use more when variance is high). Compare the no-skill control against the skill-enabled runs.

## High-risk cases to run first

Prioritize:

- `existing-non-material-system` — prevents unwanted design-system takeover;
- `compose-stability` — prevents silent alpha/experimental adoption;
- `expressive-restraint` — catches "AI Material slop";
- `adaptive-list-detail` — tests layout reasoning rather than styling;
- `visual-verification` — tests whether the agent proves its UI work.

## Current repository verification boundary

This repository's CI validates the deterministic parts of the package. It does **not** claim that Codex or OpenCode behavior has been exhaustively certified. Record real-model results before promoting a future version as behaviorally benchmarked.
