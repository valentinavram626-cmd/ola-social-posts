#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Alt text for every frame, derived from the card itself.

On 5 November 2026 a whole day of posts went out with `mediaAltText` null on
every image. The fix is not a reminder to write alt text — it is removing the
chance to forget. Alt text is now computed from the card that is already
written, so a frame cannot exist without it.

    from alt import alt_for
    alt_for(cards)   # -> one string per card, same length as the media list
"""
import html, re

MAX = 120


def _plain(s):
    """Card copy is HTML (<em>, <b>, <cur>); alt text is not."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", str(s or "")))).strip()


def _clip(s):
    if len(s) <= MAX:
        return s
    cut = s[:MAX].rsplit(" ", 1)[0].rstrip(" ,;:—-")
    return cut + "…"


def alt_for(cards):
    """One alt string per card, in order.

    A hook leads with its headline, a step with its label and sentence, the
    closing card with the ask. Every card has at least one of these fields, so
    the list is always the same length as the frames — which is what the
    scheduler checks before it sends anything.
    """
    out = []
    for c in cards:
        t = c.get("type")
        if t == "hook":
            s = _plain(c.get("h1")) or _plain(c.get("say"))
        elif t == "cta":
            s = _plain(c.get("h1"))
            say = _plain(c.get("say"))
            if say:
                s = f"{s} {say}" if s else say
        elif t == "solo":
            s = _plain(c.get("h1")) or _plain(c.get("kicker"))
        else:                                   # step, and the retired ask
            label, say = _plain(c.get("step")), _plain(c.get("say"))
            s = f"{label}: {say}" if label and say else (label or say)
        s = _clip(s) or "Ola Accountancy — Luton și Birmingham."
        out.append(s)
    return out


if __name__ == "__main__":
    import sys, topics, build
    slug = sys.argv[1] if sys.argv[1:] else None
    for sl, t in topics.BY_SLUG.items():
        if slug and sl != slug:
            continue
        print(f"\n=== {sl}")
        for lang in ("ro", "en"):
            print(f"  [{lang}]")
            for i, a in enumerate(alt_for(build.cards(t, lang)), 1):
                print(f"    {i:02d}  {a}")
