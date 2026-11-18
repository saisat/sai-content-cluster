# JSON-LD Rules and Templates

## Rules

- Always include **BlogPosting** (or Article) and **BreadcrumbList**, combined in one `@graph`.
- Include **FAQPage** only if the FAQ is visible on the page and the JSON answers match the visible answers word for word.
- Include **HowTo** only if the page contains a genuine numbered procedure the reader performs. Never add it to chase rich results.
- Use only values you know: the URL, the title and meta from the final article, the author from the bio source, and the publisher from the company context. Use `"TODO-verify"` for unknowns such as image URLs and `datePublished` for existing pages. Never invent them.
- `dateModified` = the date the final article is produced.
- The JSON must parse. QA runs `python3 -m json.tool` on it.

## Template

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "{url}#article",
      "headline": "{h1}",
      "description": "{meta_description}",
      "mainEntityOfPage": {"@type": "WebPage", "@id": "{url}"},
      "author": {"@type": "Person", "name": "{author_name}", "url": "{author_url_or_TODO-verify}"},
      "publisher": {"@type": "Organization", "name": "{publisher_name}", "logo": {"@type": "ImageObject", "url": "TODO-verify"}},
      "image": "TODO-verify",
      "datePublished": "TODO-verify",
      "dateModified": "{today}",
      "about": [{"@type": "Thing", "name": "{primary_entity}"}],
      "keywords": "{primary}, {secondary_comma_list}"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://{site_domain}/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://{site_domain}{blog_base_path}"},
        {"@type": "ListItem", "position": 3, "name": "{short_title}", "item": "{url}"}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "{q1}", "acceptedAnswer": {"@type": "Answer", "text": "{a1_verbatim}"}}
      ]
    }
  ]
}
```
Delete the FAQPage node if its condition isn't met.
