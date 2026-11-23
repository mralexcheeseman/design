---
slug: keep-scroll-video-sharp
title: Keep a scroll-scrubbed video sharp on the web
dek: We shrank a 1080p clip to 1280px so it would scrub smoothly, and it went soft. At full size with a keyframe every six frames it scrubs just as well and weighs 12.4 MB.
making: website
tools: [kling, base44]
techniques: [web-encoding]
models:
  - name: Kling 3.0 Omni (the source clip)
    tested: 2026-11-23
  - name: ffmpeg with libx264
    tested: 2026-11-23
status: tested
cost_usable: Free
back_office: published
date: 2026-11-23
updated: 2026-11-23
---

# Keep a scroll-scrubbed video sharp on the web

We shrank a 1080p clip to 1280px so it would scrub smoothly, and it went soft. At full size with a keyframe every six frames it scrubs just as well and weighs 12.4 MB.

Before, 1280px with every frame a keyframe, 4.7 MB: the ironwork and leaves smear. [pb-sharp-before.jpg](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/d61522f79a2a15bc17ed823919fce254_pb-sharp-before.jpg)
After, 1080p with a keyframe every 6 frames, 12.4 MB, same crop at actual size. [pb-sharp-after.jpg](https://media.base44.com/images/public/6b044d6aaa73f82d3c126031/5a7f342908ec7d09d8b297401363fc6a_pb-sharp-after.jpg)

## What happened

The entrance on The Back Office plays a 12-second Kling clip as you scroll. To feel smooth, the browser has to land on any frame quickly, and the usual advice is to make every frame a keyframe. That makes the file huge, so we cut it to 1280px and a low bitrate to get under 5 MB. Alex opened it on Base44 and said it looked low res.

Kling had sent 1920×1080 at about 32 Mbps, so the softness came from our encode. We made five versions and measured each against the original, where 1.0 would be identical. Every frame a keyframe at full size scored 0.975 and weighed 34 MB. A keyframe every 6 frames came close at less than half the size.

| Encode | Size | Match to source |
| --- | --- | --- |
| 1280px, every frame a keyframe | 4.7 MB | 0.859 |
| **1080p, every 6 frames, CRF 26 (chosen)** | **12.4 MB** | **0.971** |
| 1080p, every 6 frames, CRF 24 | 15.8 MB | 0.976 |
| 1080p, every 6 frames, CRF 19 | 28.9 MB | 0.986 |
| 1080p, every frame a keyframe, CRF 20 | 33.8 MB | 0.975 |

## What to do

Keep the source at its full resolution. Put a keyframe every 6 frames, a quarter of a second at 24 fps, so the browser never has far to decode when the reader scrolls to a frame. Switch off B-frames and strip the sound.

Then host the file somewhere that answers range requests. On Base44 that means the app's media library. A 12 MB file committed to the code did not play on the preview at all.

## Command (generic)

```
ffmpeg -i source.mp4 -an -c:v libx264 -preset slow -crf 26 -g 6 -keyint_min 6 -sc_threshold 0 -bf 0 -pix_fmt yuv420p -profile:v high -movflags +faststart scroll.mp4
```

Lower `-crf` for a sharper, larger file. `-g` sets the gap between keyframes in frames.

## Command we used (Off Duty Hotel Club)

```
ffmpeg -i kling-entrance.mp4 -an -c:v libx264 -preset slow -crf 26 -g 6 -keyint_min 6 -sc_threshold 0 -bf 0 -pix_fmt yuv420p -profile:v high -movflags +faststart entrance-1080.mp4
```

The Base44 sandbox has no ffmpeg. `npm i ffmpeg-static` in /tmp gives you one.

## Settings

| Setting | Value |
| --- | --- |
| Size | 1920×1080, as delivered |
| Keyframes | Every 6 frames |
| Quality | CRF 26, slow preset |
| B-frames | None |
| Sound | Removed |
| File | 12.4 MB for 12 seconds |

## Cost

Free. ffmpeg costs nothing and the five test encodes took about two minutes.

## Lessons

| Lesson | Status |
| --- | --- |
| `all-intra-for-scrub`: For a clip that scrubs with the scroll, keep the source's full 1080p and put a keyframe every 6 frames: 12 MB and sharp, where all-intra at 1280px fitted in 5 MB and looked soft. | tested |
| `video-on-the-media-library`: On Base44, put a site's video in the app's media library and link to that address, because a large file in the code's public folder did not play on the preview. | try |
| `upload-by-link`: Uploading to Base44 by public link stores the full-size file without the bytes passing through Claude. | proven |

## Next to try

Send a 720p file to phones on mobile data and keep the 1080p file for everyone else.

## History

- 2026-11-23: Soft encode found by Alex, five encodes compared, 1080p version shipped from the media library.
