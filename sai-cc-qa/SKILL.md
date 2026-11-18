---
name: sai-cc-qa
description: Quality-gate a sai-cc final article (07-final.md) against its brief, SEO/AEO standards, the author's voice bundle, company brand rules and cluster ownership, writing a pass/fail scorecard to 08-qa.md with the step responsible for each failure. Use when the user says "/sai-cc-qa", "check this article", "QA the final", or sai-cc-start reaches the QA step.
argument-hint: "<page folder>"
---

# sai-cc-qa

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md`, `seo-aeo-standards.md`, `schema-jsonld.md`, `ai-tells-fallback.md` and every file in `{core}/references/rubrics/`.

## Checks

Run the mechanical checks with shell tools where you can (word count, grep, JSON parsing). Run the judgement checks by applying each rubric honestly. UNKNOWN is allowed.

| # | Check | How | Fix-step on fail |
|---|---|---|---|
| 1 | Brief compliance | `rubrics/brief-compliance.md`, which produces the requirement table | per row |
| 2 | Metadata limits | Title ≤60 characters, meta 140–160, a single H1 containing the primary keyword | seo-aeo |
| 3 | Keyword placement | Primary keyword in title/H1/first 100 words/one H2-H3; each secondary present; no "Must NOT target" query in a heading | seo-aeo |
| 4 | AEO structure | `rubrics/aeo-structure.md` | seo-aeo / outline |
| 5 | Authenticity | `rubrics/authenticity.md` | draft / sme-interview |
| 6 | Voice match | `rubrics/voice-match.md`, using the bundle files in `okf_loaded` | draft / humanize |
| 7 | Consistency | The same counts, names and terms everywhere (e.g. the stage count in headings, tables, diagram and FAQ) | draft |
| 8 | AI tells | Scan for `ai-tells-fallback.md` patterns. Fail if more than 3 instances in total, or any banned-vocabulary word | humanize |
| 9 | CTA policy | Under `educational-only`: grep for company/programme names outside the bio, and for "enrol", "sign up", "book a call", "counselling", "register", "join our", "download", "free trial". Any hit outside the bio fails | draft |
| 10 | Company "never say" | Check against the company context's prohibited positioning and phrasing | draft |
| 11 | Links | Internal URLs exist in the registry or site-urls and are `verified`; no duplicate anchors to different URLs; no links to a sibling's owned query with the wrong anchor | seo-aeo |
| 12 | Facts and sources | Every statistic has a source; no `[VERIFY` left without a matching Appendix F item; illustrative examples are labelled | draft |
| 13 | JSON-LD | Extract Appendix A and run `python3 -m json.tool`; FAQPage answers equal the visible answers; no invented values (only `TODO-verify` placeholders) | seo-aeo |
| 14 | Length | Within brief §19 (±5%) | draft |
| 15 | Humanizer safety | Diff the protected elements against `07-optimised.md` (headings, tables, links, keyword phrases) | humanize |

## Write `08-qa.md`

Frontmatter: `overall: PASS | FAIL`, `checks_failed: [n,…]`. Then:
1. a summary table (check → PASS/FAIL/UNKNOWN → evidence → fix-step)
2. the brief-compliance requirement table
3. items for the author to confirm: draft/time-sensitive bundle facts used, and any UNKNOWN verdicts

`overall: PASS` requires no FAIL in checks 1–3, 7, 9, 11 or 13, and at most one FAIL among the rest.

## Output

`✓ qa → 08-qa.md (<PASS|FAIL>; failed: <list or none>)`
