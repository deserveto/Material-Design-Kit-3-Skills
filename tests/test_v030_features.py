import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/material-design-3"
REFERENCES = SKILL / "references"
AUDIT = SKILL / "scripts/audit_m3.py"


class V030ReferenceTests(unittest.TestCase):
    def test_component_decision_guides_are_split_by_interaction_family(self):
        expected = {
            "components-actions.md": "destructive",
            "components-navigation.md": "Navigation rail",
            "components-input-selection.md": "checkbox",
            "components-feedback-containment.md": "Snackbar",
        }
        for name, phrase in expected.items():
            path = REFERENCES / name
            self.assertTrue(path.is_file(), name)
            self.assertIn(phrase, path.read_text(encoding="utf-8"), name)

    def test_machine_readable_decision_assets_exist(self):
        prominence = json.loads((SKILL / "assets/component-prominence.json").read_text(encoding="utf-8"))
        self.assertIn("filled", prominence["actions"])
        states = json.loads((SKILL / "assets/interaction-states.json").read_text(encoding="utf-8"))
        self.assertTrue({"focus", "pressed", "selected", "loading", "error"}.issubset(states["states"]))

    def test_new_reference_set_exists_and_is_focused(self):
        expected = {
            "layout-spacing.md": ("available space", "spacing"),
            "interaction-states.md": ("focus", "pressed"),
            "platform-wear.md": ("Wear Compose Material 3", "1.6.2"),
            "migration.md": ("Material 2", "phased"),
            "review-rubric.md": ("BLOCKER", "HIGH"),
        }
        for name, phrases in expected.items():
            path = REFERENCES / name
            self.assertTrue(path.is_file(), name)
            text = path.read_text(encoding="utf-8")
            for phrase in phrases:
                self.assertIn(phrase, text, name)

    def test_skill_routes_new_guides_and_advances_version(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for name in (
            "layout-spacing.md",
            "interaction-states.md",
            "platform-wear.md",
            "migration.md",
            "review-rubric.md",
        ):
            self.assertIn(f"references/{name}", text)
        self.assertIn('version: "0.3.0"', text)
        self.assertIn("M3", text.split("---", 2)[1])

    def test_eval_corpus_covers_new_failure_modes(self):
        ids = {c["id"] for c in json.loads((SKILL / "evals/cases.json").read_text(encoding="utf-8"))}
        expected = {
            "layout-spacing-system",
            "interaction-state-contract",
            "wear-compose-platform-boundary",
            "migration-phased",
            "review-severity",
        }
        self.assertTrue(expected.issubset(ids), expected - ids)

    def test_eval_fixtures_and_result_schema_are_reproducible(self):
        fixtures = json.loads((SKILL / "evals/fixtures.json").read_text(encoding="utf-8"))
        self.assertIn("compose-stable", fixtures["fixtures"])
        self.assertIn("wear-stable", fixtures["fixtures"])
        schema = json.loads((SKILL / "evals/results.schema.json").read_text(encoding="utf-8"))
        required = set(schema["items"]["required"])
        self.assertTrue({"case_id", "harness", "model", "skill_commit", "condition", "required_passed", "required_total", "forbidden_observed"}.issubset(required))

    def test_ci_runs_official_agent_skills_validator(self):
        text = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
        self.assertIn("skills-ref", text)
        self.assertIn("skills-ref validate .agents/skills/material-design-3", text)
        self.assertIn("Python 3.11", text)


class V030AuditTests(unittest.TestCase):
    def run_audit(self, text: str, suffix=".css", *extra: str):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / f"sample{suffix}"
            path.write_text(text, encoding="utf-8")
            cmd = [sys.executable, str(AUDIT), "--json", *extra, str(path)]
            result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
            return result, json.loads(result.stdout) if result.stdout else None

    def test_flags_removed_focus_outline(self):
        result, payload = self.run_audit("button:focus { outline: none; }\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(any(f["rule"] == "m3.a11y.focus-outline-removal" for f in payload["findings"]))

    def test_flags_hardcoded_component_radius(self):
        result, payload = self.run_audit(".card { border-radius: 17px; }\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(any(f["rule"] == "m3.shape.hardcoded-radius" for f in payload["findings"]))

    def test_flags_fixed_pixel_font_size(self):
        result, payload = self.run_audit(".body { font-size: 14px; }\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(any(f["rule"] == "m3.typography.fixed-px-font-size" for f in payload["findings"]))

    def test_strict_mode_fails_when_findings_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.css"
            path.write_text("button:focus { outline: 0; }\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(AUDIT), "--strict", str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
