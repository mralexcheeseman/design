# Renders print-file SVGs to 300 dpi transparent PNGs, plus the worn-ink back (about 9% of the ink knocked
# out in a speckle so dark shirts stay soft). Needs node (npx @resvg/resvg-js-cli), numpy, scipy, Pillow.
# usage: python3 render_print.py <name>-crest.svg <name>-back.svg ...
import re, subprocess, sys
import numpy as np
from PIL import Image
from scipy import ndimage

def render(svg):
    mm = float(re.search(r'width="([\d.]+)mm"', open(svg).read()).group(1))
    png = svg[:-4] + '-300dpi.png'
    subprocess.run(['npx', '--yes', '@resvg/resvg-js-cli', '--fit-width', str(round(mm / 25.4 * 300)), svg, png], check=True, capture_output=True)
    im = Image.open(png); im.save(png, dpi=(300, 300))
    return png

def worn(png, knockout=0.09, seed=7):
    im = np.array(Image.open(png).convert('RGBA'))
    rng = np.random.default_rng(seed)
    h, w = im.shape[:2]
    noise = sum(ndimage.gaussian_filter(rng.random((h, w)), s) * wgt for s, wgt in ((1, 0.35), (4, 0.4), (14, 0.25)))
    ink = im[..., 3] > 0
    cut = noise > np.quantile(noise[ink], 1 - knockout)
    im[..., 3] = np.where(cut, 0, im[..., 3])
    Image.fromarray(im).save(png.replace('-300dpi', '-worn-300dpi'), dpi=(300, 300))

for svg in sys.argv[1:]:
    png = render(svg)
    if '-back' in svg:
        worn(png)
    print(png)
