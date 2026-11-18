---
name: sai-cc-core
description: Shared references and templates for the sai-cc content-cluster skill pack (brief schema, file conventions, SEO/AEO standards, JSON-LD templates, craft rules, rubrics). Not a workflow on its own; other sai-cc-* skills load files from here. Use /sai-cc-start to begin work.
user-invocable: false
---

# sai-cc-core

This skill holds the shared material for the `sai-cc-*` pack. It does nothing when invoked by itself. If someone invokes it, point them to `/sai-cc-start`.

## How other skills find this folder

Every `sai-cc-*` skill is installed next to this one. If a skill's base directory is `<skills>/sai-cc-draft`, this folder is `<skills>/sai-cc-core`. Paths written as `{core}/...` in the pack mean this directory.

## Contents

| File | Purpose | Loaded by |
|---|---|---|
| `references/file-conventions.md` | Config lookup, folder layout, file names, status frontmatter, resume rules | every skill |
| `references/brief-schema.md` | The canonical `01-brief.md` schema and heading-synonym map | brief-intake, brief-builder, all downstream |
| `references/routing.md` | Mode A/B/C/D/Resume detection | sai-cc-start |
| `references/seo-aeo-standards.md` | On-page SEO, AEO and GEO rules | outline, seo-aeo, qa |
| `references/schema-jsonld.md` | JSON-LD templates and rules | seo-aeo, qa |
| `references/craft-rules.md` | Long-form writing rules and voice-loading recipe | outline, draft, humanize |
| `references/ai-tells-fallback.md` | Built-in AI-tell checklist when the humanizer skill is absent | humanize, qa |
| `references/okf-usage.md` | How to read and propose updates to an author OKF bundle | outline, interview, draft, okf-update |
| `references/rubrics/*.md` | Grading prompts for QA | qa |
| `templates/*` | Config, registry, cluster map, brief, final article, URL inventory | setup, architect, intake, seo-aeo |
