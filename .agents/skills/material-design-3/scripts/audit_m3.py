#!/usr/bin/env python3
"""Conservative heuristic review for common Material 3 web UI mistakes.

This scanner is intentionally dependency-free. It identifies review candidates;
it does not certify Material Design, WCAG, or accessibility conformance.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable

SUPPORTED_EXTENSIONS = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}
EXCLUDED_DIRS = {".git", ".next", ".nuxt", ".svelte-kit", "build", "coverage", "dist", "node_modules", "out", "vendor"}
RAW_COLOR_RE = re.compile(r"(?:#[0-9a-fA-F]{3,8}\b|\brgba?\([^\n)]*\)|\bhsla?\([^\n)]*\))")
TOKEN_DECLARATION_RE = re.compile(r"--[A-Za-z0-9_-]+\s*:")
TRANSITION_ALL_RE = re.compile(r"\btransition\s*:\s*all\b", re.IGNORECASE)
GENERIC_CLICK_RE = re.compile(r"<(?:div|span)\b[^>]*\bonClick\s*=", re.IGNORECASE)
FOCUS_OUTLINE_REMOVAL_RE = re.compile(r"\boutline\s*:\s*(?:none|0)(?:\s*!important)?\s*;?", re.IGNORECASE)
HARDCODED_RADIUS_RE = re.compile(r"\bborder(?:-(?:top|bottom)-(?:left|right))?-radius\s*:\s*\d+(?:\.\d+)?px\b", re.IGNORECASE)
FIXED_PX_FONT_SIZE_RE = re.compile(r"\bfont-size\s*:\s*\d+(?:\.\d+)?px\b", re.IGNORECASE)
TEXT_SIZE_ADJUST_DISABLED_RE = re.compile(r"\b(?:-webkit-)?text-size-adjust\s*:\s*none\b", re.IGNORECASE)


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
    return {"rule": rule, "severity": severity, "path": path.as_posix(), "line": line, "message": message}


def viewport_zoom_disabled(line: str) -> bool:
    lowered = re.sub(r"\s+", "", line.lower())
    if "<meta" not in lowered or "viewport" not in lowered:
        return False
    return "user-scalable=no" in lowered or bool(re.search(r"maximum-scale=(?:1(?:\.0+)?)['\";,>]", lowered))


def audit_file(path: Path) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return findings

    for number, line in enumerate(text.splitlines(), start=1):
        if RAW_COLOR_RE.search(line) and not TOKEN_DECLARATION_RE.search(line):
            findings.append(finding("m3.color.raw-component-color", "review", path, number, "Raw color value in UI source. Prefer an existing semantic theme token unless this is intentionally a token/source definition."))
        if TRANSITION_ALL_RE.search(line):
            findings.append(finding("m3.motion.transition-all", "review", path, number, "`transition: all` obscures motion intent. Prefer explicit properties and project/Material motion tokens."))
        if GENERIC_CLICK_RE.search(line):
            findings.append(finding("m3.a11y.generic-click-target", "warning", path, number, "Generic div/span click target detected. Prefer a semantic interactive element or implement the complete keyboard/focus/accessibility contract."))
        if FOCUS_OUTLINE_REMOVAL_RE.search(line):
            findings.append(finding("m3.a11y.focus-outline-removal", "warning", path, number, "Focus outline removal detected. Only remove a browser focus indicator when an equal or better visible focus treatment is implemented and verified."))
        if HARDCODED_RADIUS_RE.search(line):
            findings.append(finding("m3.shape.hardcoded-radius", "review", path, number, "Hard-coded pixel radius detected. Prefer an existing semantic shape token or component default unless this is an intentional local exception."))
        if FIXED_PX_FONT_SIZE_RE.search(line):
            findings.append(finding("m3.typography.fixed-px-font-size", "review", path, number, "Fixed pixel font size detected. Review whether this bypasses the project's semantic typography scale or interferes with scaling/reflow; a px value alone is not an accessibility failure."))
        if TEXT_SIZE_ADJUST_DISABLED_RE.search(line):
            findings.append(finding("m3.a11y.text-size-adjust-disabled", "warning", path, number, "`text-size-adjust: none` can prevent user-agent text scaling. Remove it unless a verified accessibility-compatible reason exists."))
        if viewport_zoom_disabled(line):
            findings.append(finding("m3.a11y.viewport-zoom-disabled", "warning", path, number, "Viewport metadata appears to restrict user zoom. Do not disable pinch/browser zoom for responsive Material web interfaces."))
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
    parser = argparse.ArgumentParser(description="Heuristically review web UI source for common Material 3 implementation mistakes.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--strict", action="store_true", help="Return exit code 1 when any heuristic finding is detected. Off by default because findings are review candidates.")
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
    rule_counts = dict(sorted(Counter(item["rule"] for item in findings).items()))
    disclaimer = "Heuristic review only; this is not certification for Material Design, WCAG, or accessibility."
    if args.json:
        print(json.dumps({"tool": "audit_m3", "heuristic": True, "strict": args.strict, "disclaimer": disclaimer, "rule_counts": rule_counts, "findings": findings}, indent=2))
    else:
        print(disclaimer)
        if not findings:
            print("No review findings detected by the bundled rules.")
        else:
            for item in findings:
                print(f"{str(item['severity']).upper():7} {item['rule']} {item['path']}:{item['line']} - {item['message']}")
            print(f"{len(findings)} finding(s).")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
