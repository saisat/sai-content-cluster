# Routing (used by sai-cc-start)

## Detect the mode

Infer the mode from what the user already gave (in the invocation arguments or the conversation) before asking anything.

| Signal | Mode |
|---|---|
| A brief file or pasted brief (with or without a URL) | **A**: marketing brief → page (existing or new). If the brief names an existing URL, audit it. |
| A URL on the configured `site_domain`, no brief | **B**: self-built brief → existing page |
| A topic or keyword, no URL, no brief | **C**: self-built brief → new page |
| "plan a cluster", "pillar for X", or a list of several URLs/topics | **D**: cluster planning |
| A path to an existing page folder, or "continue/resume <slug>" | **Resume** |

Ask only when the signals conflict or are missing. Use one AskUserQuestion with at most two questions:
1. "What are you starting from?" Options: marketing brief / an existing article URL, no brief / a new topic, no brief / plan a whole cluster.
2. The URL, topic or brief path, if not already given (free text via "Other").

## Pipelines

```
A:      intake → [architect if not in registry] → audit* → outline ② → interview ③ → draft → seo-aeo → humanize → qa → final ④ → okf-update (if approved)
B:      brief-builder ① → [architect if needed] → audit → outline ② → interview ③ → draft → seo-aeo → humanize → qa → final ④ → okf-update
C:      brief-builder ① → [architect if needed] → outline ② → interview ③ → draft → seo-aeo → humanize → qa → final ④ → okf-update
D:      architect → cluster-map + mini-briefs (each `01-brief.md`, mode B or C, status awaiting-approval) → user picks a page → run B/C from outline
Resume: apply the resume rule in file-conventions.md §4
```
`*` In mode A, skip the audit when the brief targets a new page.

**Pillar close-out (A/B/C):** when the approved page's registry role is `pillar`, after the bundle update: `architect spokes <pillar>` → `brief-builder` (batch mode) for **one spoke at a time**, pausing after each brief for "next" or changes. "Draft the rest" switches to drafting the remaining briefs back to back. Every brief is left at `awaiting-approval`. Spoke briefs are approved at ① when each spoke's own run starts, so ① applies to batch-drafted briefs in every mode.
**Cluster close-out:** when every registry page for a pillar has an approved `07-final.md`, suggest `sai-cc-handoff <pillar>` (READ ME + approved finals + cluster map in one ready-to-share folder).
① ② ③ ④ are checkpoints: stop, show a short summary and ask for approval or answers. Set the file to `approved` only on an explicit yes. The user may say "run through without stopping" to skip ① and ②. ③ (the interview) and ④ are never skipped.

## Between steps

After each step, print one line: `✓ <step> → <file> (<one-line result>)`. At a checkpoint, print a summary of at most 10 lines and the file path, then ask. Do not paste whole files into chat.

## Before step QA passes

If `08-qa.md` has any FAIL, loop back once to the responsible step (the QA file names it), fix it, and re-run QA. If it still fails, present the failures to the user at checkpoint ④ rather than looping again.
