#!/usr/bin/env python3
"""Generate the 'children's books on Amazon Ireland' page (static HTML, rebuilt from the data below).

    python3 tools/gen_shop_page.py && python3 tools/build.py --check
"""
import os
import urllib.parse

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
AMAZON_TAG = "childrensb09f-21"
SHORT = {"wimpy": "https://link.amazon/B0iGjeIJi"}  # a verified short link is used instead of an unverified product code

BOOKS = [
 ("The Gruffalo", "Julia Donaldson", "classic-gruffalo", "the-gruffalo", "The Gruffalo Julia Donaldson", "A much-loved rhyming story about a clever little mouse who uses his imagination to outsmart the animals of the forest.", "Ages 2 to 6", "A mouse in a deep dark wood"),
 ("The Very Hungry Caterpillar", "Eric Carle", "classic-hungry-caterpillar", "the-very-hungry-caterpillar", "The Very Hungry Caterpillar Eric Carle", "A colourful classic following a hungry caterpillar through the days of the week before its remarkable transformation.", "Ages 0 to 4", "Fruit, a cocoon and a butterfly"),
 ("Where the Wild Things Are", "Maurice Sendak", "classic-wild-things", "where-the-wild-things-are", "Where the Wild Things Are Maurice Sendak", "Max sets sail to a mysterious land inhabited by Wild Things in one of the most celebrated children’s picture books.", "Ages 3 to 7", "A boat on a moonlit sea"),
 ("Room on the Broom", "Julia Donaldson", "shop-room-on-the-broom", None, "Room on the Broom Julia Donaldson", "A funny rhyming adventure about a friendly witch, her cat and the unusual passengers who join them on their broom.", "Ages 3 to 7", "A broom, a witch’s hat and a cauldron"),
 ("The Tiger Who Came to Tea", "Judith Kerr", "classic-tiger-tea", "the-tiger-who-came-to-tea", "The Tiger Who Came to Tea Judith Kerr", "Sophie and her mother receive an unexpected visitor who has a very big appetite in this timeless children’s classic.", "Ages 2 to 5", "A tea table in a kitchen"),
 ("The Snail and the Whale", "Julia Donaldson", "shop-snail-and-the-whale", None, "The Snail and the Whale Julia Donaldson", "A tiny sea snail travels around the world on the tail of a huge humpback whale.", "Ages 3 to 7", "A whale, a globe and a snail shell"),
 ("The Tale of Peter Rabbit", "Beatrix Potter", "classic-peter-rabbit", "the-tale-of-peter-rabbit", "The Tale of Peter Rabbit Beatrix Potter", "Peter Rabbit ignores his mother’s warning and ventures into Mr McGregor’s garden in this enduring classic.", "Ages 2 to 6", "A vegetable garden"),
 ("Guess How Much I Love You", "Sam McBratney", "classic-guess-how-much", "guess-how-much-i-love-you", "Guess How Much I Love You Sam McBratney", "Little Nutbrown Hare and Big Nutbrown Hare try to express just how much they love one another.", "Ages 0 to 4", "A moonlit meadow"),
 ("The Giving Tree", "Shel Silverstein", "shop-the-giving-tree", None, "The Giving Tree Shel Silverstein", "A simple and thought-provoking story about a boy and a tree that follows them throughout their lives.", "Ages 5 and up", "An apple tree, a swing and a stump"),
 ("Diary of a Wimpy Kid: Fight or Flight", "Jeff Kinney", "book-wimpy-kid-fight-or-flight", "diary-of-a-wimpy-kid-fight-or-flight", None, "The latest book in the Diary of a Wimpy Kid series, perfect for children who enjoy funny stories, school adventures and cartoons.", "Ages 8 to 12", "A school hallway scene"),
]
AUTHOR_PAGE = {"Julia Donaldson": "julia-donaldson"}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def url(title, search):
    if search is None:
        return SHORT["wimpy"]
    return f"https://www.amazon.ie/s?k={urllib.parse.quote_plus(search)}&tag={AMAZON_TAG}"


def card(i, b):
    title, author, img, slug, search, desc, age, alt = b
    guide = f'<a href="/{slug}/">{esc(title)}</a>' if slug else esc(title)
    by = f'<a href="/{AUTHOR_PAGE[author]}/">{esc(author)}</a>' if author in AUTHOR_PAGE else esc(author)
    more = f'<a class="more" href="/{slug}/">Read our guide to this book</a>' if slug else (f'<a class="more" href="/{AUTHOR_PAGE[author]}/">More from {esc(author)}</a>' if author in AUTHOR_PAGE else '<a class="more" href="/best-childrens-books-of-all-time/">More classics</a>')
    return (f'<li class="shopcard"><img src="/assets/img/{img}.svg" alt="{esc(alt)}" width="1200" height="400" loading="lazy" decoding="async">'
            f'<div class="shopbody"><h3><span class="n">{i}</span> {guide}</h3><p class="by">{by} · {esc(age)}</p><p>{esc(desc)}</p>'
            f'<p class="shopbtns"><a class="btn" href="{url(title, search)}" target="_blank" rel="nofollow sponsored noopener">Check price on Amazon.ie</a>{more}</p></div></li>')


def main():
    cards = "\n".join(card(i + 1, b) for i, b in enumerate(BOOKS))
    faq = [("Are these affiliate links?", "Yes. If you buy through them we may earn a small commission, at no extra cost to you. Our book guides are written for families, not for commissions."),
           ("Can I borrow these books instead?", "Most public libraries stock them. See our guide to children’s books and your local library for how to join and borrow."),
           ("Which edition should I buy?", "Check the age range, the format (paperback, hardback or board book) and whether it is the full-size or a mini edition before you order."),
           ("Do these ship to Ireland?", "Amazon.ie serves Ireland, but availability and delivery times change, so check the product page before you order.")]
    faq_html = '<section class="faq"><h2>Frequently asked questions</h2>' + "".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q, a in faq) + "</section>"
    page = f"""title: Buy Children’s Books in Ireland | 10 Favourites
h1: Buy children’s books online in Ireland: 10 favourites
short: Buy children’s books
description: Ten much-loved children’s books to buy online in Ireland, with ages, short summaries and links to check price and availability on Amazon.ie.
kind: guide
nav: /guides/
parent: guides
image: banner-best-childrens-books-of-all-time
alt: Two bookcases full of colourful books either side of an open book, a golden trophy and stars
lede: Ten enduring favourites for reading together, bedtime or a first home library, with a link to check each one on Amazon.ie.
related: best-childrens-books-of-all-time,top-20-childrens-books,childrens-book-gift-guide,build-a-childrens-home-library-on-a-budget
updated: 2026-11-14
---
<p>Choosing children’s books is hard when there are thousands of titles. These ten are popular, enduring and easy to enjoy. Each card shows the age we suggest, and links to a longer guide where we have one. Links go to Amazon.ie so you can check the current price and availability.</p>
<p class="small"><strong>Disclosure:</strong> As an Amazon Associate we earn from qualifying purchases. See <a href="/about/">About</a>.</p>
<h2>10 children’s books kids will love</h2>
<ol class="shopgrid">
{cards}
</ol>
<h2>Tips before you buy</h2>
<ul>
<li><strong>Check the age.</strong> Board books suit babies and toddlers, picture books suit about 2 to 7, and novels suit confident readers.</li>
<li><strong>Look at the format.</strong> Paperbacks are cheaper, hardbacks last longer and board books survive chewing.</li>
<li><strong>Borrow first.</strong> If you are unsure, try it from the library. See our guide to <a href="/childrens-books-and-your-local-library/">children’s books and your local library</a>.</li>
<li><strong>Want more ideas?</strong> See our <a href="/childrens-book-gift-guide/">gift guide</a>, the <a href="/best-childrens-books-of-all-time/">best children’s books of all time</a> and the <a href="/top-20-childrens-books/">Top 20 children’s books</a>.</li>
</ul>
{faq_html}
"""
    with open(os.path.join(ROOT, "content", "childrens-books-on-amazon-ireland.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    print("wrote shop page")


if __name__ == "__main__":
    main()
