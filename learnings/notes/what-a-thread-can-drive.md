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
| Kling | Generates | Every job is charged. Quote the cost and ask first. Omni prompts name references as 图片1, 图片2. Image inputs need a public link: a Drive file shared by link works as `https://lh3.googleusercontent.com/d/<id>`, the `uc?export=download` link fails. 3.0 Turbo costs 50 for 5s at 1080p, 4.0 Flash 30 for 5s at 720p. Take the `urlWithoutWatermark` result. |
| Recraft | Generates, edits, upscales | Personal account. |
| ElevenLabs | Generates speech, images, video | Video covers Veo 3.1 (Lite, Fast, Quality), Kling 3 Pro and 4, Seedance, MiniMax, Wan and Runway on Creator credits. Pass `estimate_only` to price a run for free. Don't run Veo here: Alex runs Veo by hand in Flow on his Google credits. Usage readout needs a reconnect. |
| Base44 | Builds, edits files, reads and writes data | Hand-coding with the file tools costs no builder credits. |
| Adobe | Edits, imports to Express, Firefly Boards | Can't generate new images or video. Firefly generation is by hand. |
| Picsart | Reframes video, builds motion scenes (montage, captions, photo promos), transcribes, renders MP4 or stills, files to Picsart Drive, reads balance and brand kits | Can't generate new images or video: Alex generates on picsart.com. Reframe and export cost nothing. Sources must be public links. Some media analysis spends credits, so read the tool's description first. |
| Higgsfield | Read only (balance, models, past results) | Alex generates by hand: stills on the website or through the ChatGPT Higgsfield app (Alex, 25 Nov: fine for photos). Not for video: Seedance through it was a clear no (V2a). |
| Google Flow, Veo, Gemini Omni | No connector | Alex generates by hand. Flow can also edit a finished clip from a written instruction ("Describe how to edit this video"): a candidate fix for drift, by hand only, not yet tested (seen 2026-11-25). |
| Photo Studio (Base44 app on fal) | Runs headless through its `studio` function (`run`, `tick`) | Details in project memory `odhc-photo-studio`. |

## Blocked from the cloud container (and the desktop VM)

- fal.media, res.cloudinary.com and media.base44.com return 403, so view those images in a browser.
- Some sessions also refuse img.recraft.ai, mcp.recraft.ai (Recraft's upload link), lh3.googleusercontent.com and drive.google.com. Recraft itself can still read link-shared Drive files at `https://lh3.googleusercontent.com/d/<id>`, so put references in the Drive references folder and pass that link.
- kling.ai (Kling's file upload) is refused, so Kling subjects and Kling image-to-image inputs go up from Alex's Mac. Kling refuses Drive links for subjects.
- img.recraft.ai is refused; file Recraft results to Drive with Zapier's Upload File, named by shot-sheet row.
- Creative Cloud storage (at.adobe.com) is unreachable, so Express uploads go through Alex's Mac (see [the Express playbook](../playbooks/live-text-in-adobe-express.md)).

## Small fixes that saved time

- Google Drive `create_file` fails on files under `/mnt/project-files`. Copy the file to `/home/user` first.
- The Sheets `update_values` tool parses input as if typed, so "9:16" alone becomes a time. Keep ratios inside longer text.
- The Base44 sandbox has no ffmpeg or numpy: `npm i ffmpeg-static` or `pip install --target /tmp/pylib numpy pillow`.
- Host every Base44 video in the app's media library.
- To bring a Recraft result into the container when img.recraft.ai is refused: Zapier's Google Drive Upload File takes the Recraft URL and files it in ODHC shot results under its row name, then Drive `download_file_content` saves the full-size picture locally (its path is in the result) without filling the conversation.
- Recraft's Nano Banana Pro calls time out at 60 seconds about half the time on 25 Nov, with or without a reference image, and most still charge 20. The picture lands only in Alex's Recraft library. Check `get_user` after every timeout before trying again, or run the same model on ElevenLabs (`gemini-3-pro-image`), which returns at once and is polled, so nothing is lost.

## History

- 2026-11-23: Written from the week's threads.
- 2026-11-25: ElevenLabs video models listed.
- 2026-11-25: Added Picsart (connector checked the same day).
- 2026-11-25: Kling input links, prices and the Base44 copy route, from the December Reels test.
- 2026-11-25: Veo is by hand in Flow, never through ElevenLabs.
- 2026-11-25: Flow's text edit of a finished clip noted as a drift fix to try.
- 2026-11-25: Higgsfield through ChatGPT: fine for stills (Alex), out for video (V2a).
- 2026-11-25: Kling upload host blocked (locked cast thread).
- 2026-11-25: Hotel Marisol run: blocked Recraft and Drive hosts, the Zapier-to-Drive route, Recraft timeouts.
