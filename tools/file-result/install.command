#!/bin/bash
# Installs "File Result" for ODHC. Run once:  bash ~/Downloads/file-result/install.command
# Safe to run again: it updates the app and keeps your tool list and settings.
set -e
here="$(cd "$(dirname "$0")" && pwd)"
support="$HOME/Library/Application Support/ODHC File Result"
mkdir -p "$support" "$HOME/Applications"
cp "$here/file-result.sh" "$here/classify.js" "$here/shotlist.txt" "$support/"
[ -f "$support/tools.txt" ] || cp "$here/tools.txt" "$support/tools.txt"
chmod +x "$support/file-result.sh"
rm -rf "$HOME/Applications/File Result.app"
osacompile -o "$HOME/Applications/File Result.app" "$here/FileResult.applescript"

# Local model: Ollama, free and on this Mac only.
ram_gb=$(( $(sysctl -n hw.memsize) / 1073741824 ))
if [ "$ram_gb" -ge 16 ]; then model="qwen2.5vl:7b"; else model="gemma3:4b"; fi
ollama_bin="$(command -v ollama || true)"
[ -z "$ollama_bin" ] && [ -x /Applications/Ollama.app/Contents/Resources/ollama ] && ollama_bin=/Applications/Ollama.app/Contents/Resources/ollama
if [ -n "$ollama_bin" ]; then
  open -ga Ollama 2>/dev/null || true
  for i in 1 2 3 4 5 6 7 8 9 10; do curl -s -m 1 http://127.0.0.1:11434/api/tags >/dev/null && break; sleep 1; done
  echo "Downloading the picture model $model for your ${ram_gb} GB Mac (a few GB, once)..."
  "$ollama_bin" pull "$model" && printf '%s\n' "$model" > "$support/model"
else
  echo
  echo "Ollama isn't installed, so File Result will ask for each shot ID by hand."
  echo "For automatic guesses: install Ollama from https://ollama.com/download, open it once, then run this installer again."
fi

dest="$(/bin/bash "$support/file-result.sh" find-dest)"
echo
echo "Installed: ~/Applications/File Result.app"
[ -f "$support/model" ] && echo "Shot guessing: on, using $(cat "$support/model")"
if [ -n "$dest" ]; then echo "Results go to: $dest"
else echo "Couldn't find 'ODHC shot results' in Google Drive for desktop yet. The app will ask for the folder the first time."; fi
echo "Next: drag File Result from the Finder window that opens into your Dock (replace the old one if you had it)."
open -R "$HOME/Applications/File Result.app"
