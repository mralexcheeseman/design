---
slug: log-results-from-drive
title: Log every generated picture in the shot sheet without typing
dek: A scheduled Claude task checks the Drive results folder every two hours and writes three fields. Sheet formulas work out the rest from the file name.
making: photo
tools: [higgsfield, firefly, google-flow]
techniques: [workflow, scoring]
models: []
status: try
cost_usable: One short scheduled run every two hours, no Zapier tasks
back_office: private
date: 2026-11-23
updated: 2026-11-25
---

# Log every generated picture in the shot sheet without typing

A scheduled Claude task checks the Drive results folder every two hours and writes three fields. Sheet formulas work out the rest from the file name.

## What happened

Alex generates the Higgsfield, Firefly and Flow pictures by hand and drops them in the Drive folder "ODHC shot results". Each one then had to be found again and matched to its row before it could be scored. On the first night 29 files went in, and the names had drifted from the Save as names: `H1b-solvane-jetty.jpgv1.png`, `H1-solvane-lifeguard-bastien.jpg.v1.png`, `H3e-ceresa-wheelbarrow-v2.jpg.png`.

The first plan was a Zap. The Zapier MCP connector can run actions (create a row, find a file), but it cannot create a Zap with a trigger, so Alex would have had to build it in the Zapier editor. He asked for an agent instead. On 25 Nov a scheduled task took the Zap's place: every two hours a fresh Claude run lists the folder, compares file ids with the links already in Results, and appends the missing files. By then other threads had already logged all 112 files by hand, so there was nothing left to backfill.

Google Drive storage is the rule for generated assets, so nothing goes to Cloudinary.

## What to do

1. Give the sheet a log tab (here `Results`) with headers `Added`, `File`, `Drive link`, then formula columns. The agent fills only the first three, plus a `Note` column at the end.
2. Do the parsing in the sheet, so the agent's job stays small and the logic is visible to the person. In row 1 of each formula column, one `ARRAYFORMULA` that prints its own header and leaves blank rows truly empty, so appends still find the last row:
   - ID: `REGEXEXTRACT(B:B,"^([A-Za-z]+[0-9]+[a-z]?)")` (H1, H1b, H10e, K2)
   - Version: strip the ID first, then look for `v<digit>`: `"v"&REGEXEXTRACT(LOWER(REGEXREPLACE(B:B,"^[A-Za-z]+[0-9]+[a-z]?","")),"v([0-9]+)")`. Without the strip, IDs such as `GV3` and `V2b` read as v3 and v2. This survives `.jpgv1`, `.jpg.v1` and `-v1.jpg`, and hotel names with a v (Solvane, Valbrune) are safe because a digit must follow.
   - Shot, tool, prompt, cost and credit pool: `VLOOKUP` on ID against both shot tabs stacked with `{...;...}`.
   - Score and verdict: pull the v1 or v2 block from the row where they're entered. Keep scoring in one place.
   - Use the pattern `IF(ROW(B:B)=1,"Header",IF(B:B="",,...))`. The empty second argument is what keeps blank rows blank.
3. Link back from the shot row: `HYPERLINK(XLOOKUP(id, Results!D:D, Results!C:C, "", 0, -1), ...)` opens the newest file. Guard it with `COUNTIF(...)=0` first, because XLOOKUP's "not found" value doesn't raise an error that IFERROR would catch.
4. The scheduled task: a fresh session every two hours with a standalone prompt. List the folder by parent id, de-duplicate by file id (Drive search pages overlap), skip files whose id is already in a column C link, append A:C oldest first, and never write into the formula columns. Then write a Note only where the person must act: no sheet row for the ID, no v number, or the file name names a different tool from the sheet row.
5. Tell the person the habit that keeps every column full: start each name with an ID that has a row, put `-v1` or `-v2` after it, and paste any changed prompt into that row's Notes. A prompt can't be recovered from a picture.

## Naming and filing without typing

The logger only logs what lands in the folder, so the slow part was getting each download there with the right name. Today's two clips went in as `V2b-v1-hydrogen-take1.mp4.mp4` and `V2c-v1-flowveolite-take1.mp4,.mp4`, typed by hand after a back-and-forth in chat.

[File Result](../../tools/file-result/README.md) fixes that on the Mac: drop the downloads on a Dock icon, type the shot ID, pick the tool, and it names them `V2c-v1-flowveolite-take1.mp4` (take counted from the folder) and moves them into the Drive for desktop copy of the folder. Drive for desktop uploads any size, which the cloud can't: a thread fails on Drive uploads over about 3 MB, and clips run 8 to 15 MB. An iPhone Shortcut does the same from the share sheet.

A thread can't do the renaming afterwards either. The Drive connector reports `canEdit: false` on files Alex uploaded himself, so it can't rename or move them.

## Lessons

| Slug | Lesson | Status |
| --- | --- | --- |
| `zap-needs-a-person` | The Zapier MCP can't create triggered Zaps. A scheduled Claude task does the same job with no editor step. | tested |
| `parse-in-the-sheet` | Parse IDs and versions with sheet formulas, so the logger only writes three fields and the logic stays visible. | try |
| `names-drift` | People rename files by hand. Match on the leading ID and a `v<digit>` after it, never on the full Save as name. | tested |
| `ids-need-rows` | Files made from a brief outside the sheet (MA, SE, OP, VC, SO, CT, GV on 25 Nov) log fine but get no shot, prompt or cost. Add the row before generating. | tested |
| `delete-rows-by-content` | Before deleting a "blank" row, re-read the tab and delete by what the row holds. Rows move while other threads append. | tested |
| `file-on-the-mac` | Name and move results on the Mac (File Result, Drive for desktop). The cloud can't upload clips or rename Alex's Drive files. | try |
| `version-after-id` | Read the version after the shot ID, or a V-prefixed ID is mistaken for the version. | tested |
| `log-with-apps-script` | A free alternative logger: an Apps Script on a 5-minute timer (`tools/results-log`). It de-duplicates on file id like the scheduled task, so running both never doubles a row. Keep one. | try |
| `zapier-for-thread-clips` | Thread-made clips go to Drive through the Zapier MCP Drive Upload File action from a public link (2 tasks a clip). A 9.6 MB Kling clip went up fine. | tested |
| `local-model-guesses-shot` | A local vision model (Ollama, Qwen2.5-VL 7B or Gemma 3 4B) guesses the shot ID from the picture against `ODHC shot list.txt`, and the person confirms with one click. Free, and nothing leaves the Mac. | try |

## History

- 2026-11-23: set up for the ODHC shot sheet. Results tab and backfill done; Zap instructions sent to Alex.
- 2026-11-25: Zap replaced by a scheduled task every two hours. Added Prompt, Cost, Credit pool and Note columns, fixed the version formula, and noted 43 files whose ID has no sheet row.
- 2026-11-25: File Result added (Mac drop app and iPhone Shortcut), then given a local Ollama model to guess shot and tool, a 3:4 to 4:5 crop for Flow stills, and folder drops. Shot list kept in My Drive as `ODHC shot list.txt`.
- 2026-11-25: Apps Script logger (`tools/results-log`) written as a free alternative to the scheduled task. Zapier Drive Upload File enabled for thread clips.
