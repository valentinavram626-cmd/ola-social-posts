import sys,textwrap
from PIL import Image,ImageDraw,ImageFont
txt,out=sys.argv[1],sys.argv[2]
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',62)
lines=textwrap.wrap(txt,22)
im=Image.new('RGBA',(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
lh=80;h=len(lines)*lh+60;y0=300
d.rounded_rectangle((70,y0,1010,y0+h),28,fill=(11,19,36,235),outline=(214,169,73,255),width=5)
for i,l in enumerate(lines):
  w=d.textlength(l,font=f);d.text(((1080-w)/2,y0+30+i*lh),l,font=f,fill=(243,238,227,255))
lion=Image.open('../posts/lion_t.png').convert('RGBA');lion.thumbnail((150,150))
im.alpha_composite(lion,(40,70))
im.save(out)
