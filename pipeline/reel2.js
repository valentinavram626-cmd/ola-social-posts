// Long-format reel (3 scenes). node reel2.js <id> <seconds> <json> [fps]
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const P=path.resolve(__dirname,'assets');
const posts=JSON.parse(fs.readFileSync(process.argv[4],'utf8'));
const id=process.argv[2], DUR=+process.argv[3]||22, FPS=+process.argv[5]||25;
const p=posts.find(x=>x.id===id); if(!p){console.error('no post',id);process.exit(1)}
const fsrc=x=>'file://'+P+'/fonts/'+x;
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const EN=/^en-/.test(id);
const S1=6, S2=S1+3.4*p.lines.length+0.6, S3=DUR; // scene boundaries
const lines=p.lines.slice(0,3);
const cards=lines.map((l,i)=>`<div class="card" style="animation-delay:${(S1+0.5+i*3.4).toFixed(2)}s,${(S2-0.5).toFixed(2)}s"><div class="num">${i+1}</div><p>${esc(l)}</p></div>`).join('');
const dots=Array.from({length:26},(_,i)=>{const x=(i*37)%100,y=(i*53)%100,s=6+(i*7)%14,d=(i*1.7)%9;return `<i style="left:${x}%;top:${y}%;width:${s}px;height:${s}px;animation-delay:-${d}s;animation-duration:${9+(i%5)*2}s"></i>`}).join('');
const cta=p.cta||(EN?'Want to know exactly where you stand?':'Vrei să știi exact cum stai?');
const wa=p.wa||(EN?'Message us on WhatsApp':'Scrie-ne pe WhatsApp');
const disc=p.disc||(EN?'General information. For your own situation, speak to an accountant.':'Informații generale. Pentru situația ta, vorbește cu un contabil.');
const html=`<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="${fsrc('bricolage-grotesque/700.css')}"><link rel="stylesheet" href="${fsrc('ibm-plex-sans/400.css')}"><link rel="stylesheet" href="${fsrc('ibm-plex-sans/600.css')}">
<style>
:root{--ink:#0B1324;--ink2:#131F3D;--brass:#D6A949;--brass2:#F2CF7A;--cream:#F3EEE3;--muted:#A9B3C7;--line:#24314F}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;background:var(--ink);color:var(--cream);font-family:"IBM Plex Sans";overflow:hidden;position:relative}
.blob{position:absolute;border-radius:50%;opacity:.9;animation:bl 14s ease-in-out infinite alternate}
.b1{width:1100px;height:1100px;left:35%;top:-25%;background:radial-gradient(circle,#243f82 0%,rgba(36,63,130,.5) 35%,transparent 70%)}
.b2{width:1000px;height:1000px;left:-40%;top:50%;background:radial-gradient(circle,#1c316b 0%,rgba(28,49,107,.5) 35%,transparent 70%);animation-duration:17s}
.b3{width:700px;height:700px;left:50%;top:65%;background:radial-gradient(circle,rgba(214,169,73,.32) 0%,rgba(214,169,73,.12) 35%,transparent 70%);animation-duration:11s}
@keyframes bl{from{transform:translate(0,0) scale(1)}to{transform:translate(-120px,90px) scale(1.15)}}
.grid{position:absolute;inset:0;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:90px 90px;opacity:.14;mask-image:radial-gradient(circle at 50% 40%,#000 30%,transparent 80%)}
.dots i{position:absolute;border-radius:50%;background:var(--brass2);opacity:.55;box-shadow:0 0 12px var(--brass);animation:fl linear infinite}
@keyframes fl{from{transform:translateY(0)}to{transform:translateY(-1920px)}}
.ring{position:absolute;left:50%;top:50%;width:1500px;height:1500px;margin:-750px 0 0 -750px;border:2px solid rgba(214,169,73,.18);border-radius:50%;border-top-color:rgba(214,169,73,.6);animation:rot 24s linear infinite}
.ring.r2{width:1150px;height:1150px;margin:-575px 0 0 -575px;animation-duration:18s;animation-direction:reverse;border-top-color:rgba(243,238,227,.35)}
@keyframes rot{to{transform:rotate(360deg)}}
.prog{position:absolute;left:0;top:0;height:14px;width:100%;background:rgba(255,255,255,.08)}
.prog b{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--brass),var(--brass2));animation:pr ${DUR}s linear forwards}
@keyframes pr{to{width:100%}}
header{position:absolute;left:84px;right:84px;top:120px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:20px}
.lion{height:130px;filter:drop-shadow(0 6px 18px rgba(0,0,0,.45))}
.bname{font-family:"Bricolage Grotesque";font-weight:700;font-size:32px;letter-spacing:.04em}
.loc{font-size:22px;color:var(--muted);letter-spacing:.18em;text-transform:uppercase}
footer{position:absolute;left:84px;right:84px;bottom:110px;border-radius:26px;padding:34px 44px;background:linear-gradient(135deg,var(--brass2),var(--brass));color:var(--ink);display:flex;justify-content:space-between;align-items:flex-end;gap:24px;box-shadow:0 20px 60px rgba(214,169,73,.25)}
.wa small{display:block;font-size:22px;letter-spacing:.16em;text-transform:uppercase;font-weight:600}
.wa b{font-family:"Bricolage Grotesque";font-size:60px}
.disc{font-size:20px;max-width:330px;text-align:right;line-height:1.35}
.scene{position:absolute;left:84px;right:84px;top:300px;bottom:330px;animation-fill-mode:both}
/* scene 1: fully visible at t=0, exits at S1 */
.s1{animation:out .6s ease-in both;animation-delay:${S1-0.6}s;display:flex;flex-direction:column;justify-content:center}
@keyframes out{to{opacity:0;transform:translateY(-60px) scale(.96)}}
.tag{display:inline-flex;align-self:flex-start;gap:12px;align-items:center;font-weight:600;font-size:28px;letter-spacing:.2em;text-transform:uppercase;color:var(--brass)}
.tag:before{content:"";width:50px;height:2px;background:var(--brass)}
.figure{margin-top:40px;font-family:"Bricolage Grotesque";font-weight:700;font-size:210px;line-height:.95;color:var(--brass);text-shadow:0 0 60px rgba(214,169,73,.45);animation:glow 2.4s ease-in-out infinite alternate}
@keyframes glow{from{text-shadow:0 0 30px rgba(214,169,73,.3)}to{text-shadow:0 0 90px rgba(242,207,122,.75)}}
.s1 h1{margin-top:40px;font-family:"Bricolage Grotesque";font-weight:700;font-size:84px;line-height:1.05}
.ul{height:8px;width:0;margin-top:34px;background:linear-gradient(90deg,var(--brass),transparent);border-radius:4px;animation:ul 1.1s cubic-bezier(.2,.8,.2,1) .3s forwards}
@keyframes ul{to{width:420px}}
.hint{margin-top:60px;font-size:30px;color:var(--muted);display:flex;align-items:center;gap:18px}
.hint:after{content:"";width:26px;height:26px;border-right:4px solid var(--brass);border-bottom:4px solid var(--brass);transform:rotate(45deg);animation:bob 1.2s ease-in-out infinite}
@keyframes bob{50%{transform:rotate(45deg) translate(8px,8px)}}
/* scene 2 */
.s2{opacity:0;display:flex;flex-direction:column;justify-content:center;animation:in .7s cubic-bezier(.2,.8,.2,1) both,out .6s ease-in both;animation-delay:${S1-0.1}s,${S2-0.6}s}
@keyframes in{from{opacity:0;transform:translateY(50px)}to{opacity:1;transform:none}}
.s2 .title{font-family:"Bricolage Grotesque";font-weight:700;font-size:54px;line-height:1.1;padding-bottom:30px;border-bottom:2px solid var(--line);margin-bottom:36px;display:flex;gap:26px;align-items:center}
.pill{flex:none;font-size:46px;color:var(--ink);background:var(--brass);padding:8px 26px;border-radius:18px}
.card{opacity:0;position:relative;margin-top:36px;padding:48px 44px 48px 150px;border-radius:28px;background:linear-gradient(135deg,rgba(255,255,255,.1),rgba(255,255,255,.04));border:1px solid rgba(255,255,255,.14);box-shadow:0 20px 60px rgba(0,0,0,.35);animation:cin .8s cubic-bezier(.2,.9,.2,1) both,out .5s ease-in both}
@keyframes cin{from{opacity:0;transform:translateX(160px) rotate(2deg)}to{opacity:1;transform:none}}
.card p{font-size:46px;line-height:1.3;font-weight:600}
.num{position:absolute;left:40px;top:50%;margin-top:-40px;width:80px;height:80px;border-radius:50%;background:var(--brass);color:var(--ink);font-family:"Bricolage Grotesque";font-weight:700;font-size:44px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 10px rgba(214,169,73,.18)}
/* scene 3 */
.s3{opacity:0;animation:in .8s cubic-bezier(.2,.8,.2,1) both;animation-delay:${S2-0.1}s;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.s3 .lionb{height:300px;filter:drop-shadow(0 20px 50px rgba(0,0,0,.5));animation:float 3s ease-in-out infinite alternate}
@keyframes float{to{transform:translateY(-24px)}}
.s3 h2{margin-top:50px;font-family:"Bricolage Grotesque";font-weight:700;font-size:78px;line-height:1.08}
.s3 .sub{margin-top:26px;font-size:34px;color:var(--muted)}
.btn{margin-top:60px;display:flex;align-items:center;gap:26px;padding:34px 60px;border-radius:999px;background:#25D366;color:#062b16;font-family:"Bricolage Grotesque";font-weight:700;font-size:66px;box-shadow:0 0 0 0 rgba(37,211,102,.6);animation:pulse 1.6s ease-out infinite}
@keyframes pulse{to{box-shadow:0 0 0 40px rgba(37,211,102,0)}}
.btn svg{width:70px;height:70px}
.s3 .off{margin-top:50px;font-size:30px;letter-spacing:.2em;text-transform:uppercase;color:var(--brass)}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 55%,rgba(0,0,0,.55) 100%);pointer-events:none}
</style></head><body>
<div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><div class="grid"></div><div class="dots">${dots}</div><div class="ring"></div><div class="ring r2"></div><div class="vig"></div>
<div class="prog"><b></b></div>
<header><div class="brand"><img class="lion" src="file://${P}/lion_t.png"><div class="bname">OLA ACCOUNTANCY</div></div><div class="loc">Luton · Birmingham</div></header>
<section class="scene s1"><div class="tag">${esc(p.tag)}</div>${p.figure?`<div class="figure">${esc(p.figure)}</div>`:''}<h1>${esc(p.headline)}</h1><div class="ul"></div><div class="hint">${EN?'Keep watching':'Vezi mai departe'}</div></section>
<section class="scene s2"><div class="title"><span class="pill">${esc(p.figure||'!')}</span><span>${esc(p.headline)}</span></div>${cards}</section>
<section class="scene s3"><img class="lionb" src="file://${P}/lion_t.png"><h2>${esc(cta)}</h2><div class="sub">${esc(EN?'First consultation: 30 minutes, £120 incl. VAT':'Prima consultație: 30 de minute, £120 cu TVA inclus')}</div><div class="btn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>0330 133 1886</div><div class="off">Luton · Birmingham</div></section>
<footer><div class="wa"><small>${esc(wa)}</small><b>0330 133 1886</b></div><div class="disc">${esc(disc)}</div></footer>
</body></html>`;
(async()=>{
 const out=process.argv[6]||path.join(__dirname,'tmp_'+id); fs.mkdirSync(out,{recursive:true});
 fs.writeFileSync(out+'/page.html',html);
 const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1080,height:1920}});
 await pg.goto('file://'+out+'/page.html'); await pg.evaluate(()=>document.fonts.ready);
 await pg.evaluate(()=>document.getAnimations().forEach(a=>a.pause()));
 for(let f=0;f<DUR*FPS;f++){
  await pg.evaluate(ms=>document.getAnimations().forEach(a=>a.currentTime=ms),f*1000/FPS);
  await pg.screenshot({path:`${out}/f${String(f).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});
 }
 await b.close();
})();
