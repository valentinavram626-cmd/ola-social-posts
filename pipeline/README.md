# Ola Accountancy – weekly reel production pipeline

Runs every **Wednesday 23:00 Europe/London** in a scheduled Claude session. Goal: by Thursday morning Valentin
has an approval page for the week starting **Friday** (7 days × 15 posts). Nothing is scheduled in Metricool
until he replies "aprobat".

## Fixed rules
- 15 posts/day, 7 days: 14 text reels + 1 Valentin video (19:30). Slots 07:30–21:30 hourly.
- Romanian on Instagram (Reel + Story), Facebook (Reel + Story), TikTok (max 12/day), Threads.
- English on YouTube Shorts, LinkedIn (org page), Bluesky (video), GBP (1/day, no phone number), Pinterest (board "Ola Tax", 1/day).
- Valentin's video only on RO networks; on EN networks that slot gets the `extra` English reel.
- Text must be fully visible from frame 0 (reel2.js does this – never add entry animations to scene 1).
- Reels are 22 s, 3 scenes, original synthesized music (music2.py, variants 0–5).
- Compliance: no tax-escape promises, no guarantees, no client details, no "chartered", prices VAT-inclusive
  (first consultation £120 incl. VAT / 30 min; financial consultation £420 incl. VAT / 60 min). Facts checked on GOV.UK.
- Every figure/date in a reel must be verified on GOV.UK the same week (rates change in April and at Budgets).

## Steps for the scheduled run
1. `git clone` this repo; `cd pipeline`.
2. Decide the week: first day = next Friday (`W=YYYY-MM-DD`).
3. Write topics: `week_ro.json`, `week_en.json` (same shape as the current files; 14 items/day + 1 `extra` per day
   in `week_plan.json`). Do NOT reuse keys listed in `used_topics.json` for the last 3 weeks. `topics.py` holds
   the bank of past topics as style examples (tag, figure, headline, 3 lines, caption, hashtags, bluesky ≤ 300 chars).
   Mix: deadlines of the coming month, HMRC changes, self-employed, Ltd, VAT, family allowances, Ola services.
4. Write `week_valentin.json` (day → {file,title,caption}) using edited videos in `../reels/valentin/` (rotate; new raw
   videos go through `valentin/make.sh` = captions + hook + logo + end card).
5. `bash run_week.sh $W` (≈2 h on 2 CPUs). Then `python3 gen_week.py $W` → `week_approval.html` + `week_schedule.json`.
6. Append the week's keys to `used_topics.json`, `git add ../reels/week-$W pipeline && git commit && git push`.
7. Publish `week_approval.html` as an artifact and message Valentin (Romanian, "Sir") with the link. STOP.
8. After "aprobat": schedule every slot from `week_schedule.json` in Metricool (brand 7561492, Europe/London):
   RO reel → one post {facebook REEL, instagram REEL, tiktok (≤12/day), threads} + one STORY post {facebook, instagram}
   2 min later; EN reel → {linkedin POST, youtube short} + bluesky post (bsky text, video) + GBP/Pinterest once a day.
   Media URL = raw GitHub URL of the mp4. Then update the Publishing QA agent window.
