#!/usr/bin/env python3
"""Banner for the all-time top 20 page: a tall bookcase, a trophy and stars."""
from illustrations import *  # noqa: F401,F403
from illustrations_top20 import trophy_ball  # noqa: F401

W, H = 1200, 400
b = rect(0, 0, W, 330, "#fff1d6", 0, 0) + rect(-4, 330, W + 8, 80, "#c58a50", 0, 4)
b += bookcase(80, 60, 360, 270, 3, 5) + bookcase(760, 60, 360, 270, 3, 11)
b += book_open(600, 250, 200, 90, BERRY) + trophy_ball(600, 150, 1.2)
b += "".join(star(x, y, r, c) for x, y, r, c in [(500, 70, 20, BUTTER), (700, 60, 24, PINK), (560, 30, 14, BLUE), (650, 28, 16, BUTTER)])
save("banner-best-childrens-books-of-all-time", W, H, b)
print("ok")
