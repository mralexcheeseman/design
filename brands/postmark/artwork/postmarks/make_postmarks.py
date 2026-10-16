"""Draws the Postmark cancellation stamps: one per destination, one family, one ink each.

    python3 brands/postmark/supply/postmarks/make_postmarks.py

Writes outlined SVGs (the full postmark, and <id>-ring.svg without the waves for cards) (no live text, so they print anywhere and render in <img>) to
brands/postmark/public/assets/postmarks/<id>.svg for the site, and black masters to
supply/postmarks/masters/<id>.svg for print. Needs: pip install fonttools brotli.

The family rules: a double ring, the city on the top arc and the country on the bottom
arc in Barlow Condensed 600 capitals, the destination number and "PAR AVION" in the
centre, five wavy cancellation lines to the right. Change the rules here, never per stamp.
"""
import math, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = pathlib.Path(__file__).parent
BRAND = HERE.parents[1]
FONT = TTFont(HERE / 'fonts' / 'barlow-condensed-600.woff2')
GLYPHS, CMAP, UPM = FONT.getGlyphSet(), FONT.getBestCmap(), FONT['head'].unitsPerEm
HMTX = FONT['hmtx']

# id, city (top arc), country (bottom arc), number, ink. Inks match the destination tokens in the design system.
STAMPS = [
    ('amalfi', 'AMALFI', 'ITALIA', '01', '#1f4b99'),
    ('marrakech', 'MARRAKECH', 'MAROC', '02', '#a24a2a'),
    ('kyoto', 'KYOTO', 'NIPPON', '03', '#27365e'),
    ('mexico-city', 'CIUDAD DE MÉXICO', 'MÉXICO', '04', '#b2406a'),
]

CX, CY, R_OUT, R_IN = 100, 100, 92, 64      # rings, in a 340 x 200 box
STROKE = 3.2                                # every line in the family is this weight


def advance(ch, size, track):
    return HMTX[GLYPHS_NAME(ch)][0] * size / UPM + track


def GLYPHS_NAME(ch):
    return CMAP.get(ord(ch), CMAP[ord('?')])


def glyph_path(ch, size, x, y, angle=0.0):
    """Outline of one character, baseline origin at (x, y), rotated by angle (radians)."""
    pen = SVGPathPen(GLYPHS)
    s = size / UPM
    c, si = math.cos(angle), math.sin(angle)
    # font units are y-up; SVG is y-down
    t = (s * c, s * si, s * si, -s * c, x, y)
    GLYPHS[GLYPHS_NAME(ch)].draw(TransformPen(pen, t))
    return pen.getCommands()


def text_width(text, size, track):
    return sum(advance(ch, size, track) for ch in text) - track


def straight(text, size, cx, baseline, track=0.0):
    x = cx - text_width(text, size, track) / 2
    out = []
    for ch in text:
        if ch != ' ':
            out.append(glyph_path(ch, size, x, baseline))
        x += advance(ch, size, track)
    return out


def on_arc(text, size, radius, top, track):
    """Letters centred on the top arc (reading clockwise) or the bottom arc (reading left to right)."""
    total = text_width(text, size, track) / radius          # angle the text spans
    out = []
    pos = -total / 2
    for ch in text:
        w = advance(ch, size, track)
        mid = pos + (w - track) / 2 / radius                 # glyph centre, as an angle from the top or bottom
        if top:
            a = -math.pi / 2 + mid                           # 0 = 12 o'clock
            gx, gy = CX + radius * math.cos(a), CY + radius * math.sin(a)
            rot = a + math.pi / 2
        else:
            a = math.pi / 2 - mid                            # 0 = 6 o'clock, text left to right
            r = radius + size * 0.7                          # baseline outside the cap height
            gx, gy = CX + r * math.cos(a), CY + r * math.sin(a)
            rot = a - math.pi / 2
        half = (w - track) / 2
        # move from the glyph centre back to its baseline origin along the tangent
        ox, oy = gx - half * math.cos(rot), gy - half * math.sin(rot)
        if ch != ' ':
            out.append(glyph_path(ch, size, ox, oy, rot))
        pos += w / radius
    return out


def fit(text, radius, span, size, track):
    """Shrink a long city name until it fits the arc span (radians)."""
    while text_width(text, size, track) / radius > span and size > 9:
        size -= 0.5
    return size


def waves():
    lines = []
    for i in range(5):
        y = CY - 36 + i * 18
        d = f'M{CX + R_OUT + 14},{y}'
        for k in range(4):
            x0 = CX + R_OUT + 14 + k * 32
            d += f' q8,-7 16,0 t16,0'
        lines.append(d)
    return lines


def stamp(city, country, number, ink, ring_only=False):
    r_text = (R_OUT + R_IN) / 2
    top_size = fit(city, r_text - 7, math.radians(200), 19, 2.4)
    paths = on_arc(city, top_size, r_text - 7, True, 2.4)
    paths += on_arc(country, 15, r_text - 12, False, 3)
    paths += straight(number, 34, CX, CY + 6, 1)
    paths += straight('PAR AVION', 11, CX, CY + 27, 2.2)
    glyphs = ''.join(f'<path d="{p}"/>' for p in paths)
    rings = (f'<circle cx="{CX}" cy="{CY}" r="{R_OUT}"/><circle cx="{CX}" cy="{CY}" r="{R_IN}"/>'
             f'<path d="M{CX-26},{CY-32}h52"/>')
    wave = '' if ring_only else ''.join(f'<path d="{d}"/>' for d in waves())
    box = '0 0 200 200' if ring_only else '0 0 340 200'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{box}" role="img">'
            f'<g fill="none" stroke="{ink}" stroke-width="{STROKE}" stroke-linecap="round">{rings}{wave}</g>'
            f'<g fill="{ink}">{glyphs}</g></svg>\n')


if __name__ == '__main__':
    site = BRAND / 'public' / 'assets' / 'postmarks'
    masters = HERE / 'masters'
    site.mkdir(parents=True, exist_ok=True)
    masters.mkdir(exist_ok=True)
    for sid, city, country, number, ink in STAMPS:
        (site / f'{sid}.svg').write_text(stamp(city, country, number, ink))
        (site / f'{sid}-ring.svg').write_text(stamp(city, country, number, ink, ring_only=True))  # cards: no waves, so it reads at small sizes
        (masters / f'{sid}.svg').write_text(stamp(city, country, number, '#000'))
        print(f'wrote postmarks/{sid}.svg')
