# Traces the four heritage crests (direction A, chosen by Alex 11 Oct 2026) from the
# 1024 px source sheet into single-colour vector SVGs. Draft-quality vectors: a designer
# clean-up pass is still recommended before bulk production.
# usage: python3 trace_heritage.py [out dir]
import os, sys
import numpy as np
from PIL import Image, ImageFilter
import potrace

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'explorations', 'direction-a-heritage-1024.png')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'heritage')
SCALE = 4
QUADS = {'oriole-palace': (0, 0), 'grand-valbrune': (1, 0), 'hotel-solvane': (0, 1), 'casa-thalene': (1, 1)}

def crop(gray, qx, qy):
    """Bounding box of the crest whose centre is in this quadrant (ignores bits of neighbours)."""
    from scipy import ndimage
    dark = ndimage.binary_dilation(gray < 128, iterations=6)
    labels, n = ndimage.label(dark)
    cy, cx = qy * 512 + 256, qx * 512 + 256
    coms = ndimage.center_of_mass(dark, labels, range(1, n + 1))
    mine = [i + 1 for i, (y, x) in enumerate(coms) if int(x // 512) == qx and int(y // 512) == qy]
    inside = np.isin(labels, mine)
    q = np.where(inside, gray, 255)
    ys, xs = np.where(q < 128)
    q = gray
    pad = 6
    x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad, 1023)
    y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad, 1023)
    keep = np.where(inside[y0:y1 + 1, x0:x1 + 1], q[y0:y1 + 1, x0:x1 + 1], 255).astype(np.uint8)
    return Image.fromarray(keep)

def trace(img):
    big = img.resize((img.width * SCALE, img.height * SCALE), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
    bits = np.array(big) >= 128  # potracer fills the False region
    path = potrace.Bitmap(bits).trace(turdsize=12, alphamax=1.0, opticurve=True, opttolerance=0.25)
    d = []
    for c in path:
        p = c.start_point; d.append(f'M{p.x:.1f} {p.y:.1f}')
        for s in c.segments:
            if s.is_corner:
                d.append(f'L{s.c.x:.1f} {s.c.y:.1f}L{s.end_point.x:.1f} {s.end_point.y:.1f}')
            else:
                d.append(f'C{s.c1.x:.1f} {s.c1.y:.1f} {s.c2.x:.1f} {s.c2.y:.1f} {s.end_point.x:.1f} {s.end_point.y:.1f}')
        d.append('Z')
    return big.width, big.height, ''.join(d)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    gray = np.array(Image.open(SRC).convert('L'))
    for name, (qx, qy) in QUADS.items():
        w, h, d = trace(crop(gray, qx, qy))
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
               f'<path fill="#000" fill-rule="evenodd" d="{d}"/></svg>')
        open(os.path.join(OUT, f'{name}.svg'), 'w').write(svg)
        print(name, w, h, len(svg))
