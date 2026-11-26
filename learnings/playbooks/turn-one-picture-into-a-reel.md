---
slug: turn-one-picture-into-a-reel
title: Turn one approved picture into a finished Instagram reel
dek: Animate the picture you already like, set the words in your real brand fonts as a separate layer, add sound made for the scene, and finish everything in one ffmpeg pass. One 8-second reel cost 80 Kling credits and about 950 ElevenLabs credits.
making: video
tools: [kling, elevenlabs, adobe-express, base44]
techniques: [html-import, web-encoding, film-look]
models:
  - name: Kling 3.0 Turbo (image to video)
    tested: 2026-11-25
  - name: ElevenLabs Sound Effects v3
    tested: 2026-11-25
  - name: ElevenLabs Music v2.5
    tested: 2026-11-25
status: tested
cost_usable: 80 Kling credits and about 950 ElevenLabs credits for an 8-second reel
back_office: unpublished
date: 2026-11-25
updated: 2026-11-25
---

# Turn one approved picture into a finished Instagram reel

Animate the picture you already like, set the words in your real brand fonts as a separate layer, add sound made for the scene, and finish everything in one ffmpeg pass. One 8-second reel cost 80 Kling credits and about 950 ElevenLabs credits.

## What happened

We wanted reels without starting a new picture for each one. The source was the Oriole Palace pool picture, our best-liked post. Its Creative Cloud original turned out to be 1536 x 2752, already 9:16, so it needed no expand step. Kling refused the Creative Cloud share link, so we copied the file into Drive and passed Kling the Drive image link.

The video tools couldn't set our type. Kling and Picsart have no FreightBig Pro or Neue Haas Unica, and the Adobe Fonts kit is blocked inside the cloud sandbox. So the words went through Adobe Express as white type on black, came back as a PNG, and the black became transparency in the finishing script.

Kling's clip came with its own soundtrack, which we dropped. Pool sound and a short lounge cue came from ElevenLabs. Music prompts asked for no vocals and we still ran both takes through speech-to-text to be sure. The finished reel is 1080 x 1920, 30 fps, -14 LUFS, 6 MB.

## What to do

1. **Start from a picture that already won.** For ODHC, pick from the shot sheet's Results tab where Gate is Pass and Usable is Yes (filter view "For Alex: usable and passed"), or a post Alex has already liked. Check its original size first: if it's already 9:16 (or taller than 4:5), skip any expand step.
2. **Animate it in Kling 3.0 Turbo**, image to video, 8 seconds at 1080p. Lock the camera, give each person one small action, and tell the subject who should stay still to stay still. The clip follows the picture's own ratio.
3. **Set the words as their own layer.** Write an HTML page at 1080 x 1920, white type on pure black, brand fonts from the Adobe Fonts kit, and import it to Express. Download it as PNG. The words stay editable in Express for the next version.
4. **Make the sound.** One sound effects take (8 seconds) for the room, one music take (10 seconds) for the mood. Run music through speech-to-text: an empty transcript means no vocals.
5. **Finish in one pass** with `finish_reel.py` (storefront-kit `tools/reel-line/`): it fills the frame, lays a soft full-frame shade under the words, fades the words in at 1 second, mixes sound with music 9 dB under, levels to -14 LUFS for Instagram, and writes a cover JPG at 3 seconds.
6. **Name every file** with the shot-sheet row ID and a version (`OR1-reel-v1.mp4`), file it in Drive, and put the reel in the Social Planner as a draft with the video link and the cover. Nothing posts without the owner's yes.

## Prompt (generic)

```
Locked-off camera, no camera movement. [Era and film stock] photograph come to life, [light]. [Main mover] does a slow [action] towards the camera. [Ambient motion: water, leaves, curtains] moves very gently. [Background people] barely move: one [small action], one [small action]. [The figure who must not move] stands perfectly still, watching. Calm, unhurried, natural film grain. No text, no new people, no cuts.
```

## Prompt we used (Off Duty Hotel Club)

```
Locked-off camera, no camera movement. 1960s Kodachrome resort photograph come to life, hot still afternoon light. The swimmer does a slow, lazy breaststroke towards the camera, leaving soft ripples. Sunlight shimmers across the turquoise water and the palm shadow on the pool sways very gently in a light breeze. Guests on the striped loungers barely move: one turns a magazine page, one adjusts her sunglasses. The security man in black at the top right stands perfectly still with his hands behind his back, watching. Calm, unhurried, natural film grain. No text, no new people, no cuts.
```

Sound effects:

```
Calm hotel swimming pool on a hot afternoon, 8 seconds: gentle water lapping, one swimmer's slow breaststroke splashes, a magazine page turning, faint palm leaves rustling in a light breeze, distant quiet murmur of guests. No music, no voices you can understand.
```

Music:

```
Instrumental, 10 seconds. Early-1960s hotel poolside lounge: soft brushed drums, upright bass, vibraphone and muted trumpet, slow relaxed swing at about 80 bpm, warm and slightly sly, like a quiet afternoon where someone is keeping an eye on things. No vocals. Clean ending.
```

On-screen words: label "THE ORIOLE PALACE · LOS ANGELES" in Neue Haas Unica 500, 24 px, 0.12em tracking; line "Nothing happens here. He sees to it." in FreightBig Pro Book, 56 px, 1.1 line height. Block 96 px from each side, 380 px from the bottom, clear of Instagram's caption area.

## Settings

| Setting | Value |
| --- | --- |
| Kling model | `kling-video-v3_0_turbo`, image to video |
| Length and size | 8 s, 1080p; output 1076 x 1928, 24 fps |
| Sound effects | `eleven_text_to_sound_v3`, 8 s |
| Music | `eleven_music_v2_5`, 10 s, mixed at -9 dB |
| Words | fade in at 1.0 s over 0.6 s, colour `#fbf8f0` |
| Shade | `#172016`, stops 0% to 35% clear, 25% at 60%, 65% at the bottom |
| Encode | H.264 high, CRF 18, 30 fps, faststart, AAC 192k 48 kHz, -14 LUFS |

## References

- The Oriole Palace pool picture (Creative Cloud original, 1536 x 2752), copied to the Drive references folder as `oriole-pool-security-original-9x16.jpg`.

## Cost

80 Kling credits (10 a second at 1080p) and about 950 ElevenLabs credits for one usable reel: one sound effects take (17), one music take (about 900) and a vocal check (55). We made two of each sound for choice, so the run spent about 1,944 ElevenLabs credits. Express, the PNG export and the finish cost nothing.

## Lessons

| Lesson | Status |
| --- | --- |
| `check-the-original-ratio`: read the source file's size before planning an expand; our favourite picture was already 9:16. | tested |
| `kling-needs-a-plain-image-link`: Kling refuses Creative Cloud share links; copy the file to Drive and pass `lh3.googleusercontent.com/d/<id>`. | tested |
| `words-as-a-layer`: set on-screen words in Express as white on black, export PNG and key out the black, so the reel carries the real brand fonts. | tested |
| `lock-the-watcher`: naming the figure who must stay still ("stands perfectly still, watching") kept him still for all 8 seconds. | tested |
| `drop-the-clip-sound`: Kling adds its own soundtrack; replace it with sound made for the scene. | tested |
| `check-music-for-vocals`: run each music take through speech-to-text before using it; an empty transcript means no singing. | tested |
| `music-costs-more-than-video`: a 10-second music take cost about 900 ElevenLabs credits, more than the Kling clip; make one take unless the first fails. | tested |
| `finish-in-one-pass`: one ffmpeg pass for shade, words, mix and loudness keeps every reel the same and takes seconds. | tested |

## Next to try

A second reel from a different hotel, with the words placed higher or a stronger shade where the picture is busy behind them.

## History

- 2026-11-25: First written from the OR1 Oriole pool reel.
- 2026-11-26: Step 1 points to the scored Results tab for approved stills.
