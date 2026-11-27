---
slug: one-hero-many-cuts
title: Get four posts out of every keeper before making new pictures
dek: Each picture that scores 12 of 15 or more becomes a feed post, a story, a carousel and a clip. The Cuts tab in the shot sheet tracks all four.
making: social
tools: [adobe-express, picsart, kling, higgsfield]
techniques: [workflow, credit-planning]
models: []
status: try
cost_usable: Free for the feed post, story and carousel. The clip costs whatever the picked video tool charges
back_office: private
date: 2026-11-25
updated: 2026-11-25
---

# Get four posts out of every keeper before making new pictures

Each picture that scores 12 of 15 or more becomes a feed post, a story, a carousel and a clip. The Cuts tab in the shot sheet tracks all four.

## What happened

By 25 November the Results tab held 112 files and 15 keepers. Four of those keepers had a 9:16 story cut. None had a feed post built, a carousel or a clip. Meanwhile new rows kept going into My shots, so the best pictures sat in Drive while credits went on fresh takes that mostly scored 9 to 11.

Alex agreed the rule on 25 November ("Do it all"): a strong still earns four posts before anything new gets generated.

## What to do

1. **A keeper becomes a hero.** Every take at 12 of 15 or more gets a row on the Cuts tab: hero ID and version, shot, score, Drive link. The Monday check-in adds new keepers from Results; anyone can add one by hand.
2. **Make the four cuts in this order.**
   - **Feed post**: 4:5, built in the Express social factory with live text (playbook `live-text-in-adobe-express`), caption in the Social Planner.
   - **Story**: 9:16. Expand the frame with Adobe generative expand or reframe it in Picsart (playbook `make-vertical-cuts-for-stories`, design PR #28).
   - **Carousel**: the hero plus one or two slides from the same scene (a detail crop, the guest-book line from `look.json`, the product shot).
   - **Clip**: the hero as first frame (and last frame for a push-in) in the video tool that wins V1. Never two different stills stitched together (playbook `stop-buildings-drifting`).
3. **Tick each cut when it exists** and put its link in Links and notes. Made counts the ticks and Next cut names the gap. A row turns green at four.
4. **Unticked heroes come first.** Monday's plan books open cuts before any new picture row for that hotel. Two kinds of row can still run: a test with a written question (V1, T2 and so on), and mop-up rows for a pool that lapses within 7 days.
5. **Alex OKs the cuts on Friday.** The Friday review lists every hero with cuts made and Your OK unticked. Whoever adds a later cut unticks Your OK, so the hero comes back the next Friday.

## Where it lives

| Place | What it holds |
| --- | --- |
| Shot sheet, Cuts tab | One row per hero, the four ticks, Made, Next cut, Your OK |
| Shot sheet, Friday review | Block 2 (cuts to OK) and block 5 (next week's cuts, best score first) |
| ODHC Social Planner | The finished feed, story and carousel posts, with `express_link` |

## Cost

Three of the four cuts are free: Express import, generative expand and Picsart reframe charged nothing on 25 November. The clip is the one paid cut. At Kling 3.0 Turbo prices a 5-second clip is 40 credits (row K1).

## Lessons

| Lesson | Status |
| --- | --- |
| `cuts-before-new`: Book a keeper's four cuts before new picture rows for that hotel; tests and lapsing-credit mop-ups are the only exceptions. | try |
| `same-still-clip`: The clip starts from the hero itself, so the shirt and building already carry the approved score. | tested |

## Next to try

Count posts per keeper on 18 December. If heroes average three cuts or more, the rule is working.

## History

- 2026-11-25: First written. Cuts tab seeded with the 15 keepers in Results, four with a story cut.
