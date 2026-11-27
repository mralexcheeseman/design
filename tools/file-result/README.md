# File Result

Names generated pictures and clips by shot ID and files them in the Drive folder **ODHC shot results**, where the Results log script ([../results-log](../results-log/README.md)) adds them to the shot sheet. A free model on the Mac (Ollama) looks at each file and guesses its shot, so most files take one click.

```
Download from Flow, Gemini, Higgsfield, Firefly...
  -> drop the files (or the whole folder) on File Result in the Dock
  -> for each one: "Looks like GV3 (82% sure): Seraina makes her eleventh rescue..."
     Will be filed as GV3-v1-higgsfieldnbpro-take2.png   [Skip] [Change...] [File it]
  -> it lands in ODHC shot results (Drive for desktop uploads it, any size)
  -> the Results log adds a row within 5 minutes
```

How it guesses:

- **Shot:** a name that already starts with a shot ID wins. Otherwise the local model compares the picture (or a clip's first frame) with **ODHC shot list.txt** in My Drive: the storytelling list plus the shot sheet's rows. Threads keep that file current.
- **Tool:** from the download's own name (Gemini, Higgsfield, Firefly, Kling, Veo), then the shot's usual tool, then the last tool you used.
- **Take:** counts up from what's already in the folder.

Flow stills come out 3:4. When the tool is Flow, a 3:4 still is trimmed top and bottom to 4:5 for posts. Turn that off with `echo 0 > ~/Library/Application\ Support/ODHC\ File\ Result/crop34`.

Everything runs on the Mac: nothing is uploaded to a model service, and it costs nothing. The first guess after a restart takes about a minute while the model loads; after that, roughly 10 to 30 seconds a file (an estimate until the first real run).

## Install (once, on the Mac)

1. Install [Ollama](https://ollama.com/download) and open it once. Install [Google Drive for desktop](https://www.google.com/drive/download/) too if it isn't there already (Finder should show Google Drive > My Drive > ODHC shot results).
2. Download `file-result.zip`, unzip it in Downloads, open Terminal and paste: `bash ~/Downloads/file-result/install.command`. It downloads the picture model (Qwen2.5-VL 7B on a Mac with 16 GB or more, Gemma 3 4B on smaller ones; a few GB, once).
3. Drag **File Result** from the Finder window that opens into the Dock.

The first time, macOS may ask whether File Result can control Finder or open files in the Drive folder. Say OK. Without Ollama it still works, asking for each shot ID by hand.

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
| `FileResult.applescript` | The Dock app: shows each guess with a Quick Look preview, confirm or change, then files it |
| `classify.js` | Sends a small preview to the local Ollama model with the shot list and reads back the ID |
| `shotlist.txt` | Fallback copy of the shot list, used when My Drive's `ODHC shot list.txt` isn't synced |
| `file-result.sh` | Guesses shot and tool, finds the Drive folder, normalises the ID (v2c to V2c), counts takes, crops Flow's 3:4 stills, renames and moves. Plain bash 3.2, so it runs on any Mac |
| `tools.txt` | The tool picker's list |
| `install.command` | Copies the scripts, builds the app with `osacompile` into `~/Applications`, downloads the model |

A log of every file it moved, with the original download name, is kept in `~/Library/Application Support/ODHC File Result/filed.log`.
