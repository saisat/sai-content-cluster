---
name: sai-cc-sme-interview
description: Interview the subject-matter-expert author with 5–8 targeted questions derived from the outline's [SME] slots, skipping anything their OKF bundle already answers. Saves answers to 05-interview.md and drafts proposed bundle additions (new stories, sharper positions) to 05-okf-proposals.md for approval. Use when the user says "/sai-cc-sme-interview", "interview me for this article", or sai-cc-start reaches the interview step.
argument-hint: "<page folder>"
---

# sai-cc-sme-interview

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md` and `okf-usage.md`.

The interview is where the article gets the experience no competitor has. Questions must be specific enough that a vague answer is hard to give.

## 1. Prepare

1. Read the `[SME-n]` slots in `04-outline.md` (approved).
2. For each slot, check the bundle (identity files in the lens, beliefs, any stories/POV files) for something that already answers it. If it's covered, mark the slot `covered-by: <file>` and write a one-line summary. Don't ask about it. You may ask one confirming question only if the bundle content is marked draft or time-sensitive.
3. Write each remaining question so that it:
   - asks for a specific instance ("the last time you…", "a product where…"), a decision rule ("how do you decide when…"), or a contrarian view ("what do most PMs get wrong about…")
   - names the section it feeds
   - is answerable in 2–5 sentences

## 2. Ask

- Send the questions in batches of up to 4, using AskUserQuestion with free-text answers via "Other". Give each question 2–3 options that sketch typical answer directions, so the author can pick one and elaborate, or type their own.
- If the author would rather answer in prose, accept one pasted block and split it by question.
- Ask at most one follow-up per question, and only when an answer is too general to use (no instance, no decision, no consequence).
- "Skip" is a valid answer. That slot then becomes non-experiential in the draft.

## 3. Write `05-interview.md`

For each slot: the question, the answer in the author's own words (lightly cleaned, meaning preserved), the section it feeds, and usage notes (quote-worthy line? publishable? any confidentiality flags the author mentioned, such as client names). Status `approved` once the author confirms.

## 4. Write `05-okf-proposals.md`

For each answer that adds durable knowledge about the author (a reusable story, a clearer stance, a correction to the bundle), write a proposal in the format from okf-usage.md. Default to `stories/<slug>.md` as a new concept. If the bundle has no `stories/` folder yet, propose creating it, with an index file. Set every `decision: pending`. Never edit the bundle here.

## Output

`✓ sme-interview → 05-interview.md (<n> answered, <n> covered by bundle, <n> skipped) · <n> bundle proposals`
