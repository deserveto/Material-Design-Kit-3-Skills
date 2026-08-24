import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/material-design-3"


class RepositoryDocsTests(unittest.TestCase):
    def test_codex_metadata_exists_and_is_scoped(self):
        text = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Material Design 3"', text)
        self.assertIn("allow_implicit_invocation: true", text)
        self.assertNotIn("dependencies:", text)

    def test_harness_adapters_exist_without_copying_skill_body(self):
        codex = (ROOT / "adapters/codex/AGENTS.md.example").read_text(encoding="utf-8")
        opencode = (ROOT / "adapters/opencode/AGENTS.md.example").read_text(encoding="utf-8")
        config = (ROOT / "adapters/opencode/opencode.jsonc.example").read_text(encoding="utf-8")
        self.assertIn("material-design-3", codex)
        self.assertIn("material-design-3", opencode)
        self.assertIn('"material-design-3": "allow"', config)
        self.assertLess(len(codex.splitlines()), 30)
        self.assertLess(len(opencode.splitlines()), 30)

    def test_readme_documents_portable_install_and_verification(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for required in (
            ".agents/skills/material-design-3",
            "Codex",
            "OpenCode",
            "validate_skill.py",
            "audit_m3.py",
            "Material 3 Expressive",
            "unofficial",
        ):
            self.assertIn(required, text)

    def test_eval_readme_explains_real_model_runs(self):
        text = (SKILL / "evals/README.md").read_text(encoding="utf-8")
        self.assertIn("fresh", text.lower())
        self.assertIn("without the skill", text.lower())
        self.assertIn("with the skill", text.lower())
        self.assertIn("Codex", text)
        self.assertIn("OpenCode", text)

    def test_license_and_changelog_exist(self):
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("0.1.0", changelog)
        self.assertIn("2026-08-24", changelog)


if __name__ == "__main__":
    unittest.main()
