#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run before anything is pushed or scheduled. Exits non-zero on any failure.

Every check here exists because the mistake it catches was actually made, and
in each case the mistake was *reported as success*. That is the pattern this
file exists to break: a claim that something is fine is worth nothing unless a
check that could have failed was run and did not.

    python3 preflight.py           # gate every topic
    python3 preflight.py <slug>    # gate one

  1 IDENTITIES   3 Nov: five people's handles, their contact dates and their
                 tax subjects sat in a PUBLIC repo for six days. Nothing that
                 identifies a person belongs in either repository.
  2 LOSS         5 Nov: rewriting one topic silently deleted its Google
                 Business card, because the edit replaced a span of text
                 without checking what was inside it. Compares every topic's
                 keys and card count against the last commit.
  3 FORMAT       5 Nov: a content card carried its own CTA and the closing
                 card repeated it. Three content cards, one CTA card, and no
                 ask or phone anywhere but the last.
  4 SCOPE        3 Nov: a post nearly went out calling an England-only payment
                 universal. Every topic has to say who does NOT get it.
  5 SOURCES      Every topic needs primary sources with the date they were read.
  6 ALT          5 Nov: a whole day published with alt text null on every image.
"""
import html, pathlib, re, subprocess, sys

D = pathlib.Path(__file__).parent
REPO = D.parent.parent
FAIL = []
OWN = {"ola_accountancy", "olaaccountancy", "ola-accountancy", "valentintheaccountant",
       "olaaccountancyluton", "olaaccountancybirmingham", "anthropic.com", "noreply"}
OWN_PHONE = {"03301331886", "443301331886"}
# Published institutional reporting contacts — not a person's address, and the
# scam copy is useless without them. HMRC's own wording: "send any suspicious
# text messages to 60599 (network charges apply) or email: phishing@hmrc.gov.uk
# then delete them". Exact strings only: the check still fails on any other
# address at the same domain, and on every third-party handle.
PUBLISHED_CONTACTS = {"phishing@hmrc.gov.uk"}
PUBLISHED_HANDLES = {m.split("@", 1)[1].lower() for m in PUBLISHED_CONTACTS}


def fail(check, detail):
    FAIL.append(f"{check}: {detail}")


# ---------------------------------------------------------------- 1 identities
def check_identities():
    try:
        files = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                               text=True, check=True).stdout.split()
    except subprocess.CalledProcessError:
        return fail("IDENTITIES", "could not list tracked files")
    pat_handle = re.compile(r"@([A-Za-z0-9._]{3,30})")
    pat_mail = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    pat_phone = re.compile(r"(?:\+?44|0)7\d[\d ]{7,11}")
    for rel in files:
        if not re.search(r"\.(md|txt|json|csv|ya?ml|py|html)$", rel):
            continue
        p = REPO / rel
        try:
            txt = p.read_text(errors="ignore")
        except OSError:
            continue
        for m in set(pat_mail.findall(txt)):
            if m.lower() in PUBLISHED_CONTACTS:
                continue
            if not any(o in m.lower() for o in OWN):
                fail("IDENTITIES", f"{rel}: email address {m!r}")
        for m in set(pat_handle.findall(txt)):
            low = m.lower()
            if low in PUBLISHED_HANDLES:
                continue
            if low in OWN or low.isdigit() or low in {"media", "fontsource", "import", "charset"}:
                continue
            if re.match(r"^\d", low):          # @400, @12..96 — CSS, not a person
                continue
            fail("IDENTITIES", f"{rel}: handle @{m}")
        for m in set(pat_phone.findall(txt)):
            if re.sub(r"\D", "", m) not in OWN_PHONE:
                fail("IDENTITIES", f"{rel}: phone number {m!r}")


# ---------------------------------------------------------------------- 2 loss
def check_loss():
    """Nothing disappears from a topic without someone meaning it to."""
    try:
        old_src = subprocess.run(["git", "show", "HEAD:pipeline/carousel/topics.py"],
                                 cwd=REPO, capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return print("  LOSS      skipped (no committed topics.py to compare against)")
    ns = {}
    try:
        exec(compile(old_src, "topics_HEAD", "exec"), ns)
    except Exception as e:
        return fail("LOSS", f"could not load the committed topics.py: {e}")
    old = ns.get("BY_SLUG", {})
    import topics
    for slug, was in old.items():
        now = topics.BY_SLUG.get(slug)
        if now is None:
            fail("LOSS", f"topic {slug!r} was in the last commit and is gone now")
            continue
        for k in was:
            if k not in now:
                fail("LOSS", f"{slug}: key {k!r} was there at the last commit and is gone")
        for k in ("RO", "EN"):
            if k in was and k in now and len(now[k]) < len(was[k]) - 1:
                fail("LOSS", f"{slug}: {k} dropped from {len(was[k])} cards to {len(now[k])}")


# -------------------------------------------------------------------- 3 format
def check_format(topic):
    """Four cards, three of content, the ask only on the last.

    13 Nov 2026: the two English-only brands have no RO block at all, and this
    check demanded one — so a brand working exactly as Valentin connected it
    failed the gate. The languages a topic must have are now the ones its brand
    publishes, and an Ola topic is still required to have both.
    """
    slug = topic["slug"]
    langs = [("EN", topic.get("EN"), topic.get("CTA_EN"))]
    if topic.get("brand", "ola") == "ola":
        langs.insert(0, ("RO", topic.get("RO"), topic.get("CTA_RO")))
    else:
        for k in ("RO", "CTA_RO"):
            if topic.get(k):
                fail("FORMAT", f"{slug}: brand {topic['brand']!r} publishes in English "
                               f"only but carries a {k} block")
    for lang, body, cta in langs:
        if not body:
            fail("FORMAT", f"{slug}: no {lang} cards"); continue
        if len(body) != 3:
            fail("FORMAT", f"{slug}: {lang} has {len(body)} content cards, needs 3")
        if not cta or cta.get("type") != "cta":
            fail("FORMAT", f"{slug}: {lang} has no closing CTA card")
        for i, c in enumerate(body, 1):
            if c.get("ask") or c.get("phone"):
                fail("FORMAT", f"{slug}: {lang} card {i} carries a call to action")
            if c.get("type") == "ask":
                fail("FORMAT", f"{slug}: {lang} card {i} uses the retired 'ask' type")


# --------------------------------------------------------------------- 4 scope
def check_scope(topic):
    slug, sc = topic["slug"], topic.get("SCOPE") or {}
    for k in ("nation", "category", "excluded", "from_when"):
        if not str(sc.get(k, "")).strip():
            fail("SCOPE", f"{slug}: SCOPE.{k} is empty")
    exc = str(sc.get("excluded", ""))
    if exc and len(exc) < 40:
        fail("SCOPE", f"{slug}: SCOPE.excluded is too thin to be a real answer")


# ------------------------------------------------------------------- 5 sources
def check_sources(topic):
    slug, src = topic["slug"], topic.get("SOURCES") or []
    if not src:
        return fail("SOURCES", f"{slug}: no sources at all")
    for s in src:
        if len(s) < 3 or not str(s[1]).startswith("http"):
            fail("SOURCES", f"{slug}: a source has no URL")
        elif not re.match(r"^\d{4}-\d{2}-\d{2}$", str(s[2])):
            fail("SOURCES", f"{slug}: source {s[1]} has no date it was read")


# ----------------------------------------------------------------------- 6 alt
def check_alt(topic):
    import build, alt
    slug = topic["slug"]
    for lang in (("ro", "en") if topic.get("brand", "ola") == "ola" else ("en",)):
        cards = build.cards(topic, lang)
        a = alt.alt_for(cards)
        if len(a) != len(cards):
            fail("ALT", f"{slug}: {lang} has {len(cards)} frames but {len(a)} alt strings")
        for i, s in enumerate(a, 1):
            if not s.strip():
                fail("ALT", f"{slug}: {lang} frame {i} has empty alt text")
            if re.search(r"<[^>]+>", s):
                fail("ALT", f"{slug}: {lang} frame {i} alt text still contains markup")



# ----------------------------------------------------------------------- 7 solo
def check_solos():
    """A single-image post has no card 3, so the exclusion has to be on the frame.

    Set by Valentin on 13 November 2026 with the format itself: "noi vreau sa
    facem totul real si profesional". A headline in the shape "you can get £X" is
    a claim of entitlement, and the row that keeps it honest is the one naming who
    gets nothing. Without it the post overstates, so it does not ship.
    """
    import alt, topics
    seen = set()
    for s in topics.SOLOS:
        slug = s.get("slug", "<no slug>")
        if slug in seen:
            fail("SOLO", f"{slug}: two single-image posts share a slug")
        seen.add(slug)
        brand = s.get("brand")
        if brand not in ("ola", "bham", "en"):
            fail("SOLO", f"{slug}: brand {brand!r} is not one of ola, bham, en")
        if brand in ("bham", "en") and s.get("lang") != "en":
            fail("SOLO", f"{slug}: brand {brand!r} publishes in English only, "
                         f"lang is {s.get('lang')!r}")
        if not slug.startswith(f"{brand}-"):
            fail("SOLO", f"{slug}: slug is not prefixed with its brand")
        sl = s.get("slide") or {}
        if sl.get("type") != "solo":
            fail("SOLO", f"{slug}: slide type is {sl.get('type')!r}, needs 'solo'")
        rows = sl.get("rows") or []
        if len(rows) != 3:
            fail("SOLO", f"{slug}: {len(rows)} rows, needs exactly 3")
        labels = [str(r[0]) for r in rows if r]
        excl = [l for l in labels if "exclu" in l.lower()]
        if not excl:
            fail("SOLO", f"{slug}: no row says who is EXCLUDED — labels are {labels}")
        for fld in ("kicker", "h1", "ask", "phone", "disc"):
            if not str(sl.get(fld, "")).strip():
                fail("SOLO", f"{slug}: slide.{fld} is empty")
        # 13 Nov 2026, Valentin: the nation does not go in the headline. On a
        # UK-wide brand it goes in a row instead; on Birmingham it is not needed.
        h1 = str(sl.get("h1", ""))
        for nation in ("England", "Scotland", "Wales", "Northern Ireland",
                       "Anglia", "Scoția", "Țara Galilor", "Irlanda de Nord"):
            if nation in h1:
                fail("SOLO", f"{slug}: the nation {nation!r} is in the headline")
        if "<em>" not in h1:
            fail("SOLO", f"{slug}: the headline carries no <em> figure")
        if not str(s.get("caption", "")).strip():
            fail("SOLO", f"{slug}: no caption")
        if not str(s.get("tt_title", "")).strip():
            fail("SOLO", f"{slug}: no TikTok title (a photo post is rejected without one)")
        src = s.get("SOURCES") or []
        if not src:
            fail("SOURCES", f"{slug}: no sources at all")
        for one in src:
            if len(one) < 3 or not str(one[1]).startswith("http"):
                fail("SOURCES", f"{slug}: a source has no URL")
            elif not re.match(r"^\d{4}-\d{2}-\d{2}$", str(one[2])):
                fail("SOURCES", f"{slug}: source {one[1]} has no date it was read")
        sc = s.get("SCOPE") or {}
        for k in ("nation", "category", "excluded", "from_when"):
            if not str(sc.get(k, "")).strip():
                fail("SCOPE", f"{slug}: SCOPE.{k} is empty")
        if len(str(sc.get("excluded", ""))) < 40:
            fail("SCOPE", f"{slug}: SCOPE.excluded is too thin to be a real answer")
        a = alt.alt_for([sl])
        if len(a) != 1 or not a[0].strip():
            fail("ALT", f"{slug}: no alt text for the single frame")


def main():
    import topics
    only = sys.argv[1] if sys.argv[1:] else None
    print("preflight")
    check_identities()
    check_loss()
    check_solos()
    for slug, t in topics.BY_SLUG.items():
        if only and slug != only:
            continue
        check_format(t); check_scope(t); check_sources(t); check_alt(t)
    if FAIL:
        print(f"\n{len(FAIL)} FAILURE(S) — nothing is pushed or scheduled:\n")
        for f in FAIL:
            print("  -", f)
        return 1
    print("  all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
