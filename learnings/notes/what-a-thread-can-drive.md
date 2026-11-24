---
slug: what-a-thread-can-drive
title: Know which tools a Claude thread can run and which need Alex
dek: Kling, Recraft, ElevenLabs and Base44 run from a thread. Higgsfield, Flow and Firefly generation are by hand. Several file hosts are blocked from the cloud.
making: photo
tools: [kling, recraft, higgsfield, google-flow, firefly, adobe-express, base44, elevenlabs]
techniques: [workflow]
models: []
status: tested
cost_usable: n/a
back_office: private
date: 2026-11-23
updated: 2026-11-23
---

# Know which tools a Claude thread can run and which need Alex

Kling, Recraft, ElevenLabs and Base44 run from a thread. Higgsfield, Flow and Firefly generation are by hand. Several file hosts are blocked from the cloud.

## Reach, as of 2026-11-23

| Tool | From a thread | Notes |
| --- | --- | --- |
| Kling | Generates | Every job is charged. Quote the cost and ask first. Omni prompts name references as 图片1, 图片2. |
| Recraft | Generates, edits, upscales | Personal account. A Nano Banana Pro call with three reference images can pass the tool's 60-second limit. It then returns nothing but is still charged (3 timeouts cost 60 credits on 2026-11-24). Send one take per call, check the balance after each, and look in Recraft's own history before retrying. |
| ElevenLabs | Generates speech, images, video | Usage readout needs a reconnect. |
| Base44 | Builds, edits files, reads and writes data | Hand-coding with the file tools costs no builder credits. |
| Adobe | Edits, imports to Express, Firefly Boards | Can't generate new images or video. Firefly generation is by hand. |
| Higgsfield | Read only (balance, models, past results) | Alex generates by hand. |
| Google Flow, Veo, Gemini Omni | No connector | Alex generates by hand. |
| Photo Studio (Base44 app on fal) | Runs headless through its `studio` function (`run`, `tick`) | Details in project memory `odhc-photo-studio`. |

## Blocked from the cloud container (and the desktop VM)

- fal.media, res.cloudinary.com and media.base44.com return 403, so view those images in a browser.
- Creative Cloud storage (at.adobe.com) is unreachable, so Express uploads go through Alex's Mac (see [the Express playbook](../playbooks/live-text-in-adobe-express.md)).

## Small fixes that saved time

- Google Drive `create_file` fails on files under `/mnt/project-files`. Copy the file to `/home/user` first.
- The Sheets `update_values` tool parses input as if typed, so "9:16" alone becomes a time. Keep ratios inside longer text.
- The Base44 sandbox has no ffmpeg or numpy: `npm i ffmpeg-static` or `pip install --target /tmp/pylib numpy pillow`.
- Host every Base44 video in the app's media library.

## History

- 2026-11-24: Recraft timeouts still charge.
- 2026-11-23: Written from the week's threads.
