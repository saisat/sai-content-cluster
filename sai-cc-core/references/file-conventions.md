# File Conventions

Every sai-cc skill follows these rules so that any step can run on its own, be re-run, or be resumed.

## 1. Find the config

1. Look for `content-cluster.config.md` in the current working directory, then in each parent directory up to the home directory. Use the first one found.
2. Resolve every relative path in the config against **the config file's directory**, not the current working directory.
3. If no config exists, stop and run `sai-cc-setup` (or tell the user to run `/sai-cc-setup`). Never guess the company context or author bundle.

Config keys are documented in `{core}/templates/config.md`.

## 2. Workspace layout

```
<clusters_root>/
  _system/                   one per workspace; shared by all pillars
    cluster-registry.md      source of truth: every page, role, owned keywords, status, links
    site-urls.csv            URL inventory (url,title,type,notes)
    changelog.md             one line per run that changed the registry
  <pillar-slug>/
    cluster-map.md           this pillar's spokes and link plan (a view of the registry)
    <page-slug>/             one folder per article
      00-brief-source.<ext>  original marketing brief, untouched (mode A only)
      01-brief.md            normalised brief (canonical schema)
      02-existing.md         clean extract of the live page (modes A/B)
      03-audit.md            gap audit (modes A/B)
      04-outline.md
      05-interview.md
      05-okf-proposals.md
      06-draft.md
      07-optimised.md
      07-final.md            hand-off to marketing
      08-qa.md
```

- **Slugs:** lowercase, hyphenated. `page-slug` is the last path segment of the URL (`/blog/product-lifecycle-management/` → `product-lifecycle-management`). For a new page (mode C), derive the slug from the primary keyword.
- **Pillar folder:** a page lives in the folder of the pillar it belongs to, according to the registry. The pillar page itself lives in `<pillar-slug>/<pillar-slug>/`.
- **Unassigned pages:** if a page has no pillar yet, use `<clusters_root>/_unassigned/<page-slug>/`. Move the folder when the architect assigns it, and record the move in `_system/changelog.md`.

## 3. Status frontmatter (every numbered file)

```yaml
---
step: 04-outline
page_slug: product-lifecycle-management
status: draft | awaiting-approval | approved | superseded
produced_by: sai-cc-outline
inputs: [01-brief.md, 03-audit.md]
updated: 2026-11-17
---
```

- A skill may only consume inputs whose status is `approved`, or `draft` for steps that have no checkpoint.
- Checkpoint files are `01-brief.md` (modes B/C), `04-outline.md`, `05-interview.md` and `07-final.md`. These need `approved` before the next step runs, unless the user explicitly says to continue.
- When re-running a step, overwrite the file and set `status: draft`. Then set the frontmatter of any downstream files to `status: superseded`, without deleting them.

## 4. Resume rule

A page's next step is the lowest-numbered file that is missing, `draft` at a checkpoint, `awaiting-approval`, or `superseded`. The order is: 01 → 02 → 03 → 04 → 05 → 06 → 07-optimised → 07-final → 08. Steps 02 and 03 are skipped in mode C, where `01-brief.md` frontmatter has `mode: C`.

## 5. Guardrails (apply in every skill)

- Never change, suggest changing, or invent a URL for an existing page. Never recommend redirects or consolidation as an action. Only flag them for human investigation.
- Never invent search volumes, keyword difficulty, rankings, traffic, dates or quotes. Copy them verbatim from a supplied source and cite the source. Otherwise write `not supplied`.
- Never publish, push or edit a live website. All output is a draft for review.
- Never write to the author bundle except through `sai-cc-okf-update`, after the user approves.
- Follow `cta_policy` from the config. With `educational-only`, add no product, programme or course promotion and no sign-up or counselling CTAs.
