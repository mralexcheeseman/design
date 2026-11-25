# File Result

Names generated pictures and clips by shot ID and files them in the Drive folder **ODHC shot results**, so the Results log script ([../results-log](../results-log/README.md)) adds them to the shot sheet. Nothing to type except the shot ID.

```
Download from Flow, Gemini, Higgsfield, Firefly...
  -> drop the file(s) on File Result in the Dock
  -> type V2c (add v2 if it's the second prompt version), pick the tool
  -> V2c-v1-flowveolite-take1.mp4 lands in ODHC shot results (Drive for desktop uploads it, any size)
  -> the Results log adds a row within 5 minutes; the sheet's formulas fill ID, version, shot, tool and score
```

Take numbers count up on their own from what's already in the folder. The app remembers the last ID and tool, so a second take of the same shot is two clicks.

## Install (once, on the Mac)

1. Install [Google Drive for desktop](https://www.google.com/drive/download/) and sign in, if it isn't already. In Finder you should see **Google Drive > My Drive > ODHC shot results**.
2. Download this folder (`file-result`) to Downloads and unzip it.
3. Open Terminal and paste: `bash ~/Downloads/file-result/install.command`
4. Drag **File Result** from the Finder window that opens into the Dock.

The first time you drop a file, macOS may ask whether File Result can control Finder or access the Drive folder. Say OK. If it can't find the folder on its own it asks you to pick it, once.

## From the iPhone

Files saved on the phone go the same way with a Shortcut. In the Shortcuts app, make a new shortcut called **File result** and add, in order:

1. **Receive** Images and Media from **Share Sheet** (turn on Show in Share Sheet).
2. **Ask for Input**: Text, prompt "Shot ID and version, e.g. V2c-v1".
3. **Choose from Menu**: flowveolite, flowveofast, hydrogen, seedance, higgsfieldnbpro, firefly, kling, other. Under each option add **Text** with the same word.
4. **Ask for Input**: Number, prompt "Take", default 1.
5. **Text**: the answer from step 2, a hyphen, the menu result from step 3, then `-take` and the answer from step 4 (tap each answer in as a variable).
6. **Set Name** of Shortcut Input to that Text (keep the extension on).
7. **Save File** to Google Drive > ODHC shot results, Ask Where to Save off.

Then in Photos or Files: Share > File result. The phone can't see the folder's takes, so it asks for the take number.

## Changing the tool list

Edit `~/Library/Application Support/ODHC File Result/tools.txt`: one line per tool, the file-name word first, then a description. Reinstalling keeps your edits.

## Files

| File | What it does |
| --- | --- |
| `FileResult.applescript` | The Dock app: dialogs, then hands the files to the script |
| `file-result.sh` | Finds the Drive folder, normalises the ID (v2c to V2c), counts takes, renames and moves. Plain bash 3.2, so it runs on any Mac |
| `tools.txt` | The tool picker's list |
| `install.command` | Copies the script, builds the app with `osacompile` into `~/Applications` |

A log of every file it moved, with the original download name, is kept in `~/Library/Application Support/ODHC File Result/filed.log`.
