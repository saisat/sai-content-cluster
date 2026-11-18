---
name: sai-cc-draft
description: Write the full article draft (06-draft.md) for a sai-cc page in the author's voice, from the approved outline, interview answers and OKF bundle, with labelled illustrative examples, required tables and Mermaid diagrams, and no CTAs under an educational-only policy. Use when the user says "/sai-cc-draft", "draft the article", or sai-cc-start reaches the draft step.
argument-hint: "<page folder> [feedback]"
---

# sai-cc-draft

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md`, `craft-rules.md` and `okf-usage.md`.

## Inputs

`04-outline.md` (approved), `05-interview.md` (approved), `01-brief.md`, `03-audit.md` (for reusable material), the author bundle files listed in the outline's `okf_loaded`, and the company context (for "never say" rules only).

## Write

1. Follow the outline's skeleton, answer-first lines, assets and word budget. You may sharpen the wording; don't change the structure without noting why in the frontmatter (`deviations:`).
2. **Voice:** apply the bundle's communication style and the chosen identity lens. Positions must agree with the beliefs file.
3. **Experience:** weave each interview answer into its target section in the first person, keeping the author's own phrasing where it's strong. Never add an anecdote that isn't in `05-interview.md` or a bundle story. Where a slot was skipped, write the section without first-person claims.
4. **Reused material:** where the outline says `[reuse: …]`, rework the existing text rather than discarding it, so the change log stays honest.
5. **Assets:** build every table and diagram with real content, not placeholders. Label the illustrative example "Illustrative example" in its heading or first line.
6. **Links:** place internal links mid-sentence on the planned anchors. Put external citations inline as `[Source name](url)`, with the year where known. Mark anything uncertain `[VERIFY: …]`.
7. **Policy:** follow `cta_policy`. Under `educational-only`, add no promotion anywhere, and no closing pitch.
8. **FAQ:** write the answers (40–80 words each, self-contained).
9. Don't do keyword-density work here. That's sai-cc-seo-aeo's job. Write for the reader.

Frontmatter: `step: 06-draft`, `status: draft`, `word_count`, `identity_lens`, `interview_slots_used: [SME-1, …]`, `deviations`.

## Self-check before saving

- Is every brief §10 heading and §13 asset present?
- Is the chosen resolution of every brief §23 contradiction applied consistently, e.g. the stage count is identical everywhere, including the FAQ?
- No paragraph over 5 sentences, and no "In conclusion".

## Output

`✓ draft → 06-draft.md (<n> words, <n>/<n> SME slots used, <n> VERIFY flags)`
