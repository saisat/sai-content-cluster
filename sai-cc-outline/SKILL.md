---
name: sai-cc-outline
description: Create the article outline (04-outline.md) for a sai-cc page from its brief, audit and cluster role, including answer-first slots, required tables/diagrams, internal-link placements, the author identity lens chosen from the OKF bundle, and [SME] slots that drive the interview. Use when the user says "/sai-cc-outline", "outline this article", or sai-cc-start reaches the outline step.
argument-hint: "<page folder> [feedback]"
---

# sai-cc-outline

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md`, `seo-aeo-standards.md`, `craft-rules.md` and `okf-usage.md`.

## Inputs

`01-brief.md` (approved), `03-audit.md` (if present), the registry row and cluster map, the company context, and the author bundle (loaded minimally, per okf-usage.md).

## Build the outline

1. **Choose the identity lens.** Pick 1–2 identities from the bundle with a one-line reason each. Record them, and the files loaded, in the frontmatter (`identity_lens`, `okf_loaded`).
2. **Metadata.** Take the title, meta and H1 from brief §9. If one breaks a standard (e.g. the title is over 60 characters), keep it but flag it.
3. **Resolve contradictions first.** For each contradiction in brief §23 or audit §4, state the decision the article will make (e.g. "One operational model of 7 stages; the 4-stage market curve is named once in the comparison table and linked out"). These become guardrails for the draft.
4. **Skeleton.** Follow brief §10 exactly. Merge or reorder only with a reason given. Under each H2/H3, write:
   - **Answer-first line:** the 1–3 sentence answer this section opens with (draft wording)
   - **Points:** 3–6 bullets of substance, noting audit material reused via `[reuse: audit §6 item]`
   - **Asset:** the table, diagram or example this section carries (from brief §13), with its columns specified for tables
   - **Links:** internal link placements (anchor → URL) and external citations
   - **[SME-n]:** where only the author's experience can make the section credible, a slot naming what's needed, e.g. `[SME-3] a real sunset/retirement decision you drove: the signal, who resisted, what you'd do differently`. Aim for 5–8 slots across the article, focused on the sections where practitioner judgement matters most.
5. **Definition draft.** The 40–60 word answer-first definition, worded in full.
6. **FAQ plan.** The brief §14 questions, rephrased as real queries if needed, with answer directions.
7. **Word budget per H2,** summing to the brief's §19 range.
8. **Cannibalisation guard.** List the topics this page must only summarise and link, because sibling pages own them.

Write `04-outline.md` with `status: awaiting-approval`.

## Output

`✓ outline → 04-outline.md (<n> H2s, <n> SME slots, lens: <identities>, ~<n> words)`
