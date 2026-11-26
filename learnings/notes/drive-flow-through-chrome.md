---
slug: drive-flow-through-chrome
title: Run Google Flow from a thread through Alex's Chrome
dek: Flow has no connector, but a thread with Claude in Chrome can queue stills and Veo clips in Alex's own signed-in Flow. Nano Banana Pro stills cost no Flow credits there, and 12 Veo clips rendered in about three minutes.
making: video
tools: [google-flow, nano-banana-pro]
techniques: [workflow, credit-planning]
models:
  - name: Nano Banana Pro (Flow)
    tested: 2026-11-25
  - name: Veo 3.1 Lite (Flow)
    tested: 2026-11-25
  - name: Veo 3.1 Fast (Flow)
    tested: 2026-11-25
status: tested
cost_usable: Stills free; Veo Lite 10 Flow credits a clip, Fast 20
back_office: private
date: 2026-11-25
updated: 2026-11-25
---

# Run Google Flow from a thread through Alex's Chrome

Flow has no connector, but a thread with Claude in Chrome can queue stills and Veo clips in Alex's own signed-in Flow. Nano Banana Pro stills cost no Flow credits there, and 12 Veo clips rendered in about three minutes.

## What happened

Until 25 November every Flow run was by hand: a thread wrote prompts, Alex pasted them. That afternoon a thread drove Flow in his Chrome instead. The stills run queued the storytelling shot list (IDs like GV3, SO4, MA2) on Nano Banana Pro and Alex picked 40 keepers, now filed in ODHC shot results as `<ID>-v1-flow-take<N>.jpg`.

In the evening Alex said "You do this via chrome" for the December Reels pack. The thread opened Flow in Browser 1, set Text to video, 9:16, 8 seconds, one output, and queued 12 prompts back to back: clips 1 to 8 on Veo 3.1 Lite and 9 to 12 on Veo 3.1 Fast, before Fast leaves Flow on 5 December. All 12 had rendered about three minutes after the first one went in, for 160 credits (the day's 50 free ones went first). From the thumbnails most back prints read (LIFEGUARD / HÔTEL SOLVANE, SECURITY, POOL BOY, HEAD GARDENER); the clifftop towels clip (H2e) shows only "BOY" and may need a second go.

Two Chromes were connected to Claude, so the thread had to ask which one held Alex's Google sign-in. It recommended Browser 2; Alex picked Browser 1, the signed-in one.

## What to do

1. Ask which connected browser is signed in to Google, then note it in project memory so the next thread doesn't ask.
2. Stills: open a Flow project, pick Nano Banana Pro, paste prompts one after another without waiting. Flow has no queue limit; 10 prompts took 3 browser calls.
3. Video: Video, then Ingredients with no media attached (that is text to video). Pick 9:16, the model, x1. Type the prompt, click the arrow, type the next one straight away.
4. Leave picking to Alex. He hearts the keepers and bulk downloads them into ODHC shot results; the thread names, crops and logs them (see [name results from the prompt](name-results-from-the-prompt.md)).

## Limits

- Flow won't take an uploaded reference file from a thread, so lettering on shirts is the model's own. Check every back print; mend misses in Firefly Generative Fill.
- Flow stills render 3:4. Crop to 4:5 (864 by 1080) for the feed.
- Veo is Alex's call on his Google credits. A thread queues it only when he asks in that thread, and quotes the credits first.

## Lessons

| Lesson | Status |
| --- | --- |
| `flow-stills-free-in-chrome`: Nano Banana Pro stills in Flow cost 0 Flow credits, so they are the first route for any still that needs no uploaded reference. | tested |
| `queue-flow-back-to-back`: Submit every Flow prompt without waiting for the last one; 12 Veo clips rendered in about three minutes. | tested |
| `flow-no-reference-upload`: A thread can't attach reference files in Flow, so shirt lettering is the model's own and needs checking on every take. | tested |
| `ask-which-chrome`: With two Chromes connected, ask which one is signed in to Google before queueing anything. | tested |

## History

- 2026-11-25: Written from the stills run (40 keepers) and the 12-clip December Reels run.
