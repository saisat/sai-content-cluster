---
name: sai-cc-cluster-architect
description: Design and maintain pillar/topic-cluster architecture for the sai-cc system. "spokes" mode lists the spokes needing briefs after a pillar is approved; "place" mode slots a page into the workspace cluster registry (pillar or spoke, owned keywords, cannibalisation, link edges); "plan" mode designs a full pillar cluster from a topic or URL set, writing a cluster map and mini-briefs. Use when the user says "/sai-cc-cluster-architect", "plan a pillar", "topic cluster", "which page owns this keyword", "cannibalisation", "internal link plan", or sai-cc-start needs a page placed.
argument-hint: "place <page folder> | plan <topic or URLs> | spokes <pillar-slug>"
---

# sai-cc-cluster-architect

`{core}` is the sibling `sai-cc-core` directory. Read `file-conventions.md` and `seo-aeo-standards.md` (internal-link rules), plus the config's `company_context` for the audience and positioning.

Everything you write is a **proposal** (`status: proposed`) until the marketing team approves it. You never recommend redirects, merges or URL changes as actions. Overlaps go on the cannibalisation watchlist as `investigate`.

## Inputs (whatever exists)

- `_system/cluster-registry.md`, `_system/site-urls.csv`
- all `01-brief.md` files under `clusters_root`; their §8 (ownership) and §17 (links) are the strongest evidence
- exports the user supplies (GSC query/page rows, SEMrush positions)
- WebSearch, only to check what a SERP rewards, and labelled as such

## place mode (one page)

1. Read the page's `01-brief.md`.
2. Decide its role:
   - **Pillar:** a broad head term that many subtopics hang from, which the site wants to own.
   - **Spoke:** a specific subtopic, comparison, how-to or "for X" page.
   - **Support:** a related page that links into the cluster but belongs to another pillar.
   - If the right pillar doesn't exist, propose one and mark it `proposed`.
3. Assign owned keywords: primary + secondaries. Check every other registry row for the same or near-identical primary keyword. Write any conflict to the watchlist with its evidence, and add a `Must NOT target` entry to each side.
4. Add link edges from brief §17 and the role rules: spoke→pillar (required); pillar→spoke; 1–2 spoke↔spoke where the topics touch.
5. Move the folder if the pillar changed, and record it in `_system/changelog.md`.
6. Update or create `<pillar>/cluster-map.md` from the template (Mermaid map + pages table).

## plan mode (whole cluster)

1. Define the pillar scope: what's in, what's out.
2. Generate candidate spokes from: subtopics in the brief and its competitors, SERP "people also ask" questions, the buyer/learner journey (awareness → how-to → comparison → application), existing site URLs, and the author's expertise areas (from the bundle's expertise file, if configured).
3. Score each candidate 1–5 on: audience need (40%), fit with the site's expertise (30%), search evidence (20%), effort (10%). Show the scores.
4. Map existing URLs to spokes first (optimise before creating). New spokes become `mode C` candidates.
5. For each chosen page, write a mini-brief `01-brief.md` (status `awaiting-approval`) in its folder. Fill §1, §2 (keywords, with `not supplied` volumes), §3, §8, §10 (H2s only) and §17. Leave the other sections for the brief-builder to complete when the page is started.
6. Write the cluster map and registry rows.

## spokes mode (after a pillar is approved)

Called by `sai-cc-start` at close-out with `spokes <pillar-slug>`. It prepares the list of spoke briefs to draft; it doesn't write the briefs itself.

1. Read `<pillar>/cluster-map.md` and the registry. Collect:
   - every registry page with `pillar = <pillar-slug>` and role `spoke` (existing URLs → mode B)
   - every row in the cluster map's "Gaps" table (new pages → mode C), excluding rows the user or marketing marked `rejected` or `skip`
2. Skip any spoke whose folder already has a `01-brief.md` with status `approved`, or with `source: marketing` (a marketing brief always wins). Leave an `awaiting-approval` self-built brief alone unless the pillar's brief or outline has changed since it was written. In that case, mark it `superseded` and include the spoke.
3. For each remaining spoke, create its folder at `<pillar-slug>/<spoke-slug>/`. Add a registry row if it's missing (role `spoke`, status `not-started`, a proposed primary keyword from the cluster map). Make sure a spoke→pillar link edge exists, using the pillar's owned primary keyword as the anchor.
4. Return a list: `spoke-slug | folder | mode (B/C) | url or "new page" | proposed primary keyword | priority`. Order it with existing pages first, then gaps by priority.

## Output

`✓ cluster-architect (<mode>) → registry + <pillar>/cluster-map.md (<role> | <n> spokes | <n> watchlist items)`
