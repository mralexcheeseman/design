---
slug: make-vertical-cuts-for-stories
title: Turn a landscape clip or a 4:5 picture into a 9:16 story without losing the people
dek: For a 4:5 picture, add sky and ground with generative expand, about a fifth of the height at each end. For a 16:9 clip, a subject-tracking reframe keeps the person in shot, but a 720p source comes out soft, so make the clip at 1080p or taller first.
making: social
tools: [firefly, picsart]
techniques: [refine]
models:
  - name: Adobe generative expand (Photoshop API, through the Adobe connector)
    tested: 2026-11-25
  - name: Picsart reframe video (subject tracking)
    tested: 2026-11-25
status: tested
cost_usable: Free on both (expand drew no premium credits that the tool reported)
back_office: unpublished
date: 2026-11-25
updated: 2026-11-25
---

# Turn a landscape clip or a 4:5 picture into a 9:16 story without losing the people

For a 4:5 picture, add sky and ground with generative expand, about a fifth of the height at each end. For a 16:9 clip, a subject-tracking reframe keeps the person in shot, but a 720p source comes out soft, so make the clip at 1080p or taller first.

## What happened

We wanted story and Reels versions of the house looks and the hero clips. A centre crop from 4:5 to 9:16 cuts the shirt print or the person's head, and a crop from 16:9 to 9:16 keeps only a third of the frame.

Pictures: four house looks at 1690x2112 went through generative expand with 446 px added top and bottom, which gives 1690x3004, an exact 9:16. All four came back clean. The sky carries on, the sand, terrace and road continue below, and nothing new walks into frame. The Oriole picture grew the front of the car at the bottom, which reads as natural. The Thalene picture gained a large plain white pool edge at the bottom, which suits a line of type.

Clips: the Firefly hero clips weren't made yet, so we tested the reframe on two 16:9 Veo clips of the Ski Patrol on the Valbrune slope (8 s, 1280x720). Picsart's reframe chose one fixed crop for each clip and never panned, since the man barely moves. He stays in frame and the print reads in every sampled frame, but in one clip the slow push-in carries him to the right edge, with his skis touching it at 4 s. The crop is 404x720, so the 1080x1920 export is blown up 2.7 times and looks soft next to a native vertical clip.

## What to do

1. Pictures: expand top and bottom only. Work out the padding: target height = width × 16 ÷ 9, minus the current height, split in half. Leave the prompt empty so the fill matches the picture.
2. Look at every expand at phone size before using it, checking hands, cars and any print that sits near an edge.
3. Clips: make the source at 1080p or above if it's going to be cropped to vertical, or generate it at 9:16 in the first place. A 720p clip only holds a 404 px wide vertical crop.
4. Check the reframe on a contact sheet (five frames from start to end) before export. If the subject drifts to an edge, keyframe the crop to follow, or pick the take where they stay central.
5. Compose landscape clips meant for stories with the person in the middle third, moving towards the centre of the frame.

## Prompt (generic)

```
No prompt. Generative expand: top [N] px, bottom [N] px, where N = (width × 16 / 9 − height) / 2.
```

## Prompt we used (Off Duty Hotel Club)

```
No prompt. Generative expand: top 446 px, bottom 446 px on 1690x2112 house looks.
```

## Settings

| Setting | Value |
| --- | --- |
| Expand | top and bottom 446 px, JPEG out, no prompt |
| Reframe | Picsart `reframe_video`, 9:16, subject tracking, export 1080x1920 MP4 |

## References

- House looks in Creative Cloud: 1 Lifeguard, Solvane Cove; 2 Security, Oriole Palace arrival; 3 Pool Boy, Casa Thalene pool; 4 Ski Patrol, Valbrune terrace.
- Clips: V1c and V1d in the shot sheet (Veo 3.1 Lite and Fast, 16:9).
- Results in the Drive folder "ODHC shot results": files starting `A1-` and `PX3-`.

## Cost

Free. Picsart reframe and export cost nothing. The expand call reported no credit charge, and Firefly lists Generative Expand as a standard feature, so it shouldn't touch the monthly premium credits (still to confirm against the balance).

## Lessons

| Lesson | Status |
| --- | --- |
| `expand-for-stories`: a fifth of the height added top and bottom by generative expand turns a 4:5 picture into a clean 9:16 story with room for type. | tested |
| `source-resolution-for-reframe`: a 16:9 clip at 720p only holds a 404 px wide vertical crop, so make clips at 1080p or taller, or at 9:16, if they're meant for stories. | tested |
| `contact-sheet-before-export`: a fixed reframe can leave the subject at the edge as the camera pushes in, so check five frames before export. | tested |
| `expand-not-premium`: generative expand doesn't spend Firefly premium credits, so it can't be used to use them up before renewal. | try |

## Next to try

Run the same clip through Adobe's video resize and compare it frame by frame with Picsart's reframe, then repeat both on the Firefly hero clips once they exist.

## History

- 2026-11-25: First written from shot sheet rows A1 and PX3 (Picsart half).
