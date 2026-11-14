#!/usr/bin/env python3
"""Banners for three books on the Amazon Ireland page that have no guide: props and settings only."""
from illustrations import *  # noqa: F401,F403
from illustrations_classics import ground  # noqa: F401
W, H = 1200, 400


def room_on_broom():
    b = rect(0, 0, W, H, "#27336b", 0, 0) + starfield([(100, 60), (250, 130), (400, 50), (700, 60), (900, 120), (1100, 70)], 8) + moon(1000, 90, 44)
    b += g(path("M-260,0 H260", sw=12, stroke=WOOD_DK) + path("M260,0 q60,-20 90,-30 M260,0 q60,0 96,6 M260,0 q56,20 90,40", sw=6, stroke="#d6a23a"), 600, 230, 1, -6)
    b += g(poly([(-50, 0), (50, 0), (0, -120)], PURPLE, 4) + path("M-70,0 h140", sw=9) + rect(-50, -22, 100, 12, BUTTER, 3, 2.5), 360, 190, 1, -10)
    b += g(path("M-60,0 q-10,-60 60,-60 q70,0 60,60 q-30,30 -60,30 q-30,0 -60,-30 z", "#3a3a4a", 4) + ell(0, -60, 60, 14, "#7ed957", 3.5) + "".join(circ(x, -76, r, "#bff0a0", 2.5) for x, r in [(-20, 8), (14, 10), (34, 6)]), 820, 350, 1.3)
    save("shop-room-on-the-broom", W, H, b)


def snail_whale():
    b = rect(0, 0, W, H, "#9fd8ee", 0, 0) + path("M0,90 q100,-30 200,0 t200,0 t200,0 t200,0 t200,0 t200,0 V400 H0 z", "#3a8fd1", 4)
    b += whale(560, 250, 1.8) + g(circ(0, 0, 48, "#7cc7f2", 4) + path("M-48,0 h96 M0,-48 v96 M-34,-34 q34,34 68,0 M-34,34 q34,-34 68,0", sw=2.5), 1030, 190, 1.1)
    b += ground(350, "#e8d8a5") + g(circ(0, 0, 30, "#e6a8c9", 4) + path("M0,0 m-18,0 a18,18 0 1,1 18,18 a10,10 0 1,1 -10,-10", sw=3), 190, 340, 1.1) + ell(120, 372, 60, 22, "#8a8a9a", 0, 4)
    save("shop-snail-and-the-whale", W, H, b)


def giving_tree():
    b = rect(0, 0, W, 300, "#d6efff", 0, 0) + ground(300, "#7cc46a") + sun(1060, 80, 40) + cloud(200, 70, 1)
    b += g(rect(-34, -170, 68, 170, WOOD_DK, 5) + blob([("c", 0, -240, 120), ("c", -110, -190, 84), ("c", 110, -190, 84), ("c", 0, -180, 90)], "#3a9d62") + "".join(apple(x, y, 1) for x, y in [(-70, -230), (40, -270), (90, -190), (-20, -170)]), 600, 330, 1.2)
    b += g(path("M-4,0 v-110", sw=5) + rect(-24, -110, 48, 8, WOOD, 3), 760, 340, 1.0) + path("M730,230 v110 M790,230 v110", sw=4) + rect(724, 340, 72, 18, WOOD, 4) + rect(190, 330, 80, 30, WOOD, 6) + ell(230, 330, 40, 10, "#e6c98a", 0, 4)
    save("shop-the-giving-tree", W, H, b)


def apple(x, y, s=1):
    return g(circ(0, 0, 16, BERRY, 3) + path("M0,-16 q2,-10 8,-12", sw=3), x, y, s)


for f in (room_on_broom, snail_whale, giving_tree):
    f()
print("ok")
