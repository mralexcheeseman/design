# Builds the back-print SVGs (Security, Ski Patrol, Gardener). Crests: ../crests/crests.py
import math,sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.varLib.instancer import instantiateVariableFont
F=(sys.argv[2] if len(sys.argv)>2 else 'fonts')+'/'  # Anton, Oswald, Cormorant Garamond from github.com/google/fonts (OFL)
# usage: python3 make_art.py <output dir> <fonts dir>
OUT=sys.argv[1]
def load(name,wght=None):
    f=TTFont(F+name)
    if wght: f=instantiateVariableFont(f,{'wght':wght})
    return f
anton=load('Anton-Regular.ttf'); oswald=load('Oswald[wght].ttf',500); corm=load('CormorantGaramond[wght].ttf',600)
def text(font,s,size,cx,y,track=0):
    """Outlined text centred at cx, baseline y (mm units). track in em."""
    gs=font.getGlyphSet(); cmap=font.getBestCmap(); upm=font['head'].unitsPerEm; hm=font['hmtx']
    sc=size/upm; names=[cmap[ord(c)] for c in s]
    adv=[hm[n][0]*sc+track*size for n in names]; w=sum(adv)-track*size
    x=cx-w/2; d=''; bp=BoundsPen(gs)
    for n,a in zip(names,adv):
        pen=SVGPathPen(gs); tp=TransformPen(pen,(sc,0,0,-sc,x,y)); gs[n].draw(tp); d+=pen.getCommands()
        gs[n].draw(TransformPen(bp,(sc,0,0,-sc,x,y))); x+=a
    text.bounds=bp.bounds
    return f'<path d="{d}"/>',w
def svg(w,h,body,col):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><g fill="{col}" fill-rule="nonzero">{body}</g></svg>'

def back(title,hotel,city,col,fname,hotel_col=None,stack=False):
    # hotel_col: a second, quieter ink for the hotel and city lines (two-ink back).
    # stack: one word per line, widest line 240 mm (long two-word titles).
    lines=title.split() if stack else [title]
    tw=max(text(anton,l,1,0,0)[1] for l in lines)   # measure at size 1
    size=(240 if stack else 280)/tw                  # title 280 mm wide, or 240 stacked
    text(anton,lines[0],size,150,0); top,bot=text.bounds[1],text.bounds[3]
    cap=bot-top; base=5-top; p1=''
    for i,l in enumerate(lines):
        p1+=text(anton,l,size,150,base+i*cap*1.1)[0]
    base+=(len(lines)-1)*cap*1.1
    W,H=300,(round(base+45) if stack else 120)
    p2,_=text(oswald,hotel,14,W/2,base+26,track=0.18)
    p3,_=text(oswald,city,8.5,W/2,base+40,track=0.35)
    body=p1+p2+p3 if not hotel_col else p1+f'<g fill="{hotel_col}">{p2+p3}</g>'
    open(f'{OUT}/{fname}-back.svg','w').write(svg(W,H,body,col))

def crest(icon,hotel,city,col,fname):
    W,H=90,62
    _,w1=text(corm,hotel,1,0,0,track=0.06); sz=min(9.5,74/w1)
    p2,w=text(corm,hotel,sz,W/2,46,track=0.06)
    p3,_=text(oswald,city,4.6,W/2,55,track=0.45)
    open(f'{OUT}/{fname}-crest.svg','w').write(svg(W,H,icon+p2+p3,col))

# Oriole Palace: palm inside a round-topped arch (all strokes >= 1.2 mm for print and embroidery)
cx=45
arch=f'<path fill="none" stroke="#F5F2EA" stroke-width="1.5" d="M{cx-11.5} 36 V15 A11.5 11.5 0 0 1 {cx+11.5} 15 V36 Z"/>'
trunk=f'<path d="M{cx-0.4} 35.8 C{cx-0.2} 28 {cx+0.6} 22 {cx-0.3} 15.6 L{cx+1.5} 15.6 C{cx+2.4} 22 {cx+2.2} 28 {cx+2.0} 35.8 Z"/>'
def frond(ang,length,width):
    a=math.radians(ang); x0,y0=cx+0.6,15
    x1,y1=x0+length*math.cos(a),y0-length*math.sin(a)+length*0.28   # tip droops
    nx,ny=math.sin(a),math.cos(a)
    mx,my=x0+(x1-x0)*0.5,y0+(y1-y0)*0.5-length*0.22
    return (f'<path d="M{x0:.2f} {y0:.2f} Q{mx-nx*width:.2f} {my-ny*width:.2f} {x1:.2f} {y1:.2f} '
            f'Q{mx+nx*width*0.25:.2f} {my+ny*width*0.25+1.2:.2f} {x0:.2f} {y0:.2f} Z"/>')
fronds=''.join(frond(a,l,w) for a,l,w in [(200,8.2,2.6),(160,8.6,2.8),(118,6.4,2.4),(62,6.4,2.4),(20,8.6,2.8),(-20,8.2,2.6)])
oriole_icon=arch+trunk+fronds+f'<rect x="{cx-11.5}" y="35.2" width="23" height="1.5"/>'

# Grand Valbrune: two bold peaks, snow line cut out, rule underneath
peaks=(f'<path fill-rule="evenodd" d="M{cx-15} 34 L{cx-5} 17 L{cx-1.5} 23 L{cx+4} 11 L{cx+15} 34 Z '
       f'M{cx+4} 14.4 L{cx+0.6} 21.6 L{cx+2.6} 20.4 L{cx+4} 22.2 L{cx+5.6} 20.2 L{cx+7.6} 21.4 Z '
       f'M{cx-5} 20.2 L{cx-7.6} 24.6 L{cx-6} 23.8 L{cx-4.8} 25 L{cx-3.4} 23.6 Z"/>')
valbrune_icon=peaks+f'<rect x="{cx-19}" y="36" width="38" height="1.5"/>'

back('SECURITY','THE ORIOLE PALACE','LOS ANGELES','#F5F2EA','security')
back('SKI PATROL','GRAND VALBRUNE','ST. MORITZ','#F1E6D2','ski-patrol')
back('GARDENER','VILLA CERESA','LAKE LUGANO','#E1474A','gardener')   # geranium on garden green, one ink
print('done')
