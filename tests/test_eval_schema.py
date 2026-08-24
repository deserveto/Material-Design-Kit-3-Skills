import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / ".agents/skills/material-design-3/evals/cases.json"


class EvalSchemaTests(unittest.TestCase):
    def test_cases_have_required_shape(self):
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        ids = set()
        for case in cases:
            self.assertEqual(set(case), {"id", "prompt", "required", "forbidden", "references"})
            self.assertRegex(case["id"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
            self.assertNotIn(case["id"], ids)
            ids.add(case["id"])
            self.assertTrue(case["prompt"].strip())
            self.assertTrue(case["required"])
            self.assertTrue(case["forbidden"])
            self.assertTrue(case["references"])
            self.assertTrue(all(isinstance(v, str) and v.strip() for v in case["required"]))
            self.assertTrue(all(isinstance(v, str) and v.strip() for v in case["forbidden"]))

    def test_coverage_includes_core_behavior_classes(self):
        ids = {c["id"] for c in json.loads(CASES.read_text(encoding="utf-8"))}
        expected = {
            "new-web-ui",
            "existing-non-material-system",
            "explicit-migration",
            "semantic-color",
            "adaptive-list-detail",
            "touch-target",
            "expressive-restraint",
            "compose-stability",
            "flutter-migration",
            "visual-verification",
        }
        self.assertTrue(expected.issubset(ids), expected - ids)


if __name__ == "__main__":
    unittest.main()
