"""Generate the GitHub social-preview card (1280x640) from the Atlas screenshot.

Usage: python3 docs/assets/social/make_card.py ["subtitle"] [out.png]
Spec: docs/v2/V2_GO_LIVE_POLISH_PLAN.md §10.4. Requires Pillow and the macOS system fonts named below
(swap the font paths on other platforms). The PNG is uploaded by hand in GitHub → Settings → Social preview.
"""
from PIL import Image, ImageDraw, ImageFont
import sys
W,H = 1280,640
PAPER=(0xf4,0xef,0xe3); INK=(0x14,0x12,0x0e); OCHRE=(0xa8,0x84,0x2c); LINE=(0xd8,0xd0,0xbd); SOFT=(0x6f,0x6a,0x5e)
subtitle = sys.argv[1] if len(sys.argv)>1 else "An ontology layer for product teams building products that solve real problems — with AI agents that remember."
out = sys.argv[2] if len(sys.argv)>2 else "social-preview.png"
img = Image.new("RGB",(W,H),PAPER); d = ImageDraw.Draw(img)
serif = lambda sz: ImageFont.truetype("/System/Library/Fonts/Supplemental/Charter.ttc", sz)
grot  = lambda sz: ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", sz)
mono  = lambda sz: ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", sz)
M=80  # safe margin
# kicker
d.text((M, M), "THE SOURCE-OF-TRUTH REVIEW  ·  PRD-LED CONTEXT ENGINEERING", font=grot(15), fill=SOFT, spacing=2)
d.line((M, M+30, M+560, M+30), fill=INK, width=2)
# tagline (hero)
d.text((M-3, M+62), "Memory as", font=serif(86), fill=INK)
d.text((M-3, M+150), "Infrastructure", font=serif(86), fill=INK)
d.line((M, M+262, M+160, M+262), fill=OCHRE, width=4)
# subtitle wrapped to ~560px
def wrap(text, font, width):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t, font=font) <= width: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
y=M+290
for ln in wrap(subtitle, grot(24), 560):
    d.text((M, y), ln, font=grot(24), fill=INK); y+=34
# ID chips row
x=M; y2=H-M-22
for cid in ["BR-001","UJ-002","API-003","TEST-004","CFD-005"]:
    f=mono(15); tw=d.textlength(cid,font=f)
    d.text((x,y2), cid, font=f, fill=INK); d.line((x, y2+20, x+tw, y2+20), fill=OCHRE, width=2); x+=tw+22
# atlas crop on the right third, bled off the right edge
atlas = Image.open("docs/assets/sot-html/atlas.png").convert("RGB")
aw,ah = atlas.size
crop = atlas.crop((0, int(ah*0.18), int(aw*0.62), int(ah*0.18)+int(aw*0.62*0.72)))  # a table-heavy region
target_w = 520; scale=target_w/crop.size[0]; crop = crop.resize((target_w, int(crop.size[1]*scale)), Image.LANCZOS)
x0 = W-target_w+40; y0 = 110
# hairline frame + paper shadow-free
img.paste(crop,(x0,y0))
d.rectangle((x0-1,y0-1,x0+target_w,y0+crop.size[1]), outline=LINE, width=2)
img.save(out, optimize=True)
print("wrote", out, img.size)
