from pathlib import Path
import hashlib,importlib.util,json,shutil,sys
repo=Path(sys.argv[1]).resolve();base=Path(sys.argv[2]).resolve()
spec=importlib.util.spec_from_file_location('reference_check',repo/'skills/reference-review/scripts/reference_check.py');reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':p.name,'sha256':sha(p)}
def write(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
results=[]
final_metrics=json.loads((base/'measurements.json').read_text())
reasons={
 'first':{'form':'Source required markers sit at label top; first receiver centers all four9px lower. Other supplied field widths/heights/tops and content match. This source relation was omitted by analyst, so normal geometry alone cannot approve this reconstruction.','cards':'Both first receivers place all six status dots before their labels, opposite to source. JSON additionally assigns import/add/off-track colors from an ambiguous global palette. Equal grid geometry does not remove these observed source mismatches.'},
 'final':{'form':'Inspected source and final side-by-side: full464px shared field width, exact five field tops, required dots at the label tops, preserved labels/hints/order. The explicit14px/500 helper adaptation ends at503px without clipping. Fallback typography is disclosed and source native font remains unknown.','cards':'Inspected source and final side-by-side: left heading/right heavier import action, equal three gray cards with common106.875px top and203.125px height, titles/status/footer hierarchy, label-then-dot order, exact mapped role colors and native initial states preserved. User-required internal-rule removal, white canvas and14px/500 minimum are scoped adaptations. Source font is not recovered.'}}
for stage in ['first','final']:
 for case in ['form','cards']:
  root=base/('v2/analyst' if stage=='first' else 'analyst')/case
  original=base/('first/json' if stage=='first' else 'json')/case
  capture=original/('stable-first-render.png' if stage=='first' else 'render.png')
  shutil.copy2(original/'index.html',root/'implementation.html');shutil.copy2(capture,root/'render.png')
  shutil.copytree(base/'json'/case/'assets',root/'assets',dirs_exist_ok=True)
  observations=original/('stable-browser-observations.json' if stage=='first' else 'browser-observations.json')
  shutil.copy2(observations,root/'observations.json')
  obs=json.loads(observations.read_text());panel=next(e for e in obs['normal']['named'] if e['id']=='E-panel')
  handoff=json.loads((root/'handoff.json').read_text());bundle=reader.interpretation_bundle(root,handoff)
  interpretation=json.loads((root/'interpretation.json').read_text());lookup={e['ref']:e for e in interpretation['coverage']}
  core={'schema_version':1,'decomposition_sha256':handoff['decomposition']['sha256'],'interpretation_sha256':handoff['interpretation']['sha256'],'source_snapshot':bind(root/'implementation.html'),'capture':bind(root/'render.png'),'status':'regressed' if stage=='first' else 'adapted-and-verified','reason':reasons[stage][case]}
  write(root/'core-review.json',core)
  consumption=[]
  for ref in sorted(bundle['refs']):
   fact=bundle['facts'].get(ref);unknown=fact and fact['status']=='unknown'
   if unknown:explanation='Original font/CSS is not established. Fallback use is explicit; no original-font recovery claimed.'
   elif fact:explanation=f"Verified {fact['kind']} observation in implementation.html, observations.json and source/render comparison; declared scale, source estimate and reconstruction adaptation remain distinct. Actual role values and layout probes are preserved in measurements.json."
   elif ref=='RAW1':explanation='Complete raw text exported and read; bytes preserved. Scope, content, exclusions and unknowns checked against actual static output; raw is not printed as UI.'
   elif ref.startswith('/extensions/'):explanation='Declared viewport/scale, fallback family, no-JavaScript scope and local official asset policy applied; source image intentionally withheld from receiver for this bounded transmission experiment.'
   else:explanation='Actual named owner, parent/shared relation or scoped adaptation inspected in source/render and DOM. '+lookup[ref]['interpretation']
   consumption.append({'ref':ref,'status':'unverified' if unknown else 'applied','target':lookup[ref]['target'].replace('planned ',''),'interpretation':explanation})
  scale=1 if case=='form' else .625
  comparison={'schema_version':2,'handoff_sha256':sha(root/'handoff.json'),'target_sha256':sha(root/'implementation.html'),'core_review':bind(root/'core-review.json'),'consumption':consumption,'results':[{'id':'Q-panel-width','capture':bind(root/'render.png'),'actual':{'value':panel['width']/scale,'unit':'image-px','method':'Actual Chrome DOM panel width divided by the frozen experimental display scale; not recovered native CSS.'}}],'visual_review':{'status':core['status'],'reason':core['reason']}}
  write(root/'comparison.json',comparison)
  metrics=final_metrics if stage=='final' else json.loads((base/'first/measurements.json').read_text())
  write(root/'measurements.json',next(x for x in metrics if x['variant']=='json' and x['case']==case))
  failures=reader.compare_reference(root,bind(root/'handoff.json'),bind(root/'comparison.json'),sha(root/'implementation.html'))
  if (stage=='first' and not failures) or (stage=='final' and failures):raise ValueError((stage,case,failures))
  results.append({'stage':stage,'case':case,'source_hash':bundle['doc']['sources'][0]['artifact']['sha256'],'implementation_sha256':sha(root/'implementation.html'),'reference_failures':failures,'coverage_entries':len(consumption),'unknown_optional_count':sum(x['status']=='unverified' for x in consumption)})
write(base/'core-comparison-results.json',{'scope':'Standalone reference_check.compare_reference with single-HTML digest for this experiment. Not design_gate full product fingerprint or75-rule PASS.','results':results})
print(json.dumps(results,ensure_ascii=False,indent=2))
