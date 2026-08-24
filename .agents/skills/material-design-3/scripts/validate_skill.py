#!/usr/bin/env python3
"""Validate a local Agent Skills package using only the Python standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["SKILL.md must begin with YAML frontmatter"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text, ["SKILL.md frontmatter is not closed"]
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    current_parent: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  ") and current_parent:
            continue
        if ":" not in line:
            errors.append(f"Invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value
        current_parent = key if not value else None
    return data, body, errors


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"Missing SKILL.md: {skill_file}"]

    text = skill_file.read_text(encoding="utf-8")
    meta, _body, frontmatter_errors = parse_frontmatter(text)
    errors.extend(frontmatter_errors)

    name = meta.get("name", "")
    description = meta.get("description", "")
    if not name:
        errors.append("Missing required name field")
    elif len(name) > 64:
        errors.append("Invalid name: must be at most 64 characters")
    elif not NAME_RE.fullmatch(name):
        errors.append("Invalid name: use lowercase letters, numbers, and single hyphens only")
    elif name != skill_dir.name:
        errors.append(f"Skill name {name!r} must match directory name {skill_dir.name!r}")

    if not description:
        errors.append("Missing required description field")
    elif len(description) > 1024:
        errors.append("Description exceeds 1024 characters")

    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds the recommended 500-line progressive-disclosure limit")

    for target in LINK_RE.findall(text):
        target = target.split("#", 1)[0]
        if not target or "://" in target or target.startswith("#"):
            continue
        path = (skill_dir / target).resolve()
        try:
            path.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"Referenced file escapes skill directory: {target}")
            continue
        if not path.exists():
            errors.append(f"Missing referenced file: {target}")

    return errors


def main(argv: list[str]) -> int:
    skill_dir = Path(argv[1] if len(argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
    errors = validate(skill_dir)
    if errors:
        print(f"FAIL {skill_dir}")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
