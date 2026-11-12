#!/usr/bin/env python3
"""Original 1200x400 scenes for the all-time classics pages. Settings and props only: no covers and no
existing characters are drawn.   python3 tools/illustrations_classics.py"""
from illustrations import *  # noqa: F401,F403
from illustrations_christmas import cottage, pine, snow_ground, snowflakes, candle  # noqa: F401
from illustrations_top20 import mountains, lamp_post, diamond, football  # noqa: F401

W, H = 1200, 400


def ground(y, c="#8fd08a"):
    return rect(-4, y, W + 8, H - y + 4, c, 0, 4)


def teapot(x, y, s=1, f=BERRY):
    b = ell(0, -30, 44, 32, f) + rect(-22, -66, 44, 12, f, 4) + circ(0, -72, 7, BUTTER, 3)
    b += path("M40,-40 q30,-6 26,-34 q-6,10 -28,14", f, 4) + path("M-42,-44 q-34,-14 -22,22", sw=7)
    return g(b, x, y, s)


def cup(x, y, s=1, f=WHITE):
    return g(path("M-18,-24 h36 q0,24 -18,24 q-18,0 -18,-24 z", f, 3.5) + path("M18,-18 q14,0 10,10 q-4,6 -12,4", sw=3.5), x, y, s)


def castle(x, y, s=1):
    b = rect(-120, -120, 240, 120, "#9aa3bd") + rect(-150, -210, 50, 210, "#aab2c9") + rect(100, -230, 50, 230, "#aab2c9") + rect(-30, -280, 60, 280, "#b5bdd3")
    b += poly([(-160, -210), (-90, -210), (-125, -280)], PURPLE) + poly([(90, -230), (160, -230), (125, -310)], PURPLE) + poly([(-40, -280), (40, -280), (0, -360)], PURPLE)
    b += "".join(rect(wx, wy, 14, 24, BUTTER, 3, 2.5) for wx, wy in [(-136, -170), (-136, -120), (118, -190), (118, -140), (-7, -240), (-7, -190), (-80, -80), (66, -80)])
    b += path("M-24,0 v-44 q24,-30 48,0 v44 z", WOOD_DK, 3.5)
    return g(b, x, y, s)


def window(x, y, w, h, bg="#cfe9ff", fr=WOOD):
    return rect(x, y, w, h, fr, 6) + rect(x + 10, y + 10, w - 20, h - 20, bg, 3, 3) + path(f"M{x + w / 2},{y + 10} v{h - 20} M{x + 10},{y + h / 2} h{w - 20}", sw=4, stroke=fr)


def barn(x, y, s=1):
    b = rect(-110, -130, 220, 130, "#c9463a") + poly([(-124, -126), (124, -126), (70, -196), (-70, -196)], "#8a3a2e")
    b += rect(-36, -86, 72, 86, WHITE, 3) + path("M-36,-86 l72,86 M36,-86 l-72,86", sw=4) + rect(-20, -168, 40, 24, "#fff3d6", 3, 3)
    return g(b, x, y, s)


def web(cx, cy, r):
    b = ""
    for i in range(8):
        a = i * math.pi / 4
        b += path(f"M{cx},{cy} L{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}", sw=2.5, stroke="#8a93ab")
    for k in (0.35, 0.65, 1.0):
        pts = " ".join(f"{cx + r * k * math.cos(i * math.pi / 4):.1f},{cy + r * k * math.sin(i * math.pi / 4):.1f}" for i in range(8))
        b += f'<polygon points="{pts}" fill="none" stroke="#8a93ab" stroke-width="2.5"/>'
    return b + "".join(circ(cx + r * .65 * math.cos(i), cy + r * .65 * math.sin(i), 3, "#cfe9ff", 1.5) for i in (0.4, 1.7, 3.0, 4.5))


def apple(x, y, s=1, c=BERRY):
    return g(circ(0, 0, 22, c, 3.5) + path("M0,-22 q2,-14 10,-16", sw=3.5) + ell(10, -26, 10, 5, LEAF, -20, 2.5), x, y, s)


def pear(x, y, s=1):
    return g(path("M0,-34 q-10,4 -10,20 q-14,6 -10,22 q10,10 20,8 q10,2 20,-8 q4,-16 -10,-22 q0,-16 -10,-20 z", "#c9e04a", 3.5) + path("M0,-34 q2,-8 6,-10", sw=3), x, y, s)


def strawberry(x, y, s=1):
    return g(path("M-20,-14 q20,-14 40,0 q-4,26 -20,34 q-16,-8 -20,-34 z", BERRY, 3.5) + ell(0, -16, 14, 6, LEAF, 0, 2.5) + "".join(dot(px, py, 1.8) for px, py in [(-6, -2), (6, 2), (-2, 10), (8, -6), (-10, 6)]), x, y, s)


def butterfly(x, y, s=1, c1=PURPLE, c2=BUTTER):
    return g(ell(-26, -14, 28, 20, c1, -20, 3.5) + ell(26, -14, 28, 20, c1, 20, 3.5) + ell(-20, 14, 20, 14, c2, 20, 3.5) + ell(20, 14, 20, 14, c2, -20, 3.5) + rect(-3, -22, 6, 46, INK, 3, 0) + path("M0,-22 q-8,-14 -14,-12 M0,-22 q8,-14 14,-12", sw=2.5), x, y, s)


def leafy(x, y, s=1):
    b = path("M0,0 v-130", sw=7, stroke=MEADOW)
    for ly, ang in [(-40, -50), (-70, 50), (-100, -40), (-120, 40)]:
        b += g(ell(0, 0, 50, 22, LEAF, 0, 3.5) + path("M-44,0 h88", sw=2.5), 0, ly, 1, ang)
    return g(b, x, y, s)


def boat(x, y, s=1):
    b = path("M-90,0 h180 q-20,34 -70,34 h-40 q-50,0 -70,-34 z", WOOD, 4) + path("M0,0 V-150", sw=6) + poly([(6, -146), (6, -24), (86, -24)], WHITE, 4) + poly([(-6, -120), (-6, -24), (-62, -24)], PINK, 4)
    return g(b, x, y, s)


def pot(x, y, s=1):
    return g(path("M-36,-4 q-16,-40 0,-56 h72 q16,16 0,56 q-36,16 -72,0 z", "#c98a3a", 4) + ell(0, -60, 38, 10, "#7a4a1e", 0, 3.5) + path("M-30,-58 q0,12 6,14", "#ffcf4a", 4) + txt(0, -22, "HONEY", 15, "#fff3d6"), x, y, s)


def balloon(x, y, s=1, c="#e23b3b"):
    return g(ell(0, -60, 30, 38, c, 0, 3.5) + poly([(-5, -22), (5, -22), (0, -14)], c, 3) + path("M0,-14 q-8,30 4,60", sw=2.5), x, y, s)


def lollipop(x, y, s=1, c=BERRY):
    return g(rect(-3, -90, 6, 90, WHITE, 2, 2.5) + circ(0, -110, 24, c, 3.5) + path("M0,-110 m-14,0 a14,14 0 1,1 14,14 a8,8 0 1,1 -8,-8", sw=3, stroke=WHITE), x, y, s)


def cake_stand(x, y, s=1):
    return g(rect(-50, -34, 100, 12, "#f1cf9b", 4) + rect(-6, -22, 12, 22, "#f1cf9b", 2) + rect(-24, 0, 48, 8, "#f1cf9b", 3) + rect(-40, -64, 80, 30, PINK, 6) + path("M-40,-64 q10,-12 20,0 q10,-12 20,0 q10,-12 20,0", WHITE, 3) + circ(0, -76, 7, BERRY, 2.5), x, y, s)


def blossom_tree(x, y, s=1):
    return g(rect(-12, -70, 24, 70, WOOD_DK, 4) + blob([("c", 0, -120, 54), ("c", -44, -90, 40), ("c", 44, -90, 40), ("c", 0, -76, 42)], "#ffd6e5") + "".join(dot(px, py, 5, BERRY) for px, py in [(-30, -120), (0, -150), (30, -118), (-48, -88), (48, -90), (0, -100)]), x, y, s)


def moon_bg():
    return starfield([(100, 60), (250, 130), (380, 50), (520, 100), (700, 40), (870, 120), (1000, 60), (1120, 150)], 8)


def lantern(x, y, s=1):
    return g(path("M0,-40 v-14 q12,-10 24,0", sw=3.5) + rect(-4, -40, 8, 6, INK, 1, 0) + path("M-14,-34 h28 l6,44 h-40 z", "#ffd24a", 3.5) + path("M-14,-34 v44 M14,-34 v44", sw=2.5), x, y, s)


def scroll(x, y, w=170, h=100, rot=0):
    b = rect(0, 0, w, h, "#f5e6b8", 6) + path(f"M20,30 q30,-20 50,0 t60,10 M30,70 q40,-14 70,6", sw=3, stroke="#a8743f") + dot(w - 40, 60, 6, BERRY) + path(f"M{w - 50},{h - 24} l20,20 m0,-20 l-20,20", sw=3, stroke=BERRY)
    return g(b, x, y, 1, rot)


def scene(name, body, bg=None):
    save(name, W, H, body, bg)


# ---------------------------------------------------------------- scenes
def c_harry():
    b = rect(0, 0, W, H, "#27336b", 0, 0) + moon_bg() + moon(1040, 80, 40) + hills(W, H, [(300, "#2d5b4a", 18, .3)])
    b += castle(600, 340, 1.05) + owl(260, 190, .8) + owl(920, 150, .6, flip=True)
    b += "".join(candle(x, y, .8) for x, y in [(380, 130), (440, 90), (500, 60), (700, 70), (760, 100), (820, 140)])
    scene("classic-harry-potter", b)


def c_caterpillar():
    b = sun(1040, 80, 42) + cloud(180, 70, 1) + hills(W, H, [(260, "#b8e3b0", 14, .2)]) + ground(320, "#5cb86f")
    b += leafy(200, 330, 1.8) + g(path("M0,0 v-90", sw=5) + ell(0, -40, 18, 34, "#c9a46b", 0, 3.5) + path("M-14,-50 h28 M-15,-38 h30 M-13,-26 h26", sw=2.5, stroke="#8a6a3a"), 560, 160, 1.4)
    b += path("M460,150 q100,-30 220,0", sw=8, stroke=WOOD_DK) + butterfly(900, 190, 1.6, PURPLE, BUTTER) + butterfly(1060, 260, 1, BLUE, PINK)
    b += apple(420, 370, 1.4) + pear(500, 372, 1.3) + strawberry(580, 372, 1.3) + apple(660, 370, 1.4, "#e8a02e") + apple(740, 370, 1.4, "#7a3d8a")
    scene("classic-hungry-caterpillar", b, "#d6efff")


def c_wild():
    b = rect(0, 0, W, H, "#1e4a5a", 0, 0) + moon_bg() + circ(880, 130, 76, "#fff3d6", 4)
    b += hills(W, H, [(300, "#2f7d9a", 10, .1), (340, "#3a8fd1", 12, 1.2), (370, "#2f7d9a", 10, 2.4)])
    b += ell(180, 330, 220, 70, "#2f6b4f") + tree(80, 300, 1.2, "#2a8a55") + tree(190, 290, 1.4, "#237a4b") + tree(300, 300, 1.2, "#2a8a55") + tree(390, 310, .9, "#237a4b")
    b += boat(700, 350, 1.0)
    scene("classic-wild-things", b)


def c_charlotte():
    b = sun(1050, 80, 40) + cloud(240, 70, 1) + hills(W, H, [(250, "#b8e3b0", 16, .2)]) + ground(310, "#7cc46a")
    b += barn(280, 320, 1.4)
    b += "".join(rect(px, 220, 10, 120, WOOD, 3) for px in (700, 1000)) + web(850, 220, 100) + path("M700,236 h300", sw=7, stroke=WOOD)
    b += "".join(rect(px, 300, 90, 60, "#e6c76a", 8) + path(f"M{px},{320} h90 M{px},{340} h90", sw=2.5, stroke="#b89a3a") for px in (430, 520))
    b += g(circ(0, 0, 24, BLUE, 3.5) + circ(0, 0, 12, WHITE, 2.5) + poly([(-14, 22), (-24, 62), (-8, 52), (-2, 24)], BLUE, 3) + poly([(14, 22), (24, 62), (8, 52), (2, 24)], BLUE, 3), 640, 330, 1)
    scene("classic-charlottes-web", b, "#d6efff")


def c_narnia():
    b = rect(0, 0, W, H, "#c9d9ea", 0, 0) + snow_ground(W, H, 250)
    b += "".join(pine(x, y, s) for x, y, s in [(520, 330, 1.5), (640, 310, 1.8), (760, 340, 1.4), (900, 320, 1.7), (1040, 340, 1.4), (1130, 330, 1.2)])
    b += lamp_post(720, 340, 1.2) + snowflakes([(480, 90, 12), (600, 150, 10), (840, 80, 14), (1000, 130, 10), (1120, 70, 12), (330, 60, 10)])
    w = rect(70, 70, 330, 290, WOOD, 8) + rect(94, 96, 282, 240, "#dce8f5", 0, 3) + pine(240, 330, 1.2) + pine(170, 320, .9) + pine(310, 322, .9) + snowflakes([(200, 140, 9), (290, 180, 8)])
    w += poly([(94, 96), (94, 336), (30, 376), (30, 60)], WOOD_DK, 4) + circ(44, 220, 5, BUTTER, 2) + rect(110, 360, 20, 20, WOOD_DK, 3) + rect(340, 360, 20, 20, WOOD_DK, 3)
    scene("classic-narnia", b + w)


def c_matilda():
    b = rect(0, 0, W, 310, "#ffe9b8", 0, 0) + rect(-4, 310, W + 8, 100, "#c58a50", 0, 4)
    b += rect(70, 50, 380, 200, WOOD, 8) + rect(84, 64, 352, 172, "#2f6b4f", 4, 3) + path("M110,110 h140 M110,150 h200 M300,200 q30,-30 60,0", sw=4, stroke="#e9f1e6") + txt(380, 120, "A B C", 34, "#e9f1e6")
    b += bookcase(780, 40, 340, 270, 3, 9) + rect(500, 230, 200, 16, WOOD, 4) + rect(516, 246, 12, 66, WOOD_DK, 2) + rect(672, 246, 12, 66, WOOD_DK, 2)
    b += "".join(rect(520, 230 - 26 * (i + 1), 150 - i * 12, 26, c, 4) for i, c in enumerate([BERRY, BLUE, MEADOW, BUTTER])) + "".join(star(x, y, r, c) for x, y, r, c in [(560, 90, 18, BUTTER), (620, 60, 24, PINK), (680, 110, 14, BLUE)])
    scene("classic-matilda", b)


def c_gruffalo():
    b = rect(0, 0, W, H, "#1f3b2d", 0, 0) + moon(1060, 70, 36) + "".join(tree(x, 340, s, c) for x, s, c in [(60, 1.9, "#1a5a3a"), (250, 1.5, "#237a4b"), (470, 1.9, "#1a5a3a"), (900, 1.7, "#237a4b"), (1100, 2.0, "#1a5a3a")])
    b += ground(330, "#2f5a3a") + path("M0,370 q300,-30 600,10 t600,-10", sw=22, stroke="#3a8fd1") + path("M0,370 q300,-30 600,10 t600,-10", sw=14, stroke="#7cc7f2")
    b += "".join(ell(x, y, 60, 22, WOOD, 0, 4) + circ(x + 56, y, 14, "#e6c98a", 3) for x, y in [(620, 330), (680, 300), (740, 330)])
    b += "".join(g(circ(0, 0, 12, "#a8743f", 3) + path("M-4,-12 q4,-8 8,0", sw=2.5), x, y) for x, y in [(350, 360), (420, 372), (860, 370)])
    b += g(path("M-30,0 q0,-40 30,-40 q30,0 30,40 z", "#e23b3b", 4) + "".join(dot(x, y, 4, WHITE) for x, y in [(-12, -22), (8, -26), (14, -12)]) + rect(-6, 0, 12, 18, "#f1cf9b", 3), 540, 345, 1.1)
    scene("classic-gruffalo", b)


def c_goodnight_moon():
    b = rect(0, 0, W, 300, "#8fc9a0", 0, 0) + rect(-4, 300, W + 8, 110, "#d6a86a", 0, 4) + ell(600, 350, 380, 40, BERRY, 0, 4)
    b += window(100, 60, 240, 190, "#27336b") + moon(220, 150, 40) + star(150, 110, 10) + star(290, 190, 8)
    b += rect(420, 190, 400, 120, WOOD_DK, 8) + rect(400, 140, 30, 190, WOOD, 6) + rect(430, 210, 380, 70, BLUE, 12) + ell(480, 212, 60, 24, WHITE, 0, 4) + "".join(star(520 + i * 80, 250, 10, BUTTER, 2.5) for i in range(4))
    b += rect(900, 70, 190, 150, WHITE, 6) + circ(995, 145, 64, WHITE, 5) + path("M995,145 v-40 M995,145 l28,16", sw=5) + dot(995, 145, 5)
    b += rect(930, 240, 120, 70, WOOD, 6) + path("M990,240 v-30", sw=5) + poly([(950, 214), (1030, 214), (1010, 160), (970, 160)], BUTTER) + rect(1100, 220, 70, 90, WOOD, 4) + rect(1112, 160, 46, 58, PINK, 4)
    scene("classic-goodnight-moon", b)


def c_alice():
    b = rect(0, 0, W, H, "#d9cff5", 0, 0) + hills(W, H, [(250, "#b8e3b0", 14, .2)]) + ground(320, "#6cc27a") + cloud(180, 70, 1) + cloud(930, 60, .9)
    b += rect(90, 120, 130, 240, WOOD_DK, 6) + blob([("c", 155, 100, 70), ("c", 90, 120, 48), ("c", 220, 124, 48)], "#3a9d62") + path("M130,360 v-86 q25,-34 50,0 v86 z", "#7c4dbd", 4) + dot(170, 320, 4, BUTTER)
    b += rect(330, 280, 520, 20, WHITE, 6) + rect(360, 300, 14, 60, WOOD_DK, 3) + rect(810, 300, 14, 60, WOOD_DK, 3) + teapot(450, 280, 1.1, "#7c4dbd") + "".join(cup(x, 280, 1, "#fff") for x in (560, 640, 720)) + cake_stand(790, 278, .9)
    b += "".join(g(rect(-22, -66, 44, 66, WHITE, 5) + txt(0, -34, s, 34, c), x, 330, 1.1, r) for x, s, c, r in [(930, "♥", "#d6336c", -6), (1000, "♠", INK, 4), (1070, "♦", "#d6336c", -3)])
    b += g(rect(-5, -60, 10, 60, "#f1cf9b", 3) + path("M-48,-60 q48,-60 96,0 z", PURPLE, 4) + "".join(dot(x, y, 4, WHITE) for x, y in [(-20, -76), (6, -88), (22, -70)]), 280, 360, .9)
    scene("classic-alice", b)


def c_cat_hat():
    b = rect(0, 0, W, 300, "#fff1d6", 0, 0) + rect(-4, 300, W + 8, 110, "#c58a50", 0, 4) + window(380, 40, 440, 230, "#8fa6c4")
    b += "".join(path(f"M{x},{y} l-12,30", sw=3, stroke="#d7eaff") for x in range(410, 800, 38) for y in (90, 150, 210)) + cloud(520, 110, 1.1, "#d3d9e3") + cloud(680, 160, 1, "#d3d9e3")
    b += g(poly([(0, -50), (46, 0), (0, 50), (-46, 0)], "#ffd24a", 4) + path("M0,-50 V50 M-46,0 H46", sw=3) + path("M0,50 q-20,34 4,60", sw=3), 160, 280, 1)
    b += g(path("M-70,0 q0,-70 70,-70 q70,0 70,70 q-20,-16 -35,0 q-17,-16 -35,0 q-18,-16 -35,0 q-15,-16 -35,0 z", "#3a8fd1", 4) + rect(-3, -4, 6, 70, INK, 2, 0), 960, 300, 1.1)
    b += "".join(rect(x, y - h, w, h, c, 5) for x, y, w, h, c in [(60, 370, 110, 60, BERRY), (80, 310, 80, 50, MEADOW), (1060, 370, 100, 56, BUTTER)]) + football(600, 360, 26)
    scene("classic-cat-in-the-hat", b)


def c_peter():
    b = sun(1060, 80, 40) + cloud(200, 70, 1) + hills(W, H, [(240, "#b8e3b0", 14, .2)]) + cottage(940, 270, .6) + ground(280, "#6cc27a")
    for r, y in enumerate((300, 340, 380)):
        for i in range(9):
            x = 60 + i * 60 + (r % 2) * 30
            b += circ(x, y, 24, "#5cb86f" if (i + r) % 2 else "#78cf84", 3.5) + path(f"M{x - 12},{y} q12,-16 24,0", sw=2.5)
    b += "".join(g(poly([(-8, 0), (8, 0), (0, 40)], "#ec7a2e", 3) + path("M0,0 q-10,-16 -14,-24 M0,0 q0,-20 0,-30 M0,0 q10,-16 14,-24", sw=3, stroke=MEADOW), x, 395) for x in (300, 330, 360))
    b += g(rect(-34, -44, 68, 44, "#3a8fd1", 8) + path("M34,-30 q30,-8 36,-30", sw=6) + rect(-24, -54, 48, 10, "#2d78b3", 3), 640, 300, 1) + g(path("M-40,0 h80 l-16,-50 h-48 z", "#c98a4b", 4) + circ(0, 12, 14, "#5a5a5a", 4) + path("M40,-30 h40", sw=6), 780, 330, 1)
    b += "".join(rect(px, 250, 12, 60, WOOD, 3) for px in (0, 120, 240, 360, 480)) + path("M0,266 H492 M0,292 H492", sw=6, stroke=WOOD)
    scene("classic-peter-rabbit", b, "#d6efff")


def c_pooh():
    b = sun(1040, 80, 38) + hills(W, H, [(260, "#b8e3b0", 14, .2)]) + ground(310, "#7cc46a") + "".join(tree(x, 320, s) for x, s in [(80, 1.6), (230, 1.3), (900, 1.7), (1100, 1.4)])
    b += path("M360,360 q240,-10 480,0", sw=28, stroke="#3a8fd1") + path("M440,350 q160,-70 320,0", "none", 14, WOOD_DK) + rect(440, 336, 320, 12, WOOD, 4) + path("M470,336 v-34 M730,336 v-34 M470,306 h260", sw=7, stroke=WOOD_DK)
    b += pot(560, 300, 1.5) + balloon(700, 280, 1.8) + g(rect(-30, -50, 60, 50, "#f1cf9b", 4) + poly([(-40, -50), (40, -50), (0, -90)], "#c9463a", 4) + rect(-8, -24, 16, 24, WOOD_DK, 2, 3), 330, 330, 1.1)
    scene("classic-winnie-the-pooh", b, "#d6efff")


def c_hobbit():
    b = rect(0, 0, W, H, "#e9f0ff", 0, 0) + mountains(W, 280, "#8fb3d9") + sun(1060, 70, 36) + cloud(240, 80, 1) + ground(300, "#7cc46a")
    b += ell(480, 330, 330, 180, "#5cb86f", 0, 4) + circ(480, 270, 62, MEADOW, 5) + circ(480, 270, 50, "#3a9d62", 3) + dot(504, 276, 6, BUTTER) + path("M420,300 h120", sw=4)
    b += path("M480,332 q-60,30 -140,60 M480,332 q120,20 300,56", sw=26, stroke="#c9a46b") + path("M480,332 q-60,30 -140,60 M480,332 q120,20 300,56", sw=16, stroke="#e6cc9a")
    b += lantern(820, 360, 1.3) + scroll(900, 300, 190, 100, -6) + tree(1060, 340, 1.0)
    scene("classic-the-hobbit", b)


def c_green_eggs():
    b = rect(0, 0, W, 300, "#fff1d6", 0, 0) + rect(-4, 300, W + 8, 110, "#c58a50", 0, 4)
    b += ell(600, 280, 250, 66, WHITE, 5) + ell(600, 274, 200, 44, "#f4f0e6", 3) + "".join(ell(x, 270, 56, 30, "#e9ffd3", 0, 4) + circ(x, 270, 22, "#7ed957", 3.5) for x in (540, 640))
    b += path("M470,270 q40,-50 90,-30 l10,50 q-60,20 -100,-20 z", PINK, 4) + path("M470,270 q20,-20 40,-20", sw=3, stroke=BERRY)
    b += path("M880,300 h-60", sw=0) + g(circ(0, 0, 70, "#3a3a4a", 5) + circ(0, 0, 50, "#555", 3) + rect(60, -10, 120, 20, "#3a3a4a", 8) + ell(-10, -6, 24, 14, "#e9ffd3", 0, 3) + circ(-10, -6, 9, "#7ed957", 2.5), 150, 300, 1.2)
    b += g(rect(-60, -32, 120, 30, BERRY, 6) + rect(-50, -62, 40, 30, BLUE, 5) + rect(0, -62, 40, 30, BUTTER, 5) + circ(-36, 4, 14, INK, 4) + circ(36, 4, 14, INK, 4) + rect(40, -48, 14, 16, MEADOW, 3), 1000, 360, 1.2) + g(path("M0,0 v-50 M-16,-30 h32", sw=4), 1060, 340, 1)
    scene("classic-green-eggs", b)


def c_charlie():
    b = rect(0, 0, W, 300, "#ffe0ec", 0, 0) + rect(-4, 300, W + 8, 110, "#8a5a3a", 0, 4) + path("M-10,340 q200,-30 400,10 t420,-6 t400,6", sw=40, stroke="#6a3f24") + path("M-10,340 q200,-30 400,10 t420,-6 t400,6", sw=28, stroke="#8a5a3a")
    b += rect(440, 120, 320, 190, "#b7bfd4", 6) + rect(480, 60, 40, 80, "#8a93ab", 4) + rect(690, 40, 40, 100, "#8a93ab", 4) + "".join(rect(x, y, 34, 34, BUTTER, 4, 3) for x in (470, 540, 610, 680) for y in (150, 210)) + path("M560,310 v-60 q40,-30 80,0 v60 z", BERRY, 4)
    b += "".join(lollipop(x, 330, s, c) for x, s, c in [(120, 1.5, BERRY), (210, 1.2, BLUE), (300, 1.6, PURPLE), (870, 1.4, MEADOW), (960, 1.6, BERRY), (1060, 1.3, BUTTER)])
    b += g(rect(-60, -34, 120, 68, BUTTER, 5) + txt(0, -4, "GOLDEN", 20, INK) + txt(0, 22, "TICKET", 20, INK), 600, 70, 1, -8)
    scene("classic-charlie", b)


def c_wind():
    b = sun(1050, 70, 40) + cloud(220, 60, 1) + hills(W, H, [(230, "#b8e3b0", 14, .2)]) + ground(260, "#7cc46a") + path("M-10,330 q300,-40 600,0 t640,-6", sw=90, stroke="#3a8fd1") + path("M-10,330 q300,-40 600,0 t640,-6", sw=76, stroke="#7cc7f2")
    b += "".join(tree(x, 270, 1.4, "#3a9d62") + path(f"M{x - 60},{150} q-10,60 -4,110 M{x + 60},{150} q10,60 4,110", sw=4, stroke="#2a7a4a") for x in (90, 1110))
    b += g(path("M-80,0 h160 q-20,30 -60,30 h-40 q-40,0 -60,-30 z", WOOD, 4) + path("M-40,-6 L-90,-50 M40,-6 L90,-50", sw=5, stroke=WOOD_DK), 560, 330, 1.2)
    b += g(rect(-40, -40, 80, 40, "#c9a46b", 6) + path("M-40,-30 h80 M-40,-18 h80", sw=2.5, stroke="#a8743f") + path("M-34,-40 q34,-44 68,0", sw=5), 880, 370, 1) + g(rect(-50, -8, 100, 10, "#fff", 3) + "".join(rect(x, -8, 10, 10, BERRY, 0, 0) for x in (-50, -30, -10, 10, 30)), 880, 370, 1)
    b += "".join(path(f"M{x},{370} v-50 M{x + 8},{370} v-40", sw=4, stroke=MEADOW) for x in (260, 300, 960, 1000, 1040))
    scene("classic-wind-in-the-willows", b, "#d6efff")


def c_anne():
    b = sun(1050, 70, 40) + cloud(240, 70, 1) + path("M-10,240 q300,-30 600,0 t640,-6 V400 H-10 z", "#7cc7f2", 4) + hills(W, H, [(270, "#8fd08a", 14, .3)]) + ground(310, "#5cb86f")
    b += g(rect(-110, -100, 220, 100, "#fffaf0", 4) + poly([(-130, -100), (130, -100), (0, -190)], "#2f8f5b", 4) + poly([(-70, -100), (-28, -100), (-49, -150)], "#2f8f5b", 3) + rect(-20, -60, 40, 60, "#a8743f", 3) + rect(-90, -76, 36, 36, "#cfe9ff", 3) + rect(54, -76, 36, 36, "#cfe9ff", 3), 620, 330, 1.3)
    b += blossom_tree(240, 340, 1.5) + blossom_tree(1000, 340, 1.4) + path("M620,332 q-120,26 -260,70 M640,332 q160,24 420,68", sw=26, stroke="#c9a46b")
    b += "".join(flower(x, 390, c, .9) for x, c in [(120, BERRY), (400, BUTTER), (820, PINK), (1120, BERRY)])
    scene("classic-anne", b, "#d6efff")


def c_tiger_tea():
    b = rect(0, 0, W, 300, "#fff0d9", 0, 0) + rect(-4, 300, W + 8, 110, "#c58a50", 0, 4) + window(90, 50, 220, 170, "#cfe9ff")
    b += rect(360, 60, 330, 12, WOOD, 3) + "".join(rect(x, 22, 36, 38, c, 5) for x, c in [(380, BERRY), (430, BLUE), (480, MEADOW), (540, BUTTER), (600, PURPLE)]) + rect(360, 150, 330, 12, WOOD, 3) + "".join(rect(x, 110, 30, 40, c, 5) for x, c in [(390, BUTTER), (440, PINK), (500, BLUE)])
    b += rect(780, 280, 380, 24, "#ffb3c7", 6) + rect(800, 304, 16, 70, WOOD_DK, 3) + rect(1120, 304, 16, 70, WOOD_DK, 3) + cake_stand(900, 280, 1) + teapot(1010, 280, 1) + cup(1090, 280, 1)
    b += "".join(ell(x, 276, 34, 14, "#e6b36a", 0, 3.5) for x in (810, 860)) + g(path("M-20,-10 q20,-30 40,0 v14 h-40z", WHITE, 3.5) + path("M-20,-4 h40", sw=2.5, stroke="#d9e5f0"), 970, 300, 0)
    b += rect(430, 190, 140, 110, WOOD, 5) + rect(380, 308, 60, 66, "#f1cf9b", 4) + path("M380,308 h60", sw=4)
    b += rect(40, 250, 90, 120, WOOD_DK, 5) + circ(110, 320, 6, BUTTER, 2.5) + circ(86, 280, 8, BUTTER, 2.5)
    scene("classic-tiger-tea", b)


def c_guess_how_much():
    b = rect(0, 0, W, H, "#27336b", 0, 0) + moon_bg() + circ(860, 120, 84, "#fff3d6", 4) + hills(W, H, [(280, "#2d5b4a", 16, .4), (330, "#3a8a63", 12, 1.4)])
    b += path("M300,150 c-30,-36 -80,-6 -50,34 c20,22 50,34 50,34 c0,0 30,-12 50,-34 c30,-40 -20,-70 -50,-34 z", "#ffb3c7", 4) + "".join(star(x, y, r, c) for x, y, r, c in [(120, 90, 18, BUTTER), (520, 70, 22, "#fff3d6"), (420, 180, 14, PINK)])
    b += "".join(flower(x, 390, c, 1.2) for x, c in [(110, PINK), (230, BUTTER), (480, "#fff"), (700, PINK), (950, BUTTER), (1100, "#fff")])
    b += path("M560,400 q60,-70 140,-90", sw=26, stroke="#c9a46b") + path("M560,400 q60,-70 140,-90", sw=16, stroke="#e6cc9a")
    scene("classic-guess-how-much", b)


def c_wimpy():
    b = rect(0, 0, W, 300, "#dfe9f5", 0, 0) + rect(-4, 300, W + 8, 110, "#c9b79a", 0, 4)
    b += rect(70, 50, 150, 190, "#fff", 4) + "".join(rect(84 + (i % 5) * 28, 100 + (i // 5) * 26, 22, 20, c, 2, 2) for i, c in enumerate([BERRY, BLUE, BUTTER, MEADOW, PINK] * 4)) + txt(145, 84, "MARCH", 22)
    b += rect(380, 230, 520, 22, WOOD, 6) + rect(410, 252, 18, 110, WOOD_DK, 3) + rect(850, 252, 18, 110, WOOD_DK, 3) + book_open(600, 232, 260, 120, BLUE)
    b += path("M540,150 q30,-30 60,0 M580,170 l20,40 M570,200 l-10,40", sw=4) if False else ""
    b += circ(560, 175, 16, "#fff", 3.5) + path("M560,191 v30 M560,200 l-14,10 M560,200 l14,10 M560,221 l-10,14 M560,221 l10,14", sw=3.5) + path("M640,170 h60 M640,190 h80 M640,210 h50", sw=3, stroke="#8a93ab")
    b += g(rect(-34, -22, 68, 22, "#3a3a4a", 10) + circ(-18, -12, 7, "#888", 2.5) + circ(18, -12, 7, BERRY, 2.5) + rect(-3, -24, 6, 6, "#888", 0, 0), 1010, 305, 1.4)
    b += g(path("M0,0 v-90 l50,-50", sw=7) + poly([(30, -150), (84, -128), (68, -104), (20, -126)], BUTTER, 4), 960, 252, 1)
    b += g(path("M-30,0 h60 v-24 q-6,-24 -30,-24 t-30,24 z", WHITE) + path("M-30,-12 h60", sw=3, stroke=BERRY), 200, 380, 1.1) + g(path("M-30,0 h60 v-24 q-6,-24 -30,-24 t-30,24 z", WHITE) + path("M-30,-12 h60", sw=3, stroke=BERRY), 290, 384, 1.1, 14)
    scene("classic-wimpy-kid", b)


ALL = [c_harry, c_caterpillar, c_wild, c_charlotte, c_narnia, c_matilda, c_gruffalo, c_goodnight_moon, c_alice, c_cat_hat, c_peter, c_pooh,
       c_hobbit, c_green_eggs, c_charlie, c_wind, c_anne, c_tiger_tea, c_guess_how_much, c_wimpy]

if __name__ == "__main__":
    for fn in ALL:
        fn()
    print("classic illustrations written:", len(ALL))
