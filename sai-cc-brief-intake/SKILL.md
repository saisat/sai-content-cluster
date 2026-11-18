---
name: sai-cc-brief-intake
description: Normalise a marketing/SEO content brief of any structure (.md, .docx, pasted text) into the sai-cc canonical 01-brief.md schema, flagging missing, unverified or contradictory items without inventing data. Use when the user hands over a content brief, says "/sai-cc-brief-intake", or sai-cc-start runs mode A.
argument-hint: "<brief file path> [page folder]"
---

# sai-cc-brief-intake

`{core}` is the sibling `sai-cc-core` directory. Read `{core}/references/file-conventions.md` and `{core}/references/brief-schema.md` first.

## Steps

1. **Load the brief.**
   - For `.md` or `.txt`, read it.
   - For `.docx`, try `pandoc -t gfm`. If pandoc isn't available, use the docx skill if present. Otherwise ask for a Markdown export.
   - For pasted text, save it as-is.
   - A filename like `X.docx.md` is already Markdown.
2. **Locate the page.** Take the URL and primary keyword from the brief and derive `page_slug`. Look up the pillar in `_system/cluster-registry.md`. If it isn't there, use `_unassigned/`. Create the page folder.
3. **Preserve the original.** Copy the brief, unchanged, to `00-brief-source.<ext>`.
4. **Map to the schema.** Use the heading synonym map. For each canonical section:
   - Carry content over faithfully. Tables stay tables. Numbers stay verbatim with their stated source.
   - Unescape Markdown artefacts from docx conversion (`https\://` → `https://`, `\|` → `|`).
   - Split mixed sections, and put unmappable content under §11 as `Additional instruction (source: <heading>)`.
   - Fill in the frontmatter: `mode: A`, `source: marketing`, `status: approved`. A marketing brief is already approved input.
5. **Build §23 Missing or Unverified.** Include:
   - every canonical section with no source content
   - keyword rows with no volume/KD
   - internal links not in `_system/site-urls.csv` (mark them `unverified`)
   - **internal contradictions**, e.g. a recommended FAQ answer that conflicts with the structure, or a stage count mismatch
   - data-limitation caveats that affect writing, e.g. "don't state dates for GSC numbers"
6. **Seed the URL inventory.** Append any URLs the brief marks as verified to `_system/site-urls.csv`, if they're not already there, with `notes: from brief <slug>`.
7. **Write `01-brief.md`.** Character-count the metadata in §9.

## Output to the caller

Print one line, e.g. `✓ brief-intake → <path>/01-brief.md (23 sections; 4 missing, 2 contradictions)`. List the contradictions in one line each. They matter for the outline.
