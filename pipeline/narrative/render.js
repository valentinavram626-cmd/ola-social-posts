// Render one narrative story's canvas.
//   node render.js <build-dir> <mode> [arg]
//     preview  [t1,t2,...]   stills into <build-dir>/prev/
//     frames                 every frame at 30 fps into <build-dir>/frames/
//     textonly [endSeconds]  transparent caption/chrome PNGs for compositing an
//                            opening live-action plate, into <build-dir>/textonly/
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');

const HERE = __dirname, FPS = 30;
const BUILD = path.resolve(process.argv[2] || '.');
const ASSETS = 'file://' + path.resolve(HERE, '..', 'assets');

const tl = JSON.parse(fs.readFileSync(path.join(BUILD, 'timeline.json'), 'utf8'));
const html = fs.readFileSync(path.join(HERE, 'page.html'), 'utf8')
  .split('__ASSETS__').join(ASSETS)
  .replace('__TIMELINE__', JSON.stringify(tl));
fs.writeFileSync(path.join(BUILD, 'page.built.html'), html);

(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({viewport: {width: 1080, height: 1920}});
  pg.on('pageerror', e => { console.error('PAGEERR', e.message); process.exitCode = 1; });
  await pg.goto('file://' + path.join(BUILD, 'page.built.html'));
  await pg.evaluate(() => window.ready);
  await pg.waitForTimeout(500);

  const mode = process.argv[3] || 'preview';
  if (mode === 'preview') {
    const ts = (process.argv[4] || '2,10,20,30,40,48').split(',').map(Number);
    const out = path.join(BUILD, 'prev');
    fs.mkdirSync(out, {recursive: true});
    for (const t of ts) {
      await pg.evaluate(t => window.seek(t), t);
      await pg.screenshot({path: path.join(out, `t${t}.jpg`), type: 'jpeg', quality: 86});
    }
    console.log('preview', ts.join(','));
  } else if (mode === 'textonly') {
    const end = Number(process.argv[4] || 3.4);
    await pg.evaluate(() => { window.TEXTONLY = true; });
    await pg.addStyleTag({content: 'html,body{background:transparent !important}'});
    const out = path.join(BUILD, 'textonly');
    fs.rmSync(out, {recursive: true, force: true});
    fs.mkdirSync(out, {recursive: true});
    const N = Math.ceil(end * FPS);
    for (let f = 0; f < N; f++) {
      await pg.evaluate(t => window.seek(t), f / FPS);
      await pg.screenshot({path: path.join(out, `t${String(f).padStart(5, '0')}.png`),
                           type: 'png', omitBackground: true});
    }
    console.log('textonly frames', N);
  } else if (mode === 'safe') {
    // Walk the whole piece and report any text that leaves the safe zone.
    const S = await pg.evaluate(() => window.SAFE);
    const bad = [];
    const ext = {minX: 1e9, maxX: -1e9, minY: 1e9, maxY: -1e9};
    const N = Math.ceil(tl.total * FPS);
    for (let f = 0; f < N; f += 2) {
      const t = f / FPS;
      const b = await pg.evaluate(t => window.textBounds(t), t);
      if (!b) continue;
      ext.minX = Math.min(ext.minX, Math.round(b.minX)); ext.maxX = Math.max(ext.maxX, Math.round(b.maxX));
      ext.minY = Math.min(ext.minY, Math.round(b.minY)); ext.maxY = Math.max(ext.maxY, Math.round(b.maxY));
      if (b.minX < S.L - 2 || b.maxX > S.R + 2 || b.minY < S.T - 2 || b.maxY > S.B + 2)
        bad.push({t: +t.toFixed(2), minX: Math.round(b.minX), maxX: Math.round(b.maxX),
                  minY: Math.round(b.minY), maxY: Math.round(b.maxY)});
    }
    console.log(JSON.stringify({safe: S, extent: ext, violations: bad.slice(0, 8), count: bad.length}));
    if (bad.length) process.exitCode = 2;
  } else {
    const out = path.join(BUILD, 'frames');
    fs.rmSync(out, {recursive: true, force: true});
    fs.mkdirSync(out, {recursive: true});
    const N = Math.ceil(tl.total * FPS);
    for (let f = 0; f < N; f++) {
      await pg.evaluate(t => window.seek(t), f / FPS);
      await pg.screenshot({path: path.join(out, `f${String(f).padStart(5, '0')}.jpg`),
                           type: 'jpeg', quality: 92});
      if (f % 300 === 0) console.log('frame', f, '/', N);
    }
    console.log('frames', N);
  }
  await b.close();
})();
