#!/usr/bin/env python3
"""Static site builder for childrensbooks.ie (GitHub Pages).

Reads content/*.md and content/*.html (simple "key: value" front matter, then ---, then body)
and writes clean-URL pages (slug/index.html), sitemap.xml, robots.txt, 404.html.

    python3 tools/build.py          # build
    python3 tools/build.py --check  # build, then verify every internal link and image exists
"""
import glob
import html
import json
import os
import re
import sys

import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SITE = "https://www.childrensbooks.ie"
NAME = "childrensbooks.ie"
TODAY = "2026-11-06"
OG_IMAGE = "/assets/img/og-image.png"
LOCALE = "en_IE"

NAV = [
    ("Books by age", "/books-by-age/"),
    ("Irish books", "/irish-childrens-authors/"),
    ("Bedtime", "/bedtime-stories-for-children/"),
    ("Top 20", "/top-20-childrens-books/"),
    ("Christmas", "/best-christmas-books-for-children/"),
    ("Guides", "/guides/"),
    ("About", "/about/"),
]

FOOT_AGES = [
    ("Babies and toddlers (0–2)", "/books-for-babies-and-toddlers/"),
    ("Preschoolers (3–5)", "/books-for-preschoolers/"),
    ("Early readers (6–8)", "/books-for-early-readers/"),
    ("Middle grade (9–12)", "/books-for-middle-grade-readers/"),
]
FOOT_IRISH = [
    ("Children’s book authors", "/childrens-book-authors/"),
    ("Irish children’s authors", "/irish-childrens-authors/"),
    ("Irish-language books", "/irish-language-childrens-books/"),
    ("Irish myths and legends", "/irish-myths-and-legends-for-children/"),
    ("Bedtime stories", "/bedtime-stories-for-children/"),
    ("Books about feelings", "/books-about-feelings-for-children/"),
    ("Gift guide", "/childrens-book-gift-guide/"),
    ("Top 20 children’s books", "/top-20-childrens-books/"),
    ("Christmas books", "/best-christmas-books-for-children/"),
    ("Christmas Eve box", "/christmas-eve-box-and-bedtime-stories/"),
    ("Irish Christmas", "/irish-christmas-books-and-traditions/"),
]
FOOT_GUIDES = [
    ("All guides", "/guides/"),
    ("How to choose a book", "/how-to-choose-a-childrens-book/"),
    ("Reading aloud", "/how-to-read-aloud-to-children/"),
    ("Reluctant readers", "/how-to-help-a-reluctant-reader/"),
    ("Home library on a budget", "/build-a-childrens-home-library-on-a-budget/"),
    ("Joining the library", "/childrens-books-and-your-local-library/"),
]


def esc(s):
    return html.escape(s, quote=True)


def read_front(path):
    raw = open(path, encoding="utf-8").read()
    head, _, body = raw.partition("\n---\n")
    meta = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    meta["_body"] = body.strip() + "\n"
    meta["_file"] = path
    return meta


_svg_cache = {}


def svg_size(name):
    if name not in _svg_cache:
        p = os.path.join(ROOT, "assets", "img", name + ".svg")
        if not os.path.exists(p):
            raise SystemExit(f"missing image: {name}.svg")
        m = re.search(r'viewBox="0 0 (\d+) (\d+)"', open(p, encoding="utf-8").read())
        _svg_cache[name] = (int(m.group(1)), int(m.group(2)))
    return _svg_cache[name]


def img_tag(name, alt, eager=False):
    w, h = svg_size(name)
    extra = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="/assets/img/{name}.svg" alt="{esc(alt)}" width="{w}" height="{h}" {extra} decoding="async">'


def expand_figs(text):
    def hero(m):
        name, alt = [x.strip() for x in m.group(1).split("|")]
        return img_tag(name, alt, eager=True)
    text = re.sub(r"\{\{hero:(.*?)\}\}", hero, text)

    def sub(m):
        name, alt, cap = [x.strip() for x in m.group(1).split("|")]
        return (f'\n\n<figure class="frame">{img_tag(name, alt)}<figcaption>{esc(cap)}</figcaption></figure>\n\n')
    return re.sub(r"\{\{fig:(.*?)\}\}", sub, text)


def plain(md):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    t = re.sub(r"[*_`]", "", t)
    return re.sub(r"\s+", " ", t).strip()


MD = lambda s: markdown.markdown(s, extensions=["extra", "sane_lists", "smarty"], output_format="html")


def render_md_body(body, info):
    body = expand_figs(body)
    parts = re.split(r"^:::(books|faq)[ \t]*\n(.*?)^:::[ \t]*$", body, flags=re.M | re.S)
    out = MD(parts[0])
    for i in range(1, len(parts), 3):
        kind, inner, after = parts[i], parts[i + 1], parts[i + 2]
        if kind == "books":
            info["books"] += re.findall(r"^### (.+)$", inner, flags=re.M)
            out += f'<div class="books">{MD(inner)}</div>'
        else:
            for q, a in re.findall(r"^### (.+?)\n+(.*?)(?=^### |\Z)", inner, flags=re.M | re.S):
                info["faq"].append((plain(q), plain(a)))
            out += f'<section class="faq">{MD(inner)}</section>'
        out += MD(after)
    return out


def extract_html_faq(body, info):
    m = re.search(r'<section class="faq">(.*?)</section>', body, flags=re.S)
    if m:
        for q, a in re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", m.group(1), flags=re.S):
            info["faq"].append((plain(re.sub(r"<[^>]+>", "", q)), plain(re.sub(r"<[^>]+>", "", a))))


def external_rel(h):
    def sub(m):
        url = m.group(1)
        if url.startswith("http") and SITE not in url:
            return f'<a href="{url}" rel="noopener">'
        return m.group(0)
    return re.sub(r'<a href="([^"]+)">', sub, h)


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def page_url(slug):
    return SITE + ("/" if slug == "" else f"/{slug}/")


def header(current):
    items = ""
    for label, href in NAV:
        cur = ' aria-current="page"' if current == href else ""
        items += f'<li><a href="{href}"{cur}>{esc(label)}</a></li>'
    return (f'<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap">'
            f'<a class="brand" href="/"><img src="/assets/img/logo.svg" alt="" width="44" height="44"><span class="wm">childrensbooks<b>.ie</b></span></a>'
            f'<nav class="site-nav" aria-label="Main"><ul>{items}</ul></nav></div></header>')


def footer():
    def col(title, links):
        return f"<div><h2>{title}</h2><ul>" + "".join(f'<li><a href="{h}">{esc(t)}</a></li>' for t, h in links) + "</ul></div>"
    return (f'<footer class="site-footer"><div class="wrap"><div class="cols">'
            f'<div><h2>{NAME}</h2><p>A friendly guide to children’s books for Irish families, with picture books, '
            f'first chapter books, Irish authors, Irish-language books and tips for reading together.</p></div>'
            f'{col("Books by age", FOOT_AGES)}{col("Irish and special", FOOT_IRISH)}{col("Guides", FOOT_GUIDES)}</div>'
            f'<p class="small">Illustrations on this site are original artwork. Book titles are mentioned for information only; '
            f'covers belong to their publishers and are not reproduced here. '
            f'<a href="/about/">About</a> · <a href="/privacy/">Privacy</a> · © 2026 {NAME}</p></div></footer>')


def head(title, desc, url, kind, noindex=False):
    t = esc(title)
    d = esc(desc)
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    return f"""<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#e8f4f8">
<link rel="icon" href="/assets/img/logo.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/young-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/atkinson-hyperlegible-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">
<meta property="og:type" content="{'article' if kind in ('age', 'guide', 'topic', 'book') else 'profile' if kind == 'author' else 'website'}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="{LOCALE}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Illustration of a bear and a rabbit reading a book together under a sunny sky">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE}{OG_IMAGE}">
"""


ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": NAME, "url": SITE + "/",
       "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/apple-touch-icon.png", "width": 180, "height": 180}}


def build_page(meta, pages, outputs):
    slug = meta.get("slug", "")
    kind = meta.get("kind", "page")
    url = page_url(slug)
    info = {"books": [], "faq": []}
    body = meta["_body"]
    if meta["_file"].endswith(".html"):
        body_html = expand_figs(body)
        extract_html_faq(body_html, info)
    else:
        body_html = render_md_body(body, info)
    body_html = external_rel(body_html)

    schema = []
    if slug == "":
        schema.append({"@context": "https://schema.org", "@graph": [
            ORG, {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME,
                  "description": meta["description"], "inLanguage": "en-IE", "publisher": {"@id": SITE + "/#org"}}]})
    else:
        crumbs = [("Home", SITE + "/")]
        if meta.get("parent"):
            crumbs.append((meta["parent_label"], page_url(meta["parent"])))
        crumbs.append((meta["h1"], url))
        schema.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
        if kind == "book":
            bk = {"@context": "https://schema.org", "@type": "Book", "name": meta["h1"], "url": url, "inLanguage": "en",
                  "description": meta["description"], "image": f"{SITE}/assets/img/{meta['image']}.svg",
                  "author": {"@type": "Person", "name": meta["book_author"]}, "genre": meta["book_genre"],
                                    "audience": {"@type": "PeopleAudience", "suggestedMinAge": int(meta["book_agemin"]), "suggestedMaxAge": int(meta["book_agemax"])}}
            fm = meta["book_format"].lower()
            if "hardback" in fm:
                bk["bookFormat"] = "https://schema.org/Hardcover"
            elif "paperback" in fm:
                bk["bookFormat"] = "https://schema.org/Paperback"
            if meta.get("book_illustrator"):
                bk["illustrator"] = {"@type": "Person", "name": meta["book_illustrator"]}
            if meta.get("book_publisher"):
                bk["publisher"] = {"@type": "Organization", "name": meta["book_publisher"]}
            if meta.get("book_published"):
                bk["datePublished"] = meta["book_published"]
            if meta.get("book_pages"):
                bk["numberOfPages"] = int(meta["book_pages"])
            if meta.get("book_isbn"):
                bk["isbn"] = meta["book_isbn"]
            if meta.get("book_series"):
                bk["isPartOf"] = {"@type": "BookSeries", "name": meta["book_series"]}
            schema.append(bk)
        elif kind == "author":
            pr = {"@type": "Person", "@id": url + "#person", "name": meta["person_name"], "url": url, "jobTitle": meta["person_role"],
                  "description": meta["person_description"], "image": f"{SITE}/assets/img/{meta['image']}.svg"}
            if meta.get("person_nat"):
                pr["nationality"] = meta["person_nat"]
            if meta.get("person_born"):
                pr["birthDate"] = meta["person_born"]
            if meta.get("person_works"):
                pr["knowsAbout"] = "children's books"
                pr["author"] = [{"@type": "Book", "name": t} for t in meta["person_works"].split("|")]
            schema.append({"@context": "https://schema.org", "@type": "ProfilePage", "name": meta["h1"], "url": url,
                           "description": meta["description"], "inLanguage": "en-IE", "dateModified": meta.get("updated", TODAY),
                           "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": pr})
        elif kind in ("age", "guide", "topic"):
            w, h = svg_size(meta["image"])
            schema.append({"@context": "https://schema.org", "@type": "Article", "headline": meta["h1"],
                           "description": meta["description"], "inLanguage": "en-IE",
                           "image": [f"{SITE}/assets/img/{meta['image']}.svg"],
                           "datePublished": meta.get("published", TODAY), "dateModified": meta.get("updated", TODAY),
                           "author": {"@type": "Organization", "name": NAME, "url": SITE + "/"},
                           "publisher": {"@id": SITE + "/#org"}, "mainEntityOfPage": url})
        else:
            schema.append({"@context": "https://schema.org", "@type": "CollectionPage" if kind == "hub" else "WebPage",
                           "name": meta["h1"], "url": url, "description": meta["description"], "inLanguage": "en-IE",
                           "isPartOf": {"@id": SITE + "/#website"}})
    if info["faq"]:
        schema.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in info["faq"]]})
    if info["books"]:
        schema.append({"@context": "https://schema.org", "@type": "ItemList", "name": meta["h1"],
                       "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": plain(b)} for i, b in enumerate(info["books"])]})

    out = head(meta["title"], meta["description"], url, kind)
    out += "\n".join(jsonld(s) for s in schema) + "\n</head>\n<body>\n"
    current = meta.get("nav", "")
    out += header(current) + '\n<main id="main">\n'

    if kind == "home":
        out += body_html
    else:
        crumbs_html = '<li><a href="/">Home</a></li>'
        if meta.get("parent"):
            crumbs_html += f'<li><a href="/{meta["parent"]}/">{esc(meta["parent_label"])}</a></li>'
        crumbs_html += f'<li aria-current="page">{esc(meta.get("crumb", meta["h1"]))}</li>'
        out += (f'<div class="wrap"><div class="page-head"><nav class="crumbs" aria-label="Breadcrumb"><ol>{crumbs_html}</ol></nav>'
                f'<h1>{esc(meta["h1"])}</h1><p class="lede">{esc(meta["lede"])}</p></div>'
                f'<figure class="banner frame">{img_tag(meta["image"], meta["alt"], eager=True)}</figure>'
                f'<div class="sheet">{body_html}')
        rel = [pages[s] for s in meta.get("related", "").split(",") if s.strip() and s.strip() in pages]
        if rel:
            out += '<aside class="related"><h2>Keep reading</h2><ul class="linklist">'
            for r in rel:
                out += f'<li><a href="/{r["slug"]}/"><strong>{esc(r.get("short", r["h1"]))}</strong><span>{esc(r["description"])}</span></a></li>'
            out += "</ul></aside>"
        out += "</div></div>"
    out += "\n</main>\n" + footer() + "\n</body>\n</html>\n"
    outputs[slug] = out


NOT_FOUND = """<main id="main" class="wrap" style="padding:2rem 0 3rem"><div class="sheet"><h1>That page isn’t on our shelf</h1>
<p>The page you tried to open doesn’t exist, or it may have moved. Try one of these instead:</p>
<ul><li><a href="/">Go to the home page</a></li><li><a href="/books-by-age/">Find books by age</a></li><li><a href="/guides/">Read our guides</a></li></ul></div></main>"""


def main():
    pages = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "content", "*.md")) + glob.glob(os.path.join(ROOT, "content", "*.html"))):
        m = read_front(p)
        m.setdefault("slug", os.path.splitext(os.path.basename(p))[0])
        if m["slug"] == "index":
            m["slug"] = ""
        pages[m["slug"]] = m
    # resolve parents
    for m in pages.values():
        par = m.get("parent")
        if par:
            m["parent_label"] = pages[par].get("short", pages[par]["h1"]) if par in pages else par
    outputs = {}
    for m in pages.values():
        build_page(m, pages, outputs)

    for slug, content in outputs.items():
        d = ROOT if slug == "" else os.path.join(ROOT, slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(content)

    nf = head("Page not found | " + NAME, "This page could not be found.", SITE + "/404.html", "page", noindex=True)
    nf += "</head>\n<body>\n" + header("") + NOT_FOUND + footer() + "\n</body>\n</html>\n"
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(nf)

    urls = []
    for slug, m in sorted(pages.items(), key=lambda kv: (kv[0] != "", kv[0])):
        pr = "1.0" if slug == "" else ("0.9" if m.get("kind") in ("hub", "age") else "0.7")
        if m.get("kind") == "legal":
            pr = "0.2"
        urls.append(f"<url><loc>{page_url(slug)}</loc><lastmod>{m.get('updated', TODAY)}</lastmod><priority>{pr}</priority></url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(ROOT, "CNAME"), "w").write("www.childrensbooks.ie\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print(f"built {len(outputs)} pages + 404, sitemap.xml, robots.txt, CNAME")

    if "--check" in sys.argv:
        check(pages)


def check(pages):
    bad = 0
    seen = set()
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        if "/node_modules/" in f:
            continue
        txt = open(f, encoding="utf-8").read()
        for ref in re.findall(r'(?:href|src)="(/[^"#?]*)', txt):
            if ref in seen:
                continue
            seen.add(ref)
            target = os.path.join(ROOT, ref.lstrip("/"))
            if ref.endswith("/"):
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                print("BROKEN:", ref, "in", os.path.relpath(f, ROOT))
                bad += 1
    titles = {}
    for slug, m in pages.items():
        if len(m["title"]) > 62:
            print("long title:", slug, len(m["title"]))
        if len(m["description"]) > 160:
            print("long description:", slug, len(m["description"]))
        titles.setdefault(m["title"], []).append(slug)
    for t, s in titles.items():
        if len(s) > 1:
            print("duplicate title:", t, s)
    words = {s: len(re.sub(r"<[^>]+>", " ", re.sub(r"\s+", " ", m["_body"])).split()) for s, m in pages.items()}
    print("words per page:", dict(sorted(words.items(), key=lambda kv: kv[1])))
    print("total words:", sum(words.values()))
    print("OK: no broken internal links" if not bad else f"{bad} broken links")


if __name__ == "__main__":
    main()
