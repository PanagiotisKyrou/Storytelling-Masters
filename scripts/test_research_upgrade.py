#!/usr/bin/env python3

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"


class ResearchUpgradeTests(unittest.TestCase):
    def test_all_evidence_anchors_exist(self):
        ledger = (REFS / "master-evidence-ledger.md").read_text(encoding="utf-8")
        expected = {
            "L": 4,
            "S": 4,
            "M": 4,
            "K": 5,
            "I": 4,
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

    def test_quarantined_regression_language_stays_quarantined(self):
        phrase = "seven" + " pens"
        allowed = {
            Path("references/legacy-contamination-audit.md"),
            Path("scripts/validate_run.py"),
            Path("scripts/test_validate_run.py"),
        }
        offenders = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".py", ".yaml"}:
                continue
            rel = path.relative_to(ROOT)
            if rel in allowed or rel == Path("scripts/test_research_upgrade.py"):
                continue
            if phrase in path.read_text(encoding="utf-8").lower():
                offenders.append(str(rel))
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
