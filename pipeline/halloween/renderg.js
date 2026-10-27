const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const D=__dirname, FPS=30;
const cfg=JSON.parse(fs.readFileSync(path.join(D,process.argv[2]),'utf8'));
let html=fs.readFileSync(path.join(D,'hwg.html'),'utf8')
  .replace('__TOTAL__',JSON.stringify(cfg.total))
  .replace('__BEATS__',JSON.stringify(cfg.beats))
  .replace('__END__',JSON.stringify(cfg.end));
const built=path.join(D,'hwg.built.html'); fs.writeFileSync(built,html);
(async()=>{
  const b=await chromium.launch();
  const pg=await b.newPage({viewport:{width:1080,height:1920}});
  pg.on('pageerror',e=>console.error('PAGEERR',e.message));
  await pg.goto('file://'+built); await pg.evaluate(()=>window.ready); await pg.waitForTimeout(500);
  const out=path.join(D,cfg.outdir); fs.rmSync(out,{recursive:true,force:true}); fs.mkdirSync(out,{recursive:true});
  const N=Math.ceil(cfg.total*FPS);
  for(let f=0;f<N;f++){ await pg.evaluate(t=>window.seek(t),f/FPS);
    await pg.screenshot({path:path.join(out,`f${String(f).padStart(5,'0')}.jpg`),type:'jpeg',quality:94}); }
  console.log('frames',N); await b.close();
})();
