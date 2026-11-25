---
slug: log-results-from-drive
title: Log every generated picture in the shot sheet without typing
dek: A two-step Zap (Drive New File in Folder, then Sheets Create Spreadsheet Row) writes three fields. Sheet formulas work out the rest from the file name.
making: photo
tools: [higgsfield, firefly, google-flow]
techniques: [workflow, scoring]
models: []
status: try
cost_usable: One Zapier task per file (free plan has 100 a month)
back_office: private
date: 2026-11-23
updated: 2026-11-25
---

# Log every generated picture in the shot sheet without typing

A two-step Zap (Drive New File in Folder, then Sheets Create Spreadsheet Row) writes three fields. Sheet formulas work out the rest from the file name.

## What happened

Alex generates the Higgsfield, Firefly and Flow pictures by hand and drops them in the Drive folder "ODHC shot results". Each one then had to be found again and matched to its row before it could be scored. On the first night 29 files went in, and the names had drifted from the Save as names: `H1b-solvane-jetty.jpgv1.png`, `H1-solvane-lifeguard-bastien.jpg.v1.png`, `H3e-ceresa-wheelbarrow-v2.jpg.png`.

The Zapier MCP connector can run actions (create a row, find a file), but it cannot create a Zap with a trigger. So a thread can't build "when a file lands, do X". The person has to make the Zap in the Zapier editor. Google Drive storage is the rule for generated assets, so nothing goes to Cloudinary.

## What to do

1. Give the sheet a log tab (here `Results`) with headers `Added`, `File`, `Drive link`, then formula columns. The Zap fills only the first three.
2. Do the parsing in the sheet. A Formatter step makes the Zap three steps, and the free plan allows two. In row 1 of each formula column, one `ARRAYFORMULA` that prints its own header and leaves blank rows truly empty, so Zapier's append still finds the last row:
   - ID: `REGEXEXTRACT(B:B,"^([A-Za-z]+[0-9]+[a-z]?)")` (H1, H1b, H10e, K2)
   - Version: `"v"&REGEXEXTRACT(LOWER(B:B),"v([0-9]+)")`. This survives `.jpgv1`, `.jpg.v1` and `-v1.jpg`. Hotel names with a v (Solvane, Valbrune) are safe because a digit must follow.
   - Shot and tool: `VLOOKUP` on ID against both shot tabs stacked with `{...;...}`.
   - Score and verdict: pull the v1 or v2 block from the row where they're entered. Keep scoring in one place.
   - Use the pattern `IF(ROW(B:B)=1,"Header",IF(B:B="",,...))`. The empty second argument is what keeps blank rows blank.
3. Link back from the shot row: `HYPERLINK(XLOOKUP(id, Results!D:D, Results!C:C, "", 0, -1), ...)` opens the newest file. Guard it with `COUNTIF(...)=0` first, because XLOOKUP's "not found" value doesn't raise an error that IFERROR would catch.
4. The Zap: Google Drive **New File in Folder** (that folder, no subfolders), then Google Sheets **Create Spreadsheet Row** on the log tab, mapping Created Time, Title and Alternate Link.
5. Backfill the files already in the folder by hand, because the trigger only sees new ones. Drive search pages overlap, so remove duplicates by file id.

## Naming and filing without typing

The Zap only logs what lands in the folder, so the slow part was getting each download there with the right name. Today's two clips went in as `V2b-v1-hydrogen-take1.mp4.mp4` and `V2c-v1-flowveolite-take1.mp4,.mp4`, typed by hand after a back-and-forth in chat.

[File Result](../../tools/file-result/README.md) fixes that on the Mac: drop the downloads on a Dock icon, type the shot ID, pick the tool, and it names them `V2c-v1-flowveolite-take1.mp4` (take counted from the folder) and moves them into the Drive for desktop copy of the folder. Drive for desktop uploads any size, which the cloud can't: a thread fails on Drive uploads over about 3 MB, and clips run 8 to 15 MB. An iPhone Shortcut does the same from the share sheet.

A thread can't do the renaming afterwards either. The Drive connector reports `canEdit: false` on files Alex uploaded himself, so it can't rename or move them.

Video IDs start with V, so the first version formula read the `V2` in `V2b-v1-...` as version 2. The version has to be found after the ID: `REGEXEXTRACT(LOWER(B:B),"^[a-z]+[0-9]+[a-z]?.*?v([0-9]+)")`.

## Lessons

| Slug | Lesson | Status |
| --- | --- | --- |
| `zap-needs-a-person` | The Zapier MCP can't create triggered Zaps. Give the person the exact two steps and field mapping instead. | tested |
| `parse-in-the-sheet` | Parse IDs and versions with sheet formulas so the Zap stays at two steps and works on the free plan. | try |
| `file-on-the-mac` | Name and move results on the Mac (File Result, Drive for desktop). The cloud can't upload clips or rename Alex's Drive files. | try |
| `version-after-id` | Read the version after the shot ID, or a V-prefixed ID is mistaken for the version. | tested |
| `log-with-apps-script` | Log with an Apps Script on a 5-minute timer, not a Zap. About 40 files in three days would cost about 400 Zapier tasks a month, against the free plan's 100. | try |
| `zapier-for-thread-clips` | Thread-made clips go to Drive through the Zapier MCP Drive Upload File action from a public link (2 tasks a clip). A 9.6 MB Kling clip went up fine. | tested |
| `names-drift` | People rename files by hand. Match on the leading ID and any `v<digit>`, never on the full Save as name. | tested |

## History

- 2026-11-25: logging moved to an Apps Script (`tools/results-log`) on Alex's call to save Zapier tasks. Zapier Drive Upload File enabled for thread clips.
- 2026-11-25: added File Result (Mac drop app and iPhone Shortcut) and the version formula fix for V rows. Logged V2b and V2c by hand.
- 2026-11-23: set up for the ODHC shot sheet. Results tab and backfill done; Zap built by Alex in the editor.
