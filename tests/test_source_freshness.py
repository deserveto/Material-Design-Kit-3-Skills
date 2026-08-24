import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/material-design-3/scripts/check_source_freshness.py"
SKILL = ROOT / ".agents/skills/material-design-3"


class SourceFreshnessTests(unittest.TestCase):
    def run_check(self, skill: Path, *args: str):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(skill), "--as-of", "2026-08-24", *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

    def test_current_repo_review_date_is_fresh(self):
        result = self.run_check(SKILL, "--max-age-days", "45")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("fresh", result.stdout.lower())

    def test_stale_review_date_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "sample"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                '---\nname: sample\ndescription: test\nmetadata:\n  material-reviewed: "2026-01-01"\n---\n# Sample\n',
                encoding="utf-8",
            )
            result = self.run_check(skill, "--max-age-days", "45")
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("stale", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
