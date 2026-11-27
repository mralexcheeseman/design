---
slug: spend-credits-before-renewal
title: Pick where to run a model by what each credit costs
dek: The same model can cost very different amounts in two apps. Run it where it's cheapest, and use expiring credits first.
making: video
tools: [google-flow, firefly, higgsfield, kling, recraft, picsart]
techniques: [credit-planning]
models:
  - name: Veo 3.1 Lite, Fast and Quality
    tested: 2026-11-23
  - name: Nano Banana Pro
    tested: 2026-11-23
status: try
cost_usable: n/a
back_office: private
date: 2026-11-23
updated: 2026-11-25
---

# Pick where to run a model by what each credit costs

The same model can cost very different amounts in two apps. Run it where it's cheapest, and use expiring credits first.

Credit planning stays out of The Back Office. Balances and renewal dates live in project memory (`odhc-creative-tools`), since they change daily. This note keeps the unit prices, which change only when a vendor reprices. Re-check any price older than a month before planning with it.

## What to do

Alex's rule (2026-11-23): use every credit on every plan before it renews, and use free allowances as fully as possible, even when that means Alex generates by hand and shares the results back. Quote the cost before any paid run and wait for his OK.

## Prices seen on 2026-11-23

| Where | Model | Price |
| --- | --- | --- |
| Google Flow (AI Pro, 50 free credits a day) | Veo 3.1 Lite | 10 credits a clip |
| Google Flow | Veo 3.1 Fast / Quality | 20 / 100 credits a clip (both leave Flow on 5 Dec 2026) |
| Google Flow | Omni Flash 1.2 | 3 credits a second at 720p |
| Firefly | Firefly Video | 50 credits a second at 720p, 100 at 1080p |
| Firefly | Veo 3.1 Lite (partner) | 10 credits a second |
| Firefly | Nano Banana Pro (partner) | 40 credits an image |
| Firefly | Upscaler | 10 credits |
| Higgsfield Plus | Nano Banana Pro, Nano Banana 2, Soul 2, GPT Image 2 | Unlimited |
| Higgsfield Plus | Seedance 2.0 | about 22 credits per 5 s at 720p |
| Recraft | Nano Banana 2 edit / Nano Banana Pro edit | 11 / 20 credits |
| Kling | 3.0 Omni, 12 s, 1080p | 96 credits |
| Kling | Image 4.0, one still with references | 4 credits |
| fal | Nano Banana Pro, 2K | about $0.15 an image |

## Picsart, seen on 2026-11-25

Picsart's pricing page lists the models but no credit price per model, so read the cost on the Generate button and write it here after the first run.

| Where | Model | Price |
| --- | --- | --- |
| Picsart Professional | Flux.2 Klein stills | Unlimited |
| Picsart Professional | Background removal, batch editor (50 images at a time) | Included |
| Picsart Professional | Nano Banana 2.1, GPT Image 2.5, Seedream 5, Flux 3, Ideogram 4.5, Recraft V4 | Credits, price not listed |
| Picsart Professional | Kling 4.0 and 4.0 Omni, Seedance 2.0, MiniMax H3, Wan 3.0, LTX, Gemini Omni | Credits, price not listed |
| Picsart connector | Reframe video, render scenes to MP4 or stills | Free |

## Lessons

| Lesson | Status |
| --- | --- |
| `veo-lite-cheaper-in-flow`: Veo 3.1 Lite costs 10 Flow credits a clip, with 50 free credits a day, while the same model in Firefly costs 10 premium credits a second, so Firefly's Veo is for spending credits that are about to reset. | try |
| `picsart-for-what-nobody-else-has`: Kling, Seedance and Nano Banana run on their own plans, so spend Picsart credits on the models only Picsart has (MiniMax, Seedream, Wan) and on its free unlimited stills. That way no test runs twice. | try |
| `higgsfield-unlimited-for-shirt-stills`: Make Nano Banana Pro stills on Higgsfield's Unlimited plan before paying for them on fal. | try |

## History

- 2026-11-23: Prices gathered for the week-of-23-November test plan.
- 2026-11-25: Added Picsart Professional and the lesson `picsart-for-what-nobody-else-has`.
