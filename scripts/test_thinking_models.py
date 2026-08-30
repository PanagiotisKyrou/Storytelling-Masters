#!/usr/bin/env python3

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"
MASTERS = {
    "lynch": "master-lynch.md",
    "scorsese": "master-scorsese.md",
    "mckean": "master-mckean.md",
    "kurosawa": "master-kurosawa.md",
    "inoue": "master-inoue.md",
}
REQUIRED_DIMENSIONS = {
    "attention filter",
    "generative unit",
    "development engine",
    "selection criterion",
    "uncertainty strategy",
    "audience model",
    "collaboration model",
    "correction loop",
    "stopping rule",
    "characteristic risk",
}


def parse_model(path: Path):
    text = path.read_text(encoding="utf-8")
    section = text.split("## Observable decision model", 1)[1]
    section = section.split("\n## ", 1)[0]
    rows = {}
    for line in section.splitlines():
        if not line.startswith("|") or "---" in line or "Dimension" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) == 3:
            rows[cells[0]] = (cells[1], cells[2])
    return text, rows


class ThinkingModelTests(unittest.TestCase):
    def test_models_are_complete_decision_traces(self):
        for name, filename in MASTERS.items():
            text, rows = parse_model(REFS / filename)
            self.assertEqual(set(rows), REQUIRED_DIMENSIONS, name)
            anchored = sum(bool(re.search(r"`[LSMKI]\d", pattern)) for pattern, _ in rows.values())
            self.assertGreaterEqual(anchored, 6, name)
            for dimension, (pattern, translation) in rows.items():
                self.assertGreater(len(pattern), 20, (name, dimension))
                self.assertGreater(len(translation), 20, (name, dimension))
            self.assertIn("Operational inference — S", text)

    def test_models_remain_distinct(self):
        signatures = {}
        for name, filename in MASTERS.items():
            _, rows = parse_model(REFS / filename)
            signatures[name] = (
                rows["attention filter"][1],
                rows["generative unit"][1],
                rows["selection criterion"][1],
            )
        self.assertEqual(len(set(signatures.values())), len(MASTERS))

    def test_router_uses_decision_gaps_and_abstention(self):
        router = (REFS / "master-thinking-models.md").read_text(encoding="utf-8")
        for master in ("Lynch", "Scorsese", "McKean", "Kurosawa", "Inoue"):
            self.assertRegex(router, rf"\|[^\n]+\| {master} \|")
        self.assertIn("decision_gap: We cannot yet decide", router)
        self.assertGreaterEqual(router.count("Abstain"), 1)
        self.assertGreaterEqual(router.lower().count("abstain"), 3)
        self.assertIn("not claims about personality", router)

    def test_stopping_rules_are_not_fabricated(self):
        established = {"lynch"}
        for name, filename in MASTERS.items():
            _, rows = parse_model(REFS / filename)
            pattern, translation = rows["stopping rule"]
            combined = f"{pattern} {translation}".lower()
            if name in established:
                self.assertIn("adding or removing", combined)
            else:
                self.assertTrue(
                    "not established" in combined or "no universal" in combined or "no portable" in combined,
                    name,
                )

    def test_no_psychological_persona_routing(self):
        router = (REFS / "master-thinking-models.md").read_text(encoding="utf-8").lower()
        forbidden = (
            "personality type:",
            "clinical diagnosis:",
            "hidden motive:",
            "think exactly like",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, router)
        for weak_trigger in ("dreamlike", "fast cuts", "collage", "samurai imagery", "manga linework"):
            self.assertIn(weak_trigger, router)
        self.assertIn("do not route by surface resemblance", router)

    def test_thinking_models_are_discoverable(self):
        entrypoint = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for filename in MASTERS.values():
            self.assertIn(filename, entrypoint)


if __name__ == "__main__":
    unittest.main()
