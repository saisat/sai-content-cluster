---
name: sai-cc-brief-builder
description: Build a content brief from scratch, in the sai-cc canonical 01-brief.md schema, when there is no marketing brief. Works for an existing URL (mode B) or a new topic (mode C), using SERP/competitor research, optional GSC/SEMrush exports, the cluster registry and a few targeted questions. Use when the user says "/sai-cc-brief-builder", "no brief", "make a brief for this URL/topic", or sai-cc-start runs mode B or C.
argument-hint: "<URL or topic> [exports...]"
---

# sai-cc-brief-builder

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md`, `brief-schema.md` and `seo-aeo-standards.md` from `{core}/references/`, and the config's `company_context`.

The output must be as useful as a marketing brief but **honest about evidence**. Every number comes from a supplied export or is `not supplied`. Research findings are labelled with their source and the access date.

## Inputs

- **Mode B:** an existing URL. Fetch it with defuddle (`defuddle parse <url> --markdown`), or WebFetch / the web-fetch agent if defuddle is missing. Save it to `02-existing.md` now, so the audit can reuse it.
- **Mode C:** a topic or keyword.
- **Optional:** GSC / SEMrush / Ahrefs exports (CSV/XLSX). Filter the rows to this URL or topic, and quote them with their filename.

## Steps

1. **Ask 3–4 questions in one AskUserQuestion call.** Skip any whose answer is obvious from the context.
   - Primary query to own: propose 2–3 candidates from the page title/H1 or topic.
   - Audience level: aspiring / practising / senior.
   - What should a reader be able to do afterwards?
   - Any performance data or exports to attach?
2. **SERP and competitor scan.** Use WebSearch on the primary query and 2–3 variants. For the top 5 organic results, note the page type, angle, H2 coverage and anything distinctive. Note "People also ask"-style questions where they're visible. Label the results `source: WebSearch <date>, geography unconfirmed`.
3. **Keyword family.** Build the primary keyword, 3–6 secondary keywords (variants, "what is", "process", "vs" forms) and 3–5 long-tail/supporting keywords from the SERP, the exports and the topic. Leave Volume/KD as `not supplied` unless an export provides them.
4. **Cluster check.** Read `_system/cluster-registry.md`. List pages that might overlap, the proposed ownership, and the internal link targets. Only registry or site-urls URLs count as `verified`.
5. **Existing content assessment** (mode B): a quick view of strengths and weaknesses from `02-existing.md`. The full audit comes later.
6. **Write every schema section.** Propose the metadata (§9), an H2/H3 structure (§10) that covers the competitor gaps, writer instructions (§11, including disambiguation needs), entities (§12), assets (§13), 5–8 FAQs (§14), and 2–4 authoritative external references found in the scan (§18). Give a length range with its reasoning (§19).
7. **Frontmatter:** `mode: B|C`, `source: self-generated`, `status: awaiting-approval`. Fill §23 honestly.

## Batch mode (spoke briefs after a pillar is approved)

Used when `sai-cc-start` drafts every spoke brief for an approved pillar. The steps are the same, with these differences:

1. **No questions.** Skip step 1. Derive the answers instead:
   - primary keyword: from the spoke's registry or cluster-map row
   - audience level and reader outcome: from the pillar's `01-brief.md` §4
   - exports: whatever the user already attached in this workspace
   Record every derived answer in §23 as `assumed (batch mode)`, so it's reviewed when the spoke is started.
2. **Pillar context.** Read the pillar's `01-brief.md` and `07-final.md`. Then:
   - §8 must state what this spoke owns versus the pillar, using the registry's `Must NOT target` entries.
   - §17 must include the spoke→pillar link with the pillar's owned anchor, plus 1–2 sibling-spoke links from the cluster map.
   - §11 must tell the writer to summarise and link to the pillar, not repeat it. List the pillar sections that overlap with this spoke.
3. **Bounded research.** WebSearch on the primary query plus 1 variant (not 2–3), and the top 5 results only. For mode B, fetch the existing page as usual.
4. **Status** `awaiting-approval`. If the spoke came from the cluster map's Gaps table with no validated volume, put this at the top of §23: `Volume not validated. Confirm the topic in SEMrush before starting this spoke.`

## Output

Print `✓ brief-builder → <path>/01-brief.md (primary: "<kw>", <n> H2s, <n> FAQs, evidence: SERP <date>[, exports])`. The orchestrator then runs checkpoint ①.
