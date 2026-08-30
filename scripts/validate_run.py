#!/usr/bin/env python3
"""Validate a Master Narrative Craft run record.

This validates process evidence and known contamination, not artistic quality.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Any


MASTERS = {"lynch", "scorsese", "mckean", "kurosawa", "inoue"}
INDEPENDENCE = {"isolated", "sequential-blind", "not-independent"}
CONTAMINATION = {
    "seven pens",
    "7 pens",
    "seven people, ten meanings",
    "seven people ten meanings",
    "ten meanings",
    "gate 03",
    "gate03",
    "m33",
    "word-card",
    "word card",
    "dark teal",
    "dark/teal",
}


def text_blob(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False).lower()


def nonempty(value: Any) -> bool:
    return value is not None and value != "" and value != [] and value != {}


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = data.get("mode")
    if mode not in {"story", "frame_studio", "full_run"}:
        errors.append("mode must be story, frame_studio, or full_run")

    brief = data.get("brief", {})
    for key in ("truth", "audience", "medium", "target_change"):
        if not nonempty(brief.get(key)):
            errors.append(f"brief.{key} is required")

    scouts = data.get("scouts", [])
    seen: set[str] = set()
    for index, scout in enumerate(scouts):
        master = str(scout.get("master", "")).lower()
        if master not in MASTERS:
            errors.append(f"scouts[{index}].master is invalid")
        else:
            seen.add(master)
        if scout.get("independence_method") not in INDEPENDENCE:
            errors.append(f"scouts[{index}].independence_method is invalid")
        if not nonempty(scout.get("contribution")) and not scout.get("abstain"):
            errors.append(f"scouts[{index}] needs a contribution or abstain=true")
        if not nonempty(scout.get("risk")):
            errors.append(f"scouts[{index}].risk is required")
    if data.get("exploration_depth", "standard") != "minimal" and seen != MASTERS:
        errors.append("standard runs must record all five scouts; a scout may abstain")

    selected = data.get("selected", {})
    for key in ("route", "strongest_alternative", "deciding_tradeoff"):
        if not nonempty(selected.get(key)):
            errors.append(f"selected.{key} is required")

    if mode in {"story", "full_run"}:
        beats = data.get("story", {}).get("beats", [])
        if not beats:
            errors.append("story.beats is required for STORY and FULL RUN")

    if mode in {"frame_studio", "full_run"}:
        frames = data.get("frames", [])
        if not frames:
            errors.append("frames are required for FRAME STUDIO and FULL RUN")
        unverified = bool(data.get("unverified_spec"))
        frame_fields = (
            "id",
            "story_job",
            "audience_before",
            "audience_after",
            "visual_event",
            "composition",
            "text_image_delta",
            "continuity",
            "build_method",
        )
        for index, frame in enumerate(frames):
            for key in frame_fields:
                if not nonempty(frame.get(key)):
                    errors.append(f"frames[{index}].{key} is required")
            if not unverified:
                for key in ("render_path", "inspection", "revision_status"):
                    if not nonempty(frame.get(key)):
                        errors.append(f"frames[{index}].{key} is required after rendering")
        if len(frames) > 1 and not nonempty(data.get("sequence_inspection")):
            errors.append("sequence_inspection is required for multi-frame work")

    completion = data.get("completion", {})
    if not nonempty(completion):
        errors.append("completion evidence is required")
    if mode in {"frame_studio", "full_run"} and not data.get("unverified_spec"):
        if completion.get("rendered") is not True:
            errors.append("completion.rendered must be true")
        if completion.get("inspected") is not True:
            errors.append("completion.inspected must be true")

    loaded = {str(item).lower() for item in data.get("source_case_ids", [])}
    if not ({"gate03", "gate_03", "gate-03"} & loaded):
        blob = text_blob(data)
        for phrase in sorted(CONTAMINATION):
            if phrase in blob:
                errors.append(f"quarantined Gate 03 residue detected: {phrase!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_record", type=pathlib.Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.run_record.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}")
        return 2
    if not isinstance(data, dict):
        print("INVALID: top level must be a JSON object")
        return 2
    errors = validate(data)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: process evidence is structurally complete; artistic quality remains unverified by this script")
    return 0


if __name__ == "__main__":
    sys.exit(main())
