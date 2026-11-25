#!/bin/bash
# Installs "File Result" for ODHC. Run once:  bash ~/Downloads/file-result/install.command
set -e
here="$(cd "$(dirname "$0")" && pwd)"
support="$HOME/Library/Application Support/ODHC File Result"
mkdir -p "$support" "$HOME/Applications"
cp "$here/file-result.sh" "$support/file-result.sh"
[ -f "$support/tools.txt" ] || cp "$here/tools.txt" "$support/tools.txt"
chmod +x "$support/file-result.sh"
rm -rf "$HOME/Applications/File Result.app"
osacompile -o "$HOME/Applications/File Result.app" "$here/FileResult.applescript"
dest="$(/bin/bash "$support/file-result.sh" find-dest)"
echo
echo "Installed: ~/Applications/File Result.app"
if [ -n "$dest" ]; then
  echo "Results go to: $dest"
else
  echo "Couldn't find 'ODHC shot results' in Google Drive for desktop yet. The app will ask for the folder the first time."
fi
echo "Next: drag File Result from the Finder window that opens into your Dock."
open -R "$HOME/Applications/File Result.app"
