# Recorded behavioral eval results

Store only **real, provenance-bearing fresh-session runs** in this directory.

A publishable result set should identify case/fixture IDs, harness/version, model/reasoning setting, run date, skill commit SHA, condition, whether the skill loaded, required/forbidden scores, dependency/API claim validity where relevant, reviewer notes, and output artifact reference when available.

## Do not fabricate benchmark data

Examples used by unit tests, documentation snippets, hypothetical tables, or hand-authored demonstration JSON are **not** benchmark results and should not be committed here as measured evidence.

If no real runs have been performed for a release, say so.

## Recommended naming

```text
YYYY-MM-DD-<harness>-<model>-<skill-sha>.json
```

Each file should conform to `../results.schema.json`.

## Summaries

```bash
python ../summarize_results.py ./YYYY-MM-DD-harness-model-sha.json
```

Use `--json` for CI/report ingestion. The summarizer does not execute models and does not certify a harness; it only aggregates recorded evidence.
