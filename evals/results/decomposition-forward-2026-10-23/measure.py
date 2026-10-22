from pathlib import Path
import json,re,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
source=Path(sys.argv[2]) if len(sys.argv)>2 else root/'browser-observations.json'
rows=[]
def rgb(s):
 m=re.fullmatch(r'rgb\((\d+), (\d+), (\d+)\)',s)
 return '#'+''.join(f'{int(v):02X}' for v in m.groups()) if m else s
def cls(e,c):return c in e.get('classes','').split()
for d in json.loads(source.read_text()):
 n=d['normal'];named={x['id']:x for x in n['named']};geometry=[];colors=[];relations=[]
 def metric(label,actual,expected,tolerance):geometry.append({'label':label,'actual':actual,'expected':expected,'tolerance':tolerance,'delta':abs(actual-expected),'pass':abs(actual-expected)<=tolerance})
 def color(label,actual,expected):colors.append({'label':label,'actual':rgb(actual),'expected':expected,'pass':rgb(actual)==expected})
 def role(c):return [e for e in n['all'] if cls(e,c)]
 color('canvas',n['body']['background'],'#FFFFFF')
 if d['case']=='form':
  for i,(field,y) in enumerate(zip(n['inputs'],[70,181,267,353,439])):
   for dimension,expected,tolerance in [('width',464,2),('height',40,2),('y',y,4)]:metric(f'field{i+1}.{dimension}',field['parent'][dimension],expected,tolerance)
   color(f'field{i+1}.border',field['parent']['borderColor'],'#E9EBED')
  color('heading',named['E-heading']['color'],'#36383A')
  for e in n['texts']:
   if e['text'] in ['고객사명','사업자번호','담당자명','e-mail','연락처']:color(e['text'],e['color'],'#515359')
   if e['text'] in ['예) 토스페이먼츠','담당자 연락처 또는 회사 대표 번호를 입력해 주세요.']:color(e['text'],e['color'],'#72777D')
  for i,e in enumerate(role('required-dot')):color(f'required{i+1}',e['background'],'#EF3846')
  if 'markers' not in n:n['markers']=[{'dot':dot,'label':label} for dot,label in zip(role('required-dot'),role('field-label'))]
  if 'markers' in n:
   relations=[{'label':f'required{i+1}.top-alignment','actual_delta':e['dot']['y']-e['label']['y'],'expected_delta':0,'pass':abs(e['dot']['y']-e['label']['y'])<=0.05} for i,e in enumerate(n['markers'])]
  content_ok=([i['label'] for i in n['inputs']]==['고객사명','사업자번호','담당자명','e-mail','연락처'] and [i['required'] for i in n['inputs']]==[True,True,True,True,False] and [i['type'] for i in n['inputs']]==['text','text','text','email','tel'])
 else:
  for eid in ['E-card1','E-card2','E-add']:
   e=named[eid]
   for dimension,expected,tolerance in [('width',(1193-90-2*18.125)/3,2),('height',203.125,4),('y',106.875,2)]:metric(f'{eid}.{dimension}',e[dimension],expected,tolerance)
   color(eid+'.surface',e['background'],'#F5F5F8')
  metric('equal-width-range',max(named[e]['width'] for e in ['E-card1','E-card2','E-add'])-min(named[e]['width'] for e in ['E-card1','E-card2','E-add']),0,2)
  metric('equal-top-range',max(named[e]['y'] for e in ['E-card1','E-card2','E-add'])-min(named[e]['y'] for e in ['E-card1','E-card2','E-add']),0,2)
  metric('panel-padding',named['E-grid']['x'],45,4);metric('grid-top',named['E-grid']['y'],106.875,4)
  metric('import-width',named['E-import']['width'],181.25,4);metric('import-height',named['E-import']['height'],43.75,4)
  color('heading',named['E-heading']['color'],'#111112');color('import',named['E-import']['color'],'#111112')
  for e in n['texts']:
   if e['text'].startswith('유아이볼이력서_'):color('card-title',e['color'],'#111112')
   if e['text'] in ['기술스택','학력','경력/프로젝트','공개','비공개']:color(e['text'],e['color'],'#444445')
   if e['text']=='2026.06.02 등록':color('date',e['color'],'#A2A2A2')
   if e['text']=='새로운 이력서를 추가해보세요!':color('add-label',e['color'],'#444445')
  for i,e in enumerate(role('status-dot')):color(f'status-dot{i+1}',e['background'],'#02DD6D' if i<3 else '#FE5467')
  for filename,expected,count in [('EllipsisVertical.svg','#A2A2A2',2),('CircleHelp.svg','#C7CFC9',2)]:
   if not all('maskImage' in e for e in n['all']):
    colors.append({'label':filename,'actual':None,'expected':expected,'pass':None,'status':'not-collected-by-first-harness; see manual code/visual review'});continue
   icons=[e for e in n['all'] if filename in e.get('maskImage','')]
   colors.append({'label':filename+'.count','actual':len(icons),'expected':count,'pass':len(icons)==count})
   for e in icons:color(filename,e['color'],expected)
  for i,e in enumerate(n['inputs']):color('toggle'+str(i),e['background'] if rgb(e['background'])!='rgba(0, 0, 0, 0)' else e['parent']['background'],'#02DD6D' if i==0 else '#E2E4E3')
  if 'statusItems' not in n:
   n['statusItems']=[]
   for item,dot in zip(role('status-item'),role('status-dot')):
    labels=[e for e in n['all'] if e['tag']=='SPAN' and e['text']==item['text'] and item['x']<=e['x']<=item['x']+item['width'] and abs(e['y']-item['y'])<1]
    if labels:n['statusItems'].append({'dot':dot,'label':labels[0]})
  if 'statusItems' in n:
   relations=[{'label':f'status{i+1}.label-then-dot','actual_gap':e['dot']['x']-e['label']['x']-e['label']['width'],'expected_gap':6,'pass':abs(e['dot']['x']-e['label']['x']-e['label']['width']-6)<=0.05} for i,e in enumerate(n['statusItems'])]
  content_ok=([i['type'] for i in n['inputs']]==['checkbox','checkbox'] and [i['checked'] for i in n['inputs']]==[True,False] and all(text in n['body']['text'] for text in ['이력서 관리','사람인 이력서 가져오기','유아이볼이력서_1차','유아이볼이력서_2차','새로운 이력서를 추가해보세요!']) and n['body']['text'].count('2026.06.02 등록')==2)
 stress=[]
 for phase in ['normal','narrow','enlarged']:
  e=d[phase];stress.append({'phase':phase,'horizontal_overflow':e['scrollWidth']>e['clientWidth'],'min_reading_font_px':min(float(t['fontSize'][:-2]) for t in e['texts']),'min_reading_weight':min(int(t['fontWeight']) for t in e['texts'])})
 result={'variant':d['variant'],'case':d['case'],'geometry':geometry,'color_roles':colors,'supplemental_v3_relations':relations,'supplemental_v4_emphasis':None if d['case']=='form' else {'font_size':named['E-import']['fontSize'],'weight':named['E-import']['fontWeight'],'pass':named['E-import']['fontSize']=='16px' and named['E-import']['fontWeight']=='700'},'required_content_and_native_states':content_ok,'stress':stress,'runtime_errors':d['errors'],'blocked_external_requests':d['blockedRequests'],'scripts':n['scriptCount'],'all_img_assets_loaded':all(e['loaded'] for e in n['images']),'scope':'Frozen normal geometry; supplemental role/order checks follow preserved first-render discoveries. Manual whole-image review remains separate.'}
 rows.append(result)
(root/'measurements.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'variant':r['variant'],'case':r['case'],'geometry_pass':sum(x['pass'] for x in r['geometry']),'geometry_total':len(r['geometry']),'color_failures':[x for x in r['color_roles'] if x['pass'] is False],'relation_failures':[x for x in r['supplemental_v3_relations'] if x['pass'] is False],'content_and_states':r['required_content_and_native_states']} for r in rows],ensure_ascii=False,indent=2))
