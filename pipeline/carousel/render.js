const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const D = __dirname;

(async () => {
  const job = process.argv[2];
  const cfg = JSON.parse(fs.readFileSync(path.join(D, job + '.json'), 'utf8'));
  cfg.logo = 'data:image/png;base64,' + fs.readFileSync(path.join(D,'lion.b64'),'utf8').trim();

  const html = fs.readFileSync(path.join(D,'carousel.html'),'utf8')
    .replace('<script>', `<script>const CFG=${JSON.stringify(cfg)};`);
  const built = path.join(D, `built-${job}.html`);
  fs.writeFileSync(built, html);

  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{width:1080,height:1350}, deviceScaleFactor:1 });
  await p.goto('file://' + built);
  await p.waitForFunction(() => window.READY === true);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);

  const out = path.join(D, job + '-out');
  fs.mkdirSync(out, { recursive:true });
  for (let i = 0; i < cfg.slides.length; i++) {
    await p.locator('#s'+i).screenshot({ path: path.join(out, String(i+1).padStart(2,'0') + '.png') });
  }
  await b.close();
  console.log('rendered', cfg.slides.length, 'slides →', out);
})();
