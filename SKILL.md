---
name: master-narrative-craft
description: Create or substantially improve narrative-driven stories and visual sequences, including carousels, slide decks, storyboards, keyframes, visual essays, and short videos. Use when the user asks to shape material into a story, create frames or slides, rebuild weak visuals, or review a rendered sequence; this skill creates and revises the work, not merely audits it.
---

# Master Narrative Craft

Use five researched craft systems as lenses, not as style presets or authorities above the user. The user brief, truth, audience, voice, brand, medium, and production reality come first.

## Route automatically

Choose the smallest mode that completes the request:

- **STORY** — shape the narrative, audience-state path, beats, and ending. Read [story-studio.md](references/story-studio.md).
- **FRAME STUDIO** — create or rebuild actual slides, frames, or keyframes; render, inspect, and revise them. Read [frame-studio.md](references/frame-studio.md).
- **FULL RUN** — STORY, then FRAME STUDIO, then a rendered sequence trial. Use for a net-new carousel, deck, storyboard, visual essay, or short visual video.

If the user supplies existing frames and asks for feedback, use FRAME STUDIO: inspect them, preserve what works, and rebuild material failures. Do not stop at a critique unless the user explicitly requests critique only.

## Shared brief lock

Before exploration, record:

- truth: observed/supplied, supported inference, unknown, forbidden invention;
- audience: entry model, context, outside option, accessibility needs;
- medium: dimensions, duration/page count, platform, delivery format;
- target change: what the audience should notice, understand, feel, remember, or do differently;
- user profiles: voice, brand, references, aesthetic preferences, rejected directions;
- constraints: time, tools, source rights, factual/causal limits, production ceiling.

Ask a question only when two plausible answers would materially change the result. Otherwise choose a reversible default and state it briefly.

## Preserve source boundaries

Read [research-boundaries.md](references/research-boundaries.md) before using a master dossier.

- Never imitate a living or deceased creator's surface style.
- Translate research into general craft operations.
- Label direct creator evidence, collaborator/production evidence, observation, and skill synthesis separately.
- Do not let a development case, brand example, or old visual become a universal rule.
- Use [master-evidence-ledger.md](references/master-evidence-ledger.md) to verify quotations, source context, translation/hosting caveats, and use limits.
- Keep creator quotations and names out of the user's artifact unless the user explicitly asks for them and they serve the work.

## Master exploration

Read [master-scout.md](references/master-scout.md). Run the five short scouts before selecting a direction. Freeze each scout before comparison and record the actual independence method:

- `isolated` — separate contexts or agents, when available and authorized;
- `sequential-blind` — one context, but each scout is written before comparison without reusing earlier candidate language;
- `not-independent` — exposed passes; do not present their agreement as corroboration.

Every master may return **no useful contribution for this brief**. Forced fingerprints create pastiche.

After scouting, deepen only the dossiers that can resolve a named uncertainty or expand a promising route:

- [master-lynch.md](references/master-lynch.md) — charged fragments, coherent breach, clues, recurrence, unresolved residue;
- [master-scorsese.md](references/master-scorsese.md) — frame philosophy, viewpoint, visual sequencing, storyboard precision, audience testing;
- [master-mckean.md](references/master-mckean.md) — material/register choice, image-text interdependence, association, density, reader construction;
- [master-kurosawa.md](references/master-kurosawa.md) — action, motivation, environment, tempo, previsualization, ruthless editing;
- [master-inoue.md](references/master-inoue.md) — character life, bodily truth, natural timing, changed perspective, iterative retouching.

Use [council-and-selection.md](references/council-and-selection.md) to compare candidates. Scale exploration to the risk; counts are budgets, not proof of creativity.

## Build, render, inspect

For visual work, a prose concept is not completion.

1. Build a frame ledger from the selected story.
2. Create the actual frames with the appropriate available presentation, design, image, or code-native tool.
3. Render/export the artifact at the intended dimensions.
4. Inspect every frame as pixels and inspect the sequence as thumbnails/contact sheet.
5. Revise weak hierarchy, composition, imagery, typography, continuity, or narrative work.
6. Re-render and verify the correction.

If rendering or visual inspection is unavailable, deliver a clearly labeled **unverified production specification**. Never call it finished or perfect.

Read only the relevant medium section in [medium-modules.md](references/medium-modules.md).

## Evaluation

Use [evaluation.md](references/evaluation.md). Separate:

- factual and causal integrity;
- story effect;
- frame quality;
- sequence quality;
- voice/brand fit;
- production correctness.

Use observable `PASS`, `REVISE`, or `BLOCKED` findings. A self-score, explanation, or process checklist is not evidence.

For a substantial FULL RUN, save the internal run record as JSON and run:

```bash
python scripts/validate_run.py path/to/run.json
```

Use [run-record.md](references/run-record.md) for the record shape. Use [source-register.md](references/source-register.md) when checking provenance.

The validator checks process evidence and contamination controls; it does not certify artistic excellence.

## Non-negotiables

- Do not inherit an old hook, metaphor, template, palette, or frame grammar unless the current brief selects it.
- Do not force all five masters into the final artifact.
- Do not equate novelty with quality or baseline distance with improvement.
- Do not repeat copy with imagery unless deliberate redundancy has a documented job.
- Do not use one poster layout for every frame when the story needs rhythm or spatial change.
- Do not invent lived reactions, quotations, causes, or outcomes.
- Do not judge visual quality from prompts or specifications when a render exists.
- Do not claim perfection; show what was inspected, changed, and still remains uncertain.
