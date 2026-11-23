---
slug: stop-buildings-drifting
title: Stop buildings drifting when you stitch stills into video
dek: Halfway up our drive the villa changed its front. Two of the four stills we gave Kling showed different houses, and the model blended one into the other on screen.
making: video
tools: [kling, recraft]
techniques: [waypoint-stills, edit-chain, first-last-frame]
models:
  - name: Kling 3.0 Omni
    tested: 2026-11-23
  - name: Nano Banana Pro and Nano Banana 2 edits, in Recraft
    tested: 2026-11-23
  - name: Recraft V4.1
    tested: 2026-11-23
status: tested
cost_usable: 142 credits for one usable clip
back_office: published
date: 2026-11-23
updated: 2026-11-23
---

# Stop buildings drifting when you stitch stills into video

Halfway up our drive the villa changed its front. Two of the four stills we gave Kling showed different houses, and the model blended one into the other on screen.

Before, 6 seconds in: columns, a balcony and a pediment over the door. [pb-drift-before.jpg](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/9765eb6164f67bd36b80637f41d729c9_pb-drift-before.jpg)
After, 9.6 seconds in: the same drive, now ending at a flat front with one green door. [pb-drift-after.jpg](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/0ec68f33c3ca2bea98240b0a8e42f1b3_pb-drift-after.jpg)

## What happened

We wanted the site to open on a drive up to the club's front door. Before paying for video we made the four stops as stills in Recraft: the gates, the drive, the doors closed, the doors open. Each still after the first was an edit of the one before, with one sentence saying where the camera had moved.

Kling 3.0 Omni took all four as references and made one 12-second take that hit every stop. The trouble was already in still 2. The edit that moved the camera up the drive also redrew the villa with columns and a balcony, while still 3 kept the flat front from still 1. We missed it on a contact sheet. Alex caught it on his phone at full speed.

A remake would have cost about 118 credits. First we held a title over the change with the picture dimmed behind it, and you could still see the house shift. Then Alex suggested cutting it out. We played the drive a quarter faster, stopped at 6.5 seconds while the house is still small, and cut straight to the steps at 9 seconds. The clip is now 8.3 seconds, the portico never appears, and the cut lands under the last title. It cost nothing.

## What to do

Lay your stills side by side before you spend any video credits and check the building against each one: columns, windows, doors, roofline. Redraw any still that disagrees, because the model will travel from one version to the other in plain sight.

If the clip is already made, cut the change out. Keep the frames before the building is close enough to read, jump to the frames after it has settled, and hide the join under a title. One ffmpeg command does it for free.

For a simple push-in, skip the middle stills. Give the model one photograph as the first frame and a tight crop of the same photograph as the last frame, and there is nothing for the building to drift towards.

## Prompt (generic)

```
One continuous smooth shot, [film look], [light and time of day]. Start exactly on image 1: [the opening view]. [The first movement], and the camera glides [direction] past the view in image 2. It keeps moving to [the stopping point] and settles, centred and still, on [the subject] exactly as in image 3. Then [the final action], ending exactly on image 4. Steady gimbal movement, no cuts, no people, no text.
```

## Prompt we used (Off Duty Hotel Club)

```
One continuous smooth cinematic shot, 1960s Slim Aarons Kodachrome look, late afternoon golden Riviera light. Start exactly on 图片1: standing before the closed cream wrought-iron gates. The gates swing slowly open inwards and the camera glides forward through them and up the gravel drive between the umbrella pines, clipped hedges and bougainvillea, passing the view in 图片2, with the sea glinting to the right. The camera keeps gliding steadily uphill to the foot of the front steps and settles, centred and still, on the closed green double doors exactly as in 图片3. The two doors then swing slowly open inwards, revealing the marble hall and the sunlit sea beyond, ending exactly on 图片4. Steady gimbal movement, no cuts, no people, no cars, no text, no lettering, no signs.
```

Kling's Omni model refers to reference images as 图片1, 图片2 and so on. Type them exactly like that.

## Settings

| Setting | Value |
| --- | --- |
| Mode | Omni, four image references |
| Length | 12 seconds |
| Output | 1080p, 16:9, no sound |
| Takes | One |

## References

1. [The gates](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/115760c67e9614eeb6e604383a783add_entrance-1-gates.png)
2. [The drive, where the columns appeared](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/601a305a12183d5f277dc36d449418de_entrance-2-drive.png)
3. [The doors, closed](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/7033691c250aa9ef5c8dfca6bd7a13e7_entrance-3-doors-closed.png)
4. [The doors, open](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/ec3b3ed0a9ff376da7c8b34b7cfac057_entrance-4-doors-open.png)

## Cost

142 credits for one usable clip: 46 Recraft credits for the four stills and 96 Kling credits for a single take. The cut that removed the change was free.

## Lessons

| Lesson | Status |
| --- | --- |
| `cut-past-the-change`: When a generated clip morphs between two versions of a building, cut from the last frame before it can be read to the first frame after it settles, and put a title over the join. It costs nothing and the change never shows. | try |
| `waypoints-must-match`: Kling morphs whatever the waypoint stills disagree on, so check that the building is the same in every still before you spend video credits. | tested |
| `four-refs-hold-the-path`: Give Kling Omni every waypoint as a still and name each one in the prompt, and a 12-second move lands on all of them in one take. | tested |
| `edit-chain-for-frames`: Making each still as an edit of the one before kept the trees, light and villa consistent from frame to frame. | tested |
| `nano-banana-2-for-edits`: Nano Banana 2 edits cost 11 Recraft credits against 20 for Pro and held the place just as well. | tested |
| `review-on-the-phone`: The house change was caught at full speed on a phone and missed on a contact sheet, so every clip gets watched through on the device before it ships. | tested |
| `stitched-stills-show-the-seam`: Stitching separately made stills into one clip leaves a visible change where they disagree, and a title over it softens the change without hiding it. | tested |
| `title-over-the-seam`: A flaw in a scroll clip can be hidden for free by holding a title at full strength over that stretch and dimming the picture behind it. | try |
| `one-photo-at-both-ends`: For a push-in clip, give the video model the same photograph as first frame and a tight crop of it as last frame. | try |

## Next to try

If the entrance is remade, redraw stills 1 and 2 backwards from still 3 so all four share one front (about 22 Recraft credits), then make one more Kling take. Spend nothing on it without Alex's say.

## History

- 2026-11-23: Entrance clip made, door change found, title moved over it. Written up as a playbook.
- 2026-11-23: Change cut out on Alex's suggestion: drive 0 to 6.5 s at 1.25x, hard cut to 9 s, 8.3 s clip, no credits.
