import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/material-design-3/scripts/audit_m3.py"


class AuditM3Tests(unittest.TestCase):
    def run_audit(self, *paths: Path, json_mode=False):
        cmd = [sys.executable, str(SCRIPT)]
        if json_mode:
            cmd.append("--json")
        cmd.extend(str(path) for path in paths)
        return subprocess.run(cmd, text=True, capture_output=True, cwd=ROOT)

    def test_flags_raw_component_color_but_not_token_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            component = root / "Button.css"
            component.write_text(
                ":root { --md-sys-color-primary: #6750A4; }\n"
                ".button { background: #6750A4; color: var(--md-sys-color-on-primary); }\n",
                encoding="utf-8",
            )
            result = self.run_audit(component, json_mode=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            findings = json.loads(result.stdout)["findings"]
            color_findings = [f for f in findings if f["rule"] == "m3.color.raw-component-color"]
            self.assertEqual(len(color_findings), 1)
            self.assertEqual(color_findings[0]["line"], 2)

    def test_flags_transition_all(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "motion.css"
            path.write_text(".x { transition: all 200ms ease; }\n", encoding="utf-8")
            findings = json.loads(self.run_audit(path, json_mode=True).stdout)["findings"]
            self.assertTrue(any(f["rule"] == "m3.motion.transition-all" for f in findings))

    def test_flags_generic_react_click_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "Widget.tsx"
            path.write_text('<div onClick={save}>Save</div>\n', encoding="utf-8")
            findings = json.loads(self.run_audit(path, json_mode=True).stdout)["findings"]
            self.assertTrue(any(f["rule"] == "m3.a11y.generic-click-target" for f in findings))

    def test_json_identifies_audit_as_heuristic(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "clean.css"
            path.write_text(".x { color: var(--md-sys-color-on-surface); }\n", encoding="utf-8")
            payload = json.loads(self.run_audit(path, json_mode=True).stdout)
            self.assertTrue(payload["heuristic"])
            self.assertIn("not compliance certification", payload["disclaimer"].lower())

    def test_directory_scan_ignores_dependency_and_build_dirs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "src").mkdir()
            (root / "node_modules").mkdir()
            (root / "dist").mkdir()
            (root / "src/App.tsx").write_text("const x = '#112233';\n", encoding="utf-8")
            (root / "node_modules/lib.css").write_text(".x{color:#fff}\n", encoding="utf-8")
            (root / "dist/app.css").write_text(".x{color:#000}\n", encoding="utf-8")
            findings = json.loads(self.run_audit(root, json_mode=True).stdout)["findings"]
            paths = {f["path"] for f in findings}
            self.assertTrue(any("src/App.tsx" in path for path in paths))
            self.assertFalse(any("node_modules" in path or "/dist/" in path for path in paths))


if __name__ == "__main__":
    unittest.main()
