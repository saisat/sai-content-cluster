---
name: sai-cc-okf-update
description: Apply author-approved proposals from 05-okf-proposals.md to the local clone of the author's OKF knowledge bundle, following the bundle's own AGENTS.md maintenance rules, updating index files and log.md, without committing or pushing. Use when the user says "/sai-cc-okf-update", "apply the bundle proposals", "update my OKF bundle", or sai-cc-start reaches close-out.
argument-hint: "<page folder>"
---

# sai-cc-okf-update

`{core}` is the sibling `sai-cc-core` directory. Read `okf-usage.md`. Then read the bundle's `AGENTS.md` (and its `README.md` maintenance section). **The bundle's rules override this skill.**

## Steps

1. Read `05-okf-proposals.md`. Act only on proposals marked `decision: approved`. If none are marked, ask the user which to approve (AskUserQuestion, multiSelect), and record their decisions in the file.
2. Check the clone: `git -C <bundle> status --porcelain`. If there are uncommitted changes that aren't yours, stop and tell the user. Don't mix your changes with theirs.
3. For each approved proposal:
   - **edit-concept:** make the smallest edit to the target file. Keep its frontmatter and update its timestamp field (whatever the bundle uses, e.g. `generated.at` or `timestamp`).
   - **new-concept:** create the file with frontmatter that matches the bundle's conventions. Copy the frontmatter keys from a sibling file, including `type`, `title`, `description`, `tags`, a status of `draft`, and source information pointing to the interview (`sources: [{id: interview, title: "<page-slug> SME interview <date>"}]`).
   - Add links from the relevant `index.md` files. Create a folder index if you're adding a new folder, and link it from the root `index.md`.
   - Never turn aspirations or hypotheses into facts. Never add personal or family details to a professional-only bundle.
4. Append to the bundle's `log.md` in its existing format: the date, what changed, and why ("from <page-slug> SME interview").
5. Show `git -C <bundle> diff --stat` and a short diff summary. **Don't commit or push.** Tell the user the exact commands to run if they want to (`git -C <bundle> add -A && git -C <bundle> commit -m "..." && git -C <bundle> push`).
6. Mark the applied proposals `decision: applied` in `05-okf-proposals.md`.

## Output

`✓ okf-update → <n> files changed in <bundle> (uncommitted); log.md updated`
