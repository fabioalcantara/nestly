"""Negative tests for package boundaries; no remote calls or model evaluation."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_package", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_package_passes(self):
        self.assertEqual(validator.validate(self.root)["skills"], 4)

    def test_rejects_changed_endpoint(self):
        value = json.loads((self.root / "mcp.json").read_text())
        value["mcpServers"]["nestly"]["url"] = "https://example.invalid/mcp"
        (self.root / "mcp.json").write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError, "Unexpected MCP"):
            validator.validate(self.root)

    def test_rejects_embedded_auth(self):
        value = json.loads((self.root / "mcp.json").read_text())
        value["mcpServers"]["nestly"]["headers"] = {"Authorization": "synthetic-test-only"}
        (self.root / "mcp.json").write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError, "Unexpected MCP"):
            validator.validate(self.root)

    def test_rejects_reference_escape(self):
        with self.assertRaisesRegex(ValueError, "escapes"):
            validator.local_reference(self.root, self.root / "README.md", "../outside.txt")

    def test_rejects_missing_reference(self):
        with self.assertRaisesRegex(ValueError, "Missing local"):
            validator.local_reference(self.root, self.root / "README.md", "absent.md")

    def test_rejects_env_file(self):
        (self.root / ".env").write_text("EXAMPLE=synthetic")
        with self.assertRaisesRegex(ValueError, "Environment file"):
            validator.validate(self.root)

    def test_rejects_public_customer_screenshot(self):
        (self.root / "account.png").write_text("synthetic-image-marker")
        with self.assertRaisesRegex(ValueError, "Private evidence"):
            validator.validate(self.root)

    def test_rejects_duplicate_scenario(self):
        path = self.root / "tests/scenarios.json"
        cases = json.loads(path.read_text())
        cases.append(cases[0])
        path.write_text(json.dumps(cases))
        with self.assertRaisesRegex(ValueError, "Duplicate scenario"):
            validator.validate(self.root)


if __name__ == "__main__":
    unittest.main()
