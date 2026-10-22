import json, html, os, sys
B = os.path.dirname(os.path.abspath(__file__))
import sys
W = sys.argv[1] if len(sys.argv) > 1 else "2026-10-23"
RAW = f"https://raw.githubusercontent.com/valentinavram626-cmd/ola-social-posts/main/reels/week-{W}/"
pl = json.load(open(f"{B}/week_plan.json"))
ro = {p["id"]: p for p in json.load(open(f"{B}/week_ro.json"))}
en = {p["id"]: p for p in json.load(open(f"{B}/week_en.json"))}
VAL = json.load(open(f"{B}/week_valentin.json"))  # day -> {file,title,caption}
SLOTS = ["07:30","08:30","09:30","10:30","11:30","12:30","13:30","14:30","15:30","16:30","17:30","18:30","19:30","20:30","21:30"]
VSLOT = "19:30"
DAYS_RO = {"2026-10-23":"Vineri 23 oct","2026-10-24":"Sâmbătă 24 oct","2026-10-25":"Duminică 25 oct","2026-10-26":"Luni 26 oct","2026-10-27":"Marți 27 oct","2026-10-28":"Miercuri 28 oct","2026-10-29":"Joi 29 oct"}
RO_NETS = "Instagram Reel + Story · Facebook Reel + Story · TikTok · Threads"
EN_NETS = "YouTube Short · LinkedIn · Bluesky · (GBP 1/zi, Pinterest 1/zi)"
schedule = []  # for scheduling later
secs = []
for d in pl:
    day = d["day"]; items = d["items"]; extra = d["extra"]
    rows = []
    ro_items = list(items); en_items = list(items)
    en_items.insert(SLOTS.index(VSLOT), extra)
    for i, t in enumerate(SLOTS):
        if t == VSLOT:
            v = VAL[day]
            r = {"day":day,"time":t,"ro":{"kind":"valentin","file":v["file"],"title":v["title"],"caption":v["caption"]},"en":en[f"en-{day[5:]}-{en_items[i]}"]}
        else:
            ri = i if i < SLOTS.index(VSLOT) else i-1
            r = {"day":day,"time":t,"ro":ro[f"ro-{day[5:]}-{ro_items[ri]}"],"en":en[f"en-{day[5:]}-{en_items[i]}"]}
        schedule.append(r); rows.append(r)
    cards = []
    for r in rows:
        a = r["ro"]; b = r["en"]
        if a.get("kind") == "valentin":
            ca = f'<div class="c val"><video controls preload="none" poster="{RAW}thumbs/{a["file"]}.jpg" src="{RAW}{a["file"]}.mp4"></video><div class="t"><span class="lab">VIDEO VALENTIN · RO</span><b>{html.escape(a["title"])}</b><p>{html.escape(a["caption"])}</p></div></div>'
        else:
            ca = f'<div class="c"><video controls preload="none" poster="{RAW}thumbs/{a["id"]}.jpg" src="{RAW}{a["id"]}.mp4"></video><div class="t"><span class="lab">REEL · RO</span><b>{html.escape(a["headline"])}</b><p>{html.escape(a["caption"])}</p></div></div>'
        cb = f'<div class="c"><video controls preload="none" poster="{RAW}thumbs/{b["id"]}.jpg" src="{RAW}{b["id"]}.mp4"></video><div class="t"><span class="lab">REEL · EN</span><b>{html.escape(b["headline"])}</b><p>{html.escape(b["caption"])}</p></div></div>'
        cards.append(f'<div class="slot"><div class="time">{r["time"]}</div>{ca}{cb}</div>')
    secs.append(f'<section id="d{day}"><h2>{DAYS_RO[day]} <small>15 postări RO + 15 EN</small></h2>{"".join(cards)}</section>')
json.dump(schedule, open(f"{B}/week_schedule.json","w"), ensure_ascii=False, indent=0)
# publish schedule + library index for Ola Marketing HQ
wk_dir = f"{B}/../reels/week-{W}"; os.makedirs(wk_dir, exist_ok=True)
json.dump(schedule, open(f"{wk_dir}/schedule.json","w"), ensure_ascii=False)
idx_path = f"{B}/../reels/index.json"
try: idx = json.load(open(idx_path))
except Exception: idx = {"weeks": []}
idx["weeks"] = [w for w in idx.get("weeks", []) if w.get("id") != W]
idx["weeks"].insert(0, {"id": W, "status": "awaiting_approval", "schedule": f"reels/week-{W}/schedule.json"})
json.dump(idx, open(idx_path,"w"), ensure_ascii=False, indent=1)
nav = "".join(f'<a href="#d{d["day"]}">{DAYS_RO[d["day"]][:2]} {d["day"][8:]}</a>' for d in pl)
page = f'''<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ola Week Approval</title>
<style>
:root{{--ink:#0B1324;--brass:#D6A949;--cream:#F3EEE3;--muted:#A9B3C7;--card:#131F3D}}
@media (prefers-color-scheme: light){{:root:not([data-theme="dark"]){{--ink:#F6F3EC;--cream:#0B1324;--card:#fff;--muted:#55607a}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--ink);color:var(--cream);font-family:system-ui,sans-serif;padding:16px}}
header{{position:sticky;top:0;background:var(--ink);padding:10px 0;z-index:2;border-bottom:1px solid #2a3755}}
h1{{font-size:20px;margin:0 0 8px}}nav{{display:flex;gap:8px;flex-wrap:wrap}}nav a{{color:var(--ink);background:var(--brass);padding:6px 10px;border-radius:8px;text-decoration:none;font-weight:600;font-size:14px}}
.rules{{font-size:14px;color:var(--muted);margin:10px 0}}
h2{{font-size:18px;margin:28px 0 10px}}h2 small{{color:var(--muted);font-weight:400;font-size:13px}}
.slot{{display:grid;grid-template-columns:60px 1fr 1fr;gap:10px;margin-bottom:14px;align-items:start}}
.time{{font-weight:700;color:var(--brass);padding-top:8px}}
.c{{background:var(--card);border-radius:12px;overflow:hidden;display:grid;grid-template-columns:120px 1fr;gap:10px}}
.c.val{{outline:2px solid var(--brass)}}
video{{width:120px;aspect-ratio:9/16;background:#000;object-fit:cover}}
.t{{padding:8px 10px 8px 0;font-size:13px}}.lab{{font-size:11px;letter-spacing:.12em;color:var(--brass);font-weight:700}}.t b{{display:block;margin:4px 0}}.t p{{margin:0;color:var(--muted);white-space:pre-wrap;font-size:12px}}
@media (max-width:800px){{.slot{{grid-template-columns:1fr}}.time{{padding:0}}}}
</style></head><body><header><h1>Ola Accountancy – lot 23–29 octombrie (15 postări/zi)</h1><nav>{nav}</nav>
<div class="rules">RO (stânga): {RO_NETS}. EN (dreapta): {EN_NETS}. Fiecare reel RO merge și la Stories. TikTok max 12/zi. Videoclipul dumneavoastră la 19:30, doar pe platformele RO; pe EN e înlocuit cu reel-ul din dreapta. Răspundeți cu „aprobat” sau cu lista modificărilor (ziua + ora).</div></header>
{"".join(secs)}
</body></html>'''
open(f"{B}/week_approval.html","w").write(page)
print("slots", len(schedule))
