#!/usr/bin/env python3
"""Generate content/ pages for the Top 20 list from tools/books_data.py, plus the home-page grid.

    python3 tools/gen_book_pages.py && python3 tools/build.py --check
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from books_data import BOOKS, LIST_DATE  # noqa: E402
from authors_data import AUTHORS  # noqa: E402
AUTHOR_SLUG = {a['name']: a['slug'] for a in AUTHORS}

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BY_SLUG = {b["slug"]: b for b in BOOKS}
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def nice_date(iso):
    if not iso:
        return ""
    p = iso.split("-")
    if len(p) == 3:
        return f"{int(p[2])} {MONTHS[int(p[1]) - 1]} {p[0]}"
    return p[0]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def pick(options, limit):
    for o in options:
        if len(o) <= limit:
            return o
    return options[-1][:limit]


def title_for(b):
    return pick([f"{b['title']} | Age, Plot and Tips", f"{b['title']} | Parent Guide", f"{b['title']} | Guide", b["title"]], 62)


def desc_for(b):
    return pick([
        f"{b['title']} by {b['author']}: what it is about, who it suits, reading tips and what to read next.",
        f"{b['title']} by {b['author']}: plot, age guide, reading tips and similar books.",
        f"{b['title']} by {b['author']}: plot, age guide and what to read next.",
    ], 160)


def author_phrase(b):
    s = f"by {b['author']}"
    if b.get("illustrator"):
        s += f", illustrated by {b['illustrator']}"
    return s


def front(b):
    kv = {
        "title": title_for(b), "h1": b["title"], "short": b["title"], "description": desc_for(b), "kind": "book",
        "nav": "/top-20-childrens-books/", "parent": "top-20-childrens-books", "image": b["image"], "alt": b["alt"],
        "lede": b["hook"], "related": b["related"], "updated": "2026-11-07", "crumb": b["title"],
        "book_author": b["author"], "book_illustrator": b.get("illustrator", ""), "book_publisher": b["publisher"],
        "book_published": b["published"], "book_pages": b["pages"] or "", "book_isbn": b["isbn"], "book_format": b["fmt"],
        "book_genre": b["genre"], "book_agemin": b["agemin"], "book_agemax": b["agemax"], "book_series": b["series"],
    }
    return "\n".join(f"{k}: {v}" for k, v in kv.items() if v != "") + "\n---\n"


def details_table(b):
    rows = [("Author", b["author"])]
    if b.get("illustrator"):
        rows.append(("Illustrator", b["illustrator"]))
    rows += [("Series", b["series"]), ("Format", b["fmt"]), ("Publisher", b["publisher"])]
    if b["published"]:
        rows.append(("Published", nice_date(b["published"])))
    if b["pages"]:
        rows.append(("Length", f"{b['pages']} pages"))
    rows.append(("Genre", b["genre"]))
    rows.append(("Age guide", b["age"]))
    if b["isbn"]:
        rows.append(("ISBN (edition listed)", b["isbn"]))
    return "| Detail | Information |\n| --- | --- |\n" + "\n".join(f"| {k} | {v} |" for k, v in rows)


def body(b):
    t = b["title"]
    kind_word = b["genre"].lower()
    intro = (f"**{t}** is a {kind_word} title {author_phrase(b)}. In the children’s bestseller list we checked on {LIST_DATE}, "
             f"it was number {b['rank']}. This guide explains what the book is about, who it suits, how to talk about it and what to read next.")
    out = [intro]
    if b.get("buy"):
        out.append(f'<p class="buybox"><a class="btn" href="{b["buy"]}" rel="sponsored nofollow noopener" target="_blank">Buy {t} on Amazon</a><small>Affiliate link. As an Amazon Associate we may earn from qualifying purchases, at no extra cost to you.</small></p>')
    out += [f"## What is {t} about?", *b["about"]]
    out += [f"## {t}: book details", details_table(b),
            "Ages marked as “suggested” are our own guidance, not the publisher’s. Editions and dates can differ between shops, so check the listing for the copy you want.",
            f"## Why children enjoy {t}", "\n".join(f"- {w}" for w in b["why"])]
    out += ["## Reading and talking tips", "Use these prompts to make reading time a conversation:", "\n".join(f"- {x}" for x in b["tips"])]
    if b.get("irish"):
        out += ["## An Irish connection", f"This title has an Irish link through its author, setting or subject, which makes it a good fit for our collection of [Irish children’s authors and illustrators](/irish-childrens-authors/)."]
    out += [f"## About {b['author']}", b["author_bio"], f"Read more on our [{b['author']} author page](/{AUTHOR_SLUG[b['author']]}/)."]
    nxt = []
    for s in b["next"]:
        o = BY_SLUG[s]
        nxt.append(f"- [{o['title']}](/{o['slug']}/) by {o['author']}, number {o['rank']} in the list.")
    out += ["## If your child likes this, try…", "\n".join(nxt),
            "Browse the whole list in our [Top 20 children’s books](/top-20-childrens-books/), or use our [books by age](/books-by-age/) guides to find your next read."]
    out += [f"## Frequently asked questions about {t}", ":::faq\n" + "\n\n".join(f"### {q}\n{a}" for q, a in b["faq"]) + "\n:::"]
    out += ["*Where to find it: your local library, an independent bookshop or an online retailer. Library membership is free in Ireland; see our [guide to using your library](/childrens-books-and-your-local-library/).*"]
    return "\n\n".join(out) + "\n"


def card(b, eager=False):
    w, h = 1200, 400
    return (f'<li class="bookcard"><a href="/{b["slug"]}/"><img src="/assets/img/{b["image"]}.svg" alt="" width="{w}" height="{h}" loading="lazy" decoding="async">'
            f'<span class="n">{b["rank"]}</span><strong>{esc(b["title"])}</strong><span class="by">{esc(b["author"])}</span></a></li>')


def hub():
    cards = "\n".join(card(b) for b in BOOKS)
    irish = [b for b in BOOKS if b.get("irish")]
    irish_li = "".join(f'<li><a href="/{b["slug"]}/"><strong>{esc(b["title"])}</strong><span>{esc(b["author"])}: {esc(b["hook"])}</span></a></li>' for b in irish)
    faq = [
        ("What are the bestselling children’s books in Ireland right now?",
         f"The list we checked on {LIST_DATE} was led by Diary of a Wimpy Kid: Fight or Flight, Gruffalo Granny and Bunny vs Monkey: Day of the Heroes. The full top 20 is on this page, with a guide to each book."),
        ("How often does this list change?", "Bestseller lists move every week, especially in the run-up to Christmas. The rankings here are a snapshot, and we update the page when we refresh it."),
        ("Which of these books suit reluctant readers?", "Comic and illustrated titles such as Dog Man, Bunny vs Monkey, Donut Squad, Ghost and Toast and Diary of a Wimpy Kid are popular with children who find long text a barrier. See our guide to helping a reluctant reader."),
        ("Are any of these books by Irish authors?", "Yes. Disaster Dad, Squad Girls, Milly McCarthy, Rabbit and Bear, Nina Peanut, Detective Thingy Majiggy and Classic Football Heroes: Best all have an Irish link through their author or subject."),
    ]
    faq_html = '<section class="faq"><h2>Frequently asked questions</h2>' + "".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q, a in faq) + "</section>"
    return f"""title: Top 20 Children’s Books Right Now | Bestseller Guide
h1: Top 20 children’s books right now
short: Top 20 children’s books
description: The 20 bestselling children’s books in Ireland right now, with a guide to each one: plot, age, reading tips and what to read next.
kind: hub
nav: /top-20-childrens-books/
image: banner-top-20-childrens-books
alt: A winners’ podium with the number one in the centre, a star above it and stacks of books on either side
lede: The books children are asking for this month, from Wimpy Kid and Gruffalo Granny to Irish favourites. Tap any title for a full guide.
related: childrens-book-authors,books-by-age,best-christmas-books-for-children,irish-childrens-authors
updated: 2026-11-07
---
<p>This page follows the bestselling children’s books in the list we checked on {LIST_DATE}. For every title you will find a plain-English summary, an age guide, tips for reading it together and suggestions for what to read next. We do not reproduce book covers, so the pictures here are our own illustrations.</p>
<p>Rankings change weekly, so treat the numbers as a snapshot. If you are buying for Christmas, our <a href="/best-christmas-books-for-children/">Christmas book guides</a> will help you plan, and our <a href="/books-by-age/">books by age</a> pages cover the classics.</p>

<ol class="bookgrid">
{cards}
</ol>

<p><a href="/childrens-book-authors/">Meet the authors behind the top 20</a>, with a short biography of each. Looking for the classics? See the <a href="/best-childrens-books-of-all-time/">20 best children’s books of all time</a>.</p>

<h2>How to use this list</h2>
<ul>
<li><strong>Choose by format.</strong> Comics and diaries (Dog Man, Wimpy Kid, Tom Gates, Donut Squad) suit fast, funny reading. Picture books such as Gruffalo Granny suit reading aloud. Longer novels such as Camp Half-Blood and The Danger Game suit confident readers.</li>
<li><strong>Check the age.</strong> Each page gives a suggested age. Remember that children can enjoy stories well above their own reading level when you read to them.</li>
<li><strong>Try before you buy.</strong> Many of these books are available from the library. See our guide to <a href="/childrens-books-and-your-local-library/">children’s books and your local library</a>.</li>
<li><strong>Mix it up.</strong> A bestseller is a good start, but pair it with an old favourite so reading stays a pleasure, not a chase.</li>
</ul>

<h2>Irish authors and Irish interest</h2>
<p>Seven titles on the list have an Irish link. They are a handy place to start if you want to support Irish writers and illustrators.</p>
<ul class="linklist">{irish_li}</ul>

{faq_html}
"""


def home_block():
    cards = "\n".join(card(b) for b in BOOKS)
    return f"""<!--TOP20-->
<section class="band"><div class="wrap">
<h2>Top 20 children’s books right now</h2>
<p class="intro">The books children are asking for this month. Tap a title for the plot, the age it suits and what to read next. <a href="/top-20-childrens-books/">See the full list</a> or <a href="/childrens-book-authors/">meet the authors</a>.</p>
<ol class="bookgrid">
{cards}
</ol>
</div></section>
<!--/TOP20-->"""


def main():
    cdir = os.path.join(ROOT, "content")
    for b in BOOKS:
        with open(os.path.join(cdir, b["slug"] + ".md"), "w", encoding="utf-8") as fh:
            fh.write(front(b) + body(b))
    with open(os.path.join(cdir, "top-20-childrens-books.html"), "w", encoding="utf-8") as fh:
        fh.write(hub())
    ip = os.path.join(cdir, "index.html")
    s = open(ip, encoding="utf-8").read()
    blk = home_block()
    if "<!--TOP20-->" in s:
        s = re.sub(r"<!--TOP20-->.*?<!--/TOP20-->", lambda m: blk, s, flags=re.S)
    else:
        marker = '<section class="band paper"><div class="wrap split">'
        s = s.replace(marker, blk + "\n\n" + marker, 1)
    open(ip, "w", encoding="utf-8").write(s)
    print(f"wrote {len(BOOKS)} book pages, hub and home block")


if __name__ == "__main__":
    main()
