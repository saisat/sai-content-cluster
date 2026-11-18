---
name: sai-cc-start
description: Single entry point for the sai-cc content-cluster system, which produces SEO/AEO-optimised pillar and cluster blog articles in the author's voice. Use when the user says "/sai-cc-start", "optimise this article", "work on this brief", "write a cluster article", "plan a pillar/topic cluster", "refresh this blog post for SEO/AEO", or "continue/resume <page>". Works with a marketing content brief, with only an existing URL, with only a topic, or to plan a whole cluster, and routes to the right pipeline.
argument-hint: "[brief path | URL | topic | page folder]"
---

# sai-cc-start: Entry Point and Orchestrator

You run the whole pipeline by invoking the other `sai-cc-*` skills in order, and you stop at checkpoints. `{core}` is the sibling `sai-cc-core` directory of this skill's base directory.

## 0. Preflight

1. Read `{core}/references/file-conventions.md` and `{core}/references/routing.md`.
2. Find `content-cluster.config.md` (file-conventions §1). If it's missing, say so in one line, invoke `sai-cc-setup`, then continue.
3. If the config's `author_bundle_path` is a git clone, run `git -C <path> pull --ff-only` quietly. If that fails (offline, or local changes), continue and note it.

## 1. Detect the mode

Apply routing.md "Detect the mode" to the arguments and the conversation. Ask at most one AskUserQuestion call (≤2 questions), and only if needed.

State the decision in one line, e.g. `Mode A — marketing brief → existing page product-lifecycle-management`.

## 2. Run the pipeline

Invoke each step with the Skill tool, passing the page folder path as the argument. Pipelines and checkpoints are in routing.md.

| Step | Skill |
|---|---|
| Normalise marketing brief | `sai-cc-brief-intake` |
| Build brief without one | `sai-cc-brief-builder` |
| Place page in cluster / plan cluster | `sai-cc-cluster-architect` |
| Audit live page | `sai-cc-article-audit` |
| Outline | `sai-cc-outline` |
| SME interview | `sai-cc-sme-interview` |
| Draft | `sai-cc-draft` |
| SEO/AEO pass | `sai-cc-seo-aeo` |
| Humanize | `sai-cc-humanize` |
| QA | `sai-cc-qa` |
| Apply approved bundle updates | `sai-cc-okf-update` |

Run `sai-cc-cluster-architect` (in `place` mode) right after the brief step whenever the page is missing from `_system/cluster-registry.md`.

## 3. Checkpoints

At each checkpoint (① brief in B/C, ② outline, ③ interview, ④ final), stop. Show:
- the file path
- a summary of at most 10 lines (for ②, the H2 list, the identity lens and the [SME] slots; for ④, word count, the QA verdict table and open items)
- one AskUserQuestion: Approve / Request changes / Stop here

On approve, set the file's `status: approved` and continue. On changes, re-invoke the responsible skill with the feedback, then return to the same checkpoint.

## 4. Close-out (after ④ is approved)

1. If `05-okf-proposals.md` has proposals, ask which to approve (multi-select), then invoke `sai-cc-okf-update`.
2. Update the page's row in `_system/cluster-registry.md` (article status `final`, link edges `in-draft`) and append one line to `_system/changelog.md`.
3. **Pillar only: draft all spoke briefs.** If the registry role of the approved page is `pillar`:
   1. Invoke `sai-cc-cluster-architect spokes <pillar-slug>`. It returns the spokes that need a brief and creates their folders.
   2. **Draft one spoke brief at a time (default).** Take the first spoke on the list and invoke `sai-cc-brief-builder` in **batch mode**. Pass the spoke folder, its mode (B for an existing URL, C for a gap), and the pillar's folder as context. You may run the SERP scan for all listed spokes up front and reuse it, but write only one brief per step.
   3. Leave the brief at `status: awaiting-approval` and update its registry row to `briefed (awaiting approval)`. Then **stop**. Show a summary of at most 10 lines: ownership, proposed metadata, H2 list, angle/gap, decisions needed from §23. End with: "Say **next** for the `<next-spoke>` brief, or give me changes to this one." Mention the next spoke's main flag if there is one.
   4. On "next", draft the following spoke's brief the same way. On changes, re-invoke `sai-cc-brief-builder` for this spoke with the feedback, then pause again. Keep going until the list is done or the user stops. "Draft the rest" (or similar) switches to drafting the remaining briefs back to back, with one line each: `✓ spoke brief → <folder>/01-brief.md (mode B|C, primary: "<kw>", <n> flags)`.
   5. Briefs drafted this way still go through checkpoint ① when that spoke's own run starts.
   If there are no spokes, or every spoke already has a brief, say so in one line.
   **Resume:** "next spoke brief for <pillar>" (or "continue spoke briefs") re-runs `architect spokes <pillar>` and drafts the first spoke that still has no brief.
4. Report: the path to `07-final.md`, the QA summary, open items for marketing, the spoke briefs drafted (if any), and the suggested next spoke. Suggest existing pages before gaps, and gaps whose `01-brief.md` §23 says volume is unvalidated last.

## Resume

For "continue <slug>" or a folder path, apply the resume rule (file-conventions §4) and restart at that step. Do not redo approved steps unless asked.

## Mode D

Invoke `sai-cc-cluster-architect` in `plan` mode. Show the cluster map summary and ask which page to start. Then run that page from its mini-brief (checkpoint ①).
