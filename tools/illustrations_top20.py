#!/usr/bin/env python3
"""One original 1200x400 scene per bestseller page. Scenes show settings, props and generic
creatures only. They never copy a cover or draw an existing character.

    python3 tools/illustrations.py && python3 tools/illustrations_top20.py
"""
from illustrations import *  # noqa: F401,F403
from illustrations_christmas import cottage, holly, candle, pine  # noqa: F401

W, H = 1200, 400


def ground(y, color="#8fd08a"):
    return rect(-4, y, W + 8, H - y + 4, color, 0, 4)


# ---------------------------------------------------------------- props
def dog(x, y, s=1, fur="#f4f0e6", spots=False, ear="#3d3a4f", fluff=False, flip=False):
    b = path("M44,-52 q36,-26 34,-62", sw=14, stroke=INK) + path("M44,-52 q36,-26 34,-62", sw=7, stroke=fur)
    if fluff:
        b += blob([("c", 40, -122, 16)], fur, 3)
    b += rect(-28, -24, 14, 26, fur, 6) + rect(14, -24, 14, 26, fur, 6)
    b += ell(0, -58, 52, 34, fur)
    if spots:
        b += "".join(circ(cx, cy, r, INK, 0) for cx, cy, r in [(-22, -66, 8), (6, -50, 9), (26, -70, 7), (-4, -76, 6)])
    if fluff:
        b += blob([("c", -22, -78, 16), ("c", 0, -84, 18), ("c", 22, -78, 16)], fur, 3)
    b += ell(-52, -78, 30, 26, fur) + ell(-70, -66, 17, 12, fur if not fluff else "#f6d9a8")
    b += ell(-62, -94, 11, 22, ear, 12) + ell(-36, -96, 11, 22, ear, -12)
    b += dot(-58, -82, 3.5) + dot(-78, -68, 4.5) + path("M-74,-60 q8,6 14,0", sw=2.5)
    return g(b, x, y, s, 0, flip)


def giraffe(x, y, s=1):
    b = rect(-52, -50, 14, 52, "#f3c14e", 5) + rect(34, -50, 14, 52, "#f3c14e", 5) + rect(-30, -50, 14, 52, "#f3c14e", 5) + rect(12, -50, 14, 52, "#f3c14e", 5)
    b += ell(0, -80, 66, 36, "#f6cc5a") + path("M-40,-100 L-62,-250 Q-56,-262 -40,-258 L-12,-108 Z", "#f6cc5a")
    b += ell(-56, -268, 26, 18, "#f6cc5a", -20) + dot(-62, -274, 4) + ell(-76, -262, 8, 6, "#d99a2b", 0, 2)
    b += path("M-50,-286 v-18 M-62,-284 v-16", sw=4) + circ(-50, -306, 5, "#a8743f", 2.5) + circ(-62, -302, 5, "#a8743f", 2.5)
    b += "".join(circ(cx, cy, r, "#c98a2e", 0) for cx, cy, r in [(-8, -88, 9), (22, -74, 8), (40, -92, 7), (-30, -140, 7), (-46, -190, 6), (-20, -66, 6)])
    b += path("M66,-84 q18,10 10,40", sw=4)
    return g(b, x, y, s)


def donut(x, y, r=40, icing=BERRY, sprinkles=True, face=False):
    b = circ(x, y, r, "#e8b36a") + circ(x, y, r * .8, icing, 3) + circ(x, y, r * .26, SKY, 3)
    if sprinkles:
        for i in range(9):
            a = i * 2 * math.pi / 9 + .3
            rr = r * (.55 if i % 2 else .66)
            b += path(f"M{x + rr * math.cos(a):.1f},{y + rr * math.sin(a):.1f} l{6 * math.cos(a + 1):.1f},{6 * math.sin(a + 1):.1f}", sw=3.5, stroke=[BUTTER, WHITE, BLUE][i % 3])
    if face:
        b += dot(x - r * .35, y - r * .1, 3) + dot(x + r * .35, y - r * .1, 3)
    return b


def ghostie(x, y, s=1, f="#ffffff"):
    b = path("M-44,0 V-70 C-44,-130 44,-130 44,-70 V0 L30,-14 L14,0 L0,-14 L-14,0 L-30,-14 Z", f)
    b += ell(-16, -76, 8, 12, INK, 0, 0) + ell(16, -76, 8, 12, INK, 0, 0) + dot(-18, -80, 2.5, WHITE) + dot(14, -80, 2.5, WHITE) + path("M-9,-52 q9,10 18,0", sw=3)
    return g(b, x, y, s)


def toast(x, y, s=1):
    b = path("M-46,0 V-60 C-70,-62 -66,-110 -34,-112 C-26,-132 26,-132 34,-112 C66,-110 70,-62 46,-60 V0 Z", "#e0a85a")
    b += path("M-34,-8 V-64 C-52,-66 -50,-98 -28,-100 C-20,-116 20,-116 28,-100 C50,-98 52,-66 34,-64 V-8 Z", "#fbe2a8", 3)
    b += dot(-14, -66, 4.5) + dot(14, -66, 4.5) + path("M-10,-48 q10,10 20,0", sw=3.5)
    return g(b, x, y, s)


def croissant(x, y, s=1):
    b = path("M-60,0 Q-50,-40 -22,-46 Q0,-64 22,-46 Q50,-40 60,0 Q30,-12 0,-12 Q-30,-12 -60,0 Z", "#e5a24a")
    b += path("M-22,-46 L-14,-10 M0,-60 L0,-12 M22,-46 L14,-10", sw=3, stroke="#b8741f")
    b += path("M-14,-26 l12,-6 M14,-26 l-12,-6", sw=3.5) + dot(-8, -22, 2.8) + dot(8, -22, 2.8)
    return g(b, x, y, s)


def frog(x, y, s=1, f="#5cb86f"):
    b = ell(0, -20, 34, 22, f) + circ(-16, -42, 11, f, 3.5) + circ(16, -42, 11, f, 3.5) + dot(-16, -43, 4.5) + dot(16, -43, 4.5)
    b += path("M-14,-26 q14,10 28,0", sw=3) + ell(-34, 0, 14, 6, f, 0, 3) + ell(34, 0, 14, 6, f, 0, 3)
    return g(b, x, y, s)


def lilypad(x, y, w=70):
    return ell(x, y, w, w * .24, "#7fd18b", 0, 3.5) + path(f"M{x},{y} L{x + w * .8},{y - w * .1}", sw=2.5, stroke=INK)


def pixel_hero(x, y, s=1):
    cells = ["..XXX..", ".XXXXX.", ".XOXOX.", ".XXXXX.", "XXXXXXX", "X.XXX.X", "..X.X.."]
    b = ""
    for r, row in enumerate(cells):
        for c, ch in enumerate(row):
            if ch != ".":
                b += f'<rect x="{c * 14}" y="{r * 14}" width="14" height="14" fill="{INK if ch == "O" else MEADOW}"/>'
    return g(b, x, y, s)


def diamond(x, y, r=16, f="#6fd0f0"):
    return poly([(x, y - r), (x + r, y), (x, y + r * 1.2), (x - r, y)], f, 3)


def football(x, y, r=24):
    b = circ(x, y, r, WHITE, 3.5)
    b += poly([(x, y - r * .45), (x + r * .43, y - r * .14), (x + r * .27, y + r * .36), (x - r * .27, y + r * .36), (x - r * .43, y - r * .14)], INK, 0)
    return b


def boot(x, y, s=1, f=BERRY):
    b = path("M-50,0 V-52 Q-50,-64 -38,-64 H-12 L-4,-40 Q40,-34 56,-12 Q62,0 50,6 H-44 Q-50,6 -50,0 Z", f)
    b += path("M-44,-4 h96", sw=3, stroke=WHITE) + "".join(rect(px, 6, 8, 12, WHITE, 2, 3) for px in (-34, -10, 14, 38))
    b += path("M-30,-44 l10,8 M-22,-52 l10,8", sw=2.5, stroke=WHITE)
    return g(b, x, y, s)


def lockers(x, y, n=5, w=70, h=240, cols=(BLUE, "#2aa7a0", BLUE, "#2aa7a0", BLUE)):
    b = ""
    for i in range(n):
        lx = x + i * w
        b += rect(lx, y, w, h, cols[i % len(cols)], 3) + path(f"M{lx + 12},{y + 30} h{w - 24} M{lx + 12},{y + 42} h{w - 24} M{lx + 12},{y + 54} h{w - 24}", sw=3, stroke="#1c4f78") + rect(lx + w - 22, y + h * .5, 8, 22, BUTTER, 3, 2.5)
    return b


def binder(x, y, w=110, h=140, f=BERRY, rot=0):
    b = rect(0, 0, w, h, f, 6) + rect(12, 18, w - 24, 46, PAPER, 3, 3) + path("M22,34 h56 M22,46 h40", sw=3, stroke="#9aa6c4")
    b += "".join(circ(0, 24 + i * 46, 7, "#cfd6e6", 3) for i in range(3))
    return g(b, x, y, 1, rot)


def notebook(x, y, w=150, h=110, rot=0, f=PAPER, band=BLUE):
    b = rect(0, 0, w, h, f, 6) + rect(0, 0, 24, h, band, 4) + "".join(path(f"M36,{22 + i * 18} h{w - 52}", sw=3, stroke="#9aa6c4") for i in range(5))
    return g(b, x, y, 1, rot)


def mountains(w, base, color="#8fb3d9", snow=True):
    b = path(f"M0,{base} L120,{base - 150} L220,{base - 60} L360,{base - 220} L520,{base - 70} L640,{base - 170} L800,{base - 40} L930,{base - 190} L1080,{base - 60} L{w},{base - 130} V{base} Z", color)
    if snow:
        for px, py in [(120, base - 150), (360, base - 220), (640, base - 170), (930, base - 190)]:
            b += poly([(px, py), (px - 30, py + 40), (px - 10, py + 34), (px, py + 46), (px + 14, py + 32), (px + 30, py + 40)], WHITE, 3)
    return b


def pine_t(x, y, s=1):
    return pine(x, y, s) if "pine" in globals() else ""


def lamp_post(x, y, s=1):
    return g(path("M0,0 V-180", sw=8) + rect(-18, -210, 36, 34, BUTTER, 6) + circ(0, -194, 70, BUTTER).replace('fill="#ffcf4a"', 'fill="#ffcf4a" opacity=".16"').replace('stroke="#1f2a44" stroke-width="4"', 'stroke="none"'), x, y, s)


def spotlight(x, y, w=260, h=330):
    return f'<polygon points="{x - 18},{y} {x + 18},{y} {x + w / 2},{y + h} {x - w / 2},{y + h}" fill="#fff3b0" opacity=".45"/>'


def curtains(x0, x1, top, bottom):
    b = path(f"M{x0},{top} H{x0 + 170} Q{x0 + 120},{(top + bottom) / 2} {x0 + 170},{bottom} H{x0} Z", BERRY)
    b += path(f"M{x1},{top} H{x1 - 170} Q{x1 - 120},{(top + bottom) / 2} {x1 - 170},{bottom} H{x1} Z", BERRY)
    return b


def mask(x, y, f, s=1, mood="happy"):
    b = path("M-40,-50 Q0,-72 40,-50 Q44,10 0,38 Q-44,10 -40,-50 Z", f)
    b += path("M-24,-24 q10,-10 20,0 M4,-24 q10,-10 20,0", sw=4)
    b += path("M-18,6 q18,20 36,0" if mood == "happy" else "M-18,16 q18,-18 36,0", sw=4)
    return g(b, x, y, s)


def skis(x, y, rot=-20):
    b = rect(0, 0, 220, 14, BERRY, 7, 3) + rect(0, 26, 220, 14, BLUE, 7, 3) + path("M0,7 q-26,-4 -34,-22 M0,33 q-26,-4 -34,-22", sw=5)
    return g(b, x, y, 1, rot)


def fondue(x, y, s=1):
    b = path("M-50,0 L-38,-60 H38 L50,0 Z", "#e45c5c") + ell(0, -60, 38, 10, "#ffd66b", 0, 3) + rect(-60, 0, 120, 12, WOOD_DK, 4) + candle(0, 0, .0)
    b += path("M20,-70 L66,-136", sw=4) + circ(66, -140, 11, "#f1c46f", 3) + path("M-18,-70 C-14,-100 -10,-110 -2,-124", sw=3, stroke="#9aa6c4")
    return g(b, x, y, s)


def bauble(x, y, c, r=22):
    return rect(x - 6, y - r - 10, 12, 10, BUTTER, 2, 2.5) + circ(x, y, r, c, 3.5) + path(f"M{x - r * .5},{y - r * .3} q{r * .3},-{r * .5} {r * .7},-{r * .3}", sw=3, stroke=WHITE)


def lightbulbs(x0, y0, n, dx, dy, cols):
    b = path(f"M{x0},{y0} " + " ".join(f"q{dx / 2},{dy} {dx},0" for _ in range(n)), sw=3.5)
    for i in range(n):
        b += circ(x0 + dx * (i + .5), y0 + dy / 2 + 8, 9, cols[i % len(cols)], 3)
    return b


def magnifier(x, y, s=1, r=60):
    return g(circ(0, 0, r, "#cfe9ff", 6).replace('fill="#cfe9ff"', 'fill="#cfe9ff" fill-opacity=".6"') + path(f"M{r * .7},{r * .7} L{r * 1.7},{r * 1.7}", sw=18) + path(f"M{r * .7},{r * .7} L{r * 1.7},{r * 1.7}", sw=9, stroke=BERRY), x, y, s)


def talker(x, y, kind="lamp", s=1):
    if kind == "lamp":
        b = rect(-8, -80, 16, 80, "#9aa6c4", 3) + rect(-26, 0, 52, 10, INK, 4) + poly([(-34, -80), (34, -80), (22, -128), (-22, -128)], BUTTER) + dot(-8, -100, 3.5) + dot(8, -100, 3.5) + path("M-6,-90 q6,6 12,0", sw=2.5)
    elif kind == "mug":
        b = rect(-30, -60, 60, 60, BLUE, 10) + path("M30,-46 q26,0 26,20 q0,20 -26,20", sw=6) + dot(-10, -34, 4) + dot(10, -34, 4) + path("M-8,-20 q8,8 16,0", sw=3)
    else:
        b = rect(-44, -50, 88, 50, "#d63a3a", 8) + rect(-40, -64, 80, 18, "#9aa6c4", 6) + dot(-14, -28, 4) + dot(14, -28, 4) + path("M-8,-14 q8,8 16,0", sw=3)
    return g(b, x, y, s)


def mic_stage(x, y):
    return rect(x - 190, y, 380, 30, WOOD_DK, 4) + rect(x - 190, y + 30, 380, 40, WOOD, 3)


def trophy_ball(x, y, s=1):
    return g(circ(0, -40, 40, "#ffd24a") + path("M-30,-54 q30,-26 60,0 M-34,-34 q34,-22 68,0 M-30,-14 q30,-20 60,0", sw=3, stroke="#c9961a") + rect(-24, 0, 48, 14, "#c9961a", 3) + rect(-34, 14, 68, 14, WOOD_DK, 3), x, y, s)


def cake(x, y, s=1):
    b = rect(-90, -60, 180, 60, BERRY, 8) + path("M-90,-60 q22,22 45,0 q22,22 45,0 q22,22 45,0 q22,22 45,0", "#fff", 4) + rect(-76, -110, 152, 50, BUTTER, 8)
    for cx in (-48, -16, 16, 48):
        b += rect(cx - 5, -140, 10, 30, BLUE, 2, 3) + ell(cx, -148, 5, 9, "#ff8a3c", 0, 2.5)
    return g(b, x, y, s)


def party_hat(x, y, c, s=1, rot=0):
    return g(poly([(0, -90), (-34, 0), (34, 0)], c) + circ(0, -94, 9, BUTTER, 3) + path("M-20,-34 h40 M-10,-62 h20", sw=3, stroke=WHITE), x, y, s, rot)


# ------------------------------------------------------------------ scenes
def s_wimpy():
    b = rect(0, 0, W, H, "#dfe9f5", 0, 0) + rect(0, 300, W, 100, "#c9b79a", 0, 4)
    b += lockers(60, 70, 7, 76, 250) + lockers(640, 70, 7, 76, 250, (MEADOW, "#2f7d9a"))
    b += binder(540, 230, 110, 140, BERRY, -12) + notebook(440, 290, 140, 100, 8, PAPER, BUTTER)
    b += rect(610, 330, 30, 8, INK, 3, 0)
    b += g(path("M-30,0 h60 v-24 q-6,-24 -30,-24 t-30,24 z", WHITE) + path("M-30,-12 h60", sw=3, stroke=BERRY), 590, 392, 1.1)
    b += g(path("M-30,0 h60 v-24 q-6,-24 -30,-24 t-30,24 z", WHITE) + path("M-30,-12 h60", sw=3, stroke=BERRY), 700, 380, 1.1, 18)
    b += path("M740,350 l30,-10 M750,370 l36,-6 M742,388 l32,2", sw=4, stroke="#8a93ab")
    save("book-wimpy-kid-fight-or-flight", W, H, b)


def s_gruffalo_granny():
    b = sun(1050, 80, 36) + cloud(200, 70, 1) + hills(W, H, [(250, "#b8e3b0", 14, .2)]) + ground(330, "#5cb86f")
    b += tree(120, 340, 1.5, "#4aa860") + tree(1080, 340, 1.6, "#3a9d62") + tree(300, 350, 1.1)
    b += cottage(640, 350, 1.2)
    b += path("M520,350 q-120,24 -240,50 M640,352 q40,20 120,48", sw=26, stroke="#c9a46b") + path("M520,350 q-120,24 -240,50 M640,352 q40,20 120,48", sw=16, stroke="#e6cc9a")
    b += g(path("M-44,0 L-34,-50 H34 L44,0 Z", INK) + ell(0, -50, 34, 9, "#a66a3c", 0, 3) + path("M-10,-60 q-8,-14 0,-26 M10,-60 q8,-14 0,-26", sw=3, stroke="#9aa6c4"), 860, 392, 1)
    b += g(ell(0, -14, 20, 14, "#b98c5a") + circ(18, -22, 10, "#b98c5a") + circ(24, -32, 6, "#f3d6b3", 3) + path("M-20,-14 q-24,-4 -30,-20", sw=3), 420, 396, 1)
    b += owl(960, 380, .7, flip=True) + flower(360, 390, BERRY) + flower(560, 394, BUTTER, .9)
    save("book-gruffalo-granny", W, H, b, "#d6efff")


def s_bunny_monkey():
    b = sun(120, 80, 36) + cloud(520, 70, 1) + hills(W, H, [(270, "#a9dca3", 18, .5)]) + ground(340, "#5cb86f")
    b += tree(110, 350, 1.5) + tree(1100, 350, 1.4, "#4aa860")
    b += g(path("M0,0 C30,-30 70,-30 100,-10 C86,6 70,12 60,40 C44,18 24,10 0,0 Z", "#e63c3c") + path("M-4,-2 l30,-8", sw=4) + circ(-4, -2, 9, BUTTER, 3), 330, 220, 1.4, -14)
    b += g(path("M-70,0 Q-60,-70 0,-76 Q60,-70 70,0 Z", "#ff6fa5") + ell(-24, -44, 12, 8, "#ffc2d9", -30, 0) + dot(-18, -36, 4) + dot(14, -36, 4) + path("M-8,-20 q8,8 16,0", sw=3), 620, 380, 1.4)
    b += g(circ(0, 0, 8, BERRY) + "".join(path(f"M{a * 8},{-6} l{a * 6},{-10}", sw=3) for a in (-1, 1)), 560, 330, 0)
    b += g(ell(0, -30, 54, 32, "#ffc2c9") + circ(-44, -34, 20, "#ffc2c9") + ell(-52, -54, 8, 14, "#ffc2c9", -20) + dot(-50, -38, 3.5) + ell(-60, -28, 8, 6, "#e88aa0", 0, 2.5) + path("M54,-34 q16,-4 14,-18", sw=4) + "".join(rect(px, -2, 8, 22, "#ffc2c9", 3, 3) for px in (-30, -6, 22, 40)), 900, 382, 1.1)
    b += "".join(path(f"M{px},{py} l18,-26 l12,12", sw=4, stroke=BERRY) for px, py in [(160, 250), (760, 150)])
    b += star(980, 120, 14) + star(1040, 190, 10, BERRY) + star(820, 90, 9, BLUE)
    save("book-bunny-vs-monkey-day-of-the-heroes", W, H, b, "#cdeeff")


def s_lottie_xmas():
    b = rect(0, 0, W, H, "#ffe9d9", 0, 0) + rect(0, 330, W, 70, "#d9a066", 0, 4)
    b += g(poly([(0, -170), (-70, -60), (70, -60)], MEADOW) + poly([(0, -120), (-96, 0), (96, 0)], "#3aa56a") + rect(-12, 0, 24, 24, WOOD_DK, 2, 3), 330, 352, 1.3, 14)
    b += bauble(560, 300, BERRY) + bauble(610, 340, BLUE, 18) + bauble(520, 346, BUTTER, 16) + bauble(700, 322, PURPLE, 20)
    b += lightbulbs(540, 70, 8, 70, 40, [BERRY, BUTTER, BLUE, MEADOW]) + lightbulbs(120, 110, 5, 70, 36, [BUTTER, BERRY, BLUE])
    b += notebook(760, 200, 220, 150, -6, PAPER, BERRY) + star(820, 260, 14, BUTTER) + path("M840,296 q28,-30 56,0 q28,30 56,0", sw=5, stroke=BERRY)
    b += parcel(1020, 300, 100, 70, BLUE, BUTTER) + parcel(930, 330, 70, 50, MEADOW, PAPER)
    b += holly(80, 380, 1.6) + holly(1130, 250, 1.2)
    b += "".join(star(x, y, r, c, 2.5) for x, y, r, c in [(150, 60, 10, BUTTER), (660, 150, 8, BERRY), (1100, 70, 12, BLUE)])
    save("book-lottie-brooks-twelve-disasters-of-christmas", W, H, b)


def s_disaster_dad():
    b = sun(1060, 80, 36) + cloud(180, 70, 1) + hills(W, H, [(280, "#a9dca3", 14, .3)]) + ground(340, "#8fd08a")
    b += rect(80, 180, 40, 170, WOOD_DK, 4) + rect(280, 180, 40, 170, WOOD_DK, 4) + rect(70, 150, 260, 44, BERRY, 8) + txt(200, 182, "WILDLIFE PARK", 24, WHITE)
    b += tree(1120, 350, 1.3, "#4aa860") + tree(980, 350, 1.0)
    b += giraffe(640, 392, 1.15) + g(giraffe(0, 0, .5), 820, 392, 1) + flower(480, 392, BERRY) + flower(520, 396, BUTTER, .9)
    cam = rect(-40, -28, 80, 56, INK, 8) + circ(0, 0, 20, "#6fa8dc", 4) + circ(0, 0, 8, WHITE, 3) + rect(-18, -40, 36, 12, INK, 3)
    b += g(cam, 330, 290, 1.1, -10)
    b += star(450, 120, 12) + star(960, 200, 9, BERRY)
    save("book-disaster-dad-animal-antics", W, H, b, "#cdeeff")


def s_rowley():
    b = starfield([(80, 70), (210, 130), (360, 50), (520, 110), (760, 50), (950, 100), (1130, 160), (660, 160)], 9) + moon(1030, 100, 56)
    b += path("M0,300 Q200,250 400,290 T800,280 T1200,300 V400 H0 Z", "#2c2556")
    house = rect(-110, -150, 220, 150, "#4b3f8f", 4) + poly([(-130, -150), (130, -150), (0, -250)], "#3a3077") + rect(-24, -80, 48, 80, "#241d4c", 24, 3)
    house += "".join(rect(px, -128, 36, 44, "#ffe08a", 4, 3) + path(f"M{px + 18},-128 V-84 M{px},-106 H{px + 36}", sw=2.5) for px in (-90, 54)) + rect(60, -280, 28, 60, "#4b3f8f", 3)
    b += g(house, 560, 340, 1.1) + ghostie(300, 380, 1) + ghostie(880, 360, .7, "#e9ecff") + ghostie(1010, 392, .5)
    b += "".join(path(f"M{x},{y} q-12,-14 -26,-6 q6,-12 -4,-22 q16,4 20,16 q4,-12 18,-14 q-10,10 -8,22 q14,-6 24,6 q-14,0 -24,-2 Z", INK, 3) + dot(x - 20, y - 14, 0) for x, y in [(160, 140), (470, 80), (700, 150), (820, 60)])
    b += g(poly([(0, 0), (-12, -34), (12, -34)], "#ef8a3c") + ell(0, -46, 24, 20, "#ef8a3c") + ell(0, -36, 14, 6, INK, 0, 0), 1100, 392, 1)
    save("book-rowley-jeffersons-awesome-friendly-spooky-stories-2", W, H, b, "#241d4c")


def s_donut():
    b = rect(0, 0, W, H, "#27336b", 0, 0) + starfield([(80, 60), (210, 120), (990, 60), (1130, 140), (150, 330), (1100, 330), (700, 40)], 10)
    b += circ(600, 200, 150, "#6fd0f0").replace('fill="#6fd0f0"', 'fill="#6fd0f0" opacity=".25"') + circ(600, 200, 120, "#9ff0ff").replace('fill="#9ff0ff"', 'fill="#9ff0ff" opacity=".35"')
    b += circ(600, 200, 90, "#27336b", 6) + path("M600,200 V132 M600,200 L650,222", sw=8, stroke=BUTTER) + "".join(path(f"M{600 + 78 * math.cos(a):.0f},{200 + 78 * math.sin(a):.0f} l{8 * math.cos(a):.0f},{8 * math.sin(a):.0f}", sw=4, stroke=WHITE) for a in [i * math.pi / 6 for i in range(12)])
    b += donut(260, 250, 62, BERRY, True, True) + donut(150, 130, 44, "#6fd0f0", True, True) + donut(980, 150, 58, "#ffd24a", True, True) + donut(1090, 300, 46, "#b57cf0", True, True) + donut(430, 340, 40, "#9be3a8", True, True) + donut(800, 320, 36, "#ff9ec2", True, True)
    save("book-donut-squad-destiny-of-the-donuts", W, H, b)


def s_squad_girls():
    b = rect(0, 0, W, H, "#dff2e6", 0, 0) + sun(1100, 70, 34) + cloud(300, 60, .9)
    b += rect(-4, 300, W + 8, 100, "#d9674a", 0, 4) + "".join(path(f"M0,{320 + i * 26} H{W}", sw=3, stroke=WHITE) for i in range(3))
    b += rect(60, 90, 300, 170, "#6fd0f0", 6) + "".join(path(f"M60,{130 + i * 40} H360", sw=4, stroke=WHITE) for i in range(3)) + "".join(circ(x, y, 7, BERRY, 2.5) for x, y in [(110, 114), (200, 154), (290, 114), (160, 194), (250, 234)])
    b += path("M530,120 q60,-60 120,-10 q60,50 120,-20 M560,250 q60,-60 120,-10", sw=10, stroke=BERRY) + star(600, 300, 14)
    b += g(path("M-40,0 q0,-40 22,-48 q-6,-26 22,-26 q28,0 22,26 q22,8 22,48 Z", BERRY) + path("M-30,-6 h80", sw=4, stroke=WHITE), 850, 300, 1.3)
    b += g(path("M-44,0 q10,-34 40,-34 h28 q20,0 20,18 v16 Z", PURPLE) + path("M-32,-8 h70", sw=3, stroke=WHITE) + "".join(circ(px, -22, 3, BUTTER, 0) for px in (-12, 6, 24)), 980, 370, 1.2)
    b += football(240, 380, 24) if False else ""
    b += g(path("M-60,0 q30,-40 60,0 q30,40 60,0", sw=7, stroke=BUTTER) + path("M-60,0 q30,-40 60,0 q30,40 60,0", sw=3, stroke=BERRY), 1090, 230, 1)
    b += star(760, 100, 12, BERRY) + star(480, 330, 10, BLUE)
    save("book-squad-girls", W, H, b)


def s_milly():
    b = rect(0, 0, W, H, "#e9f7ff", 0, 0) + ground(320, "#8fd08a") + rect(60, 70, 280, 240, WOOD_DK, 6) + rect(76, 86, 248, 208, "#fff1d6", 3) + txt(200, 150, "DOGGY DAYCARE", 28) + path("M110,180 h180", sw=4, stroke=BERRY)
    b += rect(80, 300, 240, 12, WOOD, 3) + "".join(path(f"M{x},300 v-60", sw=4, stroke=WOOD_DK) for x in (110, 170, 230, 290))
    b += dog(520, 380, 1.4, "#fbf8f0", True, flip=False) + dog(740, 384, 1.3, "#ffd9e8", False, "#ffbfd5", True) + dog(950, 380, 1.4, "#e8b866", False, "#c9923a", True)
    b += path("M610,330 q40,-40 80,-10 q40,30 90,-24", sw=5, stroke=BERRY) + g(poly([(0, -14), (-20, 0), (20, 0)], BUTTER) + rect(-6, 0, 12, 10, BERRY, 3, 3), 1070, 396, 1.1)
    b += g(ell(0, 0, 34, 12, "#e8e0cc") + circ(-30, 0, 9, "#e8e0cc", 3) + circ(30, 0, 9, "#e8e0cc", 3), 380, 376, 1) + flower(1110, 392, BERRY) + flower(1150, 396, BUTTER, .9)
    save("book-milly-mccarthy-and-the-doggy-daycare-drama", W, H, b)


def s_ghost_toast():
    b = rect(0, 0, W, H, "#2b2766", 0, 0) + starfield([(80, 60), (230, 130), (1000, 70), (1120, 160), (730, 50)], 9) + moon(120, 100, 40)
    b += rect(-4, 340, W + 8, 70, "#4b3f8f", 0, 4)
    house = rect(-150, -190, 300, 190, "#4b3f8f", 4) + poly([(-170, -190), (170, -190), (0, -290)], "#3a3077") + rect(-30, -90, 60, 90, "#241d4c", 30, 3) + "".join(rect(px, -160, 40, 50, "#ffe08a", 4, 3) for px in (-120, 80))
    b += g(house, 640, 360, 1.2) + ghostie(380, 390, 1.5) + toast(480, 380, 1.3) + croissant(900, 372, 1.5)
    b += g(path("M0,0 q20,-20 40,0 M0,0 l40,0", sw=0), 0, 0, 0)
    b += g(poly([(0, -34), (-20, 0), (20, 0)], "#ef8a3c") + rect(-10, -46, 20, 12, "#ef8a3c", 3), 1040, 392, 1.1)
    b += star(780, 60, 10, BUTTER) + star(260, 220, 9, BERRY)
    save("book-ghost-and-toast-slice-to-meet-you", W, H, b)


def s_lottie_holiday():
    b = rect(0, 0, W, H, "#cfe9ff", 0, 0) + sun(1080, 70, 34) + mountains(W, 300) + hills(W, H, [(310, WHITE, 16, .2), (360, "#e3eefb", 10, 1)])
    b += pine(120, 350, 1.4) + pine(240, 370, 1.0) + pine(1100, 350, 1.5) + pine(980, 372, 1.0)
    b += skis(450, 300, -24) + g(path("M0,0 V-110", sw=6) + circ(0, -114, 14, BERRY, 4) + path("M-14,-118 h28", sw=3), 700, 380, 1, 8) + g(path("M0,0 V-110", sw=6) + circ(0, -114, 14, BERRY, 4), 740, 384, 1, -8)
    b += fondue(900, 368, 1.1) + parcel(100, 300, 0, 0, BLUE) * 0
    b += g(ell(0, 0, 60, 22, "#ffe36e") + path("M-60,0 q30,-30 120,0", sw=0), 600, 366, 1)
    b += cloud(220, 70, 1) + cloud(700, 100, .8)
    save("book-the-seriously-epic-holiday-of-lottie-brooks", W, H, b)


def s_tom_gates():
    b = rect(0, 0, W, H, "#fff1c9", 0, 0) + curtains(0, W, 0, 330) + rect(0, 330, W, 70, WOOD, 0, 4) + mic_stage(600, 300)
    b += spotlight(600, 0, 360, 330) + star(600, 150, 50, BUTTER) + star(450, 90, 16, BERRY) + star(780, 80, 14, BLUE)
    b += notebook(160, 220, 200, 140, -8, PAPER, BLUE) + path("M190,262 q30,-30 60,0 q30,30 60,0", sw=5, stroke=BERRY)
    b += g(ell(0, 0, 50, 62, "#d9824a") + circ(0, 0, 18, INK, 4) + rect(40, -150, 18, 150, WOOD_DK, 3) + "".join(path(f"M{40},{-130 + i * 24} h18", sw=2.5) for i in range(5)), 1000, 330, 1, 8)
    b += g(path("M0,0 V-90", sw=5) + circ(0, -96, 14, INK, 3), 760, 382, 1) + g(path("M0,0 V-90", sw=5) + circ(0, -96, 14, INK, 3), 440, 382, 1)
    b += g(poly([(-30, 0), (30, 0), (24, -40), (-24, -40)], INK) + rect(-3, -60, 6, 24, INK, 2, 0) + circ(0, -66, 10, INK, 3), 600, 340, 1)
    save("book-tom-gates-is-not-famous-yet", W, H, b)


def s_wild_zone():
    b = rect(0, 0, W, H, "#e8c58a", 0, 0) + sun(1080, 70, 30) + hills(W, H, [(250, "#d9923b", 16, .3), (310, "#b5651d", 12, 1.2)]) + ground(350, "#9a6a2c")
    for x, y, s, c in [(100, 360, 1.5, "#e07a2e"), (260, 370, 1.1, "#c9923a"), (1080, 360, 1.5, "#d95a2b"), (940, 372, 1.1, "#e8a23c")]:
        b += tree(x, y, s, c)
    cab = rect(-70, -90, 140, 90, WOOD, 3) + poly([(-84, -90), (84, -90), (0, -150)], "#a8743f") + rect(-18, -54, 36, 54, WOOD_DK, 3) + rect(36, -76, 22, 22, "#ffe08a", 3, 3)
    b += g(cab, 220, 350, 1.1) + g(cab, 420, 358, .8)
    b += path("M560,350 V250 M620,350 V250 M680,350 V250 M740,350 V250 M540,270 H760 M540,310 H760", sw=6, stroke=WOOD_DK) + rect(600, 230, 120, 36, BERRY, 6) + txt(660, 256, "KEEP OUT", 22, WHITE)
    b += '<rect x="780" y="90" width="400" height="260" fill="#2c2a40" opacity=".55"/>' + "".join(circ(x, y, 7, "#ffe36e", 0) + circ(x + 22, y, 7, "#ffe36e", 0) for x, y in [(850, 240), (1010, 190), (1100, 280), (940, 310)])
    b += "".join(path(f"M{x},{y} q30,-20 60,0 q30,20 60,0", sw=6, stroke="#ffffff") for x, y in [(560, 170), (700, 130)]).replace('stroke="#ffffff"', 'stroke="#ffffff" opacity=".7"')
    b += star(980, 110, 10, BUTTER) if False else ""
    save("book-camp-half-blood-the-wild-zone", W, H, b)


def s_bog_frogs():
    b = rect(0, 0, W, H, "#27336b", 0, 0) + starfield([(80, 50), (190, 120), (350, 60), (520, 100), (700, 50), (880, 110), (1030, 60), (1140, 150), (440, 160), (780, 170)], 10) + moon(1040, 100, 44)
    b += path("M0,300 Q300,260 600,300 T1200,290 V400 H0 Z", "#2f8f5b") + rect(-4, 320, W + 8, 90, "#3a9d62", 0, 4)
    b += g(path("M0,0 L60,-150 L84,-140 L24,10 Z", "#9aa6c4") + rect(52, -166, 44, 22, "#6e7790", 6, 4, ) + path("M30,0 L-20,60 M30,0 L80,60 M30,0 L30,70", sw=6), 220, 340, 1.2)
    b += "".join(lilypad(x, y, w) for x, y, w in [(540, 350, 64), (720, 372, 54), (900, 352, 70), (1060, 376, 56)])
    b += frog(540, 346, 1.1) + frog(900, 348, 1.3, "#7fd18b") + frog(720, 368, .8, "#4aa860") + frog(1060, 372, .9)
    b += path("M600,230 q-8,-30 0,-60 M640,220 q-6,-24 0,-44", sw=4, stroke="#7fa6e6")
    b += txt(620, 170, "?", 52, BUTTER)
    b += "".join(star(x, y, r, c, 2.5) for x, y, r, c in [(420, 220, 12, BUTTER), (800, 200, 9, BUTTER)])
    save("book-rabbit-and-bear-the-bog-of-frogs", W, H, b)


def s_nina():
    b = rect(0, 0, W, H, "#fde9f1", 0, 0) + curtains(0, W, 0, 340) + rect(0, 340, W, 60, WOOD, 0, 4)
    b += spotlight(430, 0, 320, 340) + spotlight(790, 0, 320, 340)
    b += g(rect(0, 0, 220, 28, WOOD_DK, 4) + rect(10, 28, 10, 180, WOOD_DK, 2, 3) + rect(190, 28, 10, 180, WOOD_DK, 2, 3) + "".join(path(f"M{px},28 V208", sw=3) for px in (60, 110, 160)), 90, 150, 1)
    b += mask(430, 220, BUTTER, 1.6, "happy") + mask(790, 220, "#ff9ec2", 1.6, "sad")
    b += g(rect(-60, 0, 120, 14, MEADOW, 6, 4) + circ(-36, 22, 10, INK, 3) + circ(36, 22, 10, INK, 3), 1060, 340, 1) + g(rect(0, 0, 90, 12, "#e8c58a", 4, 3) + circ(10, 18, 8, INK, 3) + circ(70, 18, 8, INK, 3), 1040, 370, 1, -6)
    b += "".join(star(x, y, r, c, 2.5) for x, y, r, c in [(600, 90, 18, BUTTER), (280, 70, 10, BERRY), (960, 80, 10, BLUE), (610, 300, 12, BERRY)])
    b += "".join(path(f"M{x},{y} q-16,-16 0,-30 q16,14 0,30 Z", BERRY, 3) for x, y in [(610, 240), (572, 200), (650, 200)])
    save("book-nina-peanut-major-drama-alert", W, H, b)


def s_friendship_fails():
    b = rect(0, 0, W, H, "#eadcff", 0, 0) + curtains(0, W, 0, 330) + rect(0, 330, W, 70, WOOD, 0, 4) + spotlight(600, 0, 340, 330)
    b += path("M600,120 C540,60 470,110 520,170 L600,250 L680,170 C730,110 660,60 600,120 Z", BERRY) + path("M600,120 L586,170 L616,196 L596,250", sw=6, stroke=INK) + path("M586,170 L616,196", sw=0)
    for i, (x, y, c) in enumerate([(210, 250, BUTTER), (330, 290, MEADOW), (150, 330, BLUE)]):
        b += path(f"M{x - 50},{y} q50,-60 100,0", sw=12, stroke=INK) + path(f"M{x - 50},{y} q50,-60 100,0", sw=7, stroke=c) + "".join(circ(x - 40 + k * 20, y - 14 - (10 if 0 < k < 4 else 0) * 0.5, 5, [BERRY, WHITE, BLUE][k % 3], 2) for k in range(5))
    b += g(txt(0, 0, "♪", 70, INK) + txt(70, -30, "♫", 56, BERRY), 880, 200, 1) + g(txt(0, 0, "♬", 60, PURPLE), 1060, 150, 1)
    b += g(notebook(0, 0, 160, 110, 0, PAPER, PURPLE), 900, 270, 1, 6)
    b += star(420, 90, 14) + star(1100, 300, 12, BERRY) + star(760, 80, 10, BLUE)
    save("book-the-catastrophic-friendship-fails-of-lottie-brooks", W, H, b)


def s_dog_man():
    b = rect(0, 0, W, H, "#ffe9a8", 0, 0) + "".join(circ(x, y, r, c, 0) for x, y, r, c in [(120, 80, 14, BERRY), (300, 50, 10, BLUE), (980, 60, 14, MEADOW), (1130, 130, 10, PURPLE), (700, 40, 9, BERRY)])
    b += lightbulbs(0, 40, 12, 100, 30, [BERRY, BUTTER, BLUE, MEADOW, PURPLE]) if False else path("M0,40 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0 q50,40 100,0", sw=4)
    b += "".join(poly([(x, 52), (x + 26, 52), (x + 13, 100)], c, 3) for x, c in [(30, BERRY), (130, BLUE), (230, BUTTER), (330, MEADOW), (430, PURPLE), (530, BERRY), (630, BLUE), (730, BUTTER), (830, MEADOW), (930, PURPLE), (1030, BERRY), (1130, BLUE)])
    b += rect(-4, 330, W + 8, 70, "#d9a066", 0, 4) + cake(600, 352, 1.6)
    b += g(txt(0, 0, "10", 90, INK, "middle", 900), 600, 240, 1) if False else txt(600, 296, "10", 66, WHITE)
    b += party_hat(260, 360, BERRY, 1.3, -8) + party_hat(980, 360, BLUE, 1.4, 10) + party_hat(130, 380, BUTTER, 1)
    b += g(path("M0,-26 L24,-18 L24,6 Q24,24 0,34 Q-24,24 -24,6 L-24,-18 Z", BLUE) + star(0, -2, 10, BUTTER, 2), 400, 340, 1.5) + g(rect(-46, -10, 92, 20, WHITE, 10, 4) + circ(-46, -6, 12, WHITE, 4) + circ(-46, 6, 12, WHITE, 4) + circ(46, -6, 12, WHITE, 4) + circ(46, 6, 12, WHITE, 4), 830, 372, 1.1, -14)
    b += parcel(1060, 300, 90, 70, PURPLE, BUTTER) + parcel(1150, 330, 40, 40, BLUE, PAPER)
    save("book-dog-man-10th-birthday-edition", W, H, b)


def s_detective():
    b = rect(0, 0, W, H, "#e9f0ff", 0, 0) + rect(0, 320, W, 80, "#c9b79a", 0, 4) + rect(70, 60, 260, 170, "#2f6b55", 8) + path("M96,100 h200 M96,140 h150 M96,180 h180", sw=3, stroke=WHITE)
    b += rect(60, 230, 280, 14, WOOD_DK, 3)
    b += g(rect(0, 0, 120, 14, WOOD, 3) + rect(8, 14, 8, 60, WOOD_DK, 2, 3) + rect(104, 14, 8, 60, WOOD_DK, 2, 3), 500, 330, 1.6)
    b += talker(480, 322, "lamp", 1.5) + talker(660, 322, "mug", 1.6) + talker(820, 322, "stapler", 1.4)
    b += magnifier(260, 320, 1, 56) + path("M300,350 l60,-20", sw=0)
    b += path("M1020,380 q-20,-60 20,-100 q-4,40 24,50 q10,-50 40,-70 q-6,50 26,80 Z", "#ef8a3c") + path("M1050,380 q-8,-30 10,-50 q8,24 22,30 Z", BUTTER, 3)
    b += "".join(txt(x, y, "?", s, BERRY) for x, y, s in [(560, 150, 56), (730, 170, 46), (880, 140, 52)]) + star(420, 90, 12)
    save("book-detective-thingy-majiggy", W, H, b)


def s_danger_game():
    b = rect(0, 0, W, H, "#1b1f4a", 0, 0) + starfield([(80, 60), (200, 150), (1100, 60), (1130, 300), (90, 330)], 10)
    b += rect(250, 40, 700, 300, INK, 16, 6) + rect(274, 64, 652, 252, "#0f1237", 8, 3)
    b += rect(274, 270, 652, 46, "#2f8f5b", 0, 3) + "".join(rect(x, 230, 50, 40, "#4cb87a", 0, 3) for x in (340, 560, 760))
    b += pixel_hero(430, 168, 1.6).replace("1.6", "1.6")
    b += "".join(diamond(x, y) for x, y in [(560, 130), (650, 90), (740, 140), (820, 100), (880, 170)])
    b += "".join(rect(300 + i * 44, 80, 34, 18, [BERRY, BUTTER, BLUE, MEADOW, PURPLE][i], 3, 2.5) for i in range(5)) + txt(780, 78, "LEVEL 5", 22, WHITE)
    b += g(rect(-50, 0, 100, 26, "#2f3b66", 8, 4) + rect(-8, -44, 16, 44, INK, 4, 3) + circ(0, -52, 18, BERRY, 4) + circ(-30, 12, 8, BUTTER, 2.5) + circ(30, 12, 8, MEADOW, 2.5), 190, 350, 1.1) + g(rect(-50, 0, 100, 26, "#2f3b66", 8, 4) + rect(-8, -44, 16, 44, INK, 4, 3) + circ(0, -52, 18, BLUE, 4), 1010, 350, 1.1)
    b += star(1090, 120, 14, BUTTER) + star(130, 150, 10, BERRY)
    save("book-the-danger-game", W, H, b)


def s_football():
    b = rect(0, 0, W, H, "#cfe9ff", 0, 0) + sun(1100, 70, 34) + cloud(300, 70, 1)
    b += rect(0, 120, W, 40, "#6e7790", 0, 3) + "".join(rect(x, 100, 18, 60, c, 0, 2.5) for x, c in [(40, BERRY), (160, WHITE), (280, BERRY), (400, WHITE), (520, BERRY), (640, WHITE), (760, BERRY), (880, WHITE), (1000, BERRY), (1120, WHITE)])
    b += rect(-4, 160, W + 8, 240, "#4cb87a", 0, 4) + "".join(rect(x, 160, 100, 240, "#5cc88a", 0, 0) for x in range(0, W, 200))
    b += path("M0,380 H1200 M600,160 V400", sw=6, stroke=WHITE) + circ(600, 300, 60, "none", 6).replace('fill="none"', 'fill="none"').replace(f'stroke="{INK}"', 'stroke="#ffffff"')
    b += rect(60, 200, 200, 160, "none", 6).replace(f'stroke="{INK}"', 'stroke="#ffffff"') + rect(940, 200, 200, 160, "none", 6).replace(f'stroke="{INK}"', 'stroke="#ffffff"')
    b += trophy_ball(250, 350, 1.2) + boot(480, 372, 1.5, BERRY) + football(700, 356, 34) + g(boot(0, 0, 1, BLUE), 900, 380, 1.4, 0)
    b += star(460, 80, 12) + star(980, 70, 10, BERRY)
    save("book-classic-football-heroes-best", W, H, b)


def s_hub():
    b = starfield([(80, 60), (210, 120), (990, 60), (1130, 140)], 10)
    b += rect(-4, 340, W + 8, 70, "#d9a066", 0, 4)
    steps = [(340, 120, BLUE, "2"), (520, 190, BERRY, "1"), (700, 90, MEADOW, "3")]
    for x, h, c, n in steps:
        b += rect(x, 340 - h, 160, h, c, 8) + txt(x + 80, 340 - h + 60, n, 54, WHITE)
    b += trophy_ball(600, 150, 1.0) if False else star(600, 100, 34, BUTTER)
    b += book_stack(190, 392, [(180, 40, PURPLE), (160, 36, BUTTER), (170, 36, BERRY)]) + book_stack(1010, 392, [(180, 40, MEADOW), (160, 36, BLUE), (170, 36, BUTTER)])
    b += star(430, 80, 12, BERRY) + star(780, 70, 10, BLUE) + star(150, 200, 9) + star(1060, 230, 9, BERRY)
    save("banner-top-20-childrens-books", W, H, b, "#fff1c9")


ALL = [s_wimpy, s_gruffalo_granny, s_bunny_monkey, s_lottie_xmas, s_disaster_dad, s_rowley, s_donut, s_squad_girls, s_milly,
       s_ghost_toast, s_lottie_holiday, s_tom_gates, s_wild_zone, s_bog_frogs, s_nina, s_friendship_fails, s_dog_man,
       s_detective, s_danger_game, s_football, s_hub]

if __name__ == "__main__":
    for fn in ALL:
        fn()
    print("top-20 illustrations written:", len(ALL))
