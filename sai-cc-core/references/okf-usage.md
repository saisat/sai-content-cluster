# Using the Author OKF Bundle

The author bundle is a directory of cross-linked Markdown files with YAML frontmatter (Open Knowledge Format). Its location comes from the config keys `author_bundle_path` and `author_bundle_entry`.

## Reading: progressive, minimal

1. **If the bundle has an `AGENTS.md` (or `README.md` with agent instructions), read it first and obey it.** It overrides this file wherever they differ.
2. Read the entry `index.md`, then the professional profile.
3. Read the communication-style or voice file. It is always needed for writing.
4. Read the beliefs/principles file when the article takes positions.
5. Read the identity index and choose the **identity lens**: 1–2 identities that fit the topic and audience. Read only those identity files.
   - Typical choices for educational product-management articles are a practitioner/educator identity plus a product-leadership identity. For AI topics, add the AI-focused identity.
   - Respect status flags. Never use an identity marked aspirational as evidence of established practice.
6. Read any `stories/` or `pov/` files whose tags match the topic, if they exist.
7. Record what you loaded in the step file's frontmatter: `okf_loaded: [paths]` and `identity_lens: [...]`.

Do not load every file. Do not quote the bundle verbatim in articles. Use it to shape voice, stance and what to ask.

## What the bundle is for in this pack

| Use | Where |
|---|---|
| Voice, rhythm, vocabulary, what to avoid | draft, humanize, qa voice-match |
| Stances and principles that the article's opinions must be consistent with | outline, draft |
| Facts about the author (roles, experience) for the byline and E-E-A-T | seo-aeo (bio), with facts verified per the bundle's freshness rules |
| Knowing what NOT to ask in interviews | sme-interview |

## Fact discipline

- Never invent author experiences, roles, numbers or stories. Anecdotes in an article must come from the interview (`05-interview.md`) or from a bundle story file, and must be attributed to the author.
- The bundle is shared across the author's projects, so treat it as read-only. Rejecting a proposal only keeps that content out of the bundle. Stories captured in any `05-interview.md` in this workspace can be reused in other articles here (search the workspace's interview files before asking again). Tell a different facet each time, and don't copy paragraphs between articles.
- Treat bundle files marked `draft`, and anything about current roles or organisations, as needing confirmation before publication. Flag them in `08-qa.md`.

## Proposing updates (`05-okf-proposals.md`)

The interview often surfaces new stories, sharper positions or corrections. Never edit the bundle directly. Write proposals instead:

```markdown
### P1 — new-concept | edit-concept
- target: stories/<slug>.md  (or an existing file path)
- reason: <what was learned, which interview answer>
- status-on-apply: draft
- frontmatter: {type: Story, title: ..., description: ..., tags: [...]}
- content: |
    <proposed body, in the author's own words from the interview>
- index-updates: <which index.md files need a link>
- decision: pending | approved | rejected
```
Follow the bundle's own maintenance rules: edit an existing concept rather than duplicate it, keep identity-specific material in identity files, log changes, and never promote aspirations to facts.
