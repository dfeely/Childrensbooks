#!/usr/bin/env python3
"""Christmas illustrations for childrensbooks.ie. Reuses the drawing kit in illustrations.py.

    python3 tools/illustrations.py && python3 tools/illustrations_christmas.py
"""
from illustrations import *  # noqa: F401,F403  (drawing helpers, palette, save())

SNOW = "#e3eefb"


def snowflakes(pts):
    out = ""
    for x, y, r in pts:
        for a in (0, math.pi / 3, 2 * math.pi / 3):
            out += path(f"M{x - r * math.cos(a):.1f},{y - r * math.sin(a):.1f} L{x + r * math.cos(a):.1f},{y + r * math.sin(a):.1f}", sw=2.5, stroke=WHITE)
    return out


def glow(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BUTTER}" opacity=".22"/>'


def snow_ground(w, h, top, ph=0.5):
    return hills(w, h, [(top, WHITE, 14, ph), (top + 55, SNOW, 10, ph + 1)])


def holly(x, y, s=1):
    b = ell(-14, 0, 22, 11, MEADOW, -25, 3) + ell(14, 0, 22, 11, MEADOW, 25, 3)
    b += circ(-4, -2, 6, BERRY, 2.5) + circ(6, -4, 6, BERRY, 2.5) + circ(2, 5, 6, BERRY, 2.5)
    return g(b, x, y, s)


def xmas_tree(x, y, s=1):
    b = rect(-14, -30, 28, 34, WOOD_DK, 3)
    b += poly([(-112, -34), (112, -34), (0, -150)], MEADOW) + poly([(-90, -108), (90, -108), (0, -212)], "#3aa56a")
    b += poly([(-64, -176), (64, -176), (0, -262)], "#4cb87a") + star(0, -270, 22)
    for bx, by, c in [(-40, -66, BERRY), (44, -80, BUTTER), (-12, -136, BLUE), (30, -150, BERRY), (-26, -204, BUTTER), (10, -108, PURPLE)]:
        b += circ(bx, by, 9, c, 3)
    b += path("M-80,-62 Q-20,-30 60,-70 M-56,-132 Q0,-102 52,-136", sw=3, stroke=BUTTER)
    return g(b, x, y, s)


def pine(x, y, s=1):
    b = rect(-9, -26, 18, 30, WOOD_DK, 2) + poly([(-58, -20), (58, -20), (0, -100)], MEADOW) + poly([(-46, -70), (46, -70), (0, -150)], "#3aa56a")
    b += path("M-24,-96 q24,14 48,0 M-36,-48 q36,18 72,0", sw=5, stroke=WHITE)
    return g(b, x, y, s)


def snowman(x, y, s=1):
    b = path("M-36,-120 L-86,-152 M-86,-152 l-14,-12 M-86,-152 l-4,16 M36,-120 L86,-152 M86,-152 l14,-12 M86,-152 l4,16", sw=4)
    b += circ(0, -50, 52, WHITE) + circ(0, -130, 38, WHITE) + circ(0, -192, 28, WHITE)
    b += path("M-34,-164 Q0,-148 34,-164", sw=16, stroke=INK) + path("M-34,-164 Q0,-148 34,-164", sw=9, stroke=BERRY)
    b += poly([(30, -158), (38, -130), (22, -130)], BERRY, 3)
    b += dot(0, -120, 4) + dot(0, -98, 4) + dot(0, -76, 4) + dot(-9, -198, 3.5) + dot(9, -198, 3.5)
    b += poly([(0, -192), (32, -186), (0, -181)], "#ef8a3c", 2.5) + path("M-9,-182 q9,8 18,0", sw=2.5)
    b += ell(0, -216, 36, 8, INK, 0, 3) + rect(-22, -254, 44, 40, INK, 4) + path("M-22,-222 h44", sw=7, stroke=BERRY)
    return g(b, x, y, s)


def stocking(x, y, s=1, f=BERRY, trim=WHITE, book=None):
    """(x, y) is the top-centre of the cuff, where it hangs from the mantel."""
    b = path("M0,0 V-14", sw=4)
    if book:
        b += rect(-14, 24, 26, 56, book, 3) + path("M-8,36 h14 M-8,48 h14", sw=2.5, stroke=PAPER)
    b += path("M-26,14 H26 V86 Q26,126 -8,132 L-44,134 Q-58,120 -36,106 L-26,100 Z", f)
    b += rect(-30, 0, 60, 24, trim, 6)
    return g(b, x, y, s)


def candle(x, y, s=1):
    return g(rect(-8, -34, 16, 34, PAPER, 3) + ell(0, -46, 5, 9, BUTTER, 0, 2.5) + rect(-14, 0, 28, 8, WOOD_DK, 3), x, y, s)


def cottage(x, y, s=1):
    b = rect(58, -232, 28, 80, "#b7bfd4", 3)
    b += rect(-120, -110, 240, 110, "#fffaf0", 3)
    b += poly([(-142, -108), (142, -108), (98, -192), (-98, -192)], "#d2b26a")
    b += path("M-100,-122 L-86,-170 M-50,-122 L-42,-178 M0,-122 L0,-180 M50,-122 L42,-178 M100,-122 L86,-170", sw=2.5, stroke="#a8884a")
    b += rect(-26, -78, 52, 78, BERRY, 8) + circ(14, -38, 4, BUTTER, 2) + circ(0, -62, 14, LEAF, 3) + circ(0, -62, 6, "#fffaf0", 2.5) + circ(8, -70, 3, BERRY, 0)
    for wx in (-100, 56):
        b += glow(wx + 22, -72, 52) + rect(wx, -92, 44, 40, "#ffe08a", 3) + path(f"M{wx + 22},-92 V-52 M{wx},-72 H{wx + 44}", sw=3)
    b += candle(78, -52, .5)
    return g(b, x, y, s)


def sleigh(x, y, s=1):
    b = path("M-40,-26 L40,-26 Q36,2 14,4 H-30 Z", BERRY) + path("M-48,10 H34 Q54,10 56,-12", sw=4) + circ(-14, -40, 12, BUTTER, 3)
    b += path("M60,-14 H120", sw=3) + ell(140, -22, 22, 12, "#8b6a4b") + circ(160, -30, 9, "#8b6a4b") + path("M164,-40 l8,-14 m-14,14 l-4,-14", sw=3)
    return g(b, x, y, s)


# ------------------------------------------------------------------ banners
def banner_xmas():
    b = rect(-4, 340, 1208, 70, "#d9a066", 0, 4) + path("M0,340 H1200")
    b += "".join(star(x, y, r, c, 2.5) for x, y, r, c in [(90, 60, 14, BUTTER), (300, 100, 10, BERRY), (470, 50, 12, BLUE), (760, 70, 12, BUTTER), (940, 120, 10, BERRY), (1100, 60, 14, BUTTER)])
    b += xmas_tree(600, 352, 1.05) + parcel(440, 308, 78, 56, BERRY, BUTTER) + parcel(690, 296, 84, 66, BLUE, PAPER) + parcel(520, 330, 60, 36, PURPLE, BUTTER)
    b += bear(230, 388, .92) + book_open(230, 318, 150, 70, BERRY) + rabbit(980, 388, .82) + book_open(980, 330, 120, 56, MEADOW)
    b += holly(60, 380, 1.4) + holly(1140, 380, 1.4)
    save("banner-christmas", 1200, 400, b, "#dff2e6")


def banner_xmas_picture():
    b = snow_ground(1200, 400, 290, .4) + pine(90, 340, 1.5) + pine(1110, 336, 1.6) + pine(1010, 350, 1.2)
    b += snowman(310, 372, 1.0) + bear(700, 380, .9) + book_open(700, 312, 140, 64, MEADOW)
    b += snowflakes([(120, 60, 9), (240, 130, 7), (420, 70, 8), (520, 160, 6), (620, 50, 9), (860, 110, 8), (980, 60, 7), (1100, 130, 9), (760, 200, 6)])
    save("banner-christmas-picture-books", 1200, 400, b, "#a9cdee")


def banner_xmas_chapter():
    b = rect(0, 0, 1200, 400, "#ffeec2", 0, 0) + rect(0, 330, 1200, 70, "#d9a066", 0, 4)
    b += rect(70, 40, 230, 270, NIGHT) + moon(210, 110, 30) + snowflakes([(110, 120, 8), (150, 200, 7), (240, 180, 9), (110, 260, 7), (260, 250, 8)])
    b += path("M185,40 V310 M70,175 H300", sw=5) + rect(70, 40, 230, 270, "none") + rect(56, 310, 258, 18, WOOD)
    b += path("M60,30 H116 Q98,170 120,322 H60 Z", BERRY) + path("M312,30 H256 Q274,170 252,322 H312 Z", BERRY)
    b += book_stack(640, 372, [(280, 50, BERRY), (250, 46, BLUE), (270, 46, MEADOW), (220, 42, PURPLE)])
    b += rect(560, 150, 70, 60, PAPER, 8) + path("M630,164 q30,0 30,24 t-30,24", sw=5) + path("M580,138 q-8,-18 4,-30 M600,138 q-8,-18 4,-30 M620,138 q-8,-18 4,-30", sw=3, stroke="#9aa6c4")
    b += rect(560, 178, 70, 14, BERRY, 0, 0)
    b += xmas_tree(980, 372, .95) + parcel(1080, 322, 70, 50, BLUE, BUTTER) + parcel(850, 330, 60, 42, BERRY, PAPER)
    save("banner-christmas-chapter-books", 1200, 400, b)


def banner_advent():
    cols = [BERRY, MEADOW, BLUE, PURPLE, "#ef8a3c", "#2aa7a0"]
    b = starfield([(80, 60), (190, 140), (1080, 70), (1000, 200), (130, 280), (1110, 320)], 10) + snow_ground(1200, 400, 340, .2)
    b += rect(214, 46, 772, 266, WOOD, 12)
    n = 1
    for r in range(3):
        for c in range(8):
            x, y = 232 + c * 94, 62 + r * 84
            if n <= 4:
                b += rect(x, y, 82, 72, "#fff1d6", 6) + rect(x + 22, y + 12, 38, 48, cols[n % 6], 3) + path(f"M{x + 28},{y + 26} h26 M{x + 28},{y + 38} h26", sw=2.5, stroke=PAPER)
            else:
                b += rect(x, y, 82, 72, cols[n % 6], 6) + txt(x + 41, y + 47, str(n), 30, WHITE)
            n += 1
    b += snowflakes([(120, 150, 9), (1090, 150, 9), (60, 220, 7), (1150, 240, 8), (330, 20, 7), (880, 22, 8)])
    save("banner-advent-calendar", 1200, 400, b, "#27336b")


def banner_xmas_eve():
    b = starfield([(80, 60), (260, 150), (400, 50), (560, 110), (700, 40), (830, 140), (1150, 80), (1100, 230)], 9) + moon(190, 100, 52)
    b += sleigh(940, 120, .9) + snow_ground(1200, 400, 300, .7) + pine(90, 350, 1.4) + pine(1120, 340, 1.5) + xmas_tree(920, 372, .8)
    b += cottage(500, 372, 1.15)
    b += "".join(f'<circle cx="{560 + i * 14}" cy="{40 - i * 8}" r="{12 + i * 3}" fill="#fff" opacity="{.5 - i * .08:.2f}"/>' for i in range(4))
    b += snowflakes([(300, 120, 8), (700, 90, 7), (640, 200, 6), (240, 220, 7), (800, 240, 8)])
    save("banner-christmas-eve", 1200, 400, b, "#27336b")


def banner_irish_xmas():
    b = starfield([(90, 70), (240, 130), (400, 50), (560, 100), (760, 50), (940, 110), (1110, 60), (860, 170)], 9) + moon(1040, 120, 46)
    b += hills(1200, 400, [(290, "#3a9d62", 16, .6), (340, "#2f8f5b", 12, 1.4)])
    b += cottage(600, 372, 1.25) + sheep(250, 366, .9) + sheep(960, 370, .8) + sheep(1070, 360, .6)
    b += holly(90, 376, 1.7) + holly(1130, 380, 1.7) + holly(400, 390, 1.1) + holly(800, 392, 1.1)
    save("banner-irish-christmas", 1200, 400, b, "#2b3a78")


def banner_stockings():
    b = rect(0, 0, 1200, 400, "#ffe9c9", 0, 0) + rect(0, 330, 1200, 70, "#d9a066", 0, 4) + path("M0,330 H1200")
    b += rect(70, 118, 1060, 34, WOOD_DK, 4) + rect(50, 100, 1100, 22, WOOD, 4)
    b += "".join(holly(90 + i * 56, 98, .8) for i in range(19))
    b += candle(110, 100, 1.1) + candle(1090, 100, 1.1) + star(600, 56, 22)
    specs = [(250, BERRY, BLUE), (430, MEADOW, BERRY), (600, BLUE, BUTTER), (770, PURPLE, MEADOW), (950, BUTTER, PURPLE)]
    for x, f, bk in specs:
        b += stocking(x, 152, 1.05, f, WHITE, bk)
    b += "".join(star(x, y, r, c, 2.5) for x, y, r, c in [(150, 230, 10, BUTTER), (1050, 240, 10, BERRY), (340, 250, 8, BLUE), (860, 250, 8, BUTTER)])
    save("banner-stocking-fillers", 1200, 400, b)


if __name__ == "__main__":
    for fn in [banner_xmas, banner_xmas_picture, banner_xmas_chapter, banner_advent, banner_xmas_eve, banner_irish_xmas, banner_stockings]:
        fn()
    print("christmas illustrations written")
