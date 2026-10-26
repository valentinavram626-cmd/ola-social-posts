#!/usr/bin/env python3
"""Story-safe cut for Instagram/Facebook Stories.

Rule (Valentin, 26 Oct 2026): a Story may be at most 59 s. Never speed a video up — it looks
unprofessional. Cut hard at 59 s; whoever wants the rest watches the Reel.

Usage:
  python3 story_cut.py <video.mp4> [more.mp4 ...]
  python3 story_cut.py --week 2026-10-30      # process every mp4 in ../reels/week-<W>/

For each input longer than STORY_MAX seconds it writes <name>.story.mp4 next to the source
(same encoding profile, 0.4 s audio fade-out so the cut doesn't click) and prints a JSON map
{source_basename: story_basename}. Inputs within the limit are left alone and map to themselves.
"""
import json, os, subprocess, sys

STORY_MAX = 59.0      # hard ceiling for a Story clip (platform limit is 60 s)
FADE = 0.4            # audio fade-out length at the cut, seconds


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def story_version(path):
    """Return basename (without .mp4) to use for the Story post; creates the cut if needed."""
    base = os.path.splitext(os.path.basename(path))[0]
    if base.endswith(".story"):
        return base
    d = duration(path)
    if d <= STORY_MAX:
        return base
    out = os.path.join(os.path.dirname(path), base + ".story.mp4")
    if os.path.exists(out) and abs(duration(out) - STORY_MAX) < 0.2:
        return base + ".story"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-i", path, "-t", f"{STORY_MAX:.3f}",
        "-af", f"afade=t=out:st={STORY_MAX - FADE:.3f}:d={FADE}",
        "-c:v", "libx264", "-crf", "22", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], check=True)
    got = duration(out)
    assert got <= 60.0, f"{out} is {got:.2f}s – still over the Story limit"
    print(f"story cut: {base}.mp4 {d:.1f}s -> {base}.story.mp4 {got:.1f}s", file=sys.stderr)
    return base + ".story"


def main(argv):
    if argv and argv[0] == "--week":
        wk = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reels", f"week-{argv[1]}")
        files = sorted(os.path.join(wk, f) for f in os.listdir(wk)
                       if f.endswith(".mp4") and not f.endswith(".story.mp4"))
    else:
        files = argv
    result = {os.path.splitext(os.path.basename(f))[0]: story_version(f) for f in files}
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
