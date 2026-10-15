# Off Duty Hotel Club crest family: outlined, single-colour vector SVGs, drawn at final size in millimetres.
# usage: python3 crests.py <fonts dir> [out dir]
# Fonts (SIL Open Font License, github.com/google/fonts): Cinzel, Bodoni Moda.
# Rules this file follows are in .claude/skills/hotel-crest/SKILL.md.
import math, sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.varLib.instancer import instantiateVariableFont

FONTS = sys.argv[1].rstrip('/') + '/'
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))

def load(name, **axes):
    f = TTFont(FONTS + name)
    return instantiateVariableFont(f, axes) if axes else f

CAPS = load('Cinzel[wght].ttf', wght=600)                    # spaced inscription capitals
MONO = load('BodoniModa[opsz,wght].ttf', opsz=28, wght=600)  # monogram letters

def _glyphs(font, s):
    cmap = font.getBestCmap()
    return [cmap[ord(c)] for c in s]

def width(font, s, size, track=0):
    upm = font['head'].unitsPerEm; hm = font['hmtx']
    return sum(hm[n][0] for n in _glyphs(font, s)) * size / upm + track * size * (len(s) - 1)

def glyph(font, name, size, matrix):
    """Path data for one glyph; matrix maps font units (y up) through scale size/upm."""
    gs = font.getGlyphSet(); upm = font['head'].unitsPerEm; sc = size / upm
    a, b, c, d, e, f = matrix
    pen = SVGPathPen(gs)
    gs[name].draw(TransformPen(pen, (a * sc, b * sc, -c * sc, -d * sc, e, f)))
    return pen.getCommands()

def line(font, s, size, cx, baseline, track=0):
    """Text centred on cx with its baseline at y."""
    upm = font['head'].unitsPerEm; hm = font['hmtx']
    x = cx - width(font, s, size, track) / 2; d = ''
    for n in _glyphs(font, s):
        d += glyph(font, n, size, (1, 0, 0, 1, x, baseline))
        x += hm[n][0] * size / upm + track * size
    return f'<path d="{d}"/>'

def arc(font, s, size, cx, cy, r, top=True, track=0.18):
    """Text on a circle. Top: reads clockwise, baseline on r, letters point outward.
    Bottom: reads left to right, baseline on r, letters point to the centre."""
    upm = font['head'].unitsPerEm; hm = font['hmtx']
    total = width(font, s, size, track) / r                 # radians spanned
    th = (-math.pi / 2 - total / 2) if top else (math.pi / 2 + total / 2)
    d = ''
    for n in _glyphs(font, s):
        adv = hm[n][0] * size / upm
        mid = th + (adv / 2 / r if top else -adv / 2 / r)
        rot = mid + math.pi / 2 if top else mid - math.pi / 2
        px, py = cx + r * math.cos(mid), cy + r * math.sin(mid)
        ca, sa = math.cos(rot), math.sin(rot)
        # local glyph origin at (-adv/2, 0), rotated, moved onto the circle
        ox, oy = px + ca * (-adv / 2), py + sa * (-adv / 2)
        d += glyph(font, n, size, (ca, sa, -sa, ca, ox, oy))
        step = (adv + track * size) / r
        th += step if top else -step
    return f'<path d="{d}"/>'

def bounds(font, ch, size):
    gs = font.getGlyphSet(); bp = BoundsPen(gs); n = _glyphs(font, ch)[0]
    gs[n].draw(bp); sc = size / font['head'].unitsPerEm
    x0, y0, x1, y1 = bp.bounds
    return x0 * sc, y0 * sc, x1 * sc, y1 * sc

def monogram(a, b, size, cx, baseline, overlap, gap, ink, mid):
    """Two interlaced capitals: the second letter cuts a hairline gap through the first,
    so the pair reads as a monogram rather than a blob."""
    upm = MONO['head'].unitsPerEm; hm = MONO['hmtx']
    na, nb = _glyphs(MONO, a + b)
    wa, wb = hm[na][0] * size / upm, hm[nb][0] * size / upm
    x = cx - (wa + wb - overlap) / 2
    pa = glyph(MONO, na, size, (1, 0, 0, 1, x, baseline))
    pb = glyph(MONO, nb, size, (1, 0, 0, 1, x + wa - overlap, baseline))
    return (f'<mask id="m{mid}" maskUnits="userSpaceOnUse" x="-500" y="-500" width="1000" height="1000">'
            f'<rect x="-500" y="-500" width="1000" height="1000" fill="#fff"/>'
            f'<path d="{pb}" fill="#000" stroke="#000" stroke-width="{gap}" stroke-linejoin="round"/></mask>'
            f'<path d="{pa}" mask="url(#m{mid})"/><path d="{pb}"/>')

def nested(big, small, bsize, ssize, cx, baseline, ink, mid, gap=1.0, dy=0):
    """A small capital set inside a large one (e.g. P inside O), with a hairline gap where they touch."""
    nb, ns = _glyphs(MONO, big + small); upm = MONO['head'].unitsPerEm; hm = MONO['hmtx']
    bx = cx - hm[nb][0] * bsize / upm / 2
    x0, y0, x1, y1 = bounds(MONO, small, ssize)
    sx = cx - (x0 + x1) / 2
    bb = bounds(MONO, big, bsize); sy = baseline - (bb[1] + bb[3]) / 2 + (y0 + y1) / 2 + dy
    pb = glyph(MONO, nb, bsize, (1, 0, 0, 1, bx, baseline))
    ps = glyph(MONO, ns, ssize, (1, 0, 0, 1, sx, sy))
    return (f'<mask id="m{mid}" maskUnits="userSpaceOnUse" x="-500" y="-500" width="1000" height="1000">'
            f'<rect x="-500" y="-500" width="1000" height="1000" fill="#fff"/>'
            f'<path d="{ps}" fill="#000" stroke="#000" stroke-width="{gap}" stroke-linejoin="round"/></mask>'
            f'<path d="{pb}" mask="url(#m{mid})"/><path d="{ps}"/>')

def oval_monogram(letter, cx, cy, rx, ry, thick, thin, ssize, ink, mid, gap=1.0):
    """A contrast oval (thick at the sides, thin at top and bottom) with a capital set inside it."""
    outer = f'M{cx - rx} {cy} A{rx} {ry} 0 1 0 {cx + rx} {cy} A{rx} {ry} 0 1 0 {cx - rx} {cy} Z'
    irx, iry = rx - thick, ry - thin
    inner = f'M{cx - irx} {cy} A{irx} {iry} 0 1 1 {cx + irx} {cy} A{irx} {iry} 0 1 1 {cx - irx} {cy} Z'
    (n,) = _glyphs(MONO, letter); x0, y0, x1, y1 = bounds(MONO, letter, ssize)
    pl = glyph(MONO, n, ssize, (1, 0, 0, 1, cx - (x0 + x1) / 2, cy + (y0 + y1) / 2))
    return (f'<mask id="m{mid}" maskUnits="userSpaceOnUse" x="-500" y="-500" width="1000" height="1000">'
            f'<rect x="-500" y="-500" width="1000" height="1000" fill="#fff"/>'
            f'<path d="{pl}" fill="#000" stroke="#000" stroke-width="{gap}" stroke-linejoin="round"/></mask>'
            f'<path fill-rule="evenodd" d="{outer} {inner}" mask="url(#m{mid})"/><path d="{pl}"/>')

def ring(cx, cy, r, w):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="currentColor" stroke-width="{w}"/>'

def dot(cx, cy, r=0.9):
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}"/>'

def star(cx, cy, r):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rr = r if i % 2 == 0 else r * 0.42
        pts.append(f'{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}')
    return f'<polygon points="{" ".join(pts)}"/>'

# ---------- frames ----------
SEAL_R = 40  # 80 mm seal

def seal(name, city, centre, ink, est=None, city_size=4.6):
    c = SEAL_R; body = ring(c, c, c - 0.8, 1.6) + ring(c, c, 29.6, 0.8)
    body += arc(CAPS, name, 5.6, c, c, 31.6, top=True, track=0.16)
    body += arc(CAPS, city, city_size, c, c, 37.1, top=False, track=0.42 if city_size < 5 else 0.3)
    body += star(c - 34.2, c + 0.2, 1.5) + star(c + 34.2, c + 0.2, 1.5)
    if est: body += line(CAPS, est, 2.9, c, c + 22.4, track=0.4)
    return svg(2 * c, 2 * c, body + centre, ink)

ARCH_W, ARCH_H = 62, 82

def arch(name, city, centre, ink):
    w, h = ARCH_W, ARCH_H; r = w / 2
    def outline(inset, sw):
        x0, x1, y1 = inset, w - inset, h - inset; rr = r - inset
        return (f'<path fill="none" stroke="currentColor" stroke-width="{sw}" '
                f'd="M{x0} {y1} V{r} A{rr} {rr} 0 0 1 {x1} {r} V{y1} Z"/>')
    body = outline(0.8, 1.6) + outline(3.6, 0.8)
    body += f'<rect x="3.6" y="{h - 19.5}" width="{w - 7.2}" height="0.8"/>'
    nsize = min(5.0, 5.0 * (w - 13) / width(CAPS, name, 5.0, 0.1))
    body += line(CAPS, name, nsize, w / 2, h - 11.2, track=0.1)
    body += line(CAPS, city, 3.4, w / 2, h - 6.0, track=0.5)
    return svg(w, h, body + centre, ink)

def svg(w, h, body, ink):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}" '
            f'color="{ink}"><g fill="{ink}">{body}</g></svg>')

# ---------- icons ----------
def oriole(x, y, s):
    """Small perched oriole, facing right, feet at (x, y), about 10*s mm long."""
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="'
            'M-5.2 -3.2 C-4.2 -5.6 -1.6 -6.6 0.6 -6.2 C1.6 -7.6 3.4 -7.9 4.4 -7 L6.4 -6.6 L4.6 -5.9 '
            'C4.6 -4.2 3.8 -2.6 2.2 -1.7 L0.9 -0.9 L1.3 0 L0.6 0 L0.2 -0.8 L-0.4 -0.6 L-0.4 0 L-1.1 0 L-1 -0.7 '
            'C-2.8 -1.2 -4.6 -1.6 -6.6 -0.9 L-9.4 0.6 C-8.2 -1.2 -6.8 -2.4 -5.2 -3.2 Z"/>'
            '<rect x="-6" y="0" width="13" height="0.75" rx="0.37"/></g>')

def sun_and_sea(cx, cy, r):
    """Half sun of thick rays sitting on three short wave bands."""
    out = f'<path d="M{cx - 7.5} {cy} A7.5 7.5 0 0 1 {cx + 7.5} {cy} Z"/>'
    for i in range(9):
        a = math.pi + (i + 0.5) * math.pi / 9
        x0, y0 = cx + 10 * math.cos(a), cy + 10 * math.sin(a)
        x1, y1 = cx + 16.5 * math.cos(a), cy + 16.5 * math.sin(a)
        out += f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>'
    for k, w in enumerate((34, 28, 20)):
        out += wave(cx, cy + 3.6 + k * 4.4, w, 1.6, n=(6, 6, 4)[k], amp=0.32)
    return out

def peaks(cx, base, s):
    return (f'<g transform="translate({cx} {base}) scale({s})"><path fill-rule="evenodd" d="'
            'M-15 0 L-5 -17 L-1.5 -11 L4 -23 L15 0 Z '
            'M4 -19.6 L0.6 -12.4 L2.6 -13.6 L4 -11.8 L5.6 -13.8 L7.6 -12.6 Z '
            'M-5 -13.8 L-7.6 -9.4 L-6 -10.2 L-4.8 -9 L-3.4 -10.4 Z"/></g>')

def wave(cx, y, w, sw, n=4, amp=0.45):
    x0 = cx - w / 2; seg = w / n
    d = f'M{x0} {y}' + ''.join(f' c{seg*0.25} -{seg*amp} {seg*0.75} -{seg*amp} {seg} 0' if i % 2 == 0
                               else f' c{seg*0.25} {seg*amp} {seg*0.75} {seg*amp} {seg} 0' for i in range(n))
    return f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round"/>'

# ---------- the four hotels ----------
# key: (shirt, ink on that shirt). Text is at least 2.9 mm (print); the embroidery variant keeps it at 4.5 mm or more.
C = SEAL_R
def oriole_palace(ink, embroidery=False):
    return seal('THE ORIOLE PALACE', 'LOS ANGELES',
                oval_monogram('P', C, C + 0.5, 10.2, 13.2, 3.0, 0.7, 17, ink, 'op') + oriole(C + 5.4, C - 12.7, 0.6),
                ink, est=None if embroidery else 'EST · 1928', city_size=5.0 if embroidery else 4.6)
def grand_valbrune(ink):
    return arch('GRAND VALBRUNE', 'ST. MORITZ',
                monogram('G', 'V', 21, ARCH_W / 2, 36, 3.2, 1.2, ink, 'gv') + peaks(ARCH_W / 2, 58.5, 0.88), ink)
def hotel_solvane(ink):
    return seal('HÔTEL SOLVANE', 'SAINT-TROPEZ', sun_and_sea(C, C + 2, 23.2), ink)
def casa_thalene(ink):
    return arch('CASA THALENE', 'MYKONOS',
                monogram('C', 'T', 24, ARCH_W / 2, 44, 3.4, 1.2, ink, 'ct') + wave(ARCH_W / 2, 53.5, 30, 1.4), ink)

OUTPUTS = {  # file name: (svg, shirt colour for previews)
 'security-crest':          (lambda: oriole_palace('#F5F2EA', embroidery=True), '#262626'),
 'security-crest-print':    (lambda: oriole_palace('#F5F2EA'), '#262626'),
 'ski-patrol-crest':        (lambda: grand_valbrune('#F1E6D2'), '#b3261e'),
 'lifeguard-crest':         (lambda: hotel_solvane('#BA3022'), '#f2c230'),
 'pool-boy-crest':          (lambda: casa_thalene('#21456B'), '#a9c8e8'),
}

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for k, (make, _) in OUTPUTS.items():
        open(f'{OUT}/{k}.svg', 'w').write(make())
    print('wrote', ', '.join(OUTPUTS))
