---
name: sai-cc-setup
description: One-time (re-runnable) workspace setup for the sai-cc content-cluster skill pack. Creates content-cluster.config.md, scaffolds the topic-clusters/_system folder (registry, URL inventory, changelog), clones or pulls the author's OKF bundle, and checks dependencies (humanizer skill, defuddle, pandoc, git). Use when the user says "/sai-cc-setup", "set up content cluster", or when another sai-cc skill can't find the config.
---

# sai-cc-setup

`{core}` is the sibling `sai-cc-core` directory of this skill's base directory.

## 1. Detect existing setup

Look for `content-cluster.config.md` in the cwd and its parents. If found, read it, validate it (step 4) and report. Change only what the user asks to change. Setup is safe to re-run.

## 2. Gather values (ask only what you can't infer)

Infer first:
- `company_context`: look for files such as `*company*.md` or `product-marketing.md` in the cwd or its parent.
- `site_domain`: from any brief or URL in the workspace.
- `spelling`: from the company context or a brief, e.g. "optimise" means UK.

Then use one AskUserQuestion (≤4 questions) for what's still unknown, from:
1. Company context file path, and the company/publisher name
2. Site domain + blog base path
3. Author bundle: git URL, or a local path, plus the entry index path inside it
4. CTA policy (educational-only / light / distributed) and spelling

## 3. Write files

1. Copy `{core}/templates/config.md` to `<workspace>/content-cluster.config.md` and fill it in. Set `setup_date` to today.
2. Create `<clusters_root>/_system/` with:
   - `cluster-registry.md` from the template
   - `site-urls.csv` from the template, header only, unless the user supplies an inventory
   - `changelog.md` with the heading `# Changelog` and the first line `<date> setup`
3. Author bundle:
   - If a git URL is given and `author_bundle_path` doesn't exist, run `git clone <repo> <path>`. If it exists, run `git -C <path> pull --ff-only`.
   - Verify that `author_bundle_entry` exists. If not, list the `index.md` files found and ask which one is the entry.
   - Never commit or push to the bundle.

## 4. Validate dependencies

Check each one and record the result in the config's "Dependency status" table:

| Dependency | Check | Fallback |
|---|---|---|
| Humanizer skill | Is `humanizer_skill` in the available-skills list? | Set `humanizer_skill: fallback`, which uses `{core}/references/ai-tells-fallback.md` |
| defuddle CLI | `command -v defuddle` | WebFetch / web-fetch agent extraction, or pasted HTML |
| pandoc | `command -v pandoc` | docx skill if available; otherwise ask for a .md export |
| git | `command -v git` | manual bundle path |
| python3 | `command -v python3` | JSON-LD validated by careful inspection (flagged in QA) |

Offer install commands for missing tools (`npm i -g defuddle`, `brew install pandoc`), but don't run them without the user's approval.

## 5. Report

Print the config path, the bundle status (cloned/pulled/at which commit), the dependency table, and "Next: `/sai-cc-start`".
