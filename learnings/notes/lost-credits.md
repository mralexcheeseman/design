---
slug: lost-credits
title: Log every credit a tool charges for nothing
dek: When a call times out, fails or repeats itself and still charges, write it here the same day, so Alex can claim it back from the provider.
making: photo
tools: [recraft, firefly]
techniques: [credit-planning]
models:
  - name: Nano Banana Pro
    tested: 2026-11-25
status: tested
cost_usable: n/a
back_office: private
date: 2026-11-26
updated: 2026-11-26
---

# Log every credit a tool charges for nothing

When a call times out, fails or repeats itself and still charges, write it here the same day, so Alex can claim it back from the provider.

Alex's rule (26 Nov 2026): "keep a track of any additional credits we lose, I can always go back to them."

## How to log a loss

1. Add one row per lost call or batch to the log below, the day it happens.
2. Give the shot ID, the model, the images and the credits. Mark the amount **confirmed** (a balance reading or the provider's own charge matches it) or **estimated** (worked out from a unit price).
3. Say who caused it. A provider fault (timeout, failed render, charged with nothing back) can be claimed. Our own mistake (a duplicate prompt, a wrong setting) is logged so we stop repeating it, and is not claimed.
4. Read the balance (`get_user` for Recraft) after any timeout and before trying again.
5. Claim status: `not claimed`, `claimed <date>`, `refunded <date>`, `declined <date>`, or `ours, not claimable`.

## Log

| Date | Tool | Model | Shot IDs | Images | Credits | Sure? | Cause | Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-24 | Recraft | Nano Banana Pro, 3 refs | not recorded | 3 | 60 | confirmed | Timed out, charged, no image | refunded 2026-11-26 (Recraft: Gemini Flex dropped, fell back to Runware) |
| 2026-11-25 | Recraft | Nano Banana Pro edit, 2 a call | R1c, R1f | 4 | 80 | confirmed (3,711 to 3,371 matches the run log) | Timed out at 60 s, charged | claim drafted 2026-11-26, awaiting Alex |
| 2026-11-25 | Recraft | Nano Banana Pro edit, 1 a call | R1h, R1j | 2 | 40 | confirmed (same log) | Timed out at 60 s, charged; may sit in the web library | claim drafted 2026-11-26, awaiting Alex |
| 2026-11-25 | Recraft | Nano Banana Pro, 1 a call | Hotel Marisol lifestyle stills (IDs not recorded) | 3 | 60 | confirmed from the Marisol thread ("1 kept, 3 lost") | Timed out at 60 s, charged | claim drafted 2026-11-26, awaiting Alex |
| 2026-11-25 | Recraft | V4.1 raster with a custom style, 2 a call | LK1 to LK4 | 4 | about 8 | estimated (about 2 a picture) | Timed out at 60 s twice, charged | claim drafted 2026-11-26, awaiting Alex |
| 2026-11-26 | Firefly | Nano Banana Pro, 4:5, 2K | OP8 to MA10 (21 good-life stills) | 21 | 840 | confirmed from the thread's run report | Ours: every prompt ran twice and Firefly returned the same picture both times | ours, not claimable |

## Totals

- Recraft, 25 Nov, still outstanding: 188 credits for 13 images over 9 calls (180 confirmed, about 8 estimated). Claim drafted 26 Nov, awaiting Alex.
- Recraft, 24 Nov: 60 credits, refunded 26 Nov.
- Firefly, 26 Nov, our own fault: 840 credits.

## Balance gap to check

Recraft read 3,040 on 26 Nov at 11:55 UTC. Working from 3,371 after the R1 batch, the logged spend (120 for Marisol, about 16 for the style test) and the 60 refund give about 3,295. About 255 credits are not explained by any thread's log. Check Recraft's usage history before claiming anything more.

## Lessons

| Lesson | Status |
| --- | --- |
| `recraft-timeouts-still-charge`: Recraft calls through the connector give up at 60 seconds while the job keeps running and charges. Ask for one image a call and read the balance after every timeout. | tested |
| `vary-the-second-take`: A second take with the same prompt in Firefly's Nano Banana Pro returns the same picture, so write a different prompt for every extra take before the run starts. Now a pre-run rule in `learnings/README.md`. | tested |

## History

- 2026-11-27: The two lessons became pre-run rules at the top of `learnings/README.md`, at Alex's request.
- 2026-11-26: Started from the Recraft claim thread with every loss logged so far.
