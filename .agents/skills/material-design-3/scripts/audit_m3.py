#!/usr/bin/env python3
"""Conservative heuristic review for common Material 3 web UI mistakes.

This scanner is intentionally small and dependency-free. It identifies review
candidates; it does not certify Material Design or accessibility conformance.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

SUPPORTED_EXTENSIONS = {
    ".css",
    ".scss",
    ".sass",
    ".less",
    ".html",
    ".htm",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".vue",
    ".svelte",
}

EXCLUDED_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".svelte-kit",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "vendor",
}

RAW_COLOR_RE = re.compile(
    r"(?:#[0-9a-fA-F]{3,8}\b|\brgba?\([^\n)]*\)|\bhsla?\([^\n)]*\))"
)
TOKEN_DECLARATION_RE = re.compile(r"--[A-Za-z0-9_-]+\s*:")
TRANSITION_ALL_RE = re.compile(r"\btransition\s*:\s*all\b", re.IGNORECASE)
GENERIC_CLICK_RE = re.compile(r"<(?:div|span)\b[^>]*\bonClick\s*=", re.IGNORECASE)


def iter_source_files(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.is_file():
            if path.suffix.lower() in SUPPORTED_EXTENSIONS:
                yield path
            continue
        if not path.is_dir():
            continue
        for candidate in path.rglob("*"):
            if not candidate.is_file() or candidate.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue
            if any(part in EXCLUDED_DIRS for part in candidate.parts):
                continue
            yield candidate


def finding(rule: str, severity: str, path: Path, line: int, message: str) -> dict[str, object]:
    return {
        "rule": rule,
        "severity": severity,
        "path": path.as_posix(),
        "line": line,
        "message": message,
    }


def audit_file(path: Path) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return findings

    for number, line in enumerate(text.splitlines(), start=1):
        # Theme/token declaration lines are legitimate places for raw values.
        # This conservative exemption intentionally favors fewer false positives.
        if RAW_COLOR_RE.search(line) and not TOKEN_DECLARATION_RE.search(line):
            findings.append(
                finding(
                    "m3.color.raw-component-color",
                    "review",
                    path,
                    number,
                    "Raw color value in UI source. Prefer an existing semantic theme token unless this is intentionally a token/source definition.",
                )
            )

        if TRANSITION_ALL_RE.search(line):
            findings.append(
                finding(
                    "m3.motion.transition-all",
                    "review",
                    path,
                    number,
                    "`transition: all` obscures motion intent. Prefer explicit properties and project/Material motion tokens.",
                )
            )

        if GENERIC_CLICK_RE.search(line):
            findings.append(
                finding(
                    "m3.a11y.generic-click-target",
                    "warning",
                    path,
                    number,
                    "Generic div/span click target detected. Prefer a semantic interactive element or implement the complete keyboard/focus/accessibility contract.",
                )
            )

    return findings


def audit(paths: Iterable[Path]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    seen: set[Path] = set()
    for path in iter_source_files(paths):
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        results.extend(audit_file(path))
    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Heuristically review web UI source for a few common Material 3 implementation mistakes."
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to scan.")
    return parser


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv[1:])
    paths = [Path(value) for value in args.paths]
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        print("Missing path(s): " + ", ".join(missing), file=sys.stderr)
        return 2

    findings = audit(paths)
    disclaimer = "Heuristic review only; this is not compliance certification for Material Design or accessibility."

    if args.json:
        print(
            json.dumps(
                {
                    "tool": "audit_m3",
                    "heuristic": True,
                    "disclaimer": disclaimer,
                    "findings": findings,
                },
                indent=2,
            )
        )
    else:
        print(disclaimer)
        if not findings:
            print("No review findings detected by the bundled rules.")
        else:
            for item in findings:
                print(
                    f"{item['severity'].upper():7} {item['rule']} "
                    f"{item['path']}:{item['line']} - {item['message']}"
                )
            print(f"{len(findings)} finding(s).")

    # Findings do not fail the build by default. The tool is a review aid.
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
