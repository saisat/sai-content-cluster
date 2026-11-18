#!/usr/bin/env python3
"""Build a marketing hand-off package for one pillar cluster.

Usage:
  python3 build_handoff.py <clusters_root> <pillar_slug> [--date YYYY-MM-DD]

Reads _system/cluster-registry.md and each page folder's 07-final.md.
Writes <clusters_root>/<pillar>/_handoff/<date>/ containing only:
  00 READ ME - Marketing hand-off.md   (copied from <pillar>/marketing-handoff.md)
  NN PILLAR|SPOKE - <Title>.md          (one per approved final article)
  NN Cluster map.md                     (generated from the registry)
  manifest.json                         (file, title, sha256)
Interim files (briefs, audits, outlines, interviews, drafts, QA) are never copied.
Exits non-zero, listing the problems, if a page has no approved 07-final.md
or the README is missing or older than any final.
"""
import datetime, hashlib, json, os, re, sys


def table_rows(text, heading):
    """Rows of the first pipe table under a '## heading' line, as lists of cells."""
    m = re.search(r'^## ' + re.escape(heading) + r'\s*$(.*?)(?=^## |\Z)', text, re.M | re.S)
    if not m:
        return []
    rows = [l for l in m.group(1).splitlines() if l.startswith('|')]
    out = []
    for l in rows[2:]:  # skip header + separator
        out.append([c.strip() for c in l.strip().strip('|').split('|')])
    return out


def frontmatter(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r'([a-z0-9_]+):\s*(.*)$', line)
            if mm:
                val = re.sub(r'\s+#.*$', '', mm.group(2)).strip().strip('"')
                fm[mm.group(1)] = val
    return fm, (text[m.end():] if m else text)


def short_title(fm, slug):
    t = fm.get('seo_title') or slug.replace('-', ' ').title()
    return t.split(':')[0].strip()


def clean_article(fm, body, label):
    # HTML comments -> visible notes; hand-off marker -> heading
    body = body.replace('<!-- ===== HAND-OFF APPENDIX (not for publication) ===== -->',
                        '---\n\n# Hand-off notes (not for publication)')
    body = re.sub(r'<!--\s*([a-z][a-z ]*):\s*(.*?)\s*-->', lambda m: f'*{m.group(1).capitalize()}: {m.group(2)}*', body, flags=re.S)
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    rows = [
        ('Article type', label),
        ('URL', fm.get('url', '')),
        ('SEO title', fm.get('seo_title', '')),
        ('Meta description', fm.get('meta_description', '')),
        ('H1', fm.get('h1', '')),
        ('Primary keyword', fm.get('primary_keyword', '')),
        ('Secondary keywords', fm.get('secondary_keywords', '').strip('[]')),
        ('Schema', fm.get('schema', '').strip('[]')),
        ('Approved', fm.get('approved', '')),
    ]
    head = '## Publishing details\n\n| Field | Value |\n|---|---|\n' + '\n'.join(
        f'| {k} | {v.replace("|", "/")} |' for k, v in rows if v) + '\n\n---\n\n'
    return head + body.strip() + '\n'


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__); sys.exit(2)
    root, pillar = args[0], args[1]
    date = datetime.date.today().isoformat()
    if '--date' in args:
        date = args[args.index('--date') + 1]
    reg = open(os.path.join(root, '_system', 'cluster-registry.md')).read()
    pages = [r for r in table_rows(reg, 'Pages') if len(r) >= 8 and r[2] == pillar]
    edges = [r for r in table_rows(reg, 'Link edges') if len(r) >= 5]
    problems, items = [], []
    for r in pages:
        slug, url, _, role, owns, not_target, status, folder = r[:8]
        final = os.path.join(root, pillar, slug, '07-final.md')
        if not os.path.exists(final):
            problems.append(f'{slug}: no 07-final.md'); continue
        fm, body = frontmatter(open(final).read())
        if fm.get('status') != 'approved':
            problems.append(f'{slug}: 07-final.md status is {fm.get("status")!r}, not approved'); continue
        is_pillar = role.startswith('pillar')
        new = 'new' in url or 'new' in fm.get('url', '')
        notrec = 'do not' in status or 'not recommended' in role
        tags = []
        if new: tags.append('new page')
        if notrec: tags.append('not recommended')
        label = ('PILLAR' if is_pillar else 'SPOKE') + (f' [{", ".join(tags)}]' if tags else '')
        items.append(dict(slug=slug, url=url, role=role, owns=owns, not_target=not_target, status=status,
                          is_pillar=is_pillar, new=new, notrec=notrec, label=label, fm=fm, body=body,
                          title=short_title(fm, slug), mtime=os.path.getmtime(final)))
    readme = os.path.join(root, pillar, 'marketing-handoff.md')
    if not os.path.exists(readme):
        problems.append('marketing-handoff.md missing: write it first (sai-cc-handoff step 2)')
    elif items and os.path.getmtime(readme) < max(i['mtime'] for i in items):
        problems.append('marketing-handoff.md is older than a 07-final.md: refresh it first')
    if problems:
        print('NOT BUILT:\n- ' + '\n- '.join(problems)); sys.exit(1)

    # order: pillar, existing spokes, new spokes, not-recommended last
    items.sort(key=lambda i: (not i['is_pillar'], i['new'], i['notrec']))
    out = os.path.abspath(os.path.join(root, pillar, '_handoff', date))
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(os.path.join(out, f))
    manifest = []

    def write(name, content, kind):
        p = os.path.join(out, name + '.md')
        open(p, 'w').write(content)
        manifest.append(dict(title=name, file=p, kind=kind,
                             sha256=hashlib.sha256(content.encode()).hexdigest()))

    write('00 READ ME - Marketing hand-off', open(readme).read(), 'readme')
    for n, i in enumerate(items, 1):
        i['doc'] = f'{n:02d} {i["label"]} - {i["title"]}'
        write(i['doc'], clean_article(i['fm'], i['body'], i['label']), 'article')

    # cluster map from the registry
    cm_path = os.path.join(root, pillar, 'cluster-map.md')
    scope = ''
    if os.path.exists(cm_path):
        m = re.search(r'^## Scope\s*$(.*?)(?=^## |\Z)', open(cm_path).read(), re.M | re.S)
        scope = m.group(1).strip() if m else ''
    slugs = {i['slug']: i for i in items}
    node = {s: f'N{k}' for k, s in enumerate(slugs)}
    mer = ['```mermaid', 'flowchart TD']
    for s, i in slugs.items():
        mer.append(f'  {node[s]}["{"PILLAR" if i["is_pillar"] else "Spoke"}: {i["title"]}{" (new)" if i["new"] else ""}"]')
    others, seen = {}, set()
    for e in edges:
        a, b = e[0], e[1]
        if a in slugs and b in slugs:
            pair = frozenset((a, b))
            if pair not in seen:
                seen.add(pair)
                mer.append(f'  {node[a]} --- {node[b]}')
        elif a in slugs and b not in slugs and e[3] == 'cross-pillar' and b not in others:
            others[b] = f'X{len(others)}'
            mer.append(f'  {node[a]} -.-> {others[b]}["Related: {b.replace("-", " ")}"]')
    mer.append('```')
    pg = '| Doc | Role | URL | Owns (primary; secondaries) | Must not target | Status |\n|---|---|---|---|---|---|\n' + '\n'.join(
        f'| {i["doc"]} | {i["label"]} | {i["url"]} | {i["owns"]} | {i["not_target"]} | {i["status"]} |' for i in items)
    def name(s):
        return slugs[s]['doc'] if s in slugs else f'/blog/{s}/ (other cluster)'
    def stat(s):
        s = s.replace('in-draft (target unpublished)', 'in the article; target page not live yet')
        s = s.replace('in-draft', 'in the article')
        return s
    le = '| From | To | Anchor | Type | Status |\n|---|---|---|---|---|\n' + '\n'.join(
        f'| {name(e[0])} | {name(e[1])} | {e[2]} | {e[3]} | {stat(e[4])} |' for e in edges if e[0] in slugs or e[1] in slugs)
    cmap = (f'# {items[0]["title"] if items else pillar}: Cluster Map\n\n'
            f'*Generated from the cluster registry on {date}.*\n\n'
            + (f'## Scope\n\n{scope}\n\n' if scope else '')
            + '## Map\n\n' + '\n'.join(mer) + '\n\n## Pages\n\n' + pg
            + '\n\n## Internal link plan\n\nAdd a link only once both pages are live.\n\n' + le + '\n')
    write(f'{len(items) + 1:02d} Cluster map', cmap, 'cluster-map')
    json.dump(manifest, open(os.path.join(out, 'manifest.json'), 'w'), indent=1)
    print(f'BUILT {out}')
    for m in manifest:
        print(f'- {m["title"]}  ({m["kind"]})')


if __name__ == '__main__':
    main()
