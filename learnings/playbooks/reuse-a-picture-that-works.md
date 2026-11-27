---
slug: reuse-a-picture-that-works
title: Make your best picture the reference for the next ones
dek: Write down the six things that make the picture work, then attach the picture itself as the style and layout reference. A real photograph should hold the framing without the flat look a sketch brought in. Under test on Nano Banana Pro.
making: photo
tools: [nano-banana-pro, higgsfield, kling, recraft, adobe-express]
techniques: [reference-images, scoring, html-import]
models:
  - name: Nano Banana Pro on Higgsfield Unlimited
    tested: 2026-11-25
  - name: Nano Banana Pro on Kling (gemini-3-pro-image), run once against the rule below
    tested: 2026-11-25
  - name: Kling Image 4.0
    tested: 2026-11-25
status: try
cost_usable: Free on Higgsfield Unlimited
back_office: unpublished
date: 2026-11-25
updated: 2026-11-25
---

# Make your best picture the reference for the next ones

Write down the six things that make the picture work, then attach the picture itself as the style and layout reference. A real photograph should hold the framing without the flat look a sketch brought in. Under test on Nano Banana Pro.

## What happened

On 25 November Alex opened an Adobe Express page from 20 November and called it "absolutely perfect": the pool at The Oriole Palace seen from a balcony, a palm shadow across the water, guests on striped loungers and one man in black standing at the back. The caption reads "Nothing happens here. He sees to it."

It is ours. The picture is `O01_oriole-palace_society.jpg` in the Creative Cloud library, uploaded on 20 November with the rest of the Oriole Palace pictures. It most likely came from the Oriole Palace set we made on Nano Banana Pro in early November, though no run log names it. The post is `oriole-1_O01.jpg`, laid out in the Express document "Untitled - 20 November 2026 at 19.36.16". The exact prompt was never saved beside the file, so we can describe the picture and rebuild the recipe, and we can't run the original again. That is the first lesson.

Our last framing test showed where a layout reference can go wrong. In test T1 a grey blocking sketch as a third image cut Real from 2 to 1 on both scored takes (11 of 15 down to 10), and rewriting the bans as positive wording took it to 9 and 8. The sketch's flat grey seems to leak into the picture. A real photograph carries the same layout with the right texture, so that is what we test next.

## Pictures

![The post, the take from words alone, the take with the post attached, and Kling's copy](../images/reuse-a-picture-t3-sheet.jpg)

From left: the Oriole Palace post we wanted more of; T3a, the six points as words only (11 or 12 of 15, the pool turned into a lap lane); T3b, the same words with the post attached as image 2 (12 or 13 of 15, the corner-to-corner pool and palm shadow back); and Kling Image 4.0, which handed back the post itself and scored 0.

## What makes it work

| Element | What the picture does |
| --- | --- |
| Camera | High, from a second-floor balcony, looking steeply down the length of the pool. The pool runs corner to corner, lower left to upper right, and fills about half the frame. The deck edge makes a second diagonal. |
| Light | Noon sun from behind the camera. One palm's shadow lies across the water in the lower left, the darkest shape in the frame. It gives depth and a time of day. |
| Story beat | One staff member in black stands at the far wall, upright, hands behind his back, apart from everyone. He is the only vertical figure and the only one at work. You see him second, and the caption sends you back to him. |
| Crowd | About fifteen guests on white loungers with green-and-white striped cushions along both long sides: magazines, headscarves, white sunglasses, one-piece swimsuits. One swimmer mid-pool gives scale. Nobody looks at the camera. |
| Colour | Pink stucco, turquoise water, sage stripes, warm skin, cream stone. A faint warm-magenta cast, highlights close to burning out, fine grain, soft edges. The post adds the house grade and a soft full-frame shade that darkens the bottom third for the type. |
| Type | Bottom centre over the shade. A small tracked-capitals label (hotel · place, no number) and one serif line under it, on one line, about eight words. The line pays off the story beat. |

The type spec at 1080 × 1350, as the social factory builds it from 25 November: label Neue Haas Unica 500, 24px, letter-spacing 0.12em, capitals, 26px above the line; line FreightBig Pro Book 400, 56px, line-height 1.1, letter-spacing −0.01em; both in the brand's on-dark colour, centred; shade a linear gradient from clear at 35% to 65% `#172016` at the bottom edge. Fonts load from Adobe Fonts kit `lxh4muu`. The original post set the same layout in Instrument Serif and DM Sans; Alex moved social to the brand pair on 25 November, and the line came down from 62px because FreightBig sets wider. See [live text in Express](live-text-in-adobe-express.md) for getting it in with the text still editable.

## What to do

1. Find the picture's source file and its prompt, and save the prompt in the same folder as the file under the same name.
2. Write down what makes it work under the six headings above. Each line should be something a model can be told.
3. Attach the picture itself as a reference and give it one job in the first lines of the prompt: camera height and angle, the main shapes, where people stand, colour and light.
4. Say what changes. New people in new poses, and anything you need moved (here, the staff member comes forward so the shirt reads).
5. Make four takes a side against your usual prompt and score all of them. Mark any take that rebuilds the reference person for person as a copy and score it 0.

Use only pictures you made or own. A photograph by a named photographer belongs to whoever holds their archive.

## Prompt (generic)

```
Two images are attached, each with one job. Image 1 is the [product]: copy its colour and print exactly. Image 2 is one of our own photographs: take its camera height and angle, [the main shapes], where the people are, and its colour, light and grain. Move [the person who must read] to [where], and make every other person a new person in a new pose.

[Your picture prompt, describing the same kind of place and moment.]
```

## Prompt we used (Off Duty Hotel Club)

Shot sheet rows T3a (control: the Security shirt and the Oriole hero for colour) and T3b (the same with this picture as image 2). The scene text is the same in both:

```
A 1960s colour photograph for a travel magazine, Los Angeles, August 1966, at noon. Seen from a second-floor balcony, looking steeply down the length of a long rectangular pool that runs corner to corner across the frame, the turquoise water taking up half the picture and the hard shadow of one tall palm lying across it. Pink stucco walls, potted palms and a cream stone deck. Guests lie on white-framed loungers with green-and-white striped cushions along both long sides: women in one-piece swimsuits, headscarves and white sunglasses reading magazines, a man asleep under a newspaper, one swimmer doing slow lengths. Nobody looks at the camera. Apart from all of them, at the near right corner of the deck, the hotel's security man stands perfectly still with his hands clasped behind his back, the only person standing, turned away from the camera so the back of his T-shirt reads in full. ...
```

The full text for both rows is in the shot sheet.

## Settings

| Setting | Value |
| --- | --- |
| Model | Nano Banana Pro |
| Ratio | 4:5 |
| Size | 2K |
| Takes | 4 per arm |
| Scored on | Real, Shirt and Period look, 1 to 5 each (see [scoring note](../notes/score-ai-pictures.md)) |

## References

- `oriole-pool-security-clean.jpg`: the picture without type, in the Drive "ODHC shot references" folder. The Drive copy is the 600px rendition the Express connector can read; the full-size file is `O01_oriole-palace_society.jpg` in Creative Cloud, and Alex can attach that one directly.
- `oriole-pool-security-post.jpg`: the finished post with its type, same folder, for the layout of the words.
- `shirt-security-back` and `hero-oriole`: the usual product and colour references.

## Cost

Free on Higgsfield Unlimited: eight takes for the test.

## Lessons

| Lesson | Status |
| --- | --- |
| `save-the-prompt-with-the-picture`: Our best Oriole picture lost its prompt because only the image was uploaded. Save the prompt beside every keeper under the same file name. | tested |
| `photo-as-layout-reference`: Attach a picture that already works as the layout reference; a grey sketch cut Real by a point in T1. | try |
| `staff-apart-as-story-beat`: One uniformed staff member standing still among lounging guests gives the picture its story and puts the shirt in it. | try |
| `caption-pays-off-the-picture`: The one serif line works when it explains the odd figure in the picture, so write it after choosing the picture. | try |
| `social-uses-brand-type`: Social posts set type in the brand pair, FreightBig Pro and Neue Haas Unica, like the store (Alex, 25 November). | tested |
| `shadow-for-depth`: A single hard palm shadow across water gives a top-down picture its depth and its time of day. | try |
| `photo-reference-gets-copied`: With our pool picture as image 2, Kling Image 4.0 rebuilt it guest for guest in 4 of 4 takes, and Nano Banana Pro did the same in 1 of 4 (the Recraft take; none of the 3 on Kling copied), despite "make every guest a new person". Every copy scores 0, so a photo reference needs a stronger guard than one sentence. | tested |
| `kling-image-4-looks-digital`: Kling Image 4.0 held the print well (5, 4, 4, 4) but every take scored 2 on Real: glossy skin, flat stucco, a digital look. At 4 credits a picture it suits rough layout drafts. | tested |

## Baselines, 25 November

Before Alex's Higgsfield takes, a thread ran both arms on the models it can drive (shot sheet, Claude's shots, rows T3a-K to T3-R). Scores are Real/Shirt/Period out of 15.

| Arm | Kling Image 4.0 (4 credits) | Nano Banana Pro on Kling (20 credits) |
| --- | --- | --- |
| T3a, hero for colour | 10, 9, 9, 9 (avg 9.3) | 12, 12, 11, 12 (avg 11.75) |
| T3b, our picture as image 2 | 4 copies, all 0 | 13, 12 (fails: slide border), 13; the fourth failed at Kling (avg 12.7) |

Nano Banana Pro's control takes looked like real slides (Real 4) and three reached 12. Kling 4.0 held the print but looked digital. On Nano Banana Pro the picture as image 2 lifted the average by 0.9, just under the 1-point rule, and gave the only two 13s, both with every print line right. One of the four Nano Banana Pro T3b takes (on Recraft) copied the reference, and one drew a rounded slide border round the frame. The reference helps, and the copying of its guests is what needs fixing.

## Next to try

Nano Banana runs only on the Gemini app or Flow, by Alex's hand (his rule, 27 Nov). The Kling and Recraft takes above broke that rule; they stand as baselines and are never to be repeated on those routes.


Add a guard against copying before Alex runs T3b: say in the first line that image 2 is for camera, light and colour only and that its guests must not reappear, and crop the reference to drop the two foreground women who get copied most. Then run T3a and T3b. Keep the picture as a reference if T3b's four-take average beats T3a's by 1 point or more with Real no lower and no copies.

## History

- 2026-11-27: Nano Banana runs only on Gemini or Flow, by hand. Noted against the T3 baselines.
- 2026-11-25: Baselines on Kling Image 4.0 and Nano Banana Pro. The photo reference got copied guest for guest; added `photo-reference-gets-copied` and `kling-image-4-looks-digital`.
- 2026-11-25: Type spec moved to FreightBig Pro and Neue Haas Unica after Alex chose the brand pair for social.
- 2026-11-25: First written from the Oriole pool post Alex picked in Express. Test T3 set up in the shot sheet, not yet run.
