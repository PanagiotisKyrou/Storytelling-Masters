#!/usr/bin/env python3
"""Validate generic runtime reachability and scope boundaries.

This checks deterministic skill structure. It does not score creative quality.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "SKILL.md"
GENERIC_FILES = [ENTRY, *sorted((ROOT / "references").glob("*.md"))]
LAYER_SPECIFIC_TERMS = {"panos", "linkedin"}


def markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return re.findall(r"\[[^\]]+\]\(([^)#]+\.md)(?:#[^)]+)?\)", text)


def validate() -> list[str]:
    errors: list[str] = []
    entry = ENTRY.read_text(encoding="utf-8")

    required = {
        "references/collaboration-state.md",
        "references/master-thinking-models.md",
        "references/story-studio.md",
        "references/frame-studio.md",
        "references/evaluation.md",
    }
    for item in required:
        if item not in entry:
            errors.append(f"runtime entrypoint does not route to {item}")

    for path in GENERIC_FILES:
        relative = path.relative_to(ROOT)
        lowered = path.read_text(encoding="utf-8").lower()
        for term in LAYER_SPECIFIC_TERMS:
            if term in lowered:
                errors.append(f"publisher-specific term {term!r} in generic layer {relative}")
        for link in markdown_links(path):
            target = (path.parent / link).resolve()
            if not target.is_file():
                errors.append(f"broken reference from {relative}: {link}")

    policy = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "allow_implicit_invocation: true" not in policy:
        errors.append("generic co-creation skill must remain discoverable in normal work")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: runtime references are reachable and the generic layer is project-independent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
