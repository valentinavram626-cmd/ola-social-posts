const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const D=__dirname, FPS=30;
const cfg=JSON.parse(fs.readFileSync(path.join(D,process.argv[2]),'utf8'));
const html=fs.readFileSync(path.join(D,'house.html'),'utf8').replace('__CFG__',JSON.stringify(cfg));
const built=path.join(D,'built-'+path.basename(process.argv[2],'.json')+'.html');
fs.writeFileSync(built,html);
(async()=>{
  const b=await chromium.launch();
  const pg=await b.newPage({viewport:{width:1080,height:1920}});
  pg.on('pageerror',e=>console.error('PAGEERR',e.message));
  pg.on('console',m=>{if(m.type()==='error')console.error('CONSOLE',m.text())});
  await pg.goto('file://'+built); await pg.evaluate(()=>window.ready); await pg.waitForTimeout(500);
  const out=path.join(D,cfg.outdir); fs.rmSync(out,{recursive:true,force:true}); fs.mkdirSync(out,{recursive:true});
  const N=Math.ceil(cfg.total*FPS);
  const alpha = cfg.mode==='textonly';
  for(let f=0;f<N;f++){ await pg.evaluate(t=>window.seek(t),f/FPS);
    await pg.screenshot(alpha
      ? {path:path.join(out,`f${String(f).padStart(5,'0')}.png`),type:'png',omitBackground:true}
      : {path:path.join(out,`f${String(f).padStart(5,'0')}.jpg`),type:'jpeg',quality:93}); }
  console.log('frames',N); await b.close();
})();
