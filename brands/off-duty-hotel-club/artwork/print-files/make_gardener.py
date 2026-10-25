# Builds the Gardener back print (Kurhaus Edelmatt, Wengen) to the range spec in merch.md: title in Anton,
# 280 mm wide, hotel and city in Oswald 500. Other backs: make_art.py
# usage: python3 make_gardener.py <output dir> <fonts dir>   (fonts dir holds Anton.ttf and Oswald.ttf, static 500)
# Writes an outlined SVG plus 300 dpi PNGs, clean and worn-ink. Needs: pip install fonttools cairosvg numpy pillow
import sys,io
import numpy as np,cairosvg
from PIL import Image,ImageFilter
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
OUT=sys.argv[1]; F=(sys.argv[2] if len(sys.argv)>2 else 'fonts')+'/'
anton=TTFont(F+'Anton.ttf'); oswald=TTFont(F+'Oswald.ttf')
INK='#E1474A'   # ink-geranium

def text(font,s,size,cx,y,track=0):
    """Outlined text centred at cx, baseline y (mm units). track in em."""
    gs=font.getGlyphSet(); cmap=font.getBestCmap(); upm=font['head'].unitsPerEm; hm=font['hmtx']
    sc=size/upm; names=[cmap[ord(c)] for c in s]
    adv=[hm[n][0]*sc+track*size for n in names]; w=sum(adv)-track*size
    x=cx-w/2; d=''; bp=BoundsPen(gs)
    for n,a in zip(names,adv):
        pen=SVGPathPen(gs); gs[n].draw(TransformPen(pen,(sc,0,0,-sc,x,y))); d+=pen.getCommands()
        gs[n].draw(TransformPen(bp,(sc,0,0,-sc,x,y))); x+=a
    text.bounds=bp.bounds
    return f'<path d="{d}"/>',w

def svg(w,h,body,col):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><g fill="{col}" fill-rule="nonzero">{body}</g></svg>'

def back_anton(title,hotel,city,fname):
    W,H=300,120
    t,tw=text(anton,title,1,0,0); size=280/tw
    text(anton,title,size,W/2,0); base=5-text.bounds[1]
    p1,_=text(anton,title,size,W/2,base)
    p2,_=text(oswald,hotel,14,W/2,base+26,track=0.18)
    p3,_=text(oswald,city,8.5,W/2,base+40,track=0.35)
    open(f'{OUT}/{fname}-back.svg','w').write(svg(W,H,p1+p2+p3,INK))

def png(fname,worn=False,seed=5):
    """Transparent 300 dpi PNG of an SVG; worn knocks about 9% of the ink out in a speckle."""
    svgtext=open(f'{OUT}/{fname}.svg').read(); wmm=float(svgtext.split('width="')[1].split('mm')[0])
    im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svgtext.encode(),output_width=round(wmm/25.4*300)))).convert('RGBA')
    if worn:
        a=np.asarray(im).copy(); h,w=a.shape[:2]; rng=np.random.default_rng(seed)
        def noise(cell):   # smooth value noise, one random value per cell
            g=rng.random((h//cell+2,w//cell+2)); return np.asarray(Image.fromarray((g*255).astype(np.uint8)).resize((w+cell,h+cell),Image.BICUBIC))[:h,:w]/255
        n=noise(60)*0.45+noise(14)*0.35+noise(4)*0.2
        # only the big strokes wear; the hotel and city lines stay whole
        m=Image.fromarray(((a[...,3]>0)*255).astype(np.uint8)).filter(ImageFilter.MinFilter(31)).filter(ImageFilter.MaxFilter(31))
        big=np.asarray(m)>0; cut=big&(n>np.quantile(n[big],0.91)); a[...,3][cut]=0
        im=Image.fromarray(a)
    im.save(f'{OUT}/{fname}{"-worn" if worn else ""}-300dpi.png',dpi=(300,300),optimize=True)

back_anton('GARDENER','KURHAUS EDELMATT','WENGEN','gardener')
png('gardener-back'); png('gardener-back',worn=True)
print('done')
