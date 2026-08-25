#!/usr/bin/env python3
"""Check package-level and granular Material source review freshness.

This is a deterministic maintenance guard. It does not scrape upstream pages by
default; it tells maintainers exactly which source families are due for review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

REVIEW_RE = re.compile(r'^\s*material-reviewed:\s*["\']?(\d{4}-\d{2}-\d{2})["\']?\s*$', re.MULTILINE)


def read_review_date(skill_dir: Path) -> date:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError(f"Missing SKILL.md: {skill_file}")
    match = REVIEW_RE.search(skill_file.read_text(encoding="utf-8"))
    if not match:
        raise ValueError("SKILL.md metadata must include material-reviewed: YYYY-MM-DD")
    return date.fromisoformat(match.group(1))


def read_source_snapshots(skill_dir: Path) -> list[dict[str, object]]:
    path = skill_dir / "assets" / "source-snapshots.json"
    if not path.is_file():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError("source-snapshots.json schema_version must be 1")
    sources = payload.get("sources")
    if not isinstance(sources, list):
        raise ValueError("source-snapshots.json must contain a sources array")
    seen: set[str] = set()
    normalized: list[dict[str, object]] = []
    for index, item in enumerate(sources):
        if not isinstance(item, dict):
            raise ValueError(f"source snapshot #{index + 1} must be an object")
        source_id, reviewed, url = item.get("id"), item.get("reviewed"), item.get("url")
        if not isinstance(source_id, str) or not source_id:
            raise ValueError(f"source snapshot #{index + 1} has invalid id")
        if source_id in seen:
            raise ValueError(f"duplicate source snapshot id: {source_id}")
        seen.add(source_id)
        if not isinstance(reviewed, str):
            raise ValueError(f"source {source_id} has invalid reviewed date")
        reviewed_date = date.fromisoformat(reviewed)
        if not isinstance(url, str) or not url.startswith("https://"):
            raise ValueError(f"source {source_id} must have an https URL")
        normalized.append({**item, "_reviewed_date": reviewed_date})
    return normalized


def age_days(reviewed: date, today: date, label: str) -> int:
    age = (today - reviewed).days
    if age < 0:
        raise ValueError(f"{label} review date {reviewed.isoformat()} is {abs(age)} day(s) in the future")
    return age


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check whether Material source research is due for review.")
    parser.add_argument("skill_dir", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--max-age-days", type=int, default=45)
    parser.add_argument("--as-of", help="Override current date for deterministic tests, YYYY-MM-DD.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable freshness information.")
    return parser


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv[1:])
    if args.max_age_days < 0:
        print("--max-age-days must be >= 0", file=sys.stderr)
        return 2
    skill_dir = Path(args.skill_dir).resolve()
    try:
        package_reviewed = read_review_date(skill_dir)
        today = date.fromisoformat(args.as_of) if args.as_of else date.today()
        package_age = age_days(package_reviewed, today, "package")
        sources = read_source_snapshots(skill_dir)
        source_rows = []
        for source in sources:
            reviewed_date = source["_reviewed_date"]
            assert isinstance(reviewed_date, date)
            age = age_days(reviewed_date, today, f"source {source['id']}")
            source_rows.append({"id": source["id"], "kind": source.get("kind"), "url": source["url"], "reviewed": reviewed_date.isoformat(), "age_days": age, "stale": age > args.max_age_days})
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        if args.json:
            print(json.dumps({"error": str(exc)}, indent=2))
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    stale_source_ids = sorted(row["id"] for row in source_rows if row["stale"])
    package_stale = package_age > args.max_age_days
    stale = package_stale or bool(stale_source_ids)
    if args.json:
        print(json.dumps({"tool": "check_source_freshness", "as_of": today.isoformat(), "max_age_days": args.max_age_days, "package_reviewed": package_reviewed.isoformat(), "package_age_days": package_age, "package_stale": package_stale, "stale_source_ids": stale_source_ids, "sources": source_rows}, indent=2))
    elif stale:
        if package_stale:
            print(f"STALE: package research was reviewed {package_age} day(s) ago on {package_reviewed.isoformat()} (limit {args.max_age_days}).")
        if stale_source_ids:
            print("STALE source families: " + ", ".join(stale_source_ids))
        print("Re-check the named primary sources and update review dates only after verification.")
    else:
        suffix = f"; {len(source_rows)} granular source snapshot(s) also fresh" if source_rows else ""
        print(f"FRESH: Material sources reviewed {package_age} day(s) ago on {package_reviewed.isoformat()} (limit {args.max_age_days}){suffix}.")
    return 1 if stale else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
