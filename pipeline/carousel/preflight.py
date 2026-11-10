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
    slug = topic["slug"]
    for lang, body, cta in (("RO", topic.get("RO"), topic.get("CTA_RO")),
                            ("EN", topic.get("EN"), topic.get("CTA_EN"))):
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
    for lang in ("ro", "en"):
        cards = build.cards(topic, lang)
        a = alt.alt_for(cards)
        if len(a) != len(cards):
            fail("ALT", f"{slug}: {lang} has {len(cards)} frames but {len(a)} alt strings")
        for i, s in enumerate(a, 1):
            if not s.strip():
                fail("ALT", f"{slug}: {lang} frame {i} has empty alt text")
            if re.search(r"<[^>]+>", s):
                fail("ALT", f"{slug}: {lang} frame {i} alt text still contains markup")


def main():
    import topics
    only = sys.argv[1] if sys.argv[1:] else None
    print("preflight")
    check_identities()
    check_loss()
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
