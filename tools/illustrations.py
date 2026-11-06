#!/usr/bin/env python3
"""Generates every illustration on childrensbooks.ie as original SVG artwork.

All characters are generic, invented animals (a bear, a rabbit, an owl, a fox) —
nothing here copies an existing book, character or cover. Run:  python3 tools/illustrations.py
"""
import math
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "img")
os.makedirs(OUT, exist_ok=True)

INK = "#1f2a44"
SKY = "#e8f4f8"
MEADOW = "#2f8f5b"
LEAF = "#5cb86f"
BUTTER = "#ffcf4a"
BERRY = "#d6336c"
BLUE = "#3a8fd1"
PURPLE = "#7c4dbd"
PAPER = "#fffef9"
WOOD = "#c98a4b"
WOOD_DK = "#a8743f"
BEAR = "#b9773e"
BEAR_LT = "#f1cf9b"
BUNNY = "#e7defa"
PINK = "#ffb3c7"
FOX = "#ec7a2e"
CREAM = "#fff1d6"
NIGHT = "#27336b"
WHITE = "#ffffff"
BOOK_COLORS = [BERRY, MEADOW, BLUE, BUTTER, PURPLE, "#ef8a3c", "#2aa7a0", INK]


# ---------------------------------------------------------------- primitives
def circ(cx, cy, r, f, sw=4):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}" stroke="{INK}" stroke-width="{sw}"/>'


def ell(cx, cy, rx, ry, f, rot=0, sw=4):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f}" stroke="{INK}" stroke-width="{sw}"{t}/>'


def rect(x, y, w, h, f, rx=0, sw=4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>'


def path(d, f="none", sw=4, stroke=INK):
    return f'<path d="{d}" fill="{f}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'


def poly(pts, f, sw=4):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polygon points="{p}" fill="{f}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>'


def dot(cx, cy, r=5, f=INK):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}"/>'


def g(body, x=0, y=0, s=1, rot=0, flip=False):
    sx = -s if flip else s
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sx} {s})">{body}</g>'


def txt(x, y, s, size=28, f=INK, anchor="middle", weight=700):
    return (f'<text x="{x}" y="{y}" font-family="Atkinson Hyperlegible, Verdana, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{f}" text-anchor="{anchor}">{s}</text>')


def blob(shapes, f, sw=4):
    """Outlined union of shapes: stroke pass, then fill pass to hide inner outlines."""
    a, b = "", ""
    for sh in shapes:
        k = sh[0]
        if k == "c":
            _, cx, cy, r = sh
            a += f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'
        elif k == "e":
            _, cx, cy, rx, ry = sh
            a += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>'
        elif k == "r":
            _, x, y, w, h, rx = sh
            a += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'
    return (f'<g fill="{f}" stroke="{INK}" stroke-width="{sw * 2}" stroke-linejoin="round">{a}</g>'
            f'<g fill="{f}">{a}</g>')


def star(cx, cy, r, f=BUTTER, sw=3):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.46
        pts.append((round(cx + rr * math.cos(ang), 1), round(cy + rr * math.sin(ang), 1)))
    return poly(pts, f, sw)


def starfield(pts, r=8):
    return "".join(star(x, y, r) for x, y in pts)


def cloud(x, y, s=1, f=WHITE):
    return g(blob([("c", 0, 0, 30), ("c", 38, -14, 38), ("c", 82, 0, 30), ("r", 0, -2, 82, 32, 16)], f, 3), x, y, s)


def sun(x, y, r=42, face=False):
    rays = ""
    for i in range(12):
        a = i * math.pi / 6
        rays += path(f"M{x + (r + 10) * math.cos(a):.1f},{y + (r + 10) * math.sin(a):.1f} L{x + (r + 28) * math.cos(a):.1f},{y + (r + 28) * math.sin(a):.1f}", sw=5)
    out = rays + circ(x, y, r, BUTTER)
    if face:
        out += dot(x - 14, y - 6, 4) + dot(x + 14, y - 6, 4) + path(f"M{x - 14},{y + 10} q14,14 28,0", sw=4)
    return out


def moon(x, y, r=40):
    return (circ(x, y, r, "#ffe08a") + circ(x - r * .3, y - r * .25, r * .16, "#f5c95c", 0) +
            circ(x + r * .35, y + r * .2, r * .22, "#f5c95c", 0) + circ(x - r * .1, y + r * .5, r * .1, "#f5c95c", 0))


def hills(w, h, layers):
    out = ""
    for ytop, color, amp, ph in layers:
        d = f"M0,{h} L0,{ytop}"
        steps = 6
        for i in range(steps):
            x1 = w * (i + .5) / steps
            x2 = w * (i + 1) / steps
            yy = ytop + amp * math.sin(ph + (i + 1) * 1.7)
            d += f" Q{x1:.0f},{ytop - amp * (1.5 if i % 2 == 0 else -1.2):.0f} {x2:.0f},{yy:.0f}"
        d += f" L{w},{h} Z"
        out += path(d, color)
    return out


def tree(x, y, s=1, f=LEAF):
    return g(rect(-12, -70, 24, 70, WOOD_DK, 4) +
             blob([("c", 0, -120, 52), ("c", -40, -90, 38), ("c", 40, -90, 38), ("c", 0, -75, 40)], f), x, y, s)


def flower(x, y, c=BERRY, s=1):
    petals = "".join(circ(round(12 * math.cos(a), 1), round(-34 + 12 * math.sin(a), 1), 8, c, 3)
                     for a in [i * 2 * math.pi / 5 for i in range(5)])
    return g(path("M0,0 Q4,-16 0,-34", sw=4, stroke=MEADOW) + petals + circ(0, -34, 7, BUTTER, 3), x, y, s)


def shamrock(x, y, s=1, f=MEADOW):
    return g(path("M0,0 Q6,22 16,34", sw=4) +
             "".join(g(blob([("c", -11, -14, 14), ("c", 11, -14, 14), ("c", 0, -4, 3)], f, 3), 0, 0, 1, a) for a in (0, 120, 240)), x, y, s)


def sheep(x, y, s=1):
    return g(path("M-18,24 v20 M18,24 v20", sw=5) +
             blob([("c", -22, 0, 22), ("c", 0, -10, 26), ("c", 24, 0, 22), ("c", 0, 8, 24)], WHITE, 3) +
             ell(-34, 8, 14, 16, "#40465c", 0, 3), x, y, s)


# ------------------------------------------------------------------ books
def book_flat(x, y, w, h, f, band=BUTTER):
    return rect(x, y, w, h, f, 4) + \
        path(f"M{x + w * .12},{y + h * .3} h{w * .76} M{x + w * .12},{y + h * .7} h{w * .76}", sw=3, stroke=band)


def book_stack(x, y, specs):
    """specs: list of (w, h, color) from bottom up; x is centre, y is the floor."""
    out, cy = "", y
    for i, (w, h, c) in enumerate(specs):
        cy -= h
        off = (-1) ** i * (6 + 3 * i)
        out += book_flat(x - w / 2 + off, cy, w, h, c)
    return out


def book_open(cx, cy, w=220, h=110, cover=BLUE):
    hw = w / 2
    cov = path(f"M{cx - hw - 10},{cy + 6} L{cx - hw - 10},{cy + h - 2} Q{cx - hw * .5},{cy + h + 12} {cx},{cy + h + 2} Q{cx + hw * .5},{cy + h + 12} {cx + hw + 10},{cy + h - 2} L{cx + hw + 10},{cy + 6} Z", cover)
    left = path(f"M{cx},{cy + 10} Q{cx - hw * .45},{cy - 14} {cx - hw},{cy - 4} L{cx - hw},{cy + h - 14} Q{cx - hw * .45},{cy + h - 28} {cx},{cy + h - 8} Z", PAPER)
    right = path(f"M{cx},{cy + 10} Q{cx + hw * .45},{cy - 14} {cx + hw},{cy - 4} L{cx + hw},{cy + h - 14} Q{cx + hw * .45},{cy + h - 28} {cx},{cy + h - 8} Z", PAPER)
    lines = ""
    for k in range(4):
        yy = cy + 20 + k * 18
        lines += path(f"M{cx - hw + 20},{yy - 4 + k} Q{cx - hw * .5},{yy - 14 + k} {cx - 14},{yy - 2}", sw=3, stroke="#9aa6c4")
        lines += path(f"M{cx + 14},{yy - 2} Q{cx + hw * .5},{yy - 14 + k} {cx + hw - 20},{yy - 4 + k}", sw=3, stroke="#9aa6c4")
    return cov + left + right + lines


def shelf_books(x, y, w, h, seed=1):
    rnd = random.Random(seed)
    out, cx, i = "", x, 0
    while cx < x + w - 20:
        bw = rnd.randint(18, 32)
        if cx + bw > x + w:
            break
        bh = int(h * rnd.uniform(.68, 1))
        c = BOOK_COLORS[(i + seed) % len(BOOK_COLORS)]
        out += rect(cx, y - bh, bw, bh, c, 2, 3)
        out += path(f"M{cx + 3},{y - bh + 14} h{bw - 6} M{cx + 3},{y - 14} h{bw - 6}", sw=2.5, stroke=PAPER)
        cx += bw + 1
        i += 1
    return out


def bookcase(x, y, w, h, rows=3, seed=3):
    out = rect(x, y, w, h, WOOD) + rect(x + 14, y + 14, w - 28, h - 28, WOOD_DK, 0, 3)
    rh = (h - 28) / rows
    for r in range(rows):
        base = y + 14 + rh * (r + 1) - 8
        out += shelf_books(x + 18, base, w - 36, rh - 24, seed + r)
        out += rect(x + 14, base, w - 28, 10, WOOD, 0, 3)
    return out


# ---------------------------------------------------------------- characters (origin = ground, centre)
def bear(x, y, s=1, fur=BEAR, belly=BEAR_LT, arms=True, eyes="open"):
    b = ell(-34, -14, 26, 16, fur) + ell(34, -14, 26, 16, fur)
    b += ell(0, -70, 56, 64, fur) + ell(0, -62, 36, 44, belly, 0, 0)
    if arms:
        b += ell(-58, -78, 15, 34, fur, 18) + ell(58, -78, 15, 34, fur, -18)
    b += circ(-40, -190, 17, fur) + circ(40, -190, 17, fur) + circ(-40, -190, 8, belly, 0) + circ(40, -190, 8, belly, 0)
    b += circ(0, -150, 50, fur) + ell(0, -137, 24, 18, belly) + ell(0, -146, 9, 6, INK)
    b += path("M0,-140 v6 M-9,-130 q9,8 18,0", sw=3)
    if eyes == "open":
        b += dot(-19, -159, 5) + dot(19, -159, 5)
    else:
        b += path("M-26,-158 q7,6 14,0 M12,-158 q7,6 14,0", sw=3)
    return g(b, x, y, s)


def rabbit(x, y, s=1, fur=BUNNY, arms=True):
    b = ell(-20, -190, 13, 44, fur, -8) + ell(20, -190, 13, 44, fur, 8)
    b += ell(-20, -190, 6, 32, PINK, -8, 0) + ell(20, -190, 6, 32, PINK, 8, 0)
    b += ell(-26, -12, 24, 14, fur) + ell(26, -12, 24, 14, fur)
    b += ell(0, -62, 46, 56, fur) + ell(0, -56, 28, 38, WHITE, 0, 0)
    if arms:
        b += ell(-48, -68, 12, 28, fur, 15) + ell(48, -68, 12, 28, fur, -15)
    b += ell(0, -130, 42, 38, fur) + dot(-15, -136, 5) + dot(15, -136, 5)
    b += ell(0, -122, 7, 5, PINK, 0, 3) + path("M0,-117 v6 M-8,-108 q8,7 16,0", sw=3)
    b += circ(-28, -120, 7, PINK, 0) + circ(28, -120, 7, PINK, 0)
    return g(b, x, y, s)


def owl(x, y, s=1, fur="#8b6a4b", belly="#d9b98e", flip=False):
    b = ell(-18, -5, 14, 6, BUTTER, 0, 3) + ell(18, -5, 14, 6, BUTTER, 0, 3)
    b += poly([(-42, -118), (-50, -154), (-18, -134)], fur) + poly([(42, -118), (50, -154), (18, -134)], fur)
    b += ell(0, -70, 52, 68, fur) + ell(0, -58, 34, 48, belly, 0, 0)
    b += path("M-20,-62 q10,10 20,0 q10,10 20,0 M-20,-42 q10,10 20,0 q10,10 20,0 M-10,-22 q10,10 20,0", sw=3, stroke=fur)
    b += ell(-52, -68, 15, 42, "#6e5239", 10) + ell(52, -68, 15, 42, "#6e5239", -10)
    b += circ(-21, -98, 19, WHITE) + circ(21, -98, 19, WHITE) + dot(-21, -98, 8) + dot(21, -98, 8)
    b += dot(-18, -102, 2.6, WHITE) + dot(24, -102, 2.6, WHITE)
    b += poly([(-8, -88), (8, -88), (0, -72)], BUTTER)
    return g(b, x, y, s, 0, flip)


def fox(x, y, s=1, flip=False):
    b = path("M36,-24 C120,-10 140,-96 100,-132 C88,-100 74,-64 36,-62 Z", FOX)
    b += circ(100, -128, 14, WHITE, 3)
    b += ell(-18, -8, 16, 10, CREAM) + ell(18, -8, 16, 10, CREAM)
    b += ell(0, -62, 44, 62, FOX) + ell(0, -55, 26, 44, CREAM, 0, 0)
    b += poly([(-46, -150), (-40, -204), (-14, -168), (14, -168), (40, -204), (46, -150), (30, -112), (0, -98), (-30, -112)], FOX)
    b += poly([(-36, -176), (-36, -192), (-24, -172)], INK, 0) + poly([(36, -176), (36, -192), (24, -172)], INK, 0)
    b += poly([(-30, -112), (0, -98), (30, -112), (16, -134), (-16, -134)], CREAM, 3)
    b += dot(0, -102, 6) + dot(-20, -146, 5) + dot(20, -146, 5)
    return g(b, x, y, s, 0, flip)


def whale(x, y, s=1, f="#4f7fcf"):
    b = path("M-160,0 C-160,-90 -60,-130 40,-110 C120,-95 170,-40 190,-90 C200,-60 215,-30 190,-10 C215,-20 215,-60 235,-80 C240,-30 215,10 170,12 C100,40 -60,50 -160,0 Z", f)
    b += ell(-40, 14, 90, 22, "#cfe0ff", 0, 0)
    b += dot(-110, -42, 6) + path("M-120,-18 q20,12 44,0", sw=3)
    b += path("M-60,-112 C-60,-150 -90,-160 -100,-190 M-60,-112 C-60,-150 -30,-160 -20,-190", sw=4, stroke="#9ed3f5")
    return g(b, x, y, s)


def rocket(x, y, s=1, rot=0):
    b = path("M-34,40 L-66,90 L-34,76 Z M34,40 L66,90 L34,76 Z", BERRY)
    b += path("M0,-120 C50,-80 50,0 34,60 L-34,60 C-50,0 -50,-80 0,-120 Z", PAPER)
    b += path("M0,-120 C22,-104 36,-88 42,-70 L-42,-70 C-36,-88 -22,-104 0,-120 Z", BERRY)
    b += circ(0, -30, 22, "#bfe3f2") + path("M-22,60 h44 L28,76 h-56 Z", BLUE)
    b += path("M-18,76 Q0,130 18,76 Z", BUTTER)
    return g(b, x, y, s, rot)


def swan(x, y, s=1, flip=False):
    b = path("M72,-12 C104,-44 96,-84 70,-100", sw=20, stroke=INK) + path("M72,-12 C104,-44 96,-84 70,-100", sw=12, stroke=WHITE)
    b += path("M-70,0 C-60,-42 40,-50 78,-22 C92,-12 94,2 80,6 C40,16 -40,16 -70,0 Z", WHITE)
    b += path("M-30,-14 C0,-42 40,-36 60,-14 C30,-18 0,-6 -30,-14 Z", "#cfd9f2", 3)
    b += circ(66, -102, 13, WHITE, 4) + poly([(76, -106), (102, -98), (76, -94)], BUTTER, 3) + dot(64, -106, 3)
    return g(b, x, y, s, 0, flip)


def face(x, y, mood, r=1.0):
    e = dot(-12, -4, 4) + dot(12, -4, 4)
    m = {"happy": "M-14,10 q14,16 28,0", "sad": "M-12,18 q12,-12 24,0", "angry": "M-12,16 h24",
         "worried": "M-12,16 q6,-6 12,0 q6,6 12,0", "calm": "M-12,12 q12,8 24,0"}[mood]
    if mood == "angry":
        e += path("M-20,-14 l14,6 M20,-14 l-14,6", sw=3.5)
    if mood == "worried":
        e += path("M-20,-10 l12,-5 M20,-10 l-12,-5", sw=3.5)
    return g(e + path(m, sw=4), x, y, r)


def parcel(x, y, w, h, f, ribbon=BUTTER):
    return (rect(x, y, w, h, f, 4) + rect(x + w / 2 - 9, y, 18, h, ribbon, 0, 3) + rect(x, y + h / 2 - 9, w, 18, ribbon, 0, 3) +
            ell(x + w / 2 - 14, y - 10, 16, 11, ribbon, -20, 3) + ell(x + w / 2 + 14, y - 10, 16, 11, ribbon, 20, 3))


# --------------------------------------------------------------------- save
def save(name, w, h, body, bg=None):
    bgel = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as fh:
        fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{bgel}{body}</svg>')


# ------------------------------------------------------------------- scenes
def logo():
    b = path("M6,20 Q20,12 32,20 Q44,12 58,20 V50 Q44,42 32,50 Q20,42 6,50 Z", MEADOW, 3.5)
    b += path("M32,20 V50", sw=3.5) + star(32, 10, 7, BUTTER, 2.5)
    b += path("M13,28 Q20,25 26,28 M13,35 Q20,32 26,35 M38,28 Q44,25 51,28 M38,35 Q44,32 51,35", sw=2.5, stroke=PAPER)
    save("logo", 64, 64, b)


def hero():
    b = rect(0, 0, 800, 640, "#ffeec2", 0, 0) + rect(0, 470, 800, 170, "#d9a066", 0, 0) + path("M0,470 H800")
    for i in range(1, 8):
        b += path(f"M{i * 100},470 L{i * 100 - 40 * (i - 4) / 3:.0f},640", sw=2, stroke="#c58a50")
    # window
    b += rect(40, 70, 210, 270, NIGHT) + starfield([(90, 120), (205, 108), (185, 250), (80, 262), (215, 180)], 8) + moon(140, 190, 38)
    b += path("M145,70 V340 M40,205 H250", sw=5) + rect(40, 70, 210, 270, "none") + rect(26, 340, 238, 18, WOOD)
    b += path("M28,58 H86 Q70,200 92,352 H28 Z", BERRY) + path("M262,58 H204 Q220,200 200,352 H262 Z", BERRY)
    # bookcase + owl
    b += bookcase(550, 70, 220, 400, 3, 5) + owl(660, 72, .55)
    # rug
    b += ell(400, 566, 320, 64, BERRY) + '<ellipse cx="400" cy="566" rx="270" ry="46" fill="none" stroke="#ffcf4a" stroke-width="6" stroke-dasharray="14 10"/>'
    b += bear(300, 566, 1.05) + rabbit(498, 566, 1.0) + book_open(399, 520, 196, 96, BLUE)
    b += star(380, 120, 12, BUTTER) + star(470, 90, 8, BERRY) + star(330, 60, 9, BLUE)
    save("hero-reading-nook", 800, 640, b)


def banner_babies():
    b = hills(1200, 400, [(300, "#cdeccd", 14, 0.3)]) + sun(1040, 90, 40, True) + cloud(180, 90, 1) + cloud(560, 60, .8)
    # mobile
    b += path("M300,0 V50 M360,0 V80 M420,0 V50", sw=3) + star(300, 66, 16) + circ(360, 96, 15, BERRY) + star(420, 66, 16, BLUE)
    b += ell(430, 350, 380, 48, "#ffd9a8") + '<ellipse cx="430" cy="350" rx="320" ry="34" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="12 10"/>'
    b += bear(360, 362, .95, eyes="open")
    blocks = [(540, 300, 56, BERRY, "A"), (606, 300, 56, BLUE, "B"), (573, 244, 56, MEADOW, "C")]
    for x, y, s, c, t in blocks:
        b += rect(x, y, s, s, c, 6) + txt(x + s / 2, y + 40, t, 34, WHITE)
    b += book_stack(800, 372, [(150, 30, MEADOW), (130, 28, BUTTER), (140, 28, BERRY)])
    b += rabbit(930, 372, .62, arms=True)
    save("banner-babies", 1200, 400, b, "#fff4cc")


def banner_preschool():
    b = sun(120, 90, 40) + cloud(420, 70, 1) + hills(1200, 400, [(280, "#a9dca3", 16, 0.8), (330, "#5cb86f", 12, 1.6)])
    b += tree(150, 330, 1.25) + tree(1000, 340, 1.4, "#4aa860") + tree(1120, 320, 1)
    b += fox(430, 372, 1.05) + book_open(560, 300, 200, 100, BERRY) + owl(780, 372, .9, flip=True)
    b += flower(660, 380, BERRY) + flower(700, 384, BUTTER) + flower(300, 384, BLUE, .9) + flower(880, 384, PINK)
    save("banner-preschool", 1200, 400, b, "#d6efff")


def banner_early():
    b = sun(1050, 80, 40) + cloud(150, 70, 1) + cloud(620, 110, .8)
    # kite
    b += poly([(860, 70), (900, 110), (860, 160), (820, 110)], BERRY) + path("M860,70 V160 M820,110 H900", sw=3, stroke=PAPER)
    b += path("M860,160 Q830,230 900,290", sw=3) + poly([(870, 190), (884, 200), (870, 210)], BUTTER, 3)
    b += hills(1200, 400, [(310, "#8fd08a", 22, 0.4), (350, "#5cb86f", 12, 2)])
    b += rabbit(480, 372, 1.1) + book_open(480, 302, 190, 90, MEADOW) + book_stack(700, 384, [(160, 32, BLUE), (140, 30, BUTTER), (150, 30, BERRY), (120, 28, PURPLE)])
    b += flower(250, 388, BERRY) + flower(300, 392, BUTTER, .9) + flower(980, 390, BLUE) + flower(1040, 386, PINK)
    save("banner-early-readers", 1200, 400, b, "#cfe9ff")


def banner_middle():
    b = starfield([(80, 60), (210, 120), (330, 50), (520, 90), (700, 40), (900, 70), (1040, 150), (1130, 60), (620, 150)], 9)
    b += moon(960, 110, 58)
    waves = ""
    for i, (yy, c) in enumerate([(300, "#3a6fc2"), (340, "#2f5aa8"), (380, "#264a8c")]):
        d = f"M0,{yy}"
        for x in range(0, 1200, 100):
            d += f" q25,-22 50,0 t50,0"
        d += " V400 H0 Z"
        waves += path(d, c)
    boat = path("M-90,0 L90,0 L60,46 L-60,46 Z", WOOD_DK) + path("M0,0 V-170", sw=5) + path("M6,-165 Q90,-100 6,-20 Z", PAPER) + path("M-6,-150 Q-70,-95 -6,-30 Z", CREAM) + poly([(0, -170), (-44, -156), (0, -142)], BERRY)
    b += whale(210, 330, .8) + waves + g(boat, 640, 300)
    save("banner-middle-grade", 1200, 400, b, "#1f3a73")


def banner_irish_authors():
    b = ""
    for i, c in enumerate([BERRY, BUTTER, LEAF, BLUE, PURPLE]):
        b += f'<circle cx="600" cy="420" r="{380 - i * 24}" fill="none" stroke="{c}" stroke-width="22" opacity=".9"/>'
    b += cloud(140, 90, 1) + cloud(940, 70, 1.1)
    b += hills(1200, 400, [(280, "#8fd08a", 18, .5), (330, "#4aa860", 14, 1.4)])
    tower = rect(-28, -190, 56, 190, "#9aa3b8", 2) + poly([(-34, -190), (34, -190), (0, -270)], "#6e7790") + rect(-9, -40, 18, 40, INK, 8, 3) + rect(-8, -130, 16, 26, INK, 8, 3) + path("M-28,-60 h56 M-28,-100 h56 M-28,-150 h56", sw=2.5, stroke="#6e7790")
    b += g(tower, 560, 330, .85)
    b += path("M60,360 H320 M60,372 H320", sw=3, stroke="#6e7790") + sheep(780, 352, .8) + sheep(880, 366, .65) + sheep(150, 356, .7)
    b += book_open(980, 300, 190, 90, BERRY) + flower(430, 384, BUTTER) + flower(480, 390, BERRY, .9) + flower(300, 392, BLUE, .8)
    save("banner-irish-authors", 1200, 400, b, "#cfeaf5")


def banner_irish_language():
    b = ""
    for x, y, s, c in [(90, 90, 1, MEADOW), (1100, 80, 1.2, LEAF), (600, 70, .8, MEADOW), (250, 300, .9, LEAF), (950, 320, 1, MEADOW)]:
        b += shamrock(x, y, s, c)
    b += ell(600, 372, 520, 30, "#bfe6c6", 0, 0) + owl(380, 372, 1.15) + fox(840, 372, 1.0, flip=True)
    b += path("M310,110 h170 q16,0 16,16 v44 q0,16 -16,16 h-90 l-24,26 v-26 h-56 q-16,0 -16,-16 v-44 q0,-16 16,-16 Z", PAPER)
    b += txt(402, 156, "Dia duit!", 34)
    b += path("M640,50 h290 q16,0 16,16 v44 q0,16 -16,16 h-60 v26 l-24,-26 h-206 q-16,0 -16,-16 v-44 q0,-16 16,-16 Z", PAPER)
    b += txt(788, 96, "Dia is Muire duit!", 32)
    save("banner-irish-language", 1200, 400, b, "#e1f5e5")


def banner_myths():
    b = starfield([(90, 50), (220, 110), (390, 40), (560, 90), (760, 40), (980, 80), (1100, 150), (700, 130)], 9) + moon(1000, 100, 54)
    b += path("M0,260 L140,150 L260,230 L400,120 L560,240 L700,160 L860,250 L1000,170 L1200,260 V400 H0 Z", "#4b3f8f")
    b += path("M0,300 L180,230 L330,290 L520,220 L700,300 L900,240 L1200,310 V400 H0 Z", "#3a3077")
    b += rect(-4, 300, 1208, 110, "#2a4a8f", 0, 4)
    for i in range(7):
        b += path(f"M{100 + i * 170},{330 + (i % 3) * 20} q30,-8 60,0", sw=3, stroke="#7fa6e6")
    b += ell(480, 352, 130, 12, "#3c63b3", 0, 0) + swan(480, 332, 1.5) + ell(780, 372, 80, 8, "#3c63b3", 0, 0) + swan(780, 358, .95, flip=True)
    for x in (90, 130, 1100, 1140):
        b += path(f"M{x},400 Q{x - 6},350 {x + 4},300", sw=4, stroke=LEAF) + ell(x + 4, 296, 6, 18, "#8a5a3c", 0, 3)
    save("banner-myths", 1200, 400, b, "#2b2766")


def banner_bedtime():
    b = starfield([(90, 60), (210, 130), (360, 50), (510, 110), (640, 40), (850, 90), (1040, 60), (1120, 160), (730, 160)], 9) + moon(1110, 70, 46)
    b += rect(-4, 330, 1208, 80, "#c58a50", 0, 4)
    bed = rect(280, 230, 560, 120, WOOD_DK, 8) + rect(260, 170, 36, 190, WOOD, 6) + rect(830, 200, 36, 160, WOOD, 6)
    bed += rect(300, 250, 520, 70, WHITE, 14) + ell(380, 252, 78, 30, "#cfe3ff", 0, 4)
    b += bed
    bh = circ(380, 244, 40, BEAR) + circ(350, 212, 14, BEAR) + circ(410, 212, 14, BEAR) + ell(380, 256, 18, 13, BEAR_LT) + ell(380, 250, 7, 5, INK, 0, 0) + path("M352,238 q7,6 14,0 M394,238 q7,6 14,0", sw=3)
    b += bh + path("M420,262 H820 Q840,262 840,290 V330 H420 Z", BERRY) + "".join(star(470 + i * 90, 296 + (i % 2) * 14, 11, BUTTER, 2.5) for i in range(4))
    b += book_open(630, 238, 150, 62, MEADOW)
    b += txt(470, 170, "z", 40, WHITE) + txt(510, 130, "z", 52, WHITE) + txt(560, 84, "Z", 66, WHITE)
    # bedside lamp
    b += rect(910, 270, 120, 80, WOOD, 6) + path("M970,270 V230", sw=5) + poly([(930, 235), (1010, 235), (990, 175), (950, 175)], BUTTER) + circ(970, 200, 100, "#ffe08a").replace('fill="#ffe08a"', 'fill="#ffe08a" opacity=".18"').replace('stroke="#1f2a44" stroke-width="4"', 'stroke="none"')
    save("banner-bedtime", 1200, 400, b, "#2b3a78")


def banner_feelings():
    b = ""
    b += sun(150, 190, 56, False) + face(150, 190, "happy", 1.5)
    b += g(blob([("c", 0, 0, 40), ("c", 50, -16, 50), ("c", 106, 0, 40), ("r", 0, 0, 106, 40, 20)], "#9fb7d9", 4), 290, 170, 1.15) + face(367, 178, "sad", 1.5)
    b += "".join(path(f"M{320 + i * 40},{260 + (i % 2) * 20} l-10,26", sw=6, stroke=BLUE) for i in range(3))
    b += g(blob([("c", 0, 0, 40), ("c", 50, -16, 50), ("c", 106, 0, 40), ("r", 0, 0, 106, 40, 20)], "#6b5d99", 4), 540, 170, 1.15) + face(617, 178, "angry", 1.5)
    b += poly([(600, 232), (574, 280), (598, 280), (584, 330), (636, 262), (610, 262), (626, 232)], BUTTER)
    b += g("".join(path(f"M{-60},{i * 26} q30,-16 60,0 t60,0", sw=7, stroke="#b8c0d4") for i in range(5)), 800, 130, 1)
    b += circ(830, 160, 54, "#d7ddec", 3) + face(830, 160, "worried", 1.5)
    for i, c in enumerate([BERRY, "#ef8a3c", BUTTER, LEAF, BLUE, PURPLE]):
        r = 112 - i * 14
        b += f'<path d="M{1070 - r},330 A{r},{r} 0 0 1 {1070 + r},330" fill="none" stroke="{c}" stroke-width="14"/>'
    b += face(1070, 318, "calm", .8)
    b += txt(150, 340, "happy", 26) + txt(360, 360, "sad", 26) + txt(600, 370, "cross", 26) + txt(830, 280, "worried", 26) + txt(1070, 372, "calm", 26)
    save("banner-feelings", 1200, 400, b, "#fff3d6")


def banner_gifts():
    b = "".join(star(x, y, r, c, 2.5) for x, y, r, c in [(90, 70, 14, BUTTER), (260, 120, 10, BERRY), (520, 60, 12, BLUE), (980, 90, 14, BUTTER), (1120, 160, 10, MEADOW), (700, 110, 9, BERRY)])
    b += rect(-4, 340, 1208, 70, "#f4b6c6", 0, 4)
    b += parcel(140, 240, 150, 110, BLUE) + parcel(320, 270, 110, 80, MEADOW, BUTTER) + parcel(220, 160, 110, 80, BERRY, PAPER)
    b += book_stack(640, 350, [(240, 40, PURPLE), (210, 36, BUTTER), (220, 36, MEADOW), (190, 34, BERRY)])
    b += path("M640,150 V100", sw=4) + circ(640, 96, 24, BERRY) + path("M620,92 q10,-12 20,0", sw=3, stroke=PAPER)
    b += parcel(860, 230, 170, 120, BUTTER, BERRY) + parcel(1060, 280, 90, 70, BLUE, PAPER)
    save("banner-gifts", 1200, 400, b, "#ffe3ea")


def banner_library():
    b = rect(0, 0, 1200, 400, "#eaf0ff", 0, 0) + bookcase(0, 0, 420, 330, 3, 11) + bookcase(780, 0, 420, 330, 3, 21)
    b += rect(420, 20, 360, 250, "#bfe3f2") + path("M420,270 V120 Q600,-40 780,120 V270 Z", "#bfe3f2") + path("M600,20 V270 M420,150 H780", sw=5)
    b += cloud(480, 120, .8) + rect(0, 330, 1200, 70, "#d9a066", 0, 4) + ell(600, 372, 330, 30, BERRY, 0, 4)
    b += bear(520, 392, .9) + book_open(520, 330, 150, 70, BUTTER) + owl(690, 392, .85) + book_stack(840, 392, [(120, 26, BLUE), (100, 24, MEADOW)])
    save("banner-library", 1200, 400, b)


def banner_choose():
    b = starfield([(120, 80), (1080, 80), (300, 340), (900, 330), (1000, 230)], 11)
    b += book_stack(600, 380, [(380, 52, BERRY), (340, 50, BLUE), (360, 50, MEADOW), (320, 46, BUTTER), (300, 44, PURPLE)])
    lens = f'<circle cx="760" cy="170" r="92" fill="#bfe3f2" fill-opacity=".55" stroke="{INK}" stroke-width="9"/>' + path("M826,236 L920,330", sw=22) + path("M826,236 L920,330", sw=12, stroke=BERRY)
    b += lens + path("M718,170 l30,30 l54,-60", sw=12, stroke=MEADOW)
    save("banner-choose", 1200, 400, b, "#e6f4ea")


def banner_readaloud():
    b = sun(1080, 80, 36) + cloud(200, 70, 1) + rect(-4, 330, 1208, 80, "#d9a066", 0, 4) + ell(600, 366, 520, 36, BLUE, 0, 4)
    b += rect(440, 300, 90, 70, WOOD_DK, 8) + bear(500, 300, .95) + book_open(500, 236, 190, 92, BERRY)
    b += rabbit(220, 390, .7) + fox(900, 392, .75, flip=True) + owl(1030, 394, .65, flip=True) + rabbit(110, 392, .5)
    b += star(350, 120, 12) + star(680, 110, 9, BERRY) + star(780, 160, 12, BLUE)
    save("banner-read-aloud", 1200, 400, b, "#fff0c9")


def banner_reluctant():
    b = sun(1060, 80, 40, True) + cloud(160, 70, 1) + hills(1200, 400, [(340, "#8fd08a", 14, .6)])
    steps = [(220, 44, BLUE), (390, 94, MEADOW), (560, 144, PURPLE), (730, 194, BUTTER)]
    for i, (x, h, c) in enumerate(steps):
        b += book_flat(x, 372 - h, 170, h, c, PAPER)
    b += rabbit(470, 372 - 94, .7) + path("M815,178 V90", sw=5) + poly([(815, 90), (880, 108), (815, 126)], BERRY) + star(1000, 200, 10, BERRY) + star(940, 140, 8, BLUE)
    save("banner-reluctant-readers", 1200, 400, b, "#d6efff")


def banner_home_library():
    b = rect(0, 330, 1200, 70, "#d9a066", 0, 4) + bookcase(260, 20, 680, 320, 3, 31) + owl(600, 22, .5)
    b += g(rect(-34, -60, 68, 60, BERRY, 8) + path("M0,-60 Q-40,-120 -60,-150 M0,-60 Q0,-130 0,-170 M0,-60 Q40,-120 60,-150", sw=5, stroke=MEADOW) +
           "".join(ell(x, y, 16, 30, LEAF, r, 3) for x, y, r in [(-60, -160, -30), (0, -182, 0), (60, -160, 30)]), 140, 380)
    b += path("M1060,380 V190", sw=7) + poly([(1000, 190), (1120, 190), (1096, 110), (1024, 110)], BUTTER) + ell(1060, 384, 50, 10, WOOD_DK) + circ(1060, 150, 150, "#ffe08a").replace('fill="#ffe08a"', 'fill="#ffe08a" opacity=".16"').replace('stroke="#1f2a44" stroke-width="4"', 'stroke="none"')
    save("banner-home-library", 1200, 400, b, "#f4ead2")


def banner_guides():
    b = starfield([(120, 70), (300, 150), (1000, 80), (1100, 200), (880, 330)], 11)
    b += book_stack(560, 380, [(360, 56, MEADOW), (320, 52, BERRY), (340, 52, BLUE), (280, 48, BUTTER)]) + owl(560, 120, .8)
    b += path("M880,360 L1000,200 L1040,230 L930,372 Z", BUTTER) + poly([(880, 360), (860, 390), (930, 372)], CREAM) + poly([(1000, 200), (1020, 170), (1040, 230)], BERRY)
    b += cloud(150, 220, 1)
    save("banner-guides", 1200, 400, b, "#e9e4ff")


def banner_about():
    b = hills(1200, 400, [(300, "#a9dca3", 18, .2), (350, "#5cb86f", 12, 1)]) + sun(1060, 90, 40, True) + cloud(180, 80, 1)
    b += book_open(600, 232, 360, 150, BERRY)
    for x, y in [(430, 250), (770, 250)]:
        b += shamrock(x, y + 70, .8)
    b += star(520, 130, 12) + star(700, 110, 14, BLUE) + star(610, 70, 9, BERRY)
    b += flower(260, 384, BERRY) + flower(300, 392, BUTTER, .9) + flower(940, 390, PINK) + flower(980, 384, BLUE, .9)
    save("banner-about", 1200, 400, b, "#d6efff")


# ---- inline spot illustrations (800 x 500)
def spot_whale():
    b = starfield([(90, 60), (240, 120), (420, 50), (640, 90), (730, 160)], 9) + moon(640, 120, 50)
    b += path("M0,330 q40,-22 80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 V500 H0 Z", "#3a6fc2") + whale(330, 340, 1.15)
    b += path("M0,400 q40,-22 80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 t80,0 V500 H0 Z", "#2f5aa8")
    save("spot-whale-and-moon", 800, 500, b, "#1f3a73")


def spot_rocket():
    b = starfield([(80, 70), (220, 160), (380, 60), (560, 120), (700, 70), (740, 260), (120, 330)], 9)
    b += circ(160, 400, 70, "#ef8a3c") + circ(140, 380, 14, "#d9722a", 0) + circ(600, 130, 36, "#9ed3f5") + path("M550,130 H650", sw=5, stroke=BLUE)
    b += rocket(420, 330, 1.5, 28) + book_stack(640, 480, [(200, 36, BERRY), (170, 34, BUTTER)])
    save("spot-rocket", 800, 500, b, "#27336b")


def spot_castle():
    b = sun(660, 90, 38) + cloud(120, 90, 1) + hills(800, 500, [(380, "#8fd08a", 18, .5), (430, "#4aa860", 12, 1.3)])
    c = rect(-110, -150, 220, 150, "#b7bfd4", 4) + rect(-150, -190, 70, 190, "#9aa3b8", 4) + rect(80, -190, 70, 190, "#9aa3b8", 4)
    c += poly([(-158, -190), (-72, -190), (-115, -260)], BERRY) + poly([(72, -190), (158, -190), (115, -260)], BERRY) + rect(-30, -90, 60, 90, WOOD_DK, 30)
    c += rect(-136, -140, 22, 38, INK, 11, 3) + rect(114, -140, 22, 38, INK, 11, 3) + path("M-110,-150 V-176 M-70,-150 V-176 M-30,-150 V-176 M10,-150 V-176 M50,-150 V-176 M90,-150 V-176", sw=3)
    c += path("M-115,-260 V-300", sw=4) + poly([(-115, -300), (-84, -290), (-115, -280)], BUTTER)
    b += g(c, 400, 400, 1.2) + flower(120, 470, BERRY) + flower(180, 480, BUTTER) + flower(660, 478, BLUE) + flower(720, 470, PINK)
    save("spot-castle", 800, 500, b, "#d6efff")


def spot_owl_window():
    b = rect(0, 0, 800, 500, "#fff1c9", 0, 0) + rect(190, 40, 420, 360, NIGHT) + moon(500, 150, 56) + starfield([(260, 100), (330, 200), (420, 80), (560, 260), (280, 300), (360, 330)], 10)
    b += path("M400,40 V400 M190,220 H610", sw=6) + rect(190, 40, 420, 360, "none") + rect(170, 400, 460, 24, WOOD) + owl(400, 400, 1.35)
    b += path("M170,30 H250 Q230,230 262,430 H170 Z", BERRY) + path("M630,30 H550 Q570,230 538,430 H630 Z", BERRY)
    save("spot-owl-at-the-window", 800, 500, b)


def spot_picnic():
    b = sun(120, 90, 38) + cloud(520, 80, 1) + hills(800, 500, [(330, "#8fd08a", 14, .3), (400, "#5cb86f", 10, 1)]) + tree(640, 420, 1.5)
    b += path("M180,470 L300,410 H640 L600,470 Z", BERRY) + path("M300,410 L260,470 M420,410 L380,470 M540,410 L500,470", sw=2.5, stroke=PAPER)
    b += bear(300, 450, .85) + book_open(300, 385, 130, 62, BLUE)
    basket = path("M440,450 L450,400 H540 L550,450 Z", WOOD) + path("M455,400 Q495,350 535,400", sw=5) + path("M450,420 H545 M452,436 H548", sw=2.5, stroke=WOOD_DK)
    b += basket + circ(480, 392, 14, BERRY, 3) + circ(512, 396, 14, BUTTER, 3) + flower(80, 470, BERRY) + flower(130, 482, BUTTER)
    save("spot-picnic", 800, 500, b, "#d6efff")


def spot_snowy_fox():
    b = starfield([(90, 70), (250, 120), (420, 50), (600, 100), (720, 60)], 9) + moon(690, 130, 46)
    b += path("M0,360 Q200,300 400,350 T800,330 V500 H0 Z", WHITE) + path("M0,430 Q250,390 500,430 T800,410 V500 H0 Z", "#e6f0ff")
    for x, y, s in [(130, 330, .9), (680, 350, 1.1)]:
        b += g(poly([(0, -170), (-46, -60), (46, -60)], "#2f8f5b") + poly([(0, -120), (-60, 0), (60, 0)], "#2f8f5b") + rect(-10, 0, 20, 24, WOOD_DK, 2, 3), x, y, s)
    b += fox(400, 430, 1.1) + parcel(540, 392, 70, 56, BERRY)
    for x, y in [(90, 200), (240, 260), (330, 160), (520, 200), (620, 270), (760, 220), (440, 300)]:
        b += dot(x, y, 5, WHITE)
    save("spot-snowy-fox", 800, 500, b, "#27336b")


def og():
    b = rect(0, 0, 1200, 630, "#e8f4f8", 0, 0) + hills(1200, 630, [(470, "#a9dca3", 18, .3), (530, "#5cb86f", 12, 1.2)])
    b += sun(1060, 110, 46, True) + cloud(780, 120, 1.1)
    b += tree(1170, 560, 1.3) + bear(860, 590, 1.35) + rabbit(1040, 590, 1.1) + book_open(950, 520, 260, 120, BERRY)
    b += star(80, 70, 14) + star(640, 80, 10, BERRY)
    b += f'<text x="70" y="240" font-family="Young Serif, Georgia, serif" font-size="92" fill="{INK}">Children’s</text>'
    b += f'<text x="70" y="340" font-family="Young Serif, Georgia, serif" font-size="92" fill="{INK}">books, found</text>'
    b += f'<text x="70" y="440" font-family="Young Serif, Georgia, serif" font-size="92" fill="{INK}">for every age</text>'
    b += rect(62, 492, 380, 62, BUTTER, 31) + f'<text x="90" y="536" font-family="Atkinson Hyperlegible, Verdana, sans-serif" font-size="38" font-weight="700" fill="{INK}">childrensbooks.ie</text>'
    save("og-image", 1200, 630, b)


if __name__ == "__main__":
    for fn in [logo, hero, banner_babies, banner_preschool, banner_early, banner_middle, banner_irish_authors,
               banner_irish_language, banner_myths, banner_bedtime, banner_feelings, banner_gifts, banner_library,
               banner_choose, banner_readaloud, banner_reluctant, banner_home_library, banner_guides, banner_about,
               spot_whale, spot_rocket, spot_castle, spot_owl_window, spot_picnic, spot_snowy_fox, og]:
        fn()
    print("illustrations written to", os.path.normpath(OUT))
