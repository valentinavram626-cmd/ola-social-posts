"""
Ola Accountancy — single static post generator.

Five post types, one layout engine, two sizes, two languages.
Replaces the carousel format from 23 November 2026.

    tip    morning advice            slot + hero + sub + cta
    acq    acquisition, Meta style   slot + hero + sub + cta
    edu    educational               slot + hero + sub + cta   (<em> prints gold)
    joke   humour that lands true    slot + setup + punch + hook + cta
    quote  evening thought           slot + line + attribution

Sizes: feed 1080x1350, story 1080x1920.
Everything is embedded — font, lion, wordmark — so a render never needs the network.

    python3 solo.py specs.json out/
"""
import base64, json, os, pathlib, subprocess, sys

D = pathlib.Path(__file__).resolve().parent

PAL = {"base": "#060A11", "deep": "#020408", "rgbBase": "6,10,17", "rgbDeep": "2,4,8"}
GOLD, MUTED, DIM = "#C8A15A", "#A8B2C2", "#8E97A6"

SIZES = {"feed": (1080, 1350), "story": (1080, 1920)}


def _b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode((D / path).read_bytes()).decode()


def _assets():
    return {
        "font": (D / "fonts" / "archivo.css").read_text(encoding="utf-8"),
        "lion": _b64("lion.jpg", "image/jpeg"),
        "logo": _b64("logo-clean.png", "image/png"),
    }


def _shell(inner, w, h, lion_pos, lion_op, pad, A, grad_mid=".96", grad_soft=".80", grad_fade=".18"):
    b, dp, rb, rd = PAL["base"], PAL["deep"], PAL["rgbBase"], PAL["rgbDeep"]
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
{A['font']}
html,body{{margin:0;padding:0;background:{b};}}
em{{font-style:normal;color:{GOLD};}}
</style></head>
<body>
<div style="width:{w}px;height:{h}px;box-sizing:border-box;position:relative;overflow:hidden;background:{b};font-family:Archivo,system-ui,sans-serif;">
  <div style="position:absolute;inset:0;background:linear-gradient(105deg,{b} 0%,{b} 51%,{dp} 100%);"></div>
  <img src="{A['lion']}" alt="" aria-hidden="true" style="position:absolute;inset:0;width:{w}px;height:{h}px;object-fit:cover;object-position:{lion_pos};mix-blend-mode:screen;opacity:{lion_op};">
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,{b} 0%,rgba({rb},{grad_mid}) 34%,rgba({rb},{grad_soft}) 55%,rgba({rb},{grad_fade}) 86%);"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba({rb},.60) 0%,rgba({rb},0) 24%,rgba({rb},0) 56%,rgba({rd},.95) 100%);"></div>
  <div style="position:relative;height:{h}px;box-sizing:border-box;padding:{pad};display:flex;flex-direction:column;">
{inner}
  </div>
</div></body></html>"""


def _logo(A, w):
    return f'    <img src="{A["logo"]}" alt="Ola Accountancy" style="width:{w}px;height:auto;display:block;margin-left:-14px;">'


def _slot(text, size=27):
    return f"""    <div style="display:flex;align-items:center;gap:20px;">
      <span style="display:block;width:56px;height:3px;background:{GOLD};"></span>
      <span style="font-size:{size}px;font-weight:600;color:{GOLD};line-height:1;">{text}</span>
    </div>"""


def _cta(text, story, bar_stretch=True):
    fs, sub_fs = (36, 26) if story else (33, 23)
    bar = "align-self:stretch" if bar_stretch else "height:62px"
    return f"""    <div style="display:flex;align-items:center;gap:22px;padding-bottom:{40 if story else 6}px;">
      <span style="display:block;width:7px;{bar};background:{GOLD};"></span>
      <div style="display:flex;flex-direction:column;gap:7px;">
        <span style="font-size:{fs}px;font-weight:700;color:#FFFFFF;line-height:1.18;letter-spacing:-.4px;">{text}</span>
        <span style="font-size:{sub_fs}px;font-weight:500;color:{GOLD};line-height:1.2;">ola-accountancy.co.uk &nbsp;·&nbsp; Luton &amp; Birmingham</span>
      </div>
    </div>"""


def _standard(p, size, A):
    """tip, acq and edu share one layout."""
    w, h = SIZES[size]
    story = size == "story"
    hero_size = p.get("hero_size") or (78 if story else 68)
    pad = "168px 84px 210px" if story else "80px 84px 72px"
    inner = "\n".join([
        _logo(A, 390 if story else 360),
        '    <div style="margin-top:auto;"></div>',
        _slot(p["slot"]),
        f'    <h1 style="margin:26px 0 0;max-width:{760 if story else 672}px;font-size:{hero_size}px;'
        f'font-weight:700;line-height:1.05;letter-spacing:-1.8px;color:#FFFFFF;">{p["hero"]}</h1>',
        f'    <p style="margin:30px 0 0;max-width:{720 if story else 614}px;font-size:{34 if story else 31}px;'
        f'font-weight:400;line-height:1.45;color:{MUTED};">{p["sub"]}</p>',
        '    <div style="margin-top:auto;"></div>',
        _cta(p["cta"], story),
    ])
    return _shell(inner, w, h, "62% 34%" if story else "64% 39%", ".90", pad, A, grad_fade=".14")


def _joke(p, size, A):
    w, h = SIZES[size]
    story = size == "story"
    punch_size = p.get("punch_size") or (68 if story else 62)
    pad = "168px 84px 210px" if story else "80px 84px 72px"
    inner = "\n".join([
        _logo(A, 390 if story else 360),
        '    <div style="margin-top:auto;"></div>',
        _slot(p["slot"]),
        f'    <p style="margin:34px 0 0;max-width:{700 if story else 640}px;font-size:{35 if story else 33}px;'
        f'font-weight:500;line-height:1.38;color:#9BA5B4;">{p["setup"]}</p>',
        f'    <p style="margin:22px 0 0;max-width:{720 if story else 660}px;font-size:{punch_size}px;'
        f'font-weight:700;line-height:1.12;letter-spacing:-1.5px;color:#FFFFFF;">{p["punch"]}</p>',
        '    <div style="margin-top:auto;"></div>',
        f'    <div style="border-top:1px solid rgba(200,161,90,.45);padding-top:30px;">',
        f'      <p style="margin:0;max-width:{710 if story else 650}px;font-size:{33 if story else 31}px;'
        f'font-weight:500;line-height:1.36;color:{GOLD};">{p["hook"]}</p>',
        '      <div style="margin-top:26px;">',
        _cta(p["cta"], story, bar_stretch=False),
        "      </div>",
        "    </div>",
    ])
    return _shell(inner, w, h, "66% 34%", ".86", pad, A, grad_soft=".82", grad_fade=".16")


def _quote(p, size, A):
    w, h = SIZES[size]
    story = size == "story"
    line_size = p.get("line_size") or (70 if story else 62)
    pad = "168px 84px 210px" if story else "80px 84px 72px"
    # The frame supplies the quotation marks, so a writer never has to: Romanian uses the
    # low-high pair, English the curly pair, and Romanian is inferred from the post id when
    # `quote_marks` is not set. Any marks the writer typed into `line` are stripped first,
    # so the frame can never show doubled quotes.
    ro = p.get("quote_marks") == "ro" or str(p.get("id", "")).startswith("ola-ro-")
    open_q, close_q = ("&bdquo;", "&rdquo;") if ro else ("&ldquo;", "&rdquo;")
    line_text = str(p["line"]).strip().strip('"\'\u201c\u201d\u201e\u00ab\u00bb').strip()
    inner = "\n".join([
        _logo(A, 390 if story else 360),
        '    <div style="margin-top:auto;"></div>',
        _slot(p["slot"]),
        f'    <p style="margin:14px 0 0;max-width:{780 if story else 700}px;font-size:{line_size}px;'
        f'font-weight:600;line-height:1.24;letter-spacing:-1.1px;color:#FFFFFF;">{open_q}{line_text}{close_q}</p>',
        f'    <div style="margin:{34 if story else 28}px 0 0;display:flex;align-items:center;gap:18px;">',
        f'      <span style="display:block;width:54px;height:2px;background:{GOLD};"></span>',
        f'      <span style="display:block;font-size:{34 if story else 31}px;font-weight:600;color:{GOLD};line-height:1.2;letter-spacing:-.2px;">{p.get("attrib","")}</span>',
        "    </div>",
        '    <div style="margin-top:auto;"></div>',
        f'    <div style="padding-bottom:{40 if story else 6}px;">',
        f'      <span style="display:block;font-size:{25 if story else 23}px;font-weight:500;color:{DIM};line-height:1.2;">ola-accountancy.co.uk &nbsp;·&nbsp; Luton &amp; Birmingham</span>',
        "    </div>",
    ])
    return _shell(inner, w, h, "68% 30%", ".92", pad, A, grad_soft=".80", grad_fade=".18")


KINDS = {"tip": _standard, "acq": _standard, "edu": _standard, "joke": _joke, "quote": _quote}
REQUIRED = {
    "tip": ("slot", "hero", "sub", "cta"),
    "acq": ("slot", "hero", "sub", "cta"),
    "edu": ("slot", "hero", "sub", "cta"),
    "joke": ("slot", "setup", "punch", "hook", "cta"),
    "quote": ("slot", "line", "attrib"),
}


def html_for(post, size):
    kind = post["kind"]
    if kind not in KINDS:
        raise ValueError(f"{post.get('id')}: unknown kind {kind!r}, expected one of {sorted(KINDS)}")
    missing = [f for f in REQUIRED[kind] if not post.get(f)]
    if missing:
        raise ValueError(f"{post.get('id')}: {kind} is missing {', '.join(missing)}")
    if size not in SIZES:
        raise ValueError(f"{post.get('id')}: unknown size {size!r}")
    return KINDS[kind](post, size, _assets())


def build(spec_path, out_dir):
    posts = json.loads(pathlib.Path(spec_path).read_text(encoding="utf-8"))
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    jobs = []
    for post in posts:
        for size in post.get("sizes", ["feed"]):
            name = f"{post['id']}-{size}"
            (out / f"{name}.html").write_text(html_for(post, size), encoding="utf-8")
            jobs.append({"name": name, "w": SIZES[size][0], "h": SIZES[size][1]})
    (out / "_jobs.json").write_text(json.dumps(jobs), encoding="utf-8")
    subprocess.run([sys.executable, str(D / "shoot.py"), str(out)], check=True)

    # Story frames leave here as JPEG, and the PNG is removed.
    #
    # TikTok refuses image/png outright ("The content format of the Tiktok photo
    # is incorrect"), and the story frame is the one we send to TikTok. On
    # 24 November 2026 a run scheduled the raw PNGs and 30 posts across three
    # brands failed at publication time, with nobody watching. The rule to
    # convert them existed in the agent prompt and was not followed, so the rule
    # is now the renderer's: there is no story PNG left on disk to schedule by
    # mistake. Instagram and Facebook Stories take JPEG without complaint, so
    # nothing else has to change. Feed frames stay PNG.
    from PIL import Image
    converted = []
    for j in jobs:
        if not j["name"].endswith("-story"):
            continue
        png = out / f"{j['name']}.png"
        if not png.exists():
            raise SystemExit(f"story frame missing after render: {png}")
        jpg = png.with_suffix(".jpg")
        Image.open(png).convert("RGB").save(jpg, "JPEG", quality=92, optimize=True)
        png.unlink()
        converted.append(jpg.name)
    if converted:
        print(f"story frames written as JPEG for TikTok: {len(converted)}")

    return [j["name"] for j in jobs]


if __name__ == "__main__":
    names = build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "out")
    print(f"built {len(names)} images")
