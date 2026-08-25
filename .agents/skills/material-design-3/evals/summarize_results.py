#!/usr/bin/env python3
"""Summarize recorded Material 3 behavioral eval results without inventing runs."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

REQUIRED_FIELDS = {"case_id", "harness", "model", "skill_commit", "condition", "required_passed", "required_total", "forbidden_observed", "forbidden_total"}
VALID_CONDITIONS = {"without-skill", "with-skill"}


def validate_record(record: object, index: int) -> dict[str, object]:
    if not isinstance(record, dict):
        raise ValueError(f"record #{index + 1} must be an object")
    missing = sorted(REQUIRED_FIELDS - set(record))
    if missing:
        raise ValueError(f"record #{index + 1} missing required field(s): {', '.join(missing)}")
    if record["condition"] not in VALID_CONDITIONS:
        raise ValueError(f"record #{index + 1} has invalid condition: {record['condition']!r}")
    for key in ("required_passed", "required_total", "forbidden_observed", "forbidden_total"):
        if not isinstance(record[key], int) or record[key] < 0:
            raise ValueError(f"record #{index + 1} field {key} must be a non-negative integer")
    if record["required_passed"] > record["required_total"]:
        raise ValueError(f"record #{index + 1} required_passed exceeds required_total")
    if record["forbidden_observed"] > record["forbidden_total"]:
        raise ValueError(f"record #{index + 1} forbidden_observed exceeds forbidden_total")
    for key in ("case_id", "harness", "model", "skill_commit"):
        if not isinstance(record[key], str) or not record[key]:
            raise ValueError(f"record #{index + 1} field {key} must be a non-empty string")
    return record


def aggregate(records: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str], dict[str, int]] = defaultdict(lambda: {"runs": 0, "required_passed": 0, "required_total": 0, "forbidden_observed": 0, "forbidden_total": 0, "catastrophic_failures": 0})
    for record in records:
        key = (str(record["harness"]), str(record["model"]), str(record["condition"]))
        bucket = groups[key]
        bucket["runs"] += 1
        bucket["required_passed"] += int(record["required_passed"])
        bucket["required_total"] += int(record["required_total"])
        bucket["forbidden_observed"] += int(record["forbidden_observed"])
        bucket["forbidden_total"] += int(record["forbidden_total"])
        if record.get("catastrophic_failure") is True:
            bucket["catastrophic_failures"] += 1
    output = []
    for (harness, model, condition), bucket in sorted(groups.items()):
        rt, ft = bucket["required_total"], bucket["forbidden_total"]
        output.append({"harness": harness, "model": model, "condition": condition, "runs": bucket["runs"], "required_passed": bucket["required_passed"], "required_total": rt, "required_pass_rate": round(bucket["required_passed"] / rt, 6) if rt else 0.0, "forbidden_observed": bucket["forbidden_observed"], "forbidden_total": ft, "forbidden_observation_rate": round(bucket["forbidden_observed"] / ft, 6) if ft else 0.0, "catastrophic_failures": bucket["catastrophic_failures"]})
    return output


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Summarize recorded Material 3 behavioral eval results.")
    parser.add_argument("results", help="Path to a JSON array of result records.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args(argv[1:])
    try:
        payload = json.loads(Path(args.results).read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            raise ValueError("results file must contain a JSON array")
        records = [validate_record(record, index) for index, record in enumerate(payload)]
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    groups = aggregate(records)
    result = {"tool": "summarize_results", "provenance_warning": "Aggregation only. These numbers are benchmark claims only when every input record came from a documented fresh-session run.", "records": len(records), "groups": groups}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result["provenance_warning"])
        if not groups:
            print("No result records.")
        for group in groups:
            print(f"{group['harness']} | {group['model']} | {group['condition']}: {group['runs']} run(s), required {group['required_pass_rate']:.1%}, forbidden {group['forbidden_observation_rate']:.1%}, catastrophic {group['catastrophic_failures']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
