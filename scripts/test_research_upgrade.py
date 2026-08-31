#!/usr/bin/env python3

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"


class ResearchUpgradeTests(unittest.TestCase):
    def test_all_evidence_anchors_exist(self):
        ledger = (REFS / "master-evidence-ledger.md").read_text(encoding="utf-8")
        expected = {
            "L": 7,
            "S": 7,
            "M": 8,
            "K": 8,
            "I": 7,
            "J": 8,
            "N": 9,
            "C": 9,
        }
        for prefix, count in expected.items():
            for index in range(1, count + 1):
                self.assertIn(f"| {prefix}{index} |", ledger)

    def test_each_master_has_a_distinct_decision_instrument(self):
        expected = {
            "master-lynch.md": "## Breach worksheet",
            "master-scorsese.md": "## Frame-intent record",
            "master-mckean.md": "## Image-text responsibility matrix",
            "master-kurosawa.md": "## State vector",
            "master-inoue.md": "## Life pass",
            "master-mcphee.md": "## Evidence-structure map",
            "master-niemann.md": "## Visual relation lab",
            "master-mccloud.md": "## Sequence inference ledger",
        }
        for filename, marker in expected.items():
            text = (REFS / filename).read_text(encoding="utf-8")
            self.assertIn(marker, text)
            self.assertIn("master-evidence-ledger.md", text)

    def test_quote_use_is_bounded(self):
        boundaries = (REFS / "research-boundaries.md").read_text(encoding="utf-8")
        self.assertIn("Do not use quote aggregators", boundaries)
        self.assertIn("Keep quotations in internal reasoning by default", boundaries)
        self.assertIn("Contradiction rule", boundaries)

    def test_weaker_inoue_translation_is_not_core_evidence(self):
        inoue = (REFS / "master-inoue.md").read_text(encoding="utf-8")
        sources = (REFS / "source-register.md").read_text(encoding="utf-8")
        weak_host = "mangabrog.wordpress.com"
        self.assertNotIn(weak_host, inoue)
        self.assertNotIn(weak_host, sources)
        self.assertIn("Hybrid technique answered two different problems", inoue)

    def test_mckean_ai_disagreement_is_not_hidden(self):
        mckean = (REFS / "master-mckean.md").read_text(encoding="utf-8")
        self.assertIn("Disagreement boundary", mckean)
        self.assertIn("explicitly rejects generative AI", mckean)

    def test_entrypoint_keeps_research_and_quality_evidence_separate(self):
        entrypoint = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        self.assertIn("cannot prove that the resulting work is good", entrypoint)
        self.assertIn("actual words, frames, and sequences", entrypoint)

    def test_new_models_change_workflow_without_becoming_pipeline(self):
        entrypoint = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        story = (REFS / "story-studio.md").read_text(encoding="utf-8").lower()
        frame = (REFS / "frame-studio.md").read_text(encoding="utf-8").lower()
        router = (REFS / "master-thinking-models.md").read_text(encoding="utf-8").lower()
        self.assertIn("master-mcphee.md", entrypoint)
        self.assertIn("master-niemann.md", entrypoint)
        self.assertIn("master-mccloud.md", entrypoint)
        self.assertIn("when factual material has no structure yet", story)
        self.assertIn("separate concept, sequence, and surface", frame)
        self.assertIn("do not run mcphee → niemann → mccloud as an automatic pipeline", router)


if __name__ == "__main__":
    unittest.main()
