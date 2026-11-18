# Craft Rules for Long-Form Articles

These apply to the outline, draft and humanize steps. The brief and the author bundle's communication style override them where they conflict.

## Voice

- Write as the author, in the voice described by the bundle's communication-style file and the chosen identity lens. Default register: a conversational expert who explains complex ideas plainly without diluting them, and speaks to experienced professionals with respect.
- The first person is allowed and encouraged for experience ("When I've run sunset reviews…"), but only for experiences in `05-interview.md` or bundle story files.
- Take positions. Where practitioners disagree, say what you would do and why, consistent with the bundle's beliefs file.
- Use the configured spelling (UK or US) throughout, including in headings.

## Structure

- The answer comes first in every section (see seo-aeo-standards.md). Context, nuance and examples follow.
- Vary section shape. Not every H2 should follow intro → bullets → tip. Mix prose, a table, a short scenario and a decision rule.
- Paragraphs are 1–4 sentences. Use a list only for genuinely parallel items. Use a table when comparing two or more things across two or more attributes.
- Each H2 should give the reader something they can use: a decision rule, a question to ask, a metric with its definition, or a common mistake and what to do instead.

## Examples

- Label hypothetical examples clearly as illustrative ("Illustrative example: …"). Never present an invented company, number or outcome as real.
- Prefer one worked example that runs through the article over many shallow ones.
- If physical-product and digital-product practices differ, say so once and explain the difference.

## Diagrams

- Write diagrams as Mermaid code blocks (`flowchart LR` for lifecycles and processes). Add a one-line caption and an alt-text suggestion, e.g. `<!-- alt: ... -->`.
- Diagrams must show the real relationships, such as loops back to earlier stages. Don't draw a decorative linear arrow chain where the process actually iterates.

## Sources and claims

- Every statistic or external claim needs a dated source from the brief's references or one you verified. If unverified, remove the claim or mark it `[VERIFY: …]` for the QA step to flag.
- No unsupported claims about software capabilities, market sizes or "studies show".

## Never

- CTAs or promotion when `cta_policy: educational-only`. Company and programme names may appear only in the author bio.
- Copying explanations from sibling pages in the cluster. Link to them instead.
- Openers like "In today's fast-paced world", rhetorical-question hooks, and one-line moral closers at the end of sections.
- Filler transitions ("Let's dive in", "Now that we've covered X…").
