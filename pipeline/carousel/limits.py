#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every network's caption limit, in one table, checked not remembered.

Valentin, 6 November 2026: "pune ca memo sa nu se mai depășească limita
niciodată." A memo is something to forget, so this is a function instead.
Nothing is scheduled without passing through it.

    from limits import check, fits
    check(caption, "pinterest")      # raises CaptionTooLong with the numbers
    fits(caption, "threads")         # -> (True/False, length, limit)

WHY THIS FILE EXISTS. Three days, three platforms, the same fault, and not one
of the error messages said "too long":

  4-5 Nov  Threads   638 and 755 characters against a 500 limit.
           Metricool said `Media container not created by unknown cause`,
           which points at the images. The images were fine — the same four
           published to Facebook and Instagram from the same post.
  6 Nov    Pinterest 921, 929, 941 and 1046 characters against 800.
           Metricool said `Code: 400 - Invalid request` and then quoted the
           first 75 characters of the description back, which reads like a
           complaint about the words rather than their number.
  6 Nov    Instagram and TikTok, 2277 characters against 2200. Held by the
           Gatekeeper before they could fail — and they were only over
           because its own repair rounds had GROWN the caption from 1998.

That last one is the lesson worth keeping: a repair that adds a sentence can
push a caption over a limit nobody was measuring. So the check belongs after
every edit, not only after the first draft.
"""

# Characters, not bytes. Verified against live publishing failures and the
# platforms' published limits, November 2026.
LIMITS = {
    "instagram":  2200,   # caption
    "facebook":  63206,   # effectively unlimited for our copy
    "threads":     500,   # 4-5 Nov: 638 and 755 both failed, 488 published
    "tiktok":     2200,   # caption, photo and video posts alike
    "linkedin":   3000,   # post body
    "bluesky":     300,   # 3 Nov: the API rejects over this
    "pinterest":   800,   # pin description; pinTitle is a separate 100
    "gmb":        1500,   # Google Business "publication" text
}

TITLE_LIMITS = {
    "pinterest": 100,     # pinTitle
}

# A Story carries no caption of its own, so length never applies to it.
NO_CAPTION = {"story"}


class CaptionTooLong(ValueError):
    pass


def fits(text, network, *, kind=None):
    """(ok, length, limit). An unknown network is allowed through, reported as limit 0."""
    if kind and kind.lower() in NO_CAPTION:
        return True, 0, 0
    n = len(text or "")
    lim = LIMITS.get(network.lower())
    if lim is None:
        return True, n, 0
    return n <= lim, n, lim


def check(text, network, *, kind=None, label=""):
    """Raise unless the caption fits. Use this before scheduling, every time."""
    ok, n, lim = fits(text, network, kind=kind)
    if not ok:
        raise CaptionTooLong(
            f"{label or network}: {n} characters against a {lim} limit on "
            f"{network} — over by {n - lim}. Shorten the caption; do not "
            f"schedule it and do not wait for the platform to tell you, "
            f"because it will not say the length is the problem."
        )
    return n


def check_title(title, network, *, label=""):
    lim = TITLE_LIMITS.get(network.lower())
    if lim and len(title or "") > lim:
        raise CaptionTooLong(
            f"{label or network}: title is {len(title)} characters against a "
            f"{lim} limit on {network}."
        )
    return len(title or "")


def report(items):
    """items: iterable of (label, network, text). Returns the lines and a pass flag.

    For the end of a scheduling run: print it, put it in the report, and let
    the numbers be the evidence rather than a claim that the lengths were fine.
    """
    lines, ok_all = [], True
    for label, network, text in items:
        ok, n, lim = fits(text, network)
        ok_all &= ok
        lines.append(f"{label:<28}{network:<12}{n:>6}/{lim:<6}{'OVER' if not ok else 'ok'}")
    return lines, ok_all


if __name__ == "__main__":
    print(f"{'network':<12}{'caption':>9}{'title':>8}")
    for net in sorted(LIMITS):
        print(f"{net:<12}{LIMITS[net]:>9}{TITLE_LIMITS.get(net, '-'):>8}")
