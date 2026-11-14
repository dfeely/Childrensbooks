#!/usr/bin/env python3
"""Printable colouring sheets (line art), reading log and chart (SVG + PDF), thumbnails and five new banners.
    python3 tools/illustrations_printables.py   (needs rsvg-convert for the PDFs)"""
import os
import re
import subprocess
from illustrations import *  # noqa: F401,F403
from illustrations_christmas import cottage  # noqa: F401
from illustrations_classics import butterfly, apple, pear, strawberry, teapot, cup, balloon, lantern  # noqa: F401
from illustrations_top20 import dog, donut, trophy_ball, football, notebook  # noqa: F401

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PRINT = os.path.join(ROOT, "assets", "print")
os.makedirs(PRINT, exist_ok=True)
FONT = "font-family=\"Atkinson Hyperlegible, Arial, sans-serif\""


def whiten(svg):
    svg = re.sub(r'fill="(#[0-9a-fA-F]{3,8}|rgb[^"]*)"', 'fill="#ffffff"', svg)
    svg = re.sub(r'stroke="(#[0-9a-fA-F]{3,8})"', 'stroke="#1f2a44"', svg)
    return svg


def write(path_, body, w, h, bg="#ffffff"):
    with open(path_, "w", encoding="utf-8") as fh:
        fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


def sheet(name, title, body):
    """800x1000 portrait colouring sheet with a border and a title."""
    frame = rect(24, 24, 752, 952, "#ffffff", 20, 6) + f'<text x="400" y="86" text-anchor="middle" font-size="40" font-weight="700" {FONT} fill="#1f2a44">{title}</text>'
    foot = f'<text x="400" y="958" text-anchor="middle" font-size="20" {FONT} fill="#1f2a44">childrensbooks.ie · free to print for home and classroom use</text>'
    svg_body = whiten(body)
    write(os.path.join(PRINT, name + ".svg"), frame + svg_body + foot, 800, 1000)
    # PDF + preview PNG
    subprocess.run(["rsvg-convert", "-f", "pdf", "-w", "595", "-h", "744", os.path.join(PRINT, name + ".svg"), "-o", os.path.join(PRINT, name + ".pdf")], check=True)
    subprocess.run(["rsvg-convert", "-w", "480", os.path.join(PRINT, name + ".svg"), "-o", os.path.join(PRINT, name + ".png")], check=True)


def fit(body, cx, cy, bw, bh):
    """Centre `body` in a box (cx, cy, bw, bh), scaling it up or down to fit; bbox measured by rendering."""
    tmp = os.path.join(PRINT, "_fit.svg")
    write(tmp, g(body, 1000, 1000), 2000, 2000)
    out = subprocess.run(["convert", "-background", "none", tmp, "-trim", "-format", "%w %h %X %Y", "info:"], capture_output=True, text=True).stdout.split()
    os.remove(tmp)
    w, h = float(out[0]), float(out[1])
    x0, y0 = float(out[2].lstrip("+")), float(out[3].lstrip("+"))
    k = min(bw / w, bh / h)
    mx, my = x0 + w / 2 - 1000, y0 + h / 2 - 1000
    return g(body, cx - mx * k, cy - my * k, k)


def sheets():
    sheet("colouring-owl", "The night owl", fit(owl(0, 0, 1, "#8b6a4b", "#d9b98e"), 400, 520, 480, 560) + moon(650, 200, 70) + "".join(star(x, y, r, "#fff") for x, y, r in [(150, 200, 26), (260, 150, 20), (540, 130, 22), (110, 380, 18)]) + path("M60,880 q340,-70 680,0", sw=8) + tree(110, 900, 1.2) + tree(690, 900, 1.2))
    sheet("colouring-rocket", "Blast off!", fit(rocket(0, 0, 1), 400, 520, 360, 620) + "".join(star(x, y, r) for x, y, r in [(130, 200, 24), (660, 180, 28), (150, 800, 22), (660, 780, 24), (700, 420, 18)]) + circ(130, 480, 60, "#fff", 5) + path("M80,470 q50,-30 100,0", sw=4) + circ(660, 620, 44, "#fff", 5) + path("M300,900 q100,40 200,0", sw=6))
    sheet("colouring-whale", "The friendly whale", fit(whale(0, 0, 1), 400, 500, 640, 440) + path("M40,780 q60,-40 120,0 t120,0 t120,0 t120,0 t120,0 t120,0", sw=7) + path("M40,860 q60,-40 120,0 t120,0 t120,0 t120,0 t120,0 t120,0", sw=7) + cloud(160, 170, 1.4) + sun(660, 170, 50))
    sheet("colouring-fox", "The cheeky fox", fit(fox(0, 0, 1), 400, 500, 520, 560) + tree(110, 880, 1.3) + tree(690, 880, 1.3) + "".join(flower(x, 920, "#fff", 1.4) for x in (260, 400, 540)) + cloud(180, 170, 1.4) + cloud(620, 190, 1.2))
    sheet("colouring-rabbit", "Rabbit’s garden", fit(rabbit(0, 0, 1), 400, 500, 440, 640) + "".join(flower(x, y, "#fff", 1.6) for x, y in [(130, 900), (270, 920), (530, 920), (670, 900)]) + sun(650, 170, 56) + cloud(160, 190, 1.3) + path("M40,840 q360,-60 720,0", sw=7))
    sheet("colouring-bear", "Bear’s story time", fit(bear(0, 0, 1), 400, 400, 400, 460) + fit(book_open(0, 0, 260, 130, "#fff"), 400, 760, 480, 240) + "".join(star(x, y, r) for x, y, r in [(150, 170, 24), (650, 170, 24), (110, 560, 18), (690, 580, 18)]) + cloud(400, 150, 1.2))
    sheet("colouring-swan", "Swan on the lake", fit(swan(0, 0, 1), 400, 480, 560, 500) + path("M60,760 q60,-40 120,0 t120,0 t120,0 t120,0 t120,0", sw=7) + path("M60,830 q60,-40 120,0 t120,0 t120,0 t120,0 t120,0", sw=7) + "".join(path(f"M{x},800 v-120 M{x},720 q20,-30 30,-50", sw=6) for x in (90, 710)) + sun(660, 170, 54) + cloud(180, 190, 1.4))
    sheet("colouring-cottage", "The little cottage", fit(cottage(0, 0, 1), 400, 520, 560, 480) + tree(110, 880, 1.3) + tree(690, 880, 1.3) + sun(650, 170, 56) + cloud(180, 190, 1.4) + "".join(flower(x, 930, "#fff", 1.4) for x in (260, 400, 540)) + path("M400,760 q-60,60 -120,120", sw=0))


def reading_log():
    W, H = 794, 1123
    b = rect(20, 20, W - 40, H - 40, "#ffffff", 18, 5) + f'<text x="{W/2}" y="86" text-anchor="middle" font-size="42" font-weight="700" {FONT} fill="#1f2a44">My reading log</text>'
    b += f'<text x="60" y="130" font-size="20" {FONT} fill="#1f2a44">Name: ______________________</text><text x="430" y="130" font-size="20" {FONT} fill="#1f2a44">Year: ____________</text>'
    b += rect(48, 158, W - 96, 40, "#ffcf4a", 6, 3.5) + "".join(f'<text x="{x}" y="185" font-size="18" font-weight="700" {FONT} fill="#1f2a44">{t}</text>' for x, t in [(60, "#"), (100, "Book title"), (400, "Author"), (520, "Finished"), (640, "Rating")])
    for i in range(15):
        y = 198 + i * 56
        b += rect(48, y, W - 96, 56, "#ffffff" if i % 2 else "#f3f9fc", 0, 2.5) + f'<text x="60" y="{y + 35}" font-size="18" {FONT} fill="#1f2a44">{i + 1}</text>'
        b += "".join(star(692 + k * 0, y + 28, 0) for k in range(0)) + "".join(f'<polygon points="{px},{py}" fill="none"/>' for px, py in [])
        b += "".join(path(f"M{646 + k * 20},{y + 18} l2.5,7 7.5,0 -6,4.5 2.2,7.5 -6.2,-4.5 -6.2,4.5 2.2,-7.5 -6,-4.5 7.5,0 z", "none", 1.6) for k in range(5))
    b += f'<text x="{W/2}" y="{H - 38}" text-anchor="middle" font-size="16" {FONT} fill="#1f2a44">childrensbooks.ie · free to print for home and classroom use</text>'
    write(os.path.join(PRINT, "reading-log.svg"), b, W, H)


def reading_chart():
    W, H = 794, 1123
    b = rect(20, 20, W - 40, H - 40, "#ffffff", 18, 5) + f'<text x="{W/2}" y="90" text-anchor="middle" font-size="42" font-weight="700" {FONT} fill="#1f2a44">30-day reading chart</text>'
    b += f'<text x="{W/2}" y="132" text-anchor="middle" font-size="20" {FONT} fill="#1f2a44">Read for 10 minutes, then colour in a star. Name: ______________</text>'
    for i in range(30):
        cx = 110 + (i % 5) * 144
        cy = 240 + (i // 5) * 128
        b += star(cx, cy, 46, "#ffffff", 4) + f'<text x="{cx}" y="{cy + 7}" text-anchor="middle" font-size="20" font-weight="700" {FONT} fill="#1f2a44">{i + 1}</text>'
    b += rect(60, 1010, W - 120, 56, "#fff1d6", 12, 4) + f'<text x="{W/2}" y="1046" text-anchor="middle" font-size="22" font-weight="700" {FONT} fill="#1f2a44">When you reach 30: choose a new book as a reward!</text>'
    write(os.path.join(PRINT, "reading-chart.svg"), b, W, H)


def pdfs():
    for n in ("reading-log", "reading-chart"):
        subprocess.run(["rsvg-convert", "-f", "pdf", "-w", "595", "-h", "842", os.path.join(PRINT, n + ".svg"), "-o", os.path.join(PRINT, n + ".pdf")], check=True)
        subprocess.run(["rsvg-convert", "-w", "480", os.path.join(PRINT, n + ".svg"), "-o", os.path.join(PRINT, n + ".png")], check=True)


# ------------------------------------------------------------------ banners
W, H = 1200, 400


def desk():
    return rect(-4, 300, W + 8, 110, WOOD, 0, 4) + rect(-4, 300, W + 8, 16, WOOD_DK, 0, 4)


def crayon(x, y, c, rot=0):
    return g(rect(-9, -70, 18, 110, c, 3, 3) + poly([(-9, -70), (9, -70), (0, -92)], c, 3) + rect(-9, -40, 18, 12, "#fff", 0, 2.5), x, y, 1, rot)


def banner_colouring():
    b = rect(0, 0, W, 300, "#fff1d6", 0, 0) + desk()
    b += g(rect(0, 0, 260, 320, "#fff", 8) + path("M60,100 q70,-60 140,0 q-30,90 -70,100 q-40,-10 -70,-100 z", "none", 4) + circ(130, 250, 24, "none", 4), 120, 40, 1, -6)
    b += g(rect(0, 0, 260, 320, "#fff", 8) + "".join(path(p, f, 4) for p, f in [("M60,100 q70,-60 140,0 q-30,90 -70,100 q-40,-10 -70,-100 z", BERRY)]) + circ(130, 250, 24, BUTTER, 4), 800, 20, 1, 5)
    b += "".join(crayon(450 + i * 46, 340, c, (i - 3) * 6) for i, c in enumerate([BERRY, BUTTER, MEADOW, BLUE, PURPLE, "#ec7a2e", PINK]))
    b += star(1100, 100, 26) + star(420, 70, 20, PINK)
    save("banner-colouring-pages", W, H, b)


def banner_reading_log():
    b = rect(0, 0, W, 300, "#e8f4f8", 0, 0) + desk()
    b += g(rect(0, 0, 420, 270, "#fff", 8) + "".join(star(40 + (i % 5) * 80, 50 + (i // 5) * 80, 24, BUTTER if i < 9 else "#fff", 3.5) for i in range(15)), 120, 40, 1, -3)
    b += book_open(760, 300, 240, 110, MEADOW) + g(rect(-9, -90, 18, 130, BUTTER, 3) + poly([(-9, 40), (9, 40), (0, 62)], "#f1cf9b", 3) + rect(-9, -104, 18, 16, PINK, 3), 940, 240, 1, 40) + trophy_ball(1060, 300, 1) + star(700, 70, 22, PINK)
    save("banner-reading-log", W, H, b)


def banner_world_book_day():
    b = rect(0, 0, W, 300, "#fff1d6", 0, 0) + desk()
    b += "".join(path(f"M{x},0 v{y}", sw=3) + poly([(x, y), (x + 26, y + 34), (x - 26, y + 34)], c, 3.5) for x, y, c in [(100, 70, BERRY), (190, 100, BUTTER), (280, 70, BLUE), (370, 110, MEADOW), (900, 80, PURPLE), (990, 110, BERRY), (1080, 70, BUTTER)]) + path("M100,0 q500,60 1000,0", sw=0)
    b += g(poly([(-60, 0), (60, 0), (0, -130)], PURPLE, 4) + path("M-80,0 h160", sw=8) + "".join(star(x, y, 9) for x, y in [(-10, -60), (16, -30)]), 520, 300, 1.1) + g(poly([(-34, 0), (34, 0), (44, -60), (-44, -60)], "#fff", 4) + "".join(rect(-40 + i * 24, -60, 12, 60, BERRY, 0, 0) for i in range(0)) + rect(-30, -70, 60, 12, BERRY, 3) + poly([(-26, -58), (26, -58), (30, -2), (-30, -2)], "#fff", 0), 640, 300, 0)
    b += g(poly([(-50, 0), (50, 0), (60, -50), (30, -30), (0, -60), (-30, -30), (-60, -50)], BUTTER, 4) + "".join(circ(x, -14, 5, BERRY, 2.5) for x in (-30, 0, 30)), 780, 300, 1.2) + g(rect(-60, -60, 120, 60, "#c9a46b", 8) + path("M-60,-40 h120", sw=3), 330, 300, 1) + owl(1040, 300, 1.2) + book_open(640, 300, 240, 100, BLUE)
    save("banner-world-book-day", W, H, b)


def banner_activities():
    b = rect(0, 0, W, 300, "#e9f7ec", 0, 0) + desk()
    b += g(rect(0, 0, 220, 160, "#fff", 8) + path("M30,110 q40,-80 80,-20 t80,-40", sw=5, stroke=BERRY), 100, 90, 1, -5) + "".join(crayon(400 + i * 44, 340, c, (i - 2) * 8) for i, c in enumerate([BERRY, BUTTER, MEADOW, BLUE, PURPLE]))
    b += g(path("M-30,-50 l50,60 M30,-50 l-50,60", sw=6) + circ(-34, 24, 18, "none", 6) + circ(34, 24, 18, "none", 6), 760, 280, 1.1) + g(rect(-24, -60, 48, 80, "#3a8fd1", 8) + rect(-18, -80, 36, 24, "#fff", 4), 880, 320, 1) + rect(960, 260, 140, 36, BUTTER, 6) + rect(980, 224, 100, 36, PINK, 6) + star(160, 60, 24) + star(1100, 100, 22, PINK) + butterfly(620, 120, 1.2)
    save("banner-book-activities", W, H, b)


def banner_animal_books():
    b = rect(0, 0, W, 300, "#d6efff", 0, 0) + hills(W, 300, [(200, "#b8e3b0", 14, .2)]) + rect(-4, 300, W + 8, 110, "#7cc46a", 0, 4) + sun(1080, 70, 34) + cloud(180, 70, 1)
    b += sheep(170, 340, 1.1) + fox(400, 360, 1.0) + rabbit(620, 360, 1.0) + bear(840, 360, 1.0) + owl(1040, 350, .9)
    save("banner-animal-books", W, H, b)


if __name__ == "__main__":
    sheets()
    reading_log()
    reading_chart()
    pdfs()
    for f in (banner_colouring, banner_reading_log, banner_world_book_day, banner_activities, banner_animal_books):
        f()
    print("printables and banners written")
