# Canonical Brief Schema (`01-brief.md`)

Every mode produces a brief in this exact shape. Downstream skills read sections by these headings. Use `not supplied` for anything missing; never fill a gap with a guess. Keep numbers verbatim with their source.

## Frontmatter

```yaml
---
step: 01-brief
page_slug: <slug>
pillar_slug: <slug or unassigned>
mode: A | B | C              # A = marketing brief, B = no brief + existing URL, C = new page
source: marketing | self-generated
source_file: 00-brief-source.md   # mode A only
url: <existing URL or "new page">
brief_date: <date stated in the brief, or not supplied>
status: draft | awaiting-approval | approved
approval_boundary: <verbatim from brief, or "Draft for review only. No URL changes, redirects, consolidation or publishing.">
updated: <today>
---
```

## Sections (in this order)

| # | Heading | Contents |
|---|---|---|
| 1 | `## 1. Objective` | What the page must do. For existing pages, state that the URL is preserved. |
| 2 | `## 2. Keywords` | Table: `Type (primary/secondary/supporting) | Keyword | Volume | KD | Evidence | Source`. Exactly one primary. |
| 3 | `## 3. Search Intent` | Intent type plus ambiguities (e.g. a term that also means a software category). |
| 4 | `## 4. Audience and Problems` | Who the page is for, and the problems in their words. |
| 5 | `## 5. Current Performance` | Verbatim metrics with source and date window. Mode C: `not applicable`. |
| 6 | `## 6. Competitors and Gaps` | Who ranks, what they cover, and the gaps to exploit. Note the geography of the data. |
| 7 | `## 7. Existing Content Assessment` | Strengths and weaknesses of the current page. Mode C: `not applicable`. |
| 8 | `## 8. Cannibalisation and Ownership` | Overlapping URLs, which page owns which query, and the guardrail. |
| 9 | `## 9. Metadata` | Table: SEO title, meta description, H1, with character counts. |
| 10 | `## 10. Required Structure` | H2/H3 skeleton plus per-section notes, exactly as the brief requires. |
| 11 | `## 11. Writer Instructions` | Bullet list of must/must-not rules. |
| 12 | `## 12. Entities and Terms` | Comma list. Mark which must be defined. |
| 13 | `## 13. Required Assets` | Tables, diagrams, examples and templates the page must contain. |
| 14 | `## 14. FAQs` | Table: `Question | Answer direction`. |
| 15 | `## 15. AEO / GEO Notes` | Answer-first, citation and entity requirements. |
| 16 | `## 16. Schema` | Required and conditional types. |
| 17 | `## 17. Internal Links` | Table: `URL | Anchor | Purpose / guardrail`. Mark each URL as `verified` (supplied by marketing or in site-urls.csv) or `unverified`. |
| 18 | `## 18. External References` | Table: `Source | URL | Use`. |
| 19 | `## 19. Length` | Target range and the reasoning for it. |
| 20 | `## 20. Editorial Checklist` | Checkbox list. Used by sai-cc-qa. |
| 21 | `## 21. Post-Publish SEO Checklist` | Checkbox list for marketing, such as confirming in the CMS and monitoring CTR. Not checked by QA. |
| 22 | `## 22. Data Limitations` | Caveats from the source brief, verbatim or tightly paraphrased. |
| 23 | `## 23. Missing or Unverified (system)` | Added by the system: every field that was `not supplied`, every claim needing verification, and every conflict found inside the brief. |

## Heading synonym map (for intake of varied briefs)

| Canonical | Common source headings |
|---|---|
| 1 Objective | "Existing URL and optimisation objective", "Goal", "Purpose", "Brief summary" |
| 2 Keywords | "Primary keyword", "Secondary / supporting / long-tail keywords", "Keyword targets", "Target queries" |
| 3 Search Intent | "Intent", "User intent", "SERP intent" |
| 4 Audience | "Target audience", "Persona", "User problems", "Pain points" |
| 5 Current Performance | "Current SEO performance", "GSC data", "Baseline", "Ranking opportunities" |
| 6 Competitors | "Competitor analysis", "SERP analysis", "Content gap" |
| 7 Existing Content | "Strengths and weaknesses", "Content audit", "Current page" |
| 8 Cannibalisation | "Keyword cannibalisation", "URL ownership", "Overlap" |
| 9 Metadata | "SEO metadata", "Title tag", "Meta description", "H1" |
| 10 Structure | "H2/H3 structure", "Outline", "Content structure" |
| 11 Writer Instructions | "Section-by-section instructions", "Guidelines", "Do / Don't" |
| 12 Entities | "Entities", "Concepts and terminology", "NLP terms" |
| 13 Assets | "Examples, templates and comparison assets", "Visuals", "Media" |
| 14 FAQs | "FAQ questions and recommended answers", "PAA" |
| 15 AEO/GEO | "AEO and GEO recommendations", "AI search", "LLM visibility" |
| 16 Schema | "Schema recommendations", "Structured data" |
| 17 Internal Links | "Internal linking recommendations" |
| 18 External | "External reference recommendations", "Sources", "Citations" |
| 19 Length | "Recommended content length", "Word count" |
| 20 Editorial | "Editorial quality checklist" |
| 21 Post-Publish | "Final SEO quality-control checklist", "QA checklist" (items about the CMS, GSC or monitoring) |
| 22 Limitations | "Data quality and research limitations", "Caveats", "Approval boundary" |

If a source section mixes concerns, split it across canonical sections and note the split in section 23. If a source section fits nowhere, put it under section 11 as `Additional instruction (source: <heading>)`. Never drop content.
