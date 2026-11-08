#!/usr/bin/env python3
"""Original 1200x400 portrait scenes for the author pages. These are generic cartoon writers at a desk,
with props that hint at the author's work. They are NOT likenesses of the real people.

    python3 tools/illustrations_authors.py
"""
from illustrations import *  # noqa: F401,F403
from illustrations_top20 import (dog, donut, ghostie, toast, frog, lilypad, football, boot, magnifier,
                                 mountains, notebook, trophy_ball, giraffe, mic_stage, binder)  # noqa: F401
from illustrations_christmas import cottage, holly  # noqa: F401

W, H = 1200, 400
SKINS = ["#f5d0b0", "#e8b48a", "#c68b5e", "#8d5a3b", "#f1c9a5"]


def hair(style, c, cx, cy, r):
    if style == "short":
        return path(f"M{cx - r},{cy - 4} q0,-{r + 14} {r},-{r + 14} q{r},0 {r},{r + 14} q-{r * .6},-{r * .5} -{r * 2},0 z", c, 4)
    if style == "long":
        return (path(f"M{cx - r - 6},{cy + r + 24} q-10,-{r * 2 + 20} {r + 6},-{r * 2 + 18} q{r + 16},0 {r + 6},{r * 2 + 18} v8 h-12 q0,-{r + 10} -{r + 6},-{r + 18} q-{r + 6},{r + 8} -{r + 6},{r + 10} v-8 z", c, 4))
    if style == "bun":
        return circ(cx, cy - r - 12, 16, c, 4) + path(f"M{cx - r},{cy - 2} q0,-{r + 8} {r},-{r + 8} q{r},0 {r},{r + 8} q-{r * .5},-{r * .6} -{r * 2},0 z", c, 4)
    if style == "curly":
        return blob([("c", cx - r * .7, cy - r * .7, r * .5), ("c", cx, cy - r * .95, r * .55), ("c", cx + r * .7, cy - r * .7, r * .5)], c, 4)
    if style == "cap":
        return path(f"M{cx - r - 2},{cy - 8} q0,-{r + 10} {r + 2},-{r + 10} q{r + 2},0 {r + 2},{r + 10} z", BLUE, 4) + path(f"M{cx + 4},{cy - 10} h{r + 20}", sw=8, stroke=INK)
    return ""


def writer(x, y, skin=0, hc="#4a3426", style="short", shirt=BLUE, glasses=False, s=1.0):
    r = 44
    b = path("M-70,0 v-36 q0,-52 70,-52 q70,0 70,52 v36 z", shirt, 4)
    b += rect(-12, -112, 24, 28, SKINS[skin], 4)
    b += circ(0, -150, r, SKINS[skin], 4)
    b += hair(style, hc, 0, -150, r)
    b += dot(-15, -146, 4.5) + dot(15, -146, 4.5) + path("M-14,-128 q14,12 28,0", sw=3.5)
    if glasses:
        b += circ(-15, -146, 11, "none", 3) + circ(15, -146, 11, "none", 3) + path("M-4,-146 h8", sw=3)
    return g(b, x, y, s)


def desk(y=300):
    return rect(-4, y, W + 8, H - y + 4, WOOD, 0, 4) + rect(-4, y, W + 8, 16, WOOD_DK, 0, 4)


def pencil(x, y, rot=-30, c=BUTTER):
    return g(rect(-4, -60, 18, 120, c, 3, 3) + poly([(-4, 60), (14, 60), (5, 82)], "#f1cf9b", 3) + rect(-4, -74, 18, 16, PINK, 3, 3), x, y, 1, rot)


def lamp(x, y):
    return g(path("M0,0 v-90 l50,-50", sw=7) + poly([(30, -150), (84, -128), (68, -104), (20, -126)], BUTTER, 4) + ell(0, 0, 36, 10, INK, 0, 3), x, y)


def stack(x, y, n=3, cols=(BERRY, MEADOW, BLUE)):
    b = ""
    for i in range(n):
        b += rect(x, y - 30 * (i + 1), 140 - i * 10, 30, cols[i % len(cols)], 5)
        b += rect(x + 12, y - 30 * (i + 1) + 11, 30, 8, PAPER, 2, 2.5)
    return b


def scene(name, bg, fig, props, wall="#fff"):
    b = rect(0, 0, W, 300, bg, 0, 0) + desk() + fig + props
    save(name, W, H, b)


def a_kinney():
    b = rect(60, 60, 150, 190, "#fff", 4) + "".join(path(f"M80,{90 + i * 30} h110", sw=3, stroke="#c8d3e6") for i in range(5))
    b += notebook(760, 330, 190, 130, -4, PAPER, BUTTER) + pencil(980, 320, 70)
    scene("author-jeff-kinney", "#dfe9f5", writer(520, 300, 0, "#8a6a3a", "short", BLUE, False, 1.3) + b, "")


def a_donaldson():
    b = sun(1030, 90, 38) + hills(W, 300, [(200, "#b8e3b0", 14, .2)]) + tree(150, 300, 1.4) + tree(1080, 300, 1.2, "#3a9d62")
    b += stack(780, 300, 3) + flower(930, 296, BERRY, 1.1) + flower(270, 296, BUTTER)
    scene("author-julia-donaldson", "#d6efff", b + writer(520, 300, 0, "#c9c9c9", "bun", BERRY, True, 1.3), "")


def a_smart():
    b = g(ell(0, 0, 70, 44, "#ffffff") + ell(-40, -52, 14, 44, "#ffffff", -10) + ell(-10, -56, 14, 44, "#ffffff", 8) + dot(-26, 0, 5) + dot(10, 0, 5), 800, 280, 1.1)
    b += star(960, 120, 30) + star(180, 100, 22, PINK) + star(1080, 240, 18, "#ffffff")
    b += g(circ(0, 0, 46, "#a8743f") + circ(0, 12, 28, "#f1cf9b", 3) + dot(-12, -8, 5) + dot(12, -8, 5), 920, 270, 1)
    scene("author-jamie-smart", "#f6d5ff", writer(480, 300, 0, "#2b2b2b", "curly", PURPLE, False, 1.3) + b, "")


def a_kirby():
    b = stack(720, 300, 4, (PINK, BERRY, BLUE, BUTTER)) + notebook(900, 330, 190, 120, 6, "#ffe0ec", BERRY)
    b += star(150, 110, 24, BUTTER) + star(1060, 100, 26, PINK) + path("M640,120 q30,-40 60,0 q30,40 60,0", sw=5, stroke=BERRY)
    scene("author-katie-kirby", "#ffe8f0", writer(480, 300, 0, "#c98a4b", "long", "#ff8fb1", False, 1.3) + b, "")


def a_ocallaghan():
    b = rect(0, 0, W, 300, "#b8e3b0", 0, 0)
    b += rect(920, 70, 10, 230, WHITE, 3) + rect(1040, 70, 10, 230, WHITE, 3) + path("M920,70 h130", sw=10, stroke=WHITE)
    b += football(760, 270, 34) + football(200, 280, 26) + desk() + writer(500, 300, 1, "#7a4a2a", "short", MEADOW, False, 1.3)
    save("author-donncha-ocallaghan", W, H, b)


def a_cameron():
    b = donut(760, 230, 62, BERRY) + donut(900, 270, 44, "#7cc7f2") + donut(1030, 215, 38, BUTTER) + g(rect(-36, -50, 72, 86, "#d7dbe5", 8) + circ(0, -20, 12, "#6fd0f0", 3) + dot(-12, -50, 4) + dot(12, -50, 4), 220, 290, 1.1)
    scene("author-neill-cameron", "#fff0d9", writer(500, 300, 0, "#3a2a20", "short", "#ec7a2e", True, 1.3) + b, "")


def a_evanne():
    b = rect(0, 0, W, 300, "#9ed8a0", 0, 0) + rect(0, 210, W, 6, WHITE, 0, 0)
    b += rect(880, 80, 10, 220, WHITE, 3) + rect(1060, 80, 10, 220, WHITE, 3) + path("M880,80 h190", sw=10, stroke=WHITE)
    b += circ(780, 270, 22, "#fff7d6", 3.5) + path("M200,300 v-90 M170,210 h60", sw=6) + desk() + mic_stage(280, 300)
    b += writer(520, 300, 0, "#6a3a22", "long", BERRY, False, 1.3)
    save("author-evanne-ni-chuilinn", W, H, b)


def a_leona():
    b = cloud(160, 80, 1) + cloud(980, 70, .9) + shamrock(1000, 296, 1.1) + shamrock(200, 296, .9)
    b += g(path("M-40,0 v-60 q0,-30 40,-30 q40,0 40,30 v60 z", PINK, 4) + dot(-10, -50, 4) + dot(10, -50, 4) + path("M-8,-36 q8,8 16,0", sw=3), 800, 300, 1.1)
    b += stack(880, 300, 3, (BLUE, BERRY, MEADOW))
    scene("author-leona-forde", "#d6efff", b + writer(500, 300, 0, "#b5651d", "long", PURPLE, False, 1.3), "")


def a_corbett():
    b = ghostie(780, 270, 1.2) + toast(930, 300, 1.2) + star(1060, 120, 24) + star(210, 110, 20, "#ffffff")
    scene("author-phil-corbett", "#2d3a6e", writer(500, 300, 0, "#8a8a8a", "short", "#ff8a3c", True, 1.3) + b, "")


def a_riordan():
    b = mountains(W, 300, "#8fb3d9") + path("M740,300 v-150 M700,300 v-120 M780,300 v-120 M820,300 v-90 M680,150 h160", sw=8)
    b += rect(700, 156, 100, 16, "#e8e2d0", 3) + g(path("M-30,0 v-40 q0,-40 30,-40 q30,0 30,40 v40 z", "#ffd24a", 4), 980, 300, 1.1)
    b += trophy_ball(180, 300, 1)
    scene("author-rick-riordan", "#e9f0ff", b + writer(480, 300, 0, "#5a4632", "short", "#ec7a2e", False, 1.3), "")


def a_gough():
    b = lilypad(780, 290, 90) + frog(790, 282, 1.1) + lilypad(960, 296, 70) + frog(965, 290, .8, "#7bd08a")
    b += path("M600,300 q90,-30 180,0", sw=0) + shamrock(190, 296, 1)
    scene("author-julian-gough", "#cfe8ff", b + writer(480, 300, 0, "#4a3426", "short", MEADOW, True, 1.3), "")


def a_bowie():
    b = notebook(720, 330, 200, 130, -6, PAPER, BERRY) + pencil(960, 320, 40, BLUE)
    b += "".join(rect(60 + i * 72, 70, 60, 60, c, 4) for i, c in enumerate([BUTTER, PINK, "#7cc7f2"])) + "".join(path(f"M{70 + i * 72},{100} h40", sw=3) for i in range(3))
    scene("author-sarah-bowie", "#fff3c9", writer(500, 300, 0, "#a0522d", "bun", "#2aa7a0", False, 1.3) + b, "")


def a_pilkey():
    b = dog(800, 300, 1.3, "#f4f0e6", False, "#3d3a4f") + star(1000, 120, 26) + star(170, 90, 22, BERRY)
    b += g(path("M-40,0 h80 l-20,-70 h-40 z", "#ffffff", 4) + path("M-30,-70 q30,-40 60,0", "#ffffff", 4), 960, 290, 0.0)
    scene("author-dav-pilkey", "#ffe9b8", writer(480, 300, 0, "#3a3a3a", "short", BERRY, False, 1.3) + b, "")


def a_ahern():
    b = magnifier(780, 160, 1, 56) + g(rect(-18, -60, 36, 60, "#d7dbe5", 6) + dot(-6, -40, 4) + dot(6, -40, 4) + path("M-6,-26 q6,6 12,0", sw=3), 940, 300, 1.2)
    b += g(circ(0, -30, 30, BUTTER) + dot(-8, -34, 4) + dot(8, -34, 4) + path("M-8,-20 q8,8 16,0", sw=3), 1050, 300, 1.1) + star(200, 100, 22)
    scene("author-cecelia-ahern", "#e9defa", b + writer(480, 300, 0, "#c9822e", "long", PURPLE, False, 1.3), "")


def a_fletcher():
    b = rect(0, 0, W, 300, "#27336b", 0, 0) + "".join(star(x, y, r, c) for x, y, r, c in [(120, 70, 16, BUTTER), (240, 140, 12, WHITE), (1000, 80, 18, BUTTER), (1100, 170, 12, WHITE)])
    b += mic_stage(860, 300) + g(path("M0,0 v-110 M-20,-80 h40", sw=6) + ell(0, -118, 34, 22, "#d7dbe5", 0, 4), 1040, 300, 1.1) + desk()
    b += writer(500, 300, 0, "#c98a4b", "short", "#ec7a2e", False, 1.3)
    save("author-tom-fletcher", W, H, b)


def a_oldfield():
    b = rect(0, 0, W, 300, "#8fd08a", 0, 0) + rect(0, 150, W, 6, WHITE, 0, 0) + circ(600, 153, 60, "none", 6).replace("#1f2a44", WHITE)
    b += football(800, 270, 36) + boot(980, 296, 1) + trophy_ball(180, 300, 1) + desk()
    b += writer(520, 300, 0, "#5a4632", "short", BLUE, False, 1.3)
    save("author-matt-oldfield", W, H, b)


def a_pichon():
    b = notebook(720, 330, 210, 140, -5, PAPER, BERRY) + pencil(980, 320, 60, BERRY)
    b += g(path("M0,0 l30,-50 l30,50 z", BUTTER, 4) + path("M12,-20 h36", sw=3), 160, 290, 1) + "".join(star(x, y, 16, c) for x, y, c in [(1050, 110, BUTTER), (260, 90, PINK)])
    scene("author-liz-pichon", "#ffeed6", writer(500, 300, 0, "#7a3a2a", "curly", "#2aa7a0", False, 1.3) + b, "")


def a_hub():
    b = rect(0, 0, W, 300, "#e8f4f8", 0, 0) + desk()
    specs = [(0, "#4a3426", "short", BLUE, False), (1, "#2b2b2b", "long", BERRY, True), (2, "#8a6a3a", "curly", MEADOW, False),
             (3, "#c9c9c9", "bun", PURPLE, True), (4, "#a0522d", "short", "#ec7a2e", False)]
    for i, (sk, hc, st, sh, gl) in enumerate(specs):
        b += writer(160 + i * 220, 300, sk, hc, st, sh, gl, 1.0)
    b += stack(1050, 300, 3) if False else ""
    b += star(80, 80, 20) + star(1120, 70, 22, PINK) + book_open(600, 26, 110, 44, BLUE)
    save("banner-childrens-book-authors", W, H, b)


ALL = [a_kinney, a_donaldson, a_smart, a_kirby, a_ocallaghan, a_cameron, a_evanne, a_leona, a_corbett, a_riordan, a_gough,
       a_bowie, a_pilkey, a_ahern, a_fletcher, a_oldfield, a_pichon, a_hub]

if __name__ == "__main__":
    for fn in ALL:
        fn()
    print("author illustrations written:", len(ALL))
