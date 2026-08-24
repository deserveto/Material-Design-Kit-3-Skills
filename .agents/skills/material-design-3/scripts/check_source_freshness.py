#!/usr/bin/env python3
"""Fail when the Material knowledge review date exceeds a configured age.

This intentionally checks review freshness, not live upstream API versions. It is
a maintenance guard that prompts a human/agent to re-check primary sources.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REVIEW_RE = re.compile(r'^\s*material-reviewed:\s*["\']?(\d{4}-\d{2}-\d{2})["\']?\s*$', re.MULTILINE)


def read_review_date(skill_dir: Path) -> date:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError(f"Missing SKILL.md: {skill_file}")
    text = skill_file.read_text(encoding="utf-8")
    match = REVIEW_RE.search(text)
    if not match:
        raise ValueError("SKILL.md metadata must include material-reviewed: YYYY-MM-DD")
    return date.fromisoformat(match.group(1))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check whether Material source research is due for review.")
    parser.add_argument("skill_dir", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--max-age-days", type=int, default=45)
    parser.add_argument("--as-of", help="Override current date for deterministic tests, YYYY-MM-DD.")
    return parser


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv[1:])
    if args.max_age_days < 0:
        print("--max-age-days must be >= 0", file=sys.stderr)
        return 2
    try:
        reviewed = read_review_date(Path(args.skill_dir).resolve())
        today = date.fromisoformat(args.as_of) if args.as_of else date.today()
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    age = (today - reviewed).days
    if age < 0:
        print(f"ERROR: review date {reviewed.isoformat()} is {abs(age)} day(s) in the future", file=sys.stderr)
        return 2
    if age > args.max_age_days:
        print(
            f"STALE: Material sources were last reviewed {age} day(s) ago on {reviewed.isoformat()} "
            f"(limit {args.max_age_days}). Re-check primary sources and update the review date only after verification."
        )
        return 1
    print(
        f"FRESH: Material sources reviewed {age} day(s) ago on {reviewed.isoformat()} "
        f"(limit {args.max_age_days})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
