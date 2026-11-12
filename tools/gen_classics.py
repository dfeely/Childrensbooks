#!/usr/bin/env python3
"""Generate the 20 classic book pages and the all-time list page.

    python3 tools/gen_author_pages.py && python3 tools/gen_classics.py && python3 tools/build.py --check
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authors_data import AUTHORS  # noqa: E402
from classics_data import CLASSICS, CLASSIC_AUTHORS  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
HUB = "best-childrens-books-of-all-time"
AUTHOR = {a["name"]: a for a in AUTHORS + CLASSIC_AUTHORS}
BY_SLUG = {b["slug"]: b for b in CLASSICS}


def pick(options, limit):
    for o in options:
        if len(o) <= limit:
            return o
    return options[-1][:limit]


def front(b):
    t = b["title"]
    title = pick([f"{t} by {b['author']} | Review and Age Guide", f"{t} | Review and Age Guide", f"{t} | Age Guide", t], 62)
    desc = pick([f"{t} by {b['author']} ({b['year']}): what it is about, what age it suits, why children love it and what to read next."[:160],
                 f"{t}: what it is about, age guide, why children love it and what to read next."], 160)
    rel = [x for x in b["next"] if x in BY_SLUG or True] + [AUTHOR[b["author"]]["slug"], HUB]
    kv = {"title": title, "h1": t, "short": t, "description": desc, "kind": "book", "nav": "/" + HUB + "/", "parent": HUB,
          "image": b["image"], "alt": b["alt"], "lede": b["hook"], "related": ",".join(rel), "updated": "2026-11-12", "crumb": t,
          "book_author": b["author"], "book_illustrator": b.get("illustrator", ""), "book_published": b["year"],
          "book_genre": b["genre"], "book_agemin": b["agemin"], "book_agemax": b["agemax"], "book_series": b.get("series", "")}
    return "\n".join(f"{k}: {v}" for k, v in kv.items() if v != "") + "\n---\n"


def link_title(slug):
    if slug in BY_SLUG:
        return BY_SLUG[slug]["title"]
    return {"gruffalo-granny": "Gruffalo Granny"}.get(slug, slug)


def body(b):
    t, au = b["title"], AUTHOR[b["author"]]
    ill = f", illustrated by {b['illustrator']}" if b.get("illustrator") and b["illustrator"] != b["author"] else ""
    out = [f"**{t}** is a {b['genre'].lower()} by [{b['author']}](/{au['slug']}/){ill}, first published in {b['year']}. It is number {b['rank']} in our list of the [best children’s books of all time](/{HUB}/). {b['hook']}"]
    out += [f"## What is {t} about?", *b["about"]]
    rows = [("Author", f"[{b['author']}](/{au['slug']}/)")]
    if b.get("illustrator"):
        rows.append(("Illustrator", b["illustrator"]))
    rows += [("First published", b["year"]), ("Type", b["genre"]), ("Age guide", b["age"])]
    if b.get("series"):
        rows.append(("Series", b["series"]))
    out += ["## Book details", "| Detail | Information |\n|---|---|\n" + "\n".join(f"| {k} | {v} |" for k, v in rows)]
    out += [f"## Why children enjoy {t}", "\n".join(f"- {x}" for x in b["why"])]
    out += ["## Reading and talking tips", "\n".join(f"- {x}" for x in b["tips"])]
    if b.get("irish"):
        out += ["## An Irish connection", f"{b['author']} was born in Belfast. Find more in our guide to [Irish children’s authors](/irish-childrens-authors/)."]
    out += [f"## About {b['author']}", au["bio"][0], f"Read more on our [{b['author']} author page](/{au['slug']}/)."]
    nxt = "\n".join(f"- [{link_title(x)}](/{x}/)" for x in b["next"])
    out += ["## If your child likes this, try…", nxt + f"\n\nSee all 20 in our [best children’s books of all time](/{HUB}/)."]
    faq = list(b["faq"]) + [(f"Where can I borrow {t}?", f"Most public libraries stock it. See our guide to [children’s books and your local library](/childrens-books-and-your-local-library/).")]
    out += ["## Frequently asked questions", ":::faq\n" + "\n\n".join(f"### {q}\n{a}" for q, a in faq) + "\n:::"]
    return "\n\n".join(out) + "\n"


def hub():
    entries = []
    for b in CLASSICS:
        au = AUTHOR[b["author"]]
        ill = f" Illustrated by {b['illustrator']}." if b.get("illustrator") and b["illustrator"] != b["author"] else ""
        entries.append(f"### {b['rank']}. {b['title']}\n*By {b['author']}, {b['year']}. Ages {b['age'].split(' (')[0]}*\n\n{b['hook']}{ill} [Read the full guide](/{b['slug']}/) or learn about [{b['author']}](/{au['slug']}/).")
    entries = "\n\n".join(entries)
    return f"""title: Best Children’s Books of All Time | Top 20 Classics
h1: The 20 best children’s books of all time
short: Best children’s books of all time
description: Twenty classic children’s books that have lasted generations, from Peter Rabbit to Harry Potter, with an age guide and a page for each book and author.
kind: guide
nav: /{HUB}/
image: banner-best-childrens-books-of-all-time
alt: Two bookcases full of colourful books either side of an open book, a golden trophy and stars
lede: Twenty children’s books that families keep handing down, from picture books for bedtime to novels for confident readers.
related: top-20-childrens-books,childrens-book-authors,books-by-age,bedtime-stories-for-children
updated: 2026-11-12
---
There is no official list of the best children’s books ever written, so this is ours. We chose books that have stayed in print and in family bookcases for decades, that suit reading aloud or reading alone, and that have shaped the books children read today. We have avoided sales claims, because figures vary between sources. Dates are first publication, and ages are our own suggestions. Every book has its own guide and every author has their own page.

For what children are buying right now, see our [Top 20 children’s books](/top-20-childrens-books/), which changes with the bestseller charts. You can also [meet the authors](/childrens-book-authors/).

## The 20 classics

:::books
{entries}
:::

## How to use this list

- **Match the book to the age.** Picture books such as The Very Hungry Caterpillar and Goodnight Moon suit under-fives. Novels such as The Hobbit work best when children are ready for longer stories.
- **Read the long ones aloud.** Older classics such as Winnie-the-Pooh, The Wind in the Willows and Charlotte’s Web are often easier to enjoy when someone reads them to you. See our guide to [reading aloud](/how-to-read-aloud-to-children/).
- **Borrow before you buy.** Most of these are in public libraries. See our [library guide](/childrens-books-and-your-local-library/).

:::faq
### What is the best children’s book of all time?
There is no single answer, because it depends on the age of the child and what you value. Harry Potter, Charlotte’s Web and The Very Hungry Caterpillar are among the most often named.

### Which classics suit toddlers?
The Very Hungry Caterpillar, Goodnight Moon, Guess How Much I Love You and The Tiger Who Came to Tea are all good for the youngest children.

### Which classics suit older children?
Harry Potter, The Hobbit, The Lion, the Witch and the Wardrobe, Matilda and Anne of Green Gables suit confident readers from about 8 to 9 and up.

### How were these books chosen?
We looked for books that have stayed in print and popular for decades, and covered a mix of ages and styles. The list is our own judgement, not a sales ranking.
:::
"""


def main():
    cdir = os.path.join(ROOT, "content")
    for b in CLASSICS:
        with open(os.path.join(cdir, b["slug"] + ".md"), "w", encoding="utf-8") as fh:
            fh.write(front(b) + body(b))
    with open(os.path.join(cdir, HUB + ".md"), "w", encoding="utf-8") as fh:
        fh.write(hub())
    print(f"wrote {len(CLASSICS)} classic book pages and hub")


if __name__ == "__main__":
    main()
