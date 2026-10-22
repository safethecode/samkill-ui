/** @type {typeof import('playwright')} */
const playwright = await import(process.env.SAMKILL_PLAYWRIGHT_MODULE || 'playwright');
const { chromium } = playwright;
import { createServer } from 'node:http';
import { readFile, writeFile, stat } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
const root=resolve(process.argv[2] || '.');
const server=createServer(async(req,res)=>{try{const path=resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(path!==root&&!path.startsWith(root+sep))throw new Error('outside');const data=await readFile(path);res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.svg':'image/svg+xml','.css':'text/css','.png':'image/png','.json':'application/json'})[extname(path)]||'text/plain');res.end(data);}catch{res.statusCode=404;res.end('not found');}});
await new Promise(resolve=>server.listen(0,'127.0.0.1',()=>resolve(null)));const address=server.address();if(!(address instanceof Object)||!Number.isInteger(address.port)||address.port<1||address.port>65535)throw new Error('Expected a bound TCP port');const port=address.port;
const browser=await chromium.launch({channel:'chrome',headless:true});
const outputs=[];
try{
for(const variant of ['text','json'])for(const name of ['form','cards']){
 const folder=resolve(root,variant,name);try{await stat(resolve(folder,'index.html'));}catch{continue;}
 const size=name==='form'?{width:464,height:501}:{width:1193,height:355};
 const page=await browser.newPage({viewport:size,deviceScaleFactor:1});const errors=[];const blockedRequests=[];page.on('pageerror',error=>errors.push(error.message));await page.route('**/*',route=>{const url=new URL(route.request().url());if(url.hostname==='127.0.0.1')return route.continue();blockedRequests.push(url.origin);return route.abort();});
 const settle=()=>page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(()=>resolve(null)))));
 await page.goto(`http://127.0.0.1:${port}/${variant}/${name}/index.html`);await page.evaluate(()=>document.fonts.ready);await settle();
 await page.screenshot({path:resolve(folder,'render.png'),fullPage:true});
 const inspect=()=>page.evaluate(()=>{
  const box=e=>{const r=e.getBoundingClientRect();const c=getComputedStyle(e);return {x:r.x,y:r.y,width:r.width,height:r.height,fontSize:c.fontSize,fontWeight:c.fontWeight,lineHeight:c.lineHeight,color:c.color,background:c.backgroundColor,borderColor:c.borderColor,maskImage:c.maskImage,filter:c.filter,display:c.display,position:c.position,text:e.textContent.trim().replace(/\s+/g,' ')};};
  const named=[...document.querySelectorAll('[data-eid]')].map(e=>({id:e.getAttribute('data-eid'),...box(e)}));
  const inputs=[...document.querySelectorAll('input')].map(e=>({type:e.type,checked:e.checked,required:e.required,label:e.labels?.[0]?.textContent.trim()||'',parent:box(e.parentElement),...box(e)}));
  const all=[...document.querySelectorAll('body *')].map(e=>({tag:e.tagName,classes:e.className,...box(e)}));
  const texts=[...document.querySelectorAll('body *')].filter(e=>[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim())).map(box);
  const markers=[...document.querySelectorAll('.required-dot')].map(e=>({dot:box(e),label:box(e.parentElement)}));
  const statusItems=[...document.querySelectorAll('.status-item')].map(e=>({item:box(e),dot:box(e.querySelector('.status-dot')),label:box(e.querySelector('span:not(.status-dot)'))}));
  return {named,inputs,texts,all,markers,statusItems,body:box(document.body),scrollWidth:document.documentElement.scrollWidth,clientWidth:innerWidth,images:[...document.images].map(e=>({src:e.getAttribute('src'),loaded:e.complete&&e.naturalWidth>0})),scriptCount:document.scripts.length};
 });
 const normal=await inspect();let focus=null;const nativeKeyboard=[];
 await page.keyboard.press('Tab');nativeKeyboard.push(await page.evaluate(()=>({step:'first Tab',tag:document.activeElement.tagName,id:document.activeElement.id,text:document.activeElement.getAttribute('aria-label')||document.activeElement.textContent.trim()})));
 if(name==='cards'){for(const checkbox of await page.locator('input[type=checkbox]').all()){await checkbox.focus();const before=await checkbox.isChecked();await page.keyboard.press('Space');const after=await checkbox.isChecked();await page.keyboard.press('Space');nativeKeyboard.push({step:'native toggle Space and reset',before,after,reset:await checkbox.isChecked()});}}
 if(name==='form'){
  for(const input of await page.locator('input:not([type=checkbox])').all())await input.fill('테스트 입력');
  await page.locator('input').first().focus();await page.waitForFunction(()=>getComputedStyle(document.activeElement.parentElement).boxShadow.endsWith(' 2px inset'));focus=await page.evaluate(()=>({active:document.activeElement.tagName,fieldShadow:getComputedStyle(document.activeElement.parentElement).boxShadow,inputShadow:getComputedStyle(document.activeElement).boxShadow}));
 }
 await page.setViewportSize({width:390,height:size.height});await settle();const narrow=await inspect();await page.screenshot({path:resolve(folder,'narrow-render.png'),fullPage:true});
 await page.setViewportSize(size);await page.evaluate(()=>{const items=[...document.querySelectorAll('body *')].map(element=>({element,size:parseFloat(getComputedStyle(element).fontSize)}));for(const {element,size} of items)if(element instanceof HTMLElement)element.style.setProperty('font-size',`${size*2}px`,'important');});await settle();const enlarged=await inspect();await page.screenshot({path:resolve(folder,'enlarged-render.png'),fullPage:true});
 const result={variant,case:name,viewport:size,normal:{...normal,focus,nativeKeyboard},narrow,enlarged,errors,blockedRequests};await writeFile(resolve(folder,'browser-observations.json'),JSON.stringify(result,null,2));outputs.push(result);await page.close();
}
await writeFile(resolve(root,'browser-observations.json'),JSON.stringify(outputs,null,2));console.log(JSON.stringify(outputs.map(x=>({variant:x.variant,case:x.case,named:x.normal.named.length,inputs:x.normal.inputs.length,overflowNormal:x.normal.scrollWidth>x.normal.clientWidth,overflowNarrow:x.narrow.scrollWidth>x.narrow.clientWidth,errors:x.errors})),null,2));
}finally{await browser.close();server.close();}
