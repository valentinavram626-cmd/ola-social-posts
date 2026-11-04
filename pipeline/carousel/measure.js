// Measure the computed box of each slide's parts, rather than eyeballing the PNG.
// The README's lesson: ro-tiktok was "fixed" twice by guessing at padding and
// nothing moved. Numbers first.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const job = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{ width: 1200, height: 2000 }, deviceScaleFactor:1 });
  await p.goto('file://' + path.join(__dirname, `built-${job}.html`));
  await p.waitForFunction(() => window.READY === true);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  const rows = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('.slide').forEach((s, i) => {
      const S = s.getBoundingClientRect();
      const bd = s.querySelector('.bd'), ft = s.querySelector('.ft');
      const kids = [...bd.children].map(c => {
        const r = c.getBoundingClientRect();
        return { cls: c.className || c.tagName, h: Math.round(r.height),
                 top: Math.round(r.top - S.top), bot: Math.round(r.bottom - S.top) };
      });
      const B = bd.getBoundingClientRect(), F = ft.getBoundingClientRect();
      out.push({ slide: i + 1, frameH: Math.round(S.height),
        bdTop: Math.round(B.top - S.top), bdBot: Math.round(B.bottom - S.top),
        bdScroll: bd.scrollHeight, bdClient: bd.clientHeight,
        ftTop: Math.round(F.top - S.top),
        contentTop: kids.length ? Math.min(...kids.map(k => k.top)) : null,
        contentBot: kids.length ? Math.max(...kids.map(k => k.bot)) : null,
        kids });
    });
    return out;
  });
  for (const r of rows) {
    const over = r.bdScroll - r.bdClient;
    const intoFooter = r.contentBot - r.ftTop;
    console.log(`slide ${r.slide}  frame ${r.frameH}  bd ${r.bdTop}..${r.bdBot} (scroll ${r.bdScroll} vs client ${r.bdClient}${over>0?'  OVERFLOW +'+over:''})  ftTop ${r.ftTop}  content ${r.contentTop}..${r.contentBot}${intoFooter>0?'  INTO FOOTER +'+intoFooter:''}`);
    if (over > 0 || intoFooter > 0) for (const k of r.kids) console.log(`        ${k.cls.padEnd(12)} h=${String(k.h).padStart(4)}  ${k.top}..${k.bot}`);
  }
  await b.close();
})();
