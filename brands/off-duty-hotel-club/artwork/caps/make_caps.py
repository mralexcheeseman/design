# Builds the cap front print files (option C: hotel crest over the job title, one ink).
# usage: python3 make_caps.py <fonts dir>   (Anton-Regular.ttf from github.com/google/fonts, OFL)
# Writes print/<cap>-front.svg (all text outlined, true size in mm) and print/<cap>-front-300dpi.png.
import os,re,sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import cairosvg

HERE=os.path.dirname(os.path.abspath(__file__))
CRESTS=os.path.join(HERE,'../../assets/crests')
OUT=os.path.join(HERE,'print'); os.makedirs(OUT,exist_ok=True)
anton=TTFont(os.path.join(sys.argv[1],'Anton-Regular.ttf'))

CAPS=[  # id, title, crest, ink
 ('lifeguard','LIFEGUARD','hotel-solvane','#ffffff'),
 ('security','SECURITY','oriole-palace','#c9a24e'),
 ('tennis-coach','TENNIS COACH','hotel-solvane','#c0281f'),
 ('valet','VALET','oriole-palace','#f5f2ea'),
 ('beach-club','BEACH CLUB','casa-thalene','#1d3d63'),
 ('night-porter','NIGHT PORTER','grand-valbrune','#f1e6d2'),
 ('boatman','BOATMAN','villa-ceresa','#f1e6d2'),
]
CREST_H=36.0   # mm, crest height
GAP=3.0        # mm, crest to title
MAX_W=100.0    # mm, widest the art may run on a 5-panel foam front

def outline(s,size,cx,base):
    gs=anton.getGlyphSet(); cmap=anton.getBestCmap(); upm=anton['head'].unitsPerEm; hm=anton['hmtx']; sc=size/upm
    names=[cmap[ord(c)] for c in s]; w=sum(hm[n][0] for n in names)*sc
    x=cx-w/2; d=''; bp=BoundsPen(gs)
    for n in names:
        t=(sc,0,0,-sc,x,base); pen=SVGPathPen(gs); gs[n].draw(TransformPen(pen,t)); gs[n].draw(TransformPen(bp,t)); d+=pen.getCommands(); x+=hm[n][0]*sc
    return d,bp.bounds

for cid,title,crest,ink in CAPS:
    src=open(f'{CRESTS}/{crest}.svg').read()
    vw,vh=map(float,re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',src).group(1,2))
    path=re.search(r'<path[^>]*\sd="([^"]+)"',src).group(1)
    s=CREST_H/vh; cw=vw*s
    size=(18.0 if ' ' not in title else 14.4)            # same ratio as the approved draft (150px / 120px under a 300px crest)
    _,b=outline(title,size,0,0); cap_h=-b[1]; tw=b[2]-b[0]
    W=max(cw,tw); H=CREST_H+GAP+cap_h
    k=min(1.0,MAX_W/W); W*=k; H*=k                        # two-word titles are scaled down to fit
    d,_=outline(title,size,W/(2*k),CREST_H+GAP+cap_h)
    body=(f'<g transform="scale({k:.4f})">'
          f'<path fill-rule="evenodd" transform="translate({(W/k-cw)/2:.3f} 0) scale({s:.6f})" d="{path}"/>'
          f'<path d="{d}"/></g>')
    svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.1f}mm" height="{H:.1f}mm" viewBox="0 0 {W:.3f} {H:.3f}">'
         f'<g fill="{ink}">{body}</g></svg>')
    open(f'{OUT}/{cid}-front.svg','w').write(svg)
    cairosvg.svg2png(bytestring=svg.encode(),write_to=f'{OUT}/{cid}-front-300dpi.png',dpi=300)
    print(cid,f'{W:.1f} x {H:.1f} mm')
