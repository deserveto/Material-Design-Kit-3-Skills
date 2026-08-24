import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/material-design-3/scripts/validate_skill.py"
SKILL = ROOT / ".agents/skills/material-design-3"


class ValidateSkillTests(unittest.TestCase):
    def run_validator(self, skill_dir: Path):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(skill_dir)],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

    def test_repository_skill_validates(self):
        result = self.run_validator(SKILL)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_invalid_name_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "Bad_Skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: Bad_Skill\ndescription: Use when testing.\n---\n# Bad\n",
                encoding="utf-8",
            )
            result = self.run_validator(skill)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("name", result.stdout.lower())

    def test_name_longer_than_64_characters_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            name = "a" * 65
            skill = Path(tmp) / name
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: Use when testing.\n---\n# Too long\n",
                encoding="utf-8",
            )
            result = self.run_validator(skill)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("64", result.stdout)

    def test_missing_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "sample-skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: sample-skill\ndescription: Use when testing.\n---\n"
                "# Sample\nRead [missing](references/missing.md).\n",
                encoding="utf-8",
            )
            result = self.run_validator(skill)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing referenced file", result.stdout.lower())

    def test_eval_cases_are_json(self):
        cases = SKILL / "evals/cases.json"
        data = json.loads(cases.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(data), 12)

    def test_canonical_reference_set_exists(self):
        required = {
            "foundations.md",
            "components.md",
            "adaptive-accessibility.md",
            "expressive.md",
            "platform-web.md",
            "platform-compose.md",
            "platform-flutter.md",
            "sources.md",
        }
        actual = {p.name for p in (SKILL / "references").glob("*.md")}
        self.assertTrue(required.issubset(actual), required - actual)

    def test_skill_routes_to_references_and_has_verification_contract(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for heading in ("## Workflow", "## Reference routing", "## Verification", "## Common mistakes"):
            self.assertIn(heading, text)
        for name in (
            "foundations.md",
            "components.md",
            "adaptive-accessibility.md",
            "expressive.md",
            "platform-web.md",
            "platform-compose.md",
            "platform-flutter.md",
        ):
            self.assertIn(f"references/{name}", text)

    def test_platform_references_state_review_date(self):
        for name in ("platform-compose.md", "platform-flutter.md", "sources.md"):
            text = (SKILL / "references" / name).read_text(encoding="utf-8")
            self.assertIn("2026-08-24", text, name)


if __name__ == "__main__":
    unittest.main()
