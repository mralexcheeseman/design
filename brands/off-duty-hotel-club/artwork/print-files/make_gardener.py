# Builds the Head Gardener back print (Kurhaus Edelmatt, Wengen). Other backs: make_art.py
# The job title is squared block lettering drawn from rectangles, after the "Ciao" trucker hat Alex
# brought in (option A). Option B sets it in Anton like the rest of the range, for comparison.
# Hotel and city lines follow merch.md (Oswald 500, 14 mm / 8.5 mm).
# usage: python3 make_gardener.py <output dir> <fonts dir>   (fonts dir holds Anton.ttf and Oswald.ttf, static 500)
# Writes outlined SVGs plus 300 dpi PNGs, clean and worn-ink. Needs: pip install fonttools cairosvg numpy pillow
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

# Squared lettering on a grid: cap height 10, stroke S, letter width L, y down from the cap line.
# Each glyph is a list of polygons; a hole is a second contour wound the other way. Straight strokes and
# square corners as on the hat; D, R and N take a 45-degree cut or a diagonal so GARDENER stays legible.
S,L,GAP,SPACE=1.5,4.5,1.2,3.0
M=(10-S)/2                      # crossbar top, optically centred
R=L-S                           # x of the right stem
def rect(x,y,w,h): return [(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
def ring(x0,y0,x1,y1,c):        # chamfered on the right: outer clockwise, counter anticlockwise
    ci=c*0.42
    return [[(x0,y0),(x1-c,y0),(x1,y0+c),(x1,y1-c),(x1-c,y1),(x0,y1)],
            [(x0+S,y0+S),(x0+S,y1-S),(x1-S-ci,y1-S),(x1-S,y1-S-ci),(x1-S,y0+S+ci),(x1-S-ci,y0+S)]]
GLYPHS={
 'A':[rect(0,0,S,10),rect(R,0,S,10),rect(0,0,L,S),rect(0,M+0.4,L,S)],
 'D':ring(0,0,L,10,1.6),
 'E':[rect(0,0,S,10),rect(0,0,L,S),rect(0,M,L-0.5,S),rect(0,10-S,L,S)],
 'G':[rect(0,0,S,10),rect(0,0,L,S),rect(0,10-S,L,S),rect(R,M,S,10-M),rect(L/2,M,L/2,S)],
 'H':[rect(0,0,S,10),rect(R,0,S,10),rect(0,M,L,S)],
 'N':[rect(0,0,S,10),rect(R,0,S,10),[(0,0),(1.6,0),(L,10),(L-1.6,10)]],
 'R':ring(0,0,L,M+S-0.6,1.4)+[rect(0,0,S,10),[(1.7,M+S-1.0),(3.45,M+S-1.0),(L,10),(L-1.75,10)]],
}
def squared(s,unit,cx,top):
    """Squared lettering centred at cx, cap line at top, 1 grid unit = unit mm. Returns path, width."""
    w=sum(SPACE if c==' ' else L for c in s)+GAP*(len(s)-1); x=cx-w*unit/2; d=''
    for c in s:
        if c!=' ':
            for poly in GLYPHS[c]:
                d+='M'+'L'.join(f'{x+px*unit:.3f} {top+py*unit:.3f}' for px,py in poly)+'Z'
        x+=((SPACE if c==' ' else L)+GAP)*unit
    return f'<path d="{d}"/>',w*unit

def svg(w,h,body,col):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><g fill="{col}" fill-rule="nonzero">{body}</g></svg>'

def back_squared(hotel,city,fname):
    W=300
    _,w=squared('GARDENER',1,0,0); unit=280/w        # widest line is 280 mm
    p1,_=squared('HEAD',unit,W/2,5)
    top2=5+10*unit+2.6*unit
    p2,_=squared('GARDENER',unit,W/2,top2)
    base=top2+10*unit
    p3,_=text(oswald,hotel,14,W/2,base+26,track=0.18)
    p4,_=text(oswald,city,8.5,W/2,base+40,track=0.35)
    H=round(base+45)
    open(f'{OUT}/{fname}-back.svg','w').write(svg(W,H,p1+p2+p3+p4,INK))
    return unit*10

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

cap=back_squared('KURHAUS EDELMATT','WENGEN','head-gardener')
back_anton('HEAD GARDENER','KURHAUS EDELMATT','WENGEN','head-gardener-anton')
for f in ['head-gardener-back','head-gardener-anton-back']: png(f); png(f,worn=True)
print(f'done; squared cap height {cap:.1f} mm')
