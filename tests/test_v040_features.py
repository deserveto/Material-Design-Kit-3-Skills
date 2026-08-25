import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/material-design-3"
REFERENCES = SKILL / "references"
ASSETS = SKILL / "assets"
SCRIPTS = SKILL / "scripts"
EVALS = SKILL / "evals"


class V040PackageContractTests(unittest.TestCase):
    def test_skill_routes_v040_references_and_version(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn('version: "0.4.0"', text)
        for name in (
            "design-intent.md",
            "design-tokens.md",
            "color-system.md",
            "platform-android-views.md",
            "accessibility-web.md",
            "components-advanced.md",
        ):
            self.assertTrue((REFERENCES / name).is_file(), name)
            self.assertIn(f"references/{name}", text, name)
        self.assertIn("assets/platform-capabilities.json", text)
        self.assertIn("assets/source-snapshots.json", text)

    def test_platform_capabilities_snapshot_is_machine_readable(self):
        path = ASSETS / "platform-capabilities.json"
        self.assertTrue(path.is_file())
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(payload["reviewed"], "2026-08-25")
        self.assertEqual(payload["platforms"]["compose-material3"]["stable"], "1.4.0")
        self.assertEqual(payload["platforms"]["wear-compose-material3"]["stable"], "1.6.2")
        self.assertEqual(payload["platforms"]["material-web"]["library_status"], "maintenance")
        self.assertEqual(payload["platforms"]["android-views-mdc"]["library_status"], "maintenance")
        self.assertIn("search", payload["components"])
        self.assertIn("expressive-shapes", payload["components"])

    def test_source_snapshots_have_granular_review_dates(self):
        path = ASSETS / "source-snapshots.json"
        self.assertTrue(path.is_file())
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["schema_version"], 1)
        self.assertGreaterEqual(len(payload["sources"]), 8)
        ids = {item["id"] for item in payload["sources"]}
        self.assertIn("compose-material3-releases", ids)
        self.assertIn("material-web-status", ids)
        self.assertIn("dtcg-2025-10", ids)
        for item in payload["sources"]:
            self.assertRegex(item["reviewed"], r"^\d{4}-\d{2}-\d{2}$")
            self.assertTrue(item["url"].startswith("https://"))


class V040AuditContractTests(unittest.TestCase):
    def run_static_audit(self, text: str, suffix: str):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / f"sample{suffix}"
            path.write_text(text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "audit_m3.py"), "--json", str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)

    def test_static_audit_flags_viewport_zoom_lock_and_returns_rule_counts(self):
        payload = self.run_static_audit(
            '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">\n',
            ".html",
        )
        self.assertTrue(any(f["rule"] == "m3.a11y.viewport-zoom-disabled" for f in payload["findings"]))
        self.assertGreaterEqual(payload["rule_counts"]["m3.a11y.viewport-zoom-disabled"], 1)

    def test_static_audit_flags_disabled_text_size_adjust(self):
        payload = self.run_static_audit("html { text-size-adjust: none; }\n", ".css")
        self.assertTrue(any(f["rule"] == "m3.a11y.text-size-adjust-disabled" for f in payload["findings"]))

    @unittest.skipUnless(shutil.which("node"), "Node.js is not installed")
    def test_runtime_audit_help_does_not_require_optional_dependencies(self):
        script = SCRIPTS / "audit_runtime.mjs"
        self.assertTrue(script.is_file())
        result = subprocess.run(["node", str(script), "--help"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        output = result.stdout + result.stderr
        for flag in ("--base-url", "--paths", "--json", "--strict"):
            self.assertIn(flag, output)


class V040FreshnessContractTests(unittest.TestCase):
    def test_freshness_json_identifies_stale_source_ids(self):
        script = SCRIPTS / "check_source_freshness.py"
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp) / "skill"
            (skill_dir / "assets").mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                '---\nname: x\ndescription: x\nmaterial-reviewed: "2026-08-20"\n---\n',
                encoding="utf-8",
            )
            (skill_dir / "assets/source-snapshots.json").write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "sources": [
                            {"id": "fresh", "kind": "docs", "url": "https://example.com/fresh", "reviewed": "2026-08-20"},
                            {"id": "stale", "kind": "docs", "url": "https://example.com/stale", "reviewed": "2026-06-01"},
                        ],
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    str(skill_dir),
                    "--max-age-days",
                    "45",
                    "--as-of",
                    "2026-08-25",
                    "--json",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["stale_source_ids"], ["stale"])
            self.assertEqual(payload["package_reviewed"], "2026-08-20")


class V040EvalContractTests(unittest.TestCase):
    def test_result_summarizer_reports_control_and_skill_rates(self):
        script = EVALS / "summarize_results.py"
        self.assertTrue(script.is_file())
        records = [
            {
                "case_id": "a",
                "fixture_id": "web",
                "harness": "demo",
                "model": "model-x",
                "skill_commit": "abc",
                "condition": "without-skill",
                "required_passed": 1,
                "required_total": 2,
                "forbidden_observed": 1,
                "forbidden_total": 2,
            },
            {
                "case_id": "a",
                "fixture_id": "web",
                "harness": "demo",
                "model": "model-x",
                "skill_commit": "abc",
                "condition": "with-skill",
                "required_passed": 2,
                "required_total": 2,
                "forbidden_observed": 0,
                "forbidden_total": 2,
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.json"
            path.write_text(json.dumps(records), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(script), str(path), "--json"],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = json.loads(result.stdout)
            groups = {item["condition"]: item for item in payload["groups"]}
            self.assertEqual(groups["without-skill"]["required_pass_rate"], 0.5)
            self.assertEqual(groups["without-skill"]["forbidden_observation_rate"], 0.5)
            self.assertEqual(groups["with-skill"]["required_pass_rate"], 1.0)
            self.assertEqual(groups["with-skill"]["forbidden_observation_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
