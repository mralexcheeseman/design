---
slug: portrait-first-frames-for-video
title: Make 9:16 first frames for video without changing the picture
dek: Crop the 4:5 still to 9:16 around the wearer. Every pixel of the person and the print stays as it was, it costs nothing, and it takes seconds.
making: video
tools: [higgsfield, google-flow, adobe-express, recraft]
techniques: [first-last-frame]
models:
  - name: Seedance 2.0 on Higgsfield (via the ChatGPT app)
    tested: 2026-11-25
status: tested
cost_usable: Free
back_office: unpublished
date: 2026-11-25
updated: 2026-11-25
---

# Make 9:16 first frames for video without changing the picture

Crop the 4:5 still to 9:16 around the wearer. Every pixel of the person and the print stays as it was, it costs nothing, and it takes seconds.

## What happened

We wanted a Reel from the Lifeguard cove still. Seedance 2.0's image-to-video has no aspect setting, so it follows the first frame, and our still was 4:5. The run stopped before spending anything.

We tried two ways to make it 9:16. Generative expand (Adobe, or Nano Banana Pro asked to extend the canvas) adds picture above and below, but Adobe only reads images from its own trusted hosts and Recraft's request timed out without charging. Expanding also regenerates or blends the edges, which is where the print and faces drift.

A crop worked first time. A 1856 by 2304 still crops to 1296 by 2304, and a 1690 by 2112 still to 1188 by 2112. That is above 1080 wide, so it holds up at 720p and 1080p. Seven keepers took a few minutes.

## What to do

1. Keep the full height and cut the width to height × 9 ÷ 16.
2. Centre the cut on the wearer, then nudge it so the second subject (a waiter, a swan, a child) stays in.
3. Check the strip of contact sheets side by side before any paid video run.
4. Expand only when the crop would cut a person in half. In our seven, that was one boat in one picture, and we accepted the loss.

## Prompt (generic)

No prompt. A crop in any editor, or this in Python:

```
from PIL import Image
im = Image.open("[still]").convert("RGB"); W, H = im.size; w = round(H * 9 / 16)
x = max(0, min(W - w, int([centre 0 to 1] * W - w / 2)))
im.crop((x, 0, x + w, H)).save("[row]-[hotel]-[scene]-916-v1.jpg", quality=93)
```

## Prompt we used (Off Duty Hotel Club)

The same code. Centres used: Lifeguard cove 0.55, H1c 0.42, H1d 0.60, H2b 0.55, H2e 0.70, H3 0.62, H3b 0.62.

## Settings

| Setting | Value |
| --- | --- |
| Ratio | 9:16, full height kept |
| Output | JPEG, quality 93 |
| Name | `<row>-<hotel>-<scene>-916-v1.jpg` in ODHC shot results |

## References

- Source stills: the 4:5 keepers in Drive "ODHC shot results".

## Cost

Free. No credits, no generation.

## Lessons

| Lesson | Status |
| --- | --- |
| `crop-before-expand`: A 9:16 crop of a 4:5 still keeps the wearer and print untouched and fits 1080p video; expand only when the crop would cut a person. | tested |
| `seedance-follows-the-frame`: Seedance 2.0 image-to-video on Higgsfield has no aspect setting, so the first frame must already be 9:16. | tested |
| `expand-needs-a-trusted-link`: Adobe generative expand only accepts images on Adobe's own hosts, so a Drive link is refused. | tested |

## Next to try

Run the same crop on the first-frame of a Flow Veo Lite clip and compare it with Flow's own 9:16 crop on import.

## History

- 2026-11-25: First written. Seven keepers cropped for the 48-hour plan.
