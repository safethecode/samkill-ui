from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
font=ImageFont.load_default(size=17)
def make(case,iteration=False):
 source=Image.open(root/'analyst'/case/'source.png').convert('RGB')
 if case=='cards':source=source.resize((1193,355),Image.Resampling.LANCZOS)
 if iteration:
  entries=[('Source (declared scale; native CSS unknown)',source),('JSON first: omissions preserved',Image.open(root/'first/json'/case/'first-render.png').convert('RGB')),('JSON corrected: v3 handoff',Image.open(root/'json'/case/'render.png').convert('RGB'))]
 else:
  entries=[('Source (declared scale; native CSS unknown)',source),('Prose receiver: corrected',Image.open(root/'text'/case/'render.png').convert('RGB')),('JSON/raw receiver: corrected',Image.open(root/'json'/case/'render.png').convert('RGB'))]
 pad=16;caption=42
 if case=='form':
  w=sum(im.width for _,im in entries)+pad*(len(entries)+1);h=max(im.height for _,im in entries)+caption+pad*2
  board=Image.new('RGB',(w,h),'#EEEEEE');draw=ImageDraw.Draw(board);x=pad
  for label,im in entries:draw.text((x,pad),label,fill='#111111',font=font);board.paste(im,(x,pad+caption));x+=im.width+pad
 else:
  w=max(im.width for _,im in entries)+pad*2;h=sum(im.height+caption for _,im in entries)+pad*(len(entries)+1)
  board=Image.new('RGB',(w,h),'#EEEEEE');draw=ImageDraw.Draw(board);y=pad
  for label,im in entries:draw.text((pad,y),label,fill='#111111',font=font);board.paste(im,(pad,y+caption));y+=im.height+caption+pad
 board.save(root/(('iteration-' if iteration else 'comparison-')+case+'.png'))
for name in ['form','cards']:
 make(name);make(name,True)
print('Created same-scale comparison and before/after boards.')
