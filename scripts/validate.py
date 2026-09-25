"""Validate this source package without credentials or network access.

These are structural and publication-hygiene checks, not a model or live-MCP test.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "nestly-connect-verify", "nestly-launch-opportunity",
    "nestly-evolve-space", "nestly-stewardship",
}
ENDPOINT = "https://nestly.bot/mcp"


def load_json(root: Path, relative: str):
    return json.loads((root / relative).read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_reference(root: Path, source: Path, target: str):
    """Reject unresolved/traversing Markdown references inside the package."""
    if target.startswith(("https://", "http://", "#", "mailto:")):
        return
    resolved = (source.parent / target.split("#", 1)[0]).resolve()
    require(resolved.is_relative_to(root.resolve()), f"Reference escapes package: {source.name}")
    require(resolved.exists(), f"Missing local reference: {target}")


def validate(root: Path = ROOT):
    manifest = load_json(root, "plugin.json")
    require(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "Portable plugin schema missing")
    require(manifest.get("name") == "nestly", "Plugin identity must be nestly")
    require(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", ""))), "Invalid version")
    require(bool(manifest.get("description")), "Missing description")
    require(manifest.get("repository") == "https://github.com/fabioalcantara/nestly", "Unexpected public repository")
    mcp = load_json(root, "mcp.json")
    require(mcp.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json", "Portable MCP schema missing")
    require(mcp.get("mcpServers") == {"nestly": {"type": "streamable-http", "url": ENDPOINT}}, "Unexpected MCP endpoint, transport, or embedded credentials")
    marketplace = load_json(root, ".agents/plugins/marketplace.json")
    require(marketplace["plugins"][0]["source"] == {"source": "local", "path": "./"}, "Marketplace must point at package root")
    found = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    require(found == EXPECTED_SKILLS, f"Unexpected skills: {sorted(found)}")
    for name in sorted(found):
        path = root / "skills" / name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", text)
        require(match is not None, f"Invalid skill frontmatter: {name}")
        require(match[1] == name, f"Skill name/folder mismatch: {name}")
        require(20 <= len(match[2]) <= 1024, f"Invalid description length: {name}")
        require(len(text.splitlines()) < 500 and "TODO" not in text, f"Unfinished or oversized skill: {name}")
        interface = (path.parent / "agents/openai.yaml").read_text(encoding="utf-8")
        require(f"${name}" in interface, f"Default prompt missing skill name: {name}")
        require(f'url: "{ENDPOINT}"' in interface, f"MCP dependency missing: {name}")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
            local_reference(root, path, target)
    scenarios = load_json(root, "tests/scenarios.json")
    require(len(scenarios) >= 8, "Insufficient scenario coverage")
    ids = set()
    for case in scenarios:
        require(case["id"] not in ids, "Duplicate scenario ID")
        ids.add(case["id"])
        require(case["skill"] in EXPECTED_SKILLS, "Unknown scenario skill")
        require(case.get("input") and case.get("available_tools") is not None and case.get("expected") and case.get("forbidden"), "Incomplete scenario")
    for path in root.rglob("*"):
        if not path.is_file() or any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        require(path.suffix not in {".png", ".jpg", ".jpeg", ".log", ".sqlite"}, f"Private evidence must not be published: {path.name}")
        require(not path.name.startswith(".env"), "Environment file must not be published")
        raw = path.read_text(encoding="utf-8")
        require(not re.search(r"(?:sk-proj-|ghp_|github_pat_)[A-Za-z0-9_-]{20,}", raw), f"Possible credential: {path.name}")
        require(not re.search(r"plugin_asdk_app_[a-z0-9]{20,}", raw), f"Personal connector ID: {path.name}")
    return {"skills": len(found), "scenarios": len(scenarios), "status": "structural checks passed"}


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), ensure_ascii=False))
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
