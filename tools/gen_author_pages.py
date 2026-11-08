#!/usr/bin/env python3
"""Generate author pages and the authors hub from tools/authors_data.py and tools/books_data.py.

    python3 tools/gen_author_pages.py && python3 tools/build.py --check
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authors_data import AUTHORS  # noqa: E402
from books_data import BOOKS, LIST_DATE  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
HUB = "childrens-book-authors"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def pick(options, limit):
    for o in options:
        if len(o) <= limit:
            return o
    return options[-1][:limit]


def books_of(a):
    return [b for b in BOOKS if b["author"] == a["name"]]


def author_slug(name):
    for a in AUTHORS:
        if a["name"] == name:
            return a["slug"]
    return None


def front(a):
    bs = books_of(a)
    title = pick([f"{a['name']} | Books, Biography and Where to Start", f"{a['name']} | Books and Biography", a["name"]], 62)
    desc = pick([
        f"{a['name']}, {a['role'].lower()}: a short biography, their books in the current top 20, other well-known titles and where to start.",
        f"{a['name']}: biography, books in the top 20 and where to start reading.",
    ], 160)
    kv = {
        "title": title, "h1": a["name"], "short": a["name"], "description": desc, "kind": "author", "nav": "/" + HUB + "/",
        "parent": HUB, "image": a["image"], "alt": a["alt"], "lede": a["hook"],
        "related": ",".join([b["slug"] for b in bs] + [HUB, "top-20-childrens-books"]), "updated": "2026-11-08", "crumb": a["name"],
        "person_name": a["name"], "person_role": a["role"], "person_nat": a.get("nat", ""), "person_born": a.get("born", ""),
        "person_description": a["hook"], "person_works": "|".join(b["title"] for b in bs),
    }
    return "\n".join(f"{k}: {v}" for k, v in kv.items() if v != "") + "\n---\n"


def body(a):
    n = a["name"]
    bs = books_of(a)
    role = a["role"][0].lower() + a["role"][1:]
    art = "an" if role[0] in "aeiou" else "a"
    out = [f"**{n}** is {art} {role}. {a['hook']} This page is a short guide for parents, teachers and young readers: who they are, which of their books are in the current top 20 and where to start."]
    out += [f"## About {n}", *a["bio"]]
    li = "\n".join(f"- [{b['title']}](/{b['slug']}/): number {b['rank']} in the list we checked on {LIST_DATE}. {b['hook']}" for b in bs)
    out += [f"## {n}’s books in the top 20", li]
    out += [f"## Other well-known books and work", "\n".join(f"- {x}" for x in a["other"])]
    if a["honours"]:
        out += ["## Awards and recognition", "\n".join(f"- {x}" for x in a["honours"])]
    out += ["## Where to start", a["start"]]
    q1 = (f"Which books by {n} are in the top 20?", "; ".join(f"{b['title']} (number {b['rank']})" for b in bs) + f". See our [Top 20 children’s books](/top-20-childrens-books/) for the full list.")
    q2 = (f"Where should I start with {n}?", a["start"])
    q3 = (f"Who is {n}?", a["bio"][0])
    out += [f"## Frequently asked questions about {n}", ":::faq\n" + "\n\n".join(f"### {q}\n{an}" for q, an in (q3, q1, q2)) + "\n:::"]
    note = "*Biographical details are drawn from publisher biographies, reference works and the author’s own site, and may have changed. The illustration is our own and is not a likeness of the author. See [all the authors](/" + HUB + "/).*"
    if a["sources"]:
        note += "\n\nSources: " + "; ".join(f"[{t}]({u})" for t, u in a["sources"]) + "."
    out.append(note)
    return "\n\n".join(out) + "\n"


def card(a):
    bs = books_of(a)
    sub = ", ".join(b["title"] for b in bs[:2]) + (" and more" if len(bs) > 2 else "")
    return (f'<li class="bookcard"><a href="/{a["slug"]}/"><img src="/assets/img/{a["image"]}.svg" alt="" width="1200" height="400" loading="lazy" decoding="async">'
            f'<strong>{esc(a["name"])}</strong><span class="by">{esc(sub)}</span></a></li>')


def hub():
    cards = "\n".join(card(a) for a in AUTHORS)
    faq = [("Which authors are in the current top 20?", f"This page covers all {len(AUTHORS)} authors behind the top 20 children’s books we checked on {LIST_DATE}, from Jeff Kinney and Julia Donaldson to Irish writers such as Cecelia Ahern and Leona Forde."),
           ("Are the author pictures photographs?", "No. Every portrait is our own illustration of a generic writer at work. They are not likenesses of the real authors."),
           ("Where do the biographies come from?", "From publisher biographies, reference works, interviews and authors’ own websites. Each author page links its sources, and we only include facts we could check.")]
    faq_html = '<section class="faq"><h2>Frequently asked questions</h2>' + "".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q, a in faq) + "</section>"
    return f"""title: Children’s Book Authors | Top 20 Author Guides
h1: Children’s book authors
short: Children’s book authors
description: Meet the {len(AUTHORS)} authors behind the top 20 bestselling children’s books: short biographies, their books and where to start reading.
kind: hub
nav: /{HUB}/
image: banner-childrens-book-authors
alt: Five cartoon writers at a long desk with an open book above them
lede: Short guides to the writers and illustrators behind the books children are asking for right now.
related: top-20-childrens-books,irish-childrens-authors,books-by-age
updated: 2026-11-08
---
<p>Behind every bestseller is a writer with a story of their own. These pages give a short, fact-checked biography of each author in the top 20 children’s books, link to their books and suggest where to start. Our portraits are original illustrations, not photographs.</p>
<ol class="bookgrid">
{cards}
</ol>
{faq_html}
"""


def main():
    cdir = os.path.join(ROOT, "content")
    for a in AUTHORS:
        with open(os.path.join(cdir, a["slug"] + ".md"), "w", encoding="utf-8") as fh:
            fh.write(front(a) + body(a))
    with open(os.path.join(cdir, HUB + ".html"), "w", encoding="utf-8") as fh:
        fh.write(hub())
    print(f"wrote {len(AUTHORS)} author pages and hub")


if __name__ == "__main__":
    main()
