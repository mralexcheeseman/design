---
slug: what-a-thread-can-drive
title: Know which tools a Claude thread can run and which need Alex
dek: Kling, Recraft, ElevenLabs and Base44 run from a thread. Higgsfield, Flow and Firefly generation are by hand. Several file hosts are blocked from the cloud.
making: photo
tools: [kling, recraft, higgsfield, google-flow, firefly, adobe-express, base44, elevenlabs, picsart]
techniques: [workflow]
models: []
status: tested
cost_usable: n/a
back_office: private
date: 2026-11-23
updated: 2026-11-25
---

# Know which tools a Claude thread can run and which need Alex

Kling, Recraft, ElevenLabs and Base44 run from a thread. Higgsfield, Flow and Firefly generation are by hand. Several file hosts are blocked from the cloud.

## Reach, as of 2026-11-23

| Tool | From a thread | Notes |
| --- | --- | --- |
| Kling | Generates | Every job is charged. Quote the cost and ask first. Omni prompts name references as 图片1, 图片2. |
| Recraft | Generates, edits, upscales | Personal account. |
| ElevenLabs | Generates speech, images, video | Usage readout needs a reconnect. |
| Base44 | Builds, edits files, reads and writes data | Hand-coding with the file tools costs no builder credits. |
| Adobe | Edits, imports to Express, Firefly Boards | Can't generate new images or video. Firefly generation is by hand. |
| Picsart | Reframes video, builds motion scenes (montage, captions, photo promos), transcribes, renders MP4 or stills, files to Picsart Drive, reads balance and brand kits | Can't generate new images or video: Alex generates on picsart.com. Reframe and export cost nothing. Sources must be public links. Some media analysis spends credits, so read the tool's description first. |
| Higgsfield | Read only (balance, models, past results) | Alex generates by hand. |
| Google Flow, Veo, Gemini Omni | No connector | Alex generates by hand. |
| Photo Studio (Base44 app on fal) | Runs headless through its `studio` function (`run`, `tick`) | Details in project memory `odhc-photo-studio`. |

## Blocked from the cloud container (and the desktop VM)

- fal.media, res.cloudinary.com and media.base44.com return 403, so view those images in a browser.
- Creative Cloud storage (at.adobe.com) is unreachable, so Express uploads go through Alex's Mac (see [the Express playbook](../playbooks/live-text-in-adobe-express.md)).
- Recraft's upload host (mcp.recraft.ai) and elevenlabsusercontent.com refuse the cloud container (2026-11-25), so a thread can't upload a local picture to Recraft or download an ElevenLabs file. Recraft image tools need a public image link.
- Adobe image tools accept only Adobe-trusted hosts, so a Drive link (lh3.googleusercontent.com) is refused.
- Making a Drive file public by link can be refused by the thread's own permission check. Alex made the ODHC shot references folder link-viewable on 25 Nov, so every file a thread puts there gets a working link for Recraft and Kling: `https://lh3.googleusercontent.com/d/<id>`. Recraft read these first time.
- Recraft results live on img.recraft.ai, which the cloud container can't reach, so a thread sees only a small preview. The Base44 sandbox (run_command on The Back Office) can fetch them. Alex downloads keepers from his Recraft library to file them in Drive.
- The Reference library in The Back Office (`/references`, entity `Reference`) lists every reference with its direct link. Add new references there and in the Drive folder together.

## Small fixes that saved time

- Google Drive `create_file` fails on files under `/mnt/project-files` or `/tmp`. Copy the file into the working directory (for example `/home/claude/up`) first.
- The Drive connector won't download a file over 10 MB. Higgsfield 2K PNGs run 7 to 11 MB, so ask for JPEG exports of the big ones.
- The Sheets `update_values` tool parses input as if typed, so "9:16" alone becomes a time. Keep ratios inside longer text.
- The Base44 sandbox has no ffmpeg or numpy: `npm i ffmpeg-static` or `pip install --target /tmp/pylib numpy pillow`.
- Host every Base44 video in the app's media library.

## History

- 2026-11-23: Written from the week's threads.
- 2026-11-25: Added Picsart (connector checked the same day).
- 2026-11-25: Added the Recraft upload, Adobe host, Drive sharing and 10 MB limits found in the 48-hour plan tests.
- 2026-11-25: References folder link-viewable; Recraft reads Drive links; img.recraft.ai blocked from the cloud; reference library in The Back Office.
