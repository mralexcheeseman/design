---
slug: get-a-logo-mark-from-a-vector-model
title: Get a logo mark from an AI vector model that looks drawn by hand
dek: Name the genre (a publisher's colophon, with famous examples), give the animal an oval frame and a small detail budget, and the model returns a calm one-colour mark you can finish by hand in an hour.
making: social
tools: [recraft]
techniques: [vector-generation]
models:
  - name: Recraft V4.1 Pro Vector
    tested: 2026-11-27
status: tested
cost_usable: About 24 credits a usable mark (12 an image, about half usable)
back_office: unpublished
date: 2026-11-27
updated: 2026-11-27
---

# Get a logo mark from an AI vector model that looks drawn by hand

Name the genre (a publisher's colophon, with famous examples), give the animal an oval frame and a small detail budget, and the model returns a calm one-colour mark you can finish by hand in an hour.

## What happened

The Last Animal needed a mark to sit beside its name. The first three prompts asked for a "logo symbol" or an "identity mark": an aurochs in one continuous line, a Lascaux silhouette redrawn by a type designer, and a hand stencil. Every result looked like a steakhouse, a craft brewery or a tattoo. Horns, eyes and hooves were over-drawn, and the shapes had hundreds of points.

The fourth prompt named the thing we wanted by its trade name: a book publisher's colophon, with Penguin, Faber and Knopf as the tradition. It also boxed the animal in a plain upright oval and limited the detail to two or three negative-space cuts. Both animals we tried (a hare and an aurochs) came back as calm, flat silhouettes that read as a publisher's mark. Alex picked the aurochs.

The raw vector still needed finishing. The model's oval was uneven and its background shapes sat under the animal. We kept only the animal's paths, merged them, and drew a new oval with thicker sides than top and bottom, like a pen-drawn ring.

## What to do

1. Name the genre the mark belongs to (colophon, bookplate, printer's device) and two or three famous examples of it. Leave out the word "logo", which pulls in commercial clichés.
2. Give it a frame (an upright oval works) and a detail budget: a flat silhouette, two or three cuts, no eye or hoof detail.
3. Ask for one colour on the brand's background, using hex codes from `tokens.json`, and "No text."
4. Generate two or three takes per animal, pick on the silhouette alone, then redraw the frame yourself. Keep the animal paths, merge them (skia-pathops `union`), and build the ring as two ellipses with a `difference`.
5. Write the final paths with explicit `M`, `L`, `Q`, `C` and `Z` commands so they import cleanly into Adobe Express (see `live-text-in-adobe-express.md`).

## Prompt (generic)

```
Classic book publisher's colophon in the tradition of mid-century Penguin, Faber and Knopf colophons: a small [animal] [pose] in profile, inside a plain upright oval frame. Flat solid silhouette with only two or three fine negative-space cuts to suggest the shoulder and leg, very few points, carved linocut simplicity, no eye detail. One colour, [ink hex], on [paper hex]. No text. Quiet, literary, timeless.
```

## Prompt we used (The Last Animal)

```
Classic book publisher's colophon in the tradition of mid-century Penguin, Faber and Knopf colophons: a small aurochs standing calmly in profile, head slightly lowered, inside a plain upright oval frame. Flat solid silhouette with only two or three fine negative-space cuts to suggest the shoulder and leg, very few points, carved linocut simplicity, no eye detail, no hooves detail. One colour, near-black #1C1D1F, on off-white #F4F5F3. No text. Quiet, literary, timeless.
```

The prompts that failed: "Logo symbol for an essay publication called The Last Animal. A single aurochs drawn in one confident continuous line…", "Refined identity symbol: a solid silhouette of an aurochs in profile, taken from the Lascaux cave paintings…", and a Cueva de las Manos hand stencil.

## Settings

| Setting | Value |
| --- | --- |
| Model | `recraftv4_1_pro_vector` (the plain `recraftv4_1_vector` gave rougher curves) |
| Size | Square |
| Takes | 2 or 3 per prompt |
| Finishing | skia-pathops union of the animal paths, hand-built oval ring 30 units at the sides and 9 at top and bottom on a 660 × 880 box |

## Cost

About 24 credits a usable mark. Each Pro Vector image costs 12 credits. The whole search, including the three failed prompts, used 128 credits.

## Lessons

| Lesson | Status |
| --- | --- |
| `vector-colophon-prompt`: Asking for a publisher's colophon with named examples gives restrained marks. The word "logo" pulled every take towards steakhouse and brewery clichés. | tested |
| `vector-frame-and-budget`: A fixed frame (upright oval) and a detail budget (two or three cuts, no eye) keep the point count low enough to finish by hand. | tested |
| `vector-redraw-the-frame`: Keep the model's animal and redraw its frame yourself, because generated ovals come out lopsided. | tested |

## History

- 2026-11-27: Five prompts tried for The Last Animal. The colophon prompt gave both finalists; Alex picked the aurochs. Now live on the carousel template and avatar.
