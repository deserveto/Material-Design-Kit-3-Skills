import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/material-design-3"
REFERENCES = SKILL / "references"
ASSETS = SKILL / "assets"

EXPECTED_TYPE_ROLES = {
    "displayLarge": (57, 64),
    "displayMedium": (45, 52),
    "displaySmall": (36, 44),
    "headlineLarge": (32, 40),
    "headlineMedium": (28, 36),
    "headlineSmall": (24, 32),
    "titleLarge": (22, 28),
    "titleMedium": (16, 24),
    "titleSmall": (14, 20),
    "bodyLarge": (16, 24),
    "bodyMedium": (14, 20),
    "bodySmall": (12, 16),
    "labelLarge": (14, 20),
    "labelMedium": (12, 16),
    "labelSmall": (11, 16),
}

EXPECTED_MATERIAL_SHAPES = {
    "Arch", "Arrow", "Boom", "Bun", "Burst", "Circle", "ClamShell",
    "Clover4Leaf", "Clover8Leaf", "Cookie12Sided", "Cookie4Sided",
    "Cookie6Sided", "Cookie7Sided", "Cookie9Sided", "Diamond", "Fan",
    "Flower", "Gem", "Ghostish", "Heart", "Oval", "Pentagon", "Pill",
    "PixelCircle", "PixelTriangle", "Puffy", "PuffyDiamond", "SemiCircle",
    "Slanted", "SoftBoom", "SoftBurst", "Square", "Sunny", "Triangle",
    "VerySunny",
}


class DesignFoundationReferenceTests(unittest.TestCase):
    def test_typography_baseline_asset_has_all_15_roles(self):
        data = json.loads((ASSETS / "typography-baseline.json").read_text(encoding="utf-8"))
        self.assertEqual(data["reviewed"], "2026-08-24")
        self.assertEqual(data["unit"], "sp")
        self.assertTrue(data["reference_only"])
        roles = data["roles"]
        self.assertEqual(set(roles), set(EXPECTED_TYPE_ROLES))
        for role, (size, line_height) in EXPECTED_TYPE_ROLES.items():
            self.assertEqual(roles[role]["fontSize"], size, role)
            self.assertEqual(roles[role]["lineHeight"], line_height, role)
            self.assertIn(roles[role]["referenceTypefaceStyle"], {"Roboto", "Roboto Medium"})

    def test_shape_asset_separates_stable_example_from_newer_alpha_api(self):
        data = json.loads((ASSETS / "shape-baseline.json").read_text(encoding="utf-8"))
        self.assertEqual(data["reviewed"], "2026-08-24")
        self.assertTrue(data["reference_only"])
        self.assertEqual(
            data["composeBaselineExampleDp"],
            {"extraSmall": 4, "small": 8, "medium": 12, "large": 16, "extraLarge": 24},
        )
        self.assertEqual(data["endpoints"], ["RectangleShape", "CircleShape"])
        self.assertEqual(
            set(data["compose15AlphaAdditionalSlots"]),
            {"largeIncreased", "extraLargeIncreased", "extraExtraLarge"},
        )
        self.assertEqual(set(data["materialShapesExperimental"]), EXPECTED_MATERIAL_SHAPES)
        self.assertEqual(len(data["materialShapesExperimental"]), 35)

    def test_typography_reference_teaches_semantics_scaling_and_platform_translation(self):
        text = (REFERENCES / "typography.md").read_text(encoding="utf-8")
        for phrase in (
            "15",
            "baseline reference",
            "semantic",
            "custom typeface",
            "text scaling",
            "Web",
            "Compose",
            "Flutter",
            "typography-baseline.json",
        ):
            self.assertIn(phrase, text)
        self.assertIn("57", text)
        self.assertIn("64", text)
        self.assertIn("Do not", text)

    def test_shape_reference_teaches_scale_endpoints_and_experimental_boundaries(self):
        text = (REFERENCES / "shape.md").read_text(encoding="utf-8")
        for phrase in (
            "RectangleShape",
            "CircleShape",
            "4dp",
            "24dp",
            "largeIncreased",
            "extraLargeIncreased",
            "extraExtraLarge",
            "ExperimentalMaterial3ExpressiveApi",
            "35",
            "shape-baseline.json",
        ):
            self.assertIn(phrase, text)
        self.assertIn("Do not", text)

    def test_skill_routes_typography_and_shape_references(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/typography.md", text)
        self.assertIn("references/shape.md", text)

    def test_eval_corpus_covers_typography_and_shape_failures(self):
        cases = json.loads((SKILL / "evals/cases.json").read_text(encoding="utf-8"))
        ids = {case["id"] for case in cases}
        self.assertTrue(
            {"typography-hierarchy", "web-type-scale", "shape-system", "expressive-shape-stability"}.issubset(ids)
        )


if __name__ == "__main__":
    unittest.main()
