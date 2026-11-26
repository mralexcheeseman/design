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
- Video too big for the Drive connector (10 MB limit): do the whole render in the Base44 sandbox with `run_command`. It reaches the Kling CDN, ElevenLabs results and `lh3` (add `=s0` for full size). `npm i ffmpeg-static ffprobe-static` gives ffmpeg there.
- To host a file made in the Base44 sandbox: ask Kling `file_upload` for a ticket, POST the file from the sandbox to `https://kling.ai/api/mcp/files` (fields `ticket` and `file`), then pass the public Kling link to Base44 `upload_app_asset` and to Zapier's Drive upload.
- Brand type for video: Adobe Fonts (use.typekit.net) is blocked in the cloud. Import the words to Express as HTML, `download_design` as PNG, and key the black out (see the reel playbook).

## History

- 2026-11-23: Written from the week's threads.
- 2026-11-25: Added Picsart (connector checked the same day).
- 2026-11-25: Kling upload host blocked (locked cast thread).
- 2026-11-25: Hotel Marisol run: blocked Recraft and Drive hosts, the Zapier-to-Drive route, Recraft timeouts.
- 2026-11-25: Reel line run: sandbox render, Kling file hosting, type through Express.
