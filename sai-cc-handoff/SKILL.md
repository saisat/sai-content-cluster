---
name: sai-cc-handoff
description: Package a finished topic cluster for the marketing team as one ready-to-share folder. It contains a READ ME, only the approved final articles (pillar first, labelled PILLAR/SPOKE, with new or not-recommended pages flagged in the name) and a fresh cluster map, and never the interim files (briefs, audits, outlines, interviews, drafts, QA). The user uploads or shares the folder however they like. Use when the user says "/sai-cc-handoff", "hand off the cluster to marketing", "package the articles for marketing", or after the last article in a cluster is approved.
argument-hint: "<pillar-slug>"
---

# sai-cc-handoff

`{core}` is the sibling `sai-cc-core` directory. `{scripts}` is this skill's `scripts/` directory. Read `{core}/references/file-conventions.md` and the config (`clusters_root`).

This skill only builds files on disk. It doesn't upload, share or email anything; the user does that with whatever tool their team uses.

## What marketing gets

A folder `<pillar>/_handoff/<date>/` with:

| File | Source |
|---|---|
| `00 READ ME - Marketing hand-off.md` | `<pillar>/marketing-handoff.md` |
| `01 PILLAR - <Title>.md` | the pillar's `07-final.md` |
| `NN SPOKE - <Title>.md`, with `[new page]` and/or `[not recommended]` in the name where they apply | each spoke's `07-final.md` |
| `NN Cluster map.md` | generated from `_system/cluster-registry.md` and the cluster map's scope |
| `manifest.json` | list of files with checksums (for the user's records) |

Each article file starts with a **Publishing details** table (type, URL, SEO title, meta, H1, keywords, schema, approval date), then the article, then **Hand-off notes** (JSON-LD, links, sources, images, change log, open items). Internal fields (identity lens, bundle files, step names) are dropped.

**Never included:** `00-brief-source`, `01-brief`, `02-existing`, `03-audit`, `04-outline`, `05-interview`, `05-okf-proposals`, `06-draft`, `07-optimised`, `08-qa`, `_system/` files, anything about the author bundle.

## Steps

1. **Check readiness.** Every registry page for the pillar must have a `07-final.md` with `status: approved`. If some don't, list them and ask whether to wait or to hand off without them (then exclude them and say so in the READ ME).
2. **Write or refresh the READ ME** (`<pillar>/marketing-handoff.md`) if it's missing or older than any final. Refer to the articles by their **hand-off file names** (`01 PILLAR - …`), not by working folders. Include: a one-paragraph summary; an articles table (file, type, URL, SEO title, words); decisions for marketing on new pages, with recommendations; pre-publish checklists (all pages, then per page, merged from each final's Appendix F); and post-publish checks. Plain Markdown with `- [ ]` checklists.
3. **Build the package:** `python3 {scripts}/build_handoff.py <clusters_root> <pillar-slug>`. It refuses to build if step 1 or 2 isn't satisfied, and replaces any earlier package with the same date.
4. **Check the output:** open one article file and the cluster map, and confirm there are no leftover HTML comments, internal fields or interim files.
5. **Record:** append one line to `_system/changelog.md` (date, folder path, number of files).

## Output

`✓ handoff → <pillar>/_handoff/<date>/ (<n> files: READ ME, <n> articles, cluster map) — ready to upload or share`
