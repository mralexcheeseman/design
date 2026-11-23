---
slug: live-text-in-adobe-express
title: Get editable text into Adobe Express from HTML
dek: Our social posts start life as HTML so every word stays editable in Express. The photos went missing on the first import and the fonts on the second.
making: social
tools: [adobe-express]
techniques: [html-import]
models:
  - name: Adobe Express HTML import
    tested: 2026-11-21
status: proven
cost_usable: Free
back_office: published
date: 2026-11-21
updated: 2026-11-23
---

# Get editable text into Adobe Express from HTML

Our social posts start life as HTML so every word stays editable in Express. The photos went missing on the first import and the fonts on the second.

## What happened

Each Off Duty post is laid out in HTML with the brand's colours and type, then imported into Adobe Express. Alex can change a word in Express afterwards and the layout moves round it.

The first import linked its photos by URL. Express brought the text in and left empty frames where the pictures should have been. The second embedded the photos and set the type with the CSS shorthand `font: 600 48px/1.1 freight-big-pro`. The photos arrived, and every headline fell back to a default face. The third wrote each font property on its own line and went in by a Creative Cloud link, and it arrived whole, photos at full size.

## What to do

Embed every image in the HTML as a data URI. Write font-family, font-size, font-weight and line-height as four separate properties. When the file gets too big to paste, upload it to Creative Cloud and import it by its link.

## CSS (generic)

```css
.headline {
  font-family: "freight-big-pro", serif;
  font-size: 48px;
  font-weight: 600;
  line-height: 1.1;
}
```

```html
<img src="data:image/jpeg;base64,…" alt="…">
```

The shorthand `font: 600 48px/1.1` is dropped on import. Linked images arrive as empty frames.

## How we run it (Off Duty Hotel Club)

The working files are in `/mnt/project-files/odhc-social-factory/` (`FACTORY.md`, `build.py`, one `posts-NN.json` per batch). The full-size route:

1. Build `express-<size>-fullres.html` with every photo embedded.
2. `asset_initialize_file_upload` in the Adobe connector.
3. PUT the file from Alex's Mac (`curl -L -X PUT --upload-file`). The cloud container and the desktop VM can't reach Creative Cloud storage, and the Mac's safety check needs Alex's "OK to upload" in the thread each time. The upload link lasts 4 hours.
4. `asset_finalize_file_upload`, then `export_html_to_express` with `url` set to the `presignedAssetUrl`.

Brand rules that apply to every post, already settled in `brands/off-duty-hotel-club/decisions.md`: the photo shade is a soft full-frame gradient (a half-height box shows its edge as a line in Express), and labels read hotel · place with no hotel numbers.

## Settings

| Setting | Value |
| --- | --- |
| Images | Embedded as data URIs |
| Type | Longhand font properties |
| Large files | Imported by Creative Cloud link |
| Frames | Feed 1080×1350, story 1080×1920 with the top 250px and bottom 380px kept clear |

## Cost

Free. Imports cost no credits.

## Lessons

| Lesson | Status |
| --- | --- |
| `express-embeds-only`: The Express importer keeps only images embedded in the HTML as data, and every linked image arrives as a 1×1 blank. | proven |
| `express-font-longhand`: Express ignores the CSS font shorthand, so family, size, weight and line height are set as separate properties. | proven |
| `express-import-by-url`: Importing the layout by its Creative Cloud URL brings photos in at full size with the text still live. | tested |

## Next to try

Import a five-slide carousel as one file and see whether Express keeps the slides as pages.

## History

- 2026-11-20: Linked images and font shorthand found to fail.
- 2026-11-21: Creative Cloud URL import works at full size.
- 2026-11-23: Batches 02 to 04 imported the same way. Written up as a playbook.
