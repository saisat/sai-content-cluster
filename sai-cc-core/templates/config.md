---
# content-cluster.config.md — one per workspace, at the workspace root.
# Relative paths resolve against THIS file's directory.
company_context: ./company.md            # brand voice, audience, "never say" rules
company_name: Example Co                 # publisher name for JSON-LD
site_domain: www.example.com
blog_base_path: /blog/
clusters_root: ./topic-clusters
spelling: UK                             # UK | US
cta_policy: educational-only             # educational-only | light | distributed
author_name: Author Name
author_bio_source: bundle                # bundle | path/to/bio.md
author_bundle_repo: https://github.com/<user>/<repo>.git
author_bundle_path: ../ABOUT_AUTHOR      # local clone (sai-cc-setup clones/pulls it)
author_bundle_entry: path/inside/repo/index.md
humanizer_skill: humanizer:humanizer     # skill name to invoke; "fallback" uses the built-in checklist
setup_date: YYYY-MM-DD
---

# Content Cluster Config

Edit the frontmatter above. Re-run `/sai-cc-setup` to validate it.

## Dependency status (written by sai-cc-setup)

| Dependency | Status | Fallback in use |
|---|---|---|
