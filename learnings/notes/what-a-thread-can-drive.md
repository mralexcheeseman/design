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
| Recraft | Generates, edits, upscales | Personal account. A Nano Banana Pro call with three reference images can pass the tool's 60-second limit. It then returns nothing but is still charged (3 timeouts cost 60 credits on 2026-11-24). Send one take per call, check the balance after each, and look in Recraft's own history before retrying. |
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
- kling.ai (Kling's file upload) is refused, so Kling subjects go up from Alex's Mac, because Kling refuses Drive links for subjects. Image-to-image inputs can be Drive links (see below). The upload route that works: start a Remote Control session on the iMac, point it at the files through Google Drive for Desktop, and have it run Kling's `file_upload` and post each file to the upload link straight away (a link lasts 10 minutes). Kling's result links (s15-kling.klingai.com) are refused too; file them to Drive with Zapier's Upload File, giving the new name without an extension (it adds one).
- img.recraft.ai is refused; file Recraft results to Drive with Zapier's Upload File, named by shot-sheet row.
- Creative Cloud storage (at.adobe.com) is unreachable, so Express uploads go through Alex's Mac (see [the Express playbook](../playbooks/live-text-in-adobe-express.md)).

## Small fixes that saved time

- Google Drive `create_file` fails on files under `/mnt/project-files`. Copy the file to `/home/user` first.
- The Sheets `update_values` tool parses input as if typed, so "9:16" alone becomes a time. Keep ratios inside longer text.
- The Base44 sandbox has no ffmpeg or numpy: `npm i ffmpeg-static` or `pip install --target /tmp/pylib numpy pillow`.
- Host every Base44 video in the app's media library.
- To bring a Recraft result into the container when img.recraft.ai is refused: Zapier's Google Drive Upload File takes the Recraft URL and files it in ODHC shot results under its row name, then Drive `download_file_content` saves the full-size picture locally (its path is in the result) without filling the conversation.
- Nano Banana and Nano Banana Pro run only on the Gemini app or Flow, by Alex's hand (his rule, 27 Nov). A thread never runs them through Recraft, Kling, ElevenLabs or any other route: it writes the prompt and hands it over. On 25 Nov a thread broke this rule for test T3, and Recraft timed out on 5 of 6 calls while still charging.
- Kling takes link-shared Drive files at `https://lh3.googleusercontent.com/d/<id>` as references, so its `file_upload` isn't needed (kling.ai upload is refused from the cloud). Its result host s15-kling.klingai.com is refused too, so file results through the Zapier-to-Drive route above.

- Kling takes a public res.cloudinary.com link as `first_image` or `tail_image` even though this container can't open it. A Cloudinary crop in the link (`c_crop,ar_4:5,w_0.55,g_auto:subject/c_scale,w_1615/`) makes a tail frame without uploading anything new.
- Kling result files over 10 MB can't come back through Drive's `download_file_content`, so a thread can't watch its own clips. File them to Drive with Zapier and let Alex score them.
- elevenlabsusercontent.com is reachable, so ElevenLabs audio downloads straight into the container and uploads to Drive with `create_file`.

## History

- 2026-11-24: Recraft timeouts still charge.
- 2026-11-23: Written from the week's threads.
- 2026-11-25: Added Picsart (connector checked the same day).
- 2026-11-27: Nano Banana runs only on Gemini or Flow, by hand (Alex). Removed the Kling and ElevenLabs routes.
- 2026-11-25: T3 baselines: Kling takes Drive links, Recraft timed out 5 of 6.
- 2026-11-25: Kling upload host blocked (locked cast thread).
- 2026-11-25: Hotel Marisol run: blocked Recraft and Drive hosts, the Zapier-to-Drive route, Recraft timeouts.
- 2026-11-27: Kling takes Cloudinary links and crops; big Kling clips can't be watched from a thread; ElevenLabs audio downloads directly (go rows run 27 Nov).
- 2026-11-27: Kling uploads through Remote Control on the iMac; Kling result links refused (locked cast thread).
