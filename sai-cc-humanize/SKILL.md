---
name: sai-cc-humanize
description: Remove AI-sounding prose from an optimised sai-cc article while locking every SEO/AEO-critical element, producing 07-final.md. Delegates to the configured humanizer skill (falls back to a built-in AI-tell checklist) and then verifies protected elements are byte-identical. Use when the user says "/sai-cc-humanize", "humanize this article", or sai-cc-start reaches this step.
argument-hint: "<page folder>"
---

# sai-cc-humanize

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md`, `craft-rules.md` (the voice section) and `ai-tells-fallback.md`.

This step runs **after** SEO/AEO, because the optimisation pass adds the most formulaic text: summaries, definitions, FAQ answers and bios. It rewrites prose only.

## 1. Build the protected list

Extract the following from `07-optimised.md` into `{page}/.humanize-protected.json` (a working file):
- the entire frontmatter
- every heading line (`#`, `##`, `###`)
- the answer-first definition paragraph under the H1: you may change wording only if the primary keyword phrase and the "<term> is" opening survive, and it stays at 40–60 words
- every sentence containing the primary or a secondary keyword: those keyword phrases must survive verbatim
- all tables, Mermaid/code blocks, and Markdown links (anchor text + URL)
- FAQ question headings
- the byline and the "About the author" facts
- everything below `HAND-OFF APPENDIX`

## 2. Humanize

- If `humanizer_skill` in the config is available (not `fallback`), invoke it with the Skill tool. Give it the article body (from the H1 down to the appendix marker, excluding the appendix) and these instructions:
  > Rewrite to remove AI tells. Preserve meaning, structure and facts. Keep these unchanged: all headings, tables, code blocks, links, the keyword phrases [list], the byline and the author facts. Keep the author's voice: [2–3 line summary from the bundle's communication style]. Keep FAQ answers at 40–80 words and self-contained.
- Otherwise, apply `ai-tells-fallback.md` yourself, section by section.
- Keep the configured spelling.

## 3. Verify

Compare the result with the protected list:
- Headings, tables, code blocks, links, frontmatter, byline and appendix must be identical. Restore any that changed.
- Every listed keyword phrase must still be present at least as many times as before. Restore the original sentence if one went missing.
- The definition must be 40–60 words and start with the primary term.
- FAQ answers must be 40–80 words. The JSON-LD FAQ text must equal the visible answers. If humanizing changed an answer, update the JSON-LD copy to match it.

Write `07-final.md` with `status: awaiting-approval` and `produced_by: sai-cc-humanize`, plus `humanizer: <skill|fallback>`. Delete the working file.

## Output

`✓ humanize → 07-final.md (<n> paragraphs rewritten, <n> protected items restored, humanizer: <name>)`
