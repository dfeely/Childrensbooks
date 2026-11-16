#!/usr/bin/env python3
"""Eight 1200x400 banners for the series and title pages (settings and generic props only)."""
from illustrations import *  # noqa: F401,F403
from illustrations_classics import ground, lantern, teapot, pot, balloon, leafy, castle  # noqa: F401
from illustrations_top20 import mountains, magnifier, football  # noqa: F401
W, H = 1200, 400


def artemis():
    b = rect(0, 0, W, H, "#1f2a3a", 0, 0) + "".join(star(x, y, r, c) for x, y, r, c in [(120, 70, 14, BUTTER), (300, 130, 10, "#fff"), (900, 70, 16, BUTTER), (1080, 150, 10, "#fff")])
    b += ground(300, "#2d5b4a") + "".join(g(poly([(0, -50), (28, -20), (0, 20), (-28, -20)], c, 4) + path("M-28,-20 h56 M0,-50 L0,20", sw=2.5), x, y, s) for x, y, s, c in [(260, 330, 1.4, "#58d3a2"), (360, 350, 1.0, BLUE), (840, 340, 1.5, PINK), (950, 350, 1.0, BUTTER)])
    b += "".join(ell(x, 360, 24, 8, BUTTER, 0, 3) for x in (500, 540, 580, 620, 660, 700)) + g(path("M0,0 q-20,-70 -60,-70 q20,40 60,70 q40,-30 60,-70 q-40,0 -60,70", "#bfeaff", 3.5), 600, 230, 1.6) + lantern(1080, 330, 1.4)
    save("series-artemis-fowl", W, H, b)


def percy():
    b = rect(0, 0, W, H, "#cfe9ff", 0, 0) + sun(1050, 80, 40) + hills(W, H, [(260, "#b8e3b0", 14, .2)]) + path("M-10,320 q100,-30 200,0 t200,0 t200,0 t200,0 t200,0 t200,0 V400 H-10 z", "#3a8fd1", 4)
    b += "".join(rect(x, 140, 40, 170, "#f3ead6", 4) + rect(x - 6, 130, 52, 14, "#e2d6b8", 4) + rect(x - 6, 306, 52, 14, "#e2d6b8", 4) for x in (420, 520, 620, 720)) + poly([(400, 130), (780, 130), (590, 60)], "#e2d6b8", 4)
    b += g(path("M0,0 v-150 M-26,-150 q26,-40 52,0 M-26,-150 v-30 M0,-150 v-40 M26,-150 v-30", sw=7), 950, 330, 1.2)
    save("series-percy-jackson", W, H, b)


def alex():
    b = rect(0, 0, W, H, "#1b2340", 0, 0) + moon(1050, 80, 40) + "".join(rect(x, 400 - h, 70, h, c, 4) + "".join(rect(x + 12 + (i % 2) * 28, 400 - h + 20 + (i // 2) * 34, 14, 18, BUTTER, 2, 2.5) for i in range(int(h / 34) * 2 - 2)) for x, h, c in [(80, 250, "#2d3a66"), (180, 190, "#3a4a80"), (280, 280, "#2d3a66"), (800, 220, "#3a4a80"), (900, 300, "#2d3a66"), (1000, 180, "#3a4a80")])
    b += poly([(560, 400), (600, 400), (700, 40), (500, 40)], "#fff6b8", 0) + rect(540, 320, 140, 80, "#3a3a4a", 8) + rect(590, 306, 40, 18, "#3a3a4a", 5) + circ(610, 350, 10, BUTTER, 3)
    save("series-alex-rider", W, H, b)


def bluey():
    b = sun(1060, 80, 40) + cloud(220, 70, 1) + hills(W, H, [(250, "#b8e3b0", 14, .2)]) + ground(300, "#7cc46a")
    b += "".join(rect(x, 190, 14, 120, WOOD, 3) for x in range(0, 1200, 120)) + path("M0,210 H1200 M0,260 H1200", sw=7, stroke=WOOD)
    b += g(circ(0, 0, 30, "#ff8fb1", 4) + path("M-30,0 q30,-18 60,0 M0,-30 q-18,30 0,60", sw=3), 330, 350, 1.2) + g(path("M0,0 v-160 M-80,-160 h160", sw=7) + path("M-60,-160 v90 h30 v-90 M30,-160 v90 h30 v-90", sw=4, stroke=WOOD_DK), 700, 320, 1) + rect(670, 250, 60, 10, BERRY, 3) + football(900, 350, 30) + flower(1000, 360, BERRY) + flower(1080, 364, BUTTER)
    save("series-bluey", W, H, b)


def peppa():
    b = rect(0, 0, W, H, "#bcd3e6", 0, 0) + cloud(240, 80, 1.6, "#9fb3c7") + cloud(700, 70, 1.4, "#9fb3c7") + cloud(1020, 100, 1.2, "#9fb3c7") + "".join(path(f"M{x},{y} l-10,26", sw=3, stroke="#5a8fc7") for x in range(60, 1200, 70) for y in (140, 220))
    b += ground(310, "#7cc46a") + "".join(ell(x, 350, 100, 24, "#8fc5ff", 0, 4) for x in (260, 640, 980)) + "".join(g(path("M-18,0 v-60 h30 v60 q0,10 -14,10 h-32 q-6,0 -6,-10z", "#e23b3b", 4) + rect(-18, -60, 30, 10, "#fff", 3), x, 340, 1.2) for x in (150, 800, 1100))
    b += g(path("M-80,0 q80,-110 160,0 z", "#d6336c", 4) + path("M0,-40 v90 q0,16 18,16", sw=5), 470, 300, 1)
    save("series-peppa-pig", W, H, b)


def ladybird():
    def bug(x, y, s=1):
        return g(ell(0, 0, 48, 40, "#e23b3b", 0, 4) + path("M0,-40 v80", sw=3.5) + circ(0, -42, 18, INK, 3) + "".join(dot(px, py, 6, INK) for px, py in [(-24, -10), (24, -10), (-26, 14), (26, 14), (-10, 24), (10, 24)]) + path("M-8,-58 q-14,-18 -24,-16 M8,-58 q14,-18 24,-16", sw=3), x, y, s)
    b = rect(0, 0, W, 300, "#e9f7ec", 0, 0) + ground(300, "#5cb86f") + leafy(160, 330, 2.0) + leafy(1040, 330, 2.0) + bug(300, 260, 1.5) + bug(900, 250, 1.2)
    b += "".join(g(rect(0, 0, 130, 90, "#fff", 8) + txt(65, 56, t, 30, INK), x, 150, 1, r) for x, t, r in [(450, "a", -6), (590, "b", 4), (730, "c", -3)]) + book_open(600, 350, 200, 70, BLUE)
    save("series-ladybird", W, H, b)


def classics():
    b = rect(0, 0, W, 300, "#e9f0ff", 0, 0) + mountains(W, 300, "#8fb3d9") + sun(1060, 70, 36) + ground(300, "#7cc46a") + cottage_house(260, 330) + tree(560, 330, 1.4) + tree(1000, 330, 1.2)
    b += book_stack(700, 380, 3) if False else "" + book_open(780, 360, 220, 90, MEADOW)
    save("series-classic-novels", W, H, b)


def cottage_house(x, y):
    return g(rect(-80, -90, 160, 90, "#fff6e0", 4) + poly([(-100, -90), (100, -90), (0, -160)], BERRY, 4) + rect(-16, -50, 32, 50, WOOD_DK, 3) + rect(-62, -66, 30, 30, "#cfe9ff", 3) + rect(32, -66, 30, 30, "#cfe9ff", 3), x, y, 1.5)


def nursery():
    b = rect(0, 0, W, H, "#27336b", 0, 0) + moon(1000, 90, 46) + "".join(star(x, y, r, c) for x, y, r, c in [(120, 70, 20, BUTTER), (260, 150, 14, "#fff"), (480, 80, 18, PINK), (760, 60, 16, BUTTER), (860, 160, 12, "#fff")])
    b += ground(310, "#2d5b4a") + g(path("M-70,0 q-24,-70 70,-70 q94,0 70,70 q-40,24 -70,24 q-30,0 -70,-24 z", "#3a3a4a", 4) + ell(0, -70, 70, 16, "#f1cf9b", 3.5), 300, 340, 1.3)
    b += g(path("M0,0 q-50,-40 0,-110 q50,70 0,110 z", "#fff1e6", 4) + path("M0,-110 q-10,-26 -20,-30 M0,-110 q10,-26 20,-30", sw=4, stroke=MEADOW) + ell(0, -90, 24, 12, "#c264d6", 0, 0), 620, 340, 1.4)
    b += g(rect(-60, -50, 120, 50, "#c9a46b", 8) + path("M-60,-34 h120 M-60,-18 h120", sw=2.5, stroke="#a8743f") + path("M-48,-50 q48,-70 96,0", sw=6), 900, 340, 1.2)
    save("series-nursery-fairy-tales", W, H, b)


for f in (artemis, percy, alex, bluey, peppa, ladybird, classics, nursery):
    f()
print("ok")
