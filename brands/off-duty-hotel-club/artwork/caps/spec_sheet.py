# Factory spec sheet (one page per cap) from print/<cap>-front-300dpi.png. usage: python3 spec_sheet.py <fonts dir>
import sys
from PIL import Image,ImageDraw,ImageFont
F=sys.argv[1]
def font(n,s): return ImageFont.truetype(f'{F}/{n}',s)
SHEETS=[
 ('lifeguard','LIFEGUARD · Hôtel Solvane','#b8261c',[
  'Cap: 5-panel high-profile trucker, thick foam front, polyester mesh back, curved peak, plastic snapback',
  'Colour: rescue red front, mesh, peak, snap and sweatband trim. Please propose your nearest stock red to the swatch shown',
  'Print: 1-colour screen print, opaque white (high-opacity plastisol)',
  'Artwork size: 68.0 mm wide x 54.6 mm high. File: lifeguard-front.svg (all text outlined)',
  'Position: centred on the front seam, top of crest 12 mm below the crown edge',
  'Sweatband: cotton twill. Woven care label inside. One size']),
 ('security','SECURITY · The Oriole Palace','#2b2a28',[
  'Cap: 5-panel high-profile trucker, thick foam front, polyester mesh back, curved peak, plastic snapback',
  'Colour: washed black front, mesh, peak, snap and sweatband trim. Please propose your nearest stock washed black',
  'Print: 1-colour screen print, gold. Please propose your nearest Pantone gold to the swatch shown, and quote a metallic gold too',
  'Artwork size: 60.1 mm wide x 54.6 mm high. File: security-front.svg (all text outlined)',
  'Position: centred on the front seam, top of crest 12 mm below the crown edge',
  'Sweatband: cotton twill. Woven care label inside. One size']),
]
for cid,name,bg,lines in SHEETS:
    W,H=2480,1754
    im=Image.new('RGB',(W,H),'#f5f2ea'); d=ImageDraw.Draw(im)
    d.text((120,100),'OFF DUTY HOTEL CLUB · HAT CHECK · SAMPLE SPEC',font=font('Oswald.ttf',44),fill='#1c1812')
    d.text((120,170),name,font=font('Anton-Regular.ttf',110),fill='#1c1812')
    panel=Image.new('RGB',(1000,900),bg.strip())
    art=Image.open(f'print/{cid}-front-300dpi.png').convert('RGBA'); art.thumbnail((760,760))
    panel.paste(art,((1000-art.width)//2,(900-art.height)//2),art)
    im.paste(panel,(120,360))
    y=380
    for l in lines:
        words=l.split(' '); line=''
        for w in words:
            t=(line+' '+w).strip()
            if d.textlength(t,font=font('DMSans.ttf',40))>1180: d.text((1200,y),line,font=font('DMSans.ttf',40),fill='#1c1812'); y+=56; line=w
            else: line=t
        d.text((1200,y),line,font=font('DMSans.ttf',40),fill='#1c1812'); y+=90
    d.text((120,1320),'Colours on screen are a guide only. Please send a photo of the blank in our colours before printing.',font=font('DMSans.ttf',36),fill='#5a5246')
    d.text((120,1380),'Contact: Alex Cheeseman, hello@offdutyhotel.club',font=font('DMSans.ttf',36),fill='#5a5246')
    im.save(f'print/{cid}-spec-sheet.pdf',resolution=300); im.save(f'print/{cid}-spec-sheet.jpg',quality=88)
