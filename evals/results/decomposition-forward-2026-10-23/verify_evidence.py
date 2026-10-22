from pathlib import Path
import hashlib,json,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
results=[]
for manifest,prefix in [('input-freeze.json','v1'),('input-freeze-v2.json','v2'),('input-freeze-v3.json','v3'),('implementation-freeze.json','first'),('implementation-freeze-v3.json','v3'),('input-freeze-v4.json',''),('implementation-freeze-v4.json','')]:
 data=json.loads((root/manifest).read_text());count=0
 for entry in data['files']:
  relative=Path(entry['path'])
  if relative.is_absolute() or not (root/relative).resolve().is_relative_to(root):raise ValueError('Invalid frozen path')
  archived=root/prefix/relative if prefix else root/relative
  candidate=archived if archived.exists() else root/relative
  if sha(candidate)!=entry['sha256']:raise ValueError(f'{manifest}: changed {relative}')
  count+=1
 if 'acceptance_plan_sha256' in data and data['acceptance_plan_sha256']!=sha(root/'plan.json'):raise ValueError('Frozen acceptance plan changed')
 results.append({'manifest':manifest,'verified':count,'archive_prefix':prefix,'unchanged_assets_and_shared_tasks':'current exact hash fallback when not separately archived'})
if (root/'artifact-manifest.json').exists():
 files=json.loads((root/'artifact-manifest.json').read_text())['files']
 for entry in files:
  path=(root/entry['path']).resolve()
  if not path.is_relative_to(root) or sha(path)!=entry['sha256']:raise ValueError(f"Changed artifact {entry['path']}")
 results.append({'artifact_manifest_verified':len(files)})
print(json.dumps({'status':'verified','scope':'Snapshot bytes and frozen acceptance plan only; not model comprehension or appearance','results':results},indent=2))
