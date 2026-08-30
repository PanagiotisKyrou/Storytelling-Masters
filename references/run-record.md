# Run Record

For a substantial FULL RUN, keep a compact JSON record. This makes provenance, abstention, selection, rendering, and inspection auditable without turning the creative work into form-filling.

Required top-level fields:

- `mode`: `story`, `frame_studio`, or `full_run`;
- `brief`: `truth`, `audience`, `medium`, and `target_change`;
- `source_case_ids`: development/regression cases intentionally loaded;
- `test_context`: `production`, `development`, or `held_out`;
- `scouts`: master name, contribution or abstention, risk, and independence method;
- `selected`: route, strongest alternative, and deciding tradeoff;
- `story.beats` for STORY or FULL RUN;
- `frames` and `sequence_inspection` for FRAME STUDIO or FULL RUN;
- `completion`: what was rendered, inspected, revised, and what remains uncertain.

Each frame record should contain:

- `id`, `story_job`, `audience_before`, `audience_after`;
- `visual_event`, `composition`, `text_image_delta`, `continuity`;
- `build_method`, `render_path`, `inspection`, `revision_status`.

Use `unverified_spec: true` only when building or rendering is genuinely unavailable. That is a declared limitation, not a pass.

Run `python scripts/validate_run.py run.json`. The validator checks evidence of process and guards known case leakage. It cannot judge beauty or certify a story.
