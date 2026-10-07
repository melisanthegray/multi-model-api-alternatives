import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class AlternativesTests(unittest.TestCase):
    def test_migration_matrix(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Checked 2026-10-07", text)
        self.assertIn("Migration worksheet", text)
        for name in ("ArgoLink", "Together", "fal", "Replicate", "Fireworks", "Hugging Face", "LiteLLM", "Portkey"):
            self.assertIn(name, text)
        for field in ("model IDs", "base URL", "usage", "idempotency"):
            self.assertIn(field, text)

    def test_sources(self):
        text = (ROOT / "sources.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(len(re.findall(r"https://[^) ]+", text)), 12)

    def test_no_retired_or_secret_material(self):
        text = "\n".join(p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md"))
        self.assertNotIn("api." + "argolink.io", text)
        self.assertNotIn("sk-", text.lower())


if __name__ == "__main__":
    unittest.main()
