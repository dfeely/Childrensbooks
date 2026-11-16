#!/usr/bin/env python3
"""Create small redirect pages for old URLs (from the previous bookshop) so they stop returning 404.

GitHub Pages cannot do server redirects, so each old path gets an index.html that sends visitors (and search
engines) to the closest new page using a canonical link and an instant meta refresh.

    python3 tools/gen_redirects.py
"""
import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SITE = "https://www.childrensbooks.ie"

MAP = {
 "alice-in-wonderland": "/alices-adventures-in-wonderland/",
 "ark-angel": "/alex-rider-books-in-order/",
 "artemis-fowl-p-b": "/artemis-fowl-books-in-order/",
 "artemis-fowl-the-atlantis-complex-p-b": "/artemis-fowl-books-in-order/",
 "bluey-lets-play-outside-": "/best-bluey-books-for-kids/",
 "bluey-wheres-bluey-": "/best-bluey-books-for-kids/",
 "bluey-the-pool-board-book": "/best-bluey-books-for-kids/",
 "charlie-and-the-chocolate-factory-": "/charlie-and-the-chocolate-factory/",
 "crow(barrington-stokes)": "/how-to-help-a-reluctant-reader/",
 "death-note-black-3-": "/books-by-age/",
 "dk-childrens-encyclopedia-": "/books-by-age/",
 "dolphin-adventure": "/books-by-age/",
 "enormous-turnip-ladybird-tales-h-b": "/best-nursery-rhyme-and-fairy-tale-books/",
 "goodnight-farm-board-book": "/best-nursery-rhyme-and-fairy-tale-books/",
 "goodnight-peppa": "/best-peppa-pig-books/",
 "heidi-p-b-n-e-puffin-classic": "/best-classic-childrens-novels/",
 "hugless-douglas-p-b": "/books-for-preschoolers/",
 "king-henry-": "/irish-childrens-authors/",
 "kings-of-the-boyne-": "/irish-childrens-authors/",
 "ladybird-first-favourite-nursery-rhymes": "/best-ladybird-books-for-children/",
 "ladybird-key-words-flashcards": "/best-ladybird-books-for-children/",
 "ladybird-stories-for-3-year-olds-h-b": "/best-ladybird-books-for-children/",
 "lbird-2b-have-a-go": "/best-ladybird-books-for-children/",
 "lbird-3a-things-we-like": "/best-ladybird-books-for-children/",
 "little-women(-sisterhood-edition)": "/best-classic-childrens-novels/",
 "magic-porridge-pot-ladybird-tales-h-b": "/best-nursery-rhyme-and-fairy-tale-books/",
 "monsters-of-men-10th-anniversary-edition-": "/books-by-age/",
 "my-box-of-bedtime-stories-": "/best-nursery-rhyme-and-fairy-tale-books/",
 "pencil-(10th-anniversary-edition)-": "/books-by-age/",
 "peppa-pig-i-love-you-mummy-pig-": "/best-peppa-pig-books/",
 "peppa-pig-peppa-and-friends-board-book": "/best-peppa-pig-books/",
 "peppa-pig-peppa-goes-to-the-library-board": "/best-peppa-pig-books/",
 "peppa-pig-peppa-washing-day-board-book": "/best-peppa-pig-books/",
 "percy-jackson-and-the-lightning-thief": "/percy-jackson-books-in-order/",
 "queenie": "/books-by-age/",
 "rosie-frost-and-the-falcon-queen-": "/books-by-age/",
 "twinkle-twinkle-little-star_16631": "/best-nursery-rhyme-and-fairy-tale-books/",
 "bedtime-stories-_24736": "/bedtime-stories-for-children/",
 "ladybird-9780007115167": "/best-ladybird-books-for-children/",
 "little-red-riding-hood_18486": "/best-nursery-rhyme-and-fairy-tale-books/",
 "index.php": "/",
}

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Page moved | childrensbooks.ie</title>
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow">
<link rel="canonical" href="{url}"><meta http-equiv="refresh" content="0; url={url}">
<script>location.replace({url!r});</script></head>
<body style="font-family:Arial,sans-serif;padding:2rem"><p>This page has moved. <a href="{url}">Continue to the new page</a>.</p></body></html>
"""


def main():
    n = 0
    for old, new in MAP.items():
        d = os.path.join(ROOT, old)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(TEMPLATE.format(url=SITE + new))
        n += 1
    print(f"wrote {n} redirects")


if __name__ == "__main__":
    main()
