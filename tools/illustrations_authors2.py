#!/usr/bin/env python3
"""Generic cartoon-writer portraits for the classic authors (not likenesses).   python3 tools/illustrations_authors2.py"""
from illustrations_authors import *  # noqa: F401,F403
from illustrations_classics import (teapot, cup, castle, barn, web, apple, butterfly, boat, pot, balloon, lollipop, cake_stand,  # noqa: F401
                                    blossom_tree, lantern, scroll, window, leafy, strawberry)

from illustrations_classics import candle, pine, snowflakes, lamp_post, mountains, cottage, moon_bg  # noqa: F401
from illustrations_authors import lamp as _lamp  # noqa: F401


def sc(name, bg, fig, props):
    save(name, W, H, rect(0, 0, W, 300, bg, 0, 0) + desk() + props + fig)


def P(name, bg, props, skin=0, hc="#4a3426", style="short", shirt=BLUE, gl=False):
    sc(name, bg, writer(500, 300, skin, hc, style, shirt, gl, 1.3), props)


def run():
    P("author-jk-rowling", "#27336b", "".join(star(x, y, r, c) for x, y, r, c in [(120, 60, 14, BUTTER), (1000, 80, 18, BUTTER), (1100, 160, 12, WHITE), (240, 140, 10, WHITE)]) + "".join(candle(x, y, .8) for x, y in [(760, 120), (840, 80), (920, 140)]) + stack(220, 300, 3, (BERRY, PURPLE, BLUE)), 0, "#c9822e", "long", PURPLE)
    P("author-eric-carle", "#d6efff", apple(760, 300, 1.4) + strawberry(850, 300, 1.4) + butterfly(940, 150, 1.4) + leafy(200, 300, 1.3) + sun(1060, 80, 36), 0, "#d9d9d9", "short", MEADOW, True)
    P("author-maurice-sendak", "#1e4a5a", moon_bg() + circ(960, 110, 60, "#fff3d6", 4) + boat(820, 300, .8) + tree(180, 300, 1.2, "#2a8a55"), 0, "#6a6a6a", "short", BERRY, True)
    P("author-eb-white", "#d6efff", barn(250, 300, 1.2) + web(900, 190, 80) + rect(800, 190, 10, 110, WOOD, 3) + rect(1000, 190, 10, 110, WOOD, 3) + sun(1080, 70, 34), 0, "#8a8a8a", "short", "#2a7aa0", True)
    P("author-cs-lewis", "#c9d9ea", pine(780, 300, 1.4) + pine(900, 300, 1.7) + pine(1020, 300, 1.3) + snowflakes([(700, 90, 12), (860, 60, 10), (1000, 110, 12), (180, 90, 10)]) + lamp_post(1100, 300, 1) + rect(130, 120, 130, 180, WOOD, 6) + rect(146, 136, 98, 148, "#dce8f5", 0, 3), 0, "#6a6a6a", "short", "#8a5a3a")
    P("author-roald-dahl", "#ffe0ec", lollipop(740, 300, 1.4) + lollipop(820, 300, 1.2, BLUE) + g(rect(-60, -34, 120, 68, BUTTER, 5) + txt(0, -4, "GOLDEN", 18, INK) + txt(0, 20, "TICKET", 18, INK), 960, 120, 1, -8) + ell(1060, 260, 36, 32, "#ffb98a", 0, 4), 0, "#7a6a5a", "short", "#2a7aa0")
    P("author-margaret-wise-brown", "#8fc9a0", window(100, 60, 200, 160, "#27336b") + moon(200, 140, 34) + g(path("M0,0 v-50 l-20,-20 h40 l-20,20", sw=0) + poly([(-30, -90), (30, -90), (44, -50), (-44, -50)], BUTTER, 4) + rect(-6, -50, 12, 50, WOOD, 3), 830, 300, 1) + circ(980, 190, 44, WHITE, 5) + path("M980,190 v-30 M980,190 l20,10", sw=4), 0, "#5a3a2a", "bun", "#d6336c")
    P("author-lewis-carroll", "#d9cff5", rect(700, 262, 440, 16, WHITE, 5) + teapot(790, 262, 1, PURPLE) + cup(900, 262) + cup(980, 262) + "".join(g(rect(-18, -54, 36, 54, WHITE, 4) + txt(0, -26, s, 28, c), x, 300, 1, r) for x, s, c, r in [(1070, "♥", "#d6336c", -5), (1130, "♠", INK, 5)]) + g(circ(0, 0, 40, WHITE, 4) + path("M0,0 v-26 M0,0 l16,8", sw=4), 200, 200, 1), 0, "#4a3426", "short", "#3a3a4a", True)
    P("author-dr-seuss", "#fff1d6", g(rect(-4, 0, 8, 80, WOOD, 2) + ell(0, -30, 38, 30, "#7ed957", 3.5), 780, 300, 1) + ell(900, 270, 90, 26, WHITE, 5) + "".join(path(f"M{x},{y} h110", sw=4, stroke=BLUE) for x, y in [(160, 100), (150, 130), (170, 160)]) + star(1070, 110, 22, BERRY), 0, "#3a3a3a", "short", BERRY, True)
    P("author-beatrix-potter", "#d6efff", "".join(circ(x, 276, 22, "#5cb86f", 3.5) + circ(x, 276, 12, "#78cf84", 2) for x in (740, 790, 840, 890)) + g(rect(-24, -30, 48, 30, "#3a8fd1", 6) + path("M24,-20 q20,-4 24,-20", sw=5), 1000, 300, 1) + sun(1080, 60, 32) + cottage(220, 300, .55), 0, "#7a4a2a", "bun", "#8a5a9a")
    P("author-aa-milne", "#d6efff", pot(780, 300, 1.4) + balloon(900, 270, 1.6) + tree(1060, 300, 1.2) + tree(180, 300, 1.4) + sun(120, 70, 30), 0, "#4a3a2a", "short", "#6a8a3a", False)
    P("author-jrr-tolkien", "#e9f0ff", mountains(W, 300, "#8fb3d9") + ell(900, 330, 200, 100, "#5cb86f", 0, 4) + circ(900, 280, 36, MEADOW, 4) + dot(914, 284, 4, BUTTER) + lantern(1100, 300, 1.2) + scroll(200, 230, 150, 70, -5), 0, "#8a8a8a", "short", "#6a8a3a", True)
    P("author-kenneth-grahame", "#d6efff", path("M600,300 q200,-20 600,6 V400 H600 z", "#7cc7f2", 4) + boat(930, 330, .8) + tree(1100, 300, 1.2, "#3a9d62") + tree(700, 300, 1.0, "#3a9d62") + sun(120, 70, 30), 0, "#6a6a6a", "short", "#7a5a3a", False)
    P("author-lm-montgomery", "#d6efff", blossom_tree(800, 300, 1.2) + blossom_tree(1040, 300, 1.0) + g(rect(-80, -70, 160, 70, "#fffaf0", 4) + poly([(-94, -70), (94, -70), (0, -130)], "#2f8f5b", 4) + rect(-14, -40, 28, 40, "#a8743f", 3), 220, 300, 1.1), 0, "#6a3a2a", "long", "#2f8f5b")
    P("author-judith-kerr", "#fff0d9", rect(700, 262, 440, 18, "#ffb3c7", 6) + cake_stand(790, 262, .9) + teapot(900, 262, .9) + cup(990, 262) + window(110, 50, 200, 160, "#cfe9ff") + star(1100, 100, 18), 0, "#8a8a8a", "short", "#d6336c", True)
    P("author-sam-mcbratney", "#27336b", moon_bg() + circ(900, 120, 64, "#fff3d6", 4) + path("M240,150 c-26,-30 -66,-6 -42,28 c16,18 42,28 42,28 c0,0 26,-10 42,-28 c24,-34 -16,-58 -42,-28 z", "#ffb3c7", 4) + "".join(flower(x, 296, c, 1.2) for x, c in [(760, PINK), (1000, BUTTER), (1100, WHITE)]), 0, "#8a8a8a", "short", "#3a8a63", True)
    sc("banner-classic-authors", "#fff1d6", "".join(writer(160 + i * 190, 300, sk, hc, st, sh, gl, .95) for i, (sk, hc, st, sh, gl) in enumerate([(0, "#c9822e", "long", PURPLE, False), (0, "#8a8a8a", "short", "#2a7aa0", True), (0, "#4a3a2a", "short", "#6a8a3a", False), (0, "#7a4a2a", "bun", "#8a5a9a", False), (0, "#3a3a3a", "short", BERRY, True), (0, "#6a3a2a", "long", "#2f8f5b", False)])) + star(60, 60, 18) + star(1140, 70, 20, PINK), "")
    print("author portraits written")


if __name__ == "__main__":
    run()
