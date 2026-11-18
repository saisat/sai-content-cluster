---
name: sai-cc-seo-aeo
description: Apply the SEO, AEO and GEO optimisation pass to a sai-cc draft, producing 07-optimised.md with final metadata, answer-first definition, keyword placement, AEO-ready sections and FAQ, registry-verified internal links, author byline/bio, JSON-LD (BlogPosting + BreadcrumbList, FAQPage only when visible) and the hand-off appendices. Use when the user says "/sai-cc-seo-aeo", "optimise for SEO/AEO", or sai-cc-start reaches this step.
argument-hint: "<page folder>"
---

# sai-cc-seo-aeo

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md`, `seo-aeo-standards.md`, `schema-jsonld.md`, and `{core}/templates/final-article.md` (the target shape).

## Inputs

`06-draft.md`, `01-brief.md`, `_system/cluster-registry.md` (owned keywords, Must NOT target, link edges), `03-audit.md` (for the change log), the config (domain, author, publisher, bio source).

## Pass (edit with a light hand; this is optimisation, not a rewrite)

1. **Metadata:** finalise the SEO title, meta and H1 in the frontmatter, with character counts. Use the brief's values unless they break a hard limit. If so, keep the brief's value and add a compliant alternative in Appendix F.
2. **Definition:** make sure a 40–60 word answer-first definition sits directly under the H1 and byline.
3. **"In short" box:** 3–5 stand-alone takeaways near the top.
4. **Keyword placement:** check the primary keyword in the title, H1, definition and one H2/H3. Check each secondary keyword once. Add them only where natural. Make sure no heading targets a "Must NOT target" query that a sibling owns.
5. **Section openings:** check each H2's first 1–3 sentences answer its heading. Tighten them where they don't.
6. **Headings:** make them descriptive and close to how people phrase queries, without changing the brief's required headings beyond small wording fixes.
7. **Links:** check every planned internal link is present, uses a descriptive anchor, and points at a verified URL. Remove links to unverified URLs and list them in Appendix F. Pillar pages must link to every registry spoke that has a URL.
8. **Byline and bio:** add `*By <author_name> · Updated <date>*` under the H1. Add an "About the author" bio from the bio source. Use only verified, current facts per the bundle's freshness rules, and put `[VERIFY]` on anything time-sensitive.
9. **JSON-LD:** build it per schema-jsonld.md and place it in Appendix A. Copy the FAQ answers verbatim from the visible FAQ.
10. **Appendices B–F:** the links placed, the external references (with access dates), image/diagram alt texts, the change log vs `02-existing.md` (mode A/B; "new page" for C), and open items for marketing (TODO-verify values plus brief §21).

Write `07-optimised.md` (status `draft`).

## Output

`✓ seo-aeo → 07-optimised.md (title <n>ch, meta <n>ch, <n> internal links, schema: <types>)`
