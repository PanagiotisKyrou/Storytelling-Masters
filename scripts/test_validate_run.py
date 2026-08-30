#!/usr/bin/env python3

import copy
import unittest

from validate_run import MASTERS, validate


def sample() -> dict:
    scouts = [
        {
            "master": master,
            "contribution": "A distinct brief-specific operation",
            "risk": "Could distract from the governing idea",
            "independence_method": "sequential-blind",
        }
        for master in sorted(MASTERS)
    ]
    return {
        "mode": "full_run",
        "brief": {
            "truth": "A library return slot jams in wet weather",
            "audience": "Library operations team",
            "medium": "Three-slide internal presentation",
            "target_change": "See the delay as a handoff problem",
        },
        "source_case_ids": [],
        "test_context": "held_out",
        "scouts": scouts,
        "selected": {
            "route": "Follow one returned book through the jam",
            "strongest_alternative": "Map the full process",
            "deciding_tradeoff": "Concrete causality beats coverage",
        },
        "story": {"beats": ["return", "jam", "delayed discovery"]},
        "frames": [
            {
                "id": "01",
                "story_job": "establish",
                "audience_before": "unknown",
                "audience_after": "sees the return",
                "visual_event": "book enters slot",
                "composition": "side section",
                "text_image_delta": "text names time; image shows position",
                "continuity": "same book",
                "build_method": "SVG",
                "render_path": "01.png",
                "inspection": "clear at target size",
                "revision_status": "verified",
            },
            {
                "id": "02",
                "story_job": "reveal cause",
                "audience_before": "sees return",
                "audience_after": "sees obstruction",
                "visual_event": "book catches on swollen flap",
                "composition": "closer side section",
                "text_image_delta": "text gives weather condition",
                "continuity": "same book and slot",
                "build_method": "SVG",
                "render_path": "02.png",
                "inspection": "obstruction legible",
                "revision_status": "verified",
            },
        ],
        "sequence_inspection": "Cause reads across the pair without captions",
        "completion": {"rendered": True, "inspected": True, "remaining_uncertainty": "No user test"},
    }


class ValidationTests(unittest.TestCase):
    def test_clean_held_out_run_passes(self):
        self.assertEqual(validate(sample()), [])

    def test_gate_residue_fails_when_case_not_loaded(self):
        run = copy.deepcopy(sample())
        run["selected"]["route"] = "Seven pens explain ten meanings"
        errors = validate(run)
        self.assertTrue(any("residue" in error for error in errors))

    def test_unrendered_frame_fails(self):
        run = copy.deepcopy(sample())
        del run["frames"][0]["render_path"]
        self.assertTrue(any("render_path" in error for error in validate(run)))

    def test_loaded_regression_can_contain_quarantined_terms(self):
        run = copy.deepcopy(sample())
        run["source_case_ids"] = ["gate03"]
        run["selected"]["route"] = "Seven pens are intentionally under regression"
        self.assertFalse(any("residue" in error for error in validate(run)))


if __name__ == "__main__":
    unittest.main()
