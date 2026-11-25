#!/bin/bash
# ODHC File Result: names generated files by shot ID and moves them into the
# Drive-synced "ODHC shot results" folder. The Results log script then logs each one.
# Works with macOS's built-in bash 3.2. Dialogs live in the app (File Result.app);
# this script only does the file work.
#
#   file-result.sh find-dest                 print the results folder, or nothing
#   file-result.sh set-dest <folder>         remember the results folder
#   file-result.sh last                      print "ID version tool" used last time
#   file-result.sh tools                     print the tool list
#   file-result.sh file <ID> <version> <tool> <file>...   rename and move

set -u
HOME_DIR="${ODHC_HOME:-$HOME/Library/Application Support/ODHC File Result}"
mkdir -p "$HOME_DIR"
DEST_FILE="$HOME_DIR/dest"
LAST_FILE="$HOME_DIR/last"
TOOLS_FILE="$HOME_DIR/tools.txt"
LOG_FILE="$HOME_DIR/filed.log"

find_dest() {
  if [ -f "$DEST_FILE" ] && [ -d "$(cat "$DEST_FILE")" ]; then cat "$DEST_FILE"; return; fi
  for d in "$HOME"/Library/CloudStorage/GoogleDrive-*/"My Drive"/"ODHC shot results" \
           "$HOME"/Library/CloudStorage/GoogleDrive-*/*/"ODHC shot results" \
           "/Volumes/GoogleDrive/My Drive/ODHC shot results"; do
    if [ -d "$d" ]; then printf '%s\n' "$d" > "$DEST_FILE"; printf '%s\n' "$d"; return; fi
  done
}

# V2c, v2c, px3 -> V2c, PX3. Prints nothing if it isn't a shot ID.
norm_id() {
  local s; s=$(printf '%s' "$1" | tr -d '[:space:]')
  if printf '%s' "$s" | grep -Eq '^[A-Za-z]+[0-9]+[A-Za-z]?$'; then
    local head tail
    head=$(printf '%s' "$s" | sed -E 's/^([A-Za-z]+[0-9]+).*/\1/' | tr '[:lower:]' '[:upper:]')
    tail=$(printf '%s' "$s" | sed -E 's/^[A-Za-z]+[0-9]+//' | tr '[:upper:]' '[:lower:]')
    printf '%s%s' "$head" "$tail"
  fi
}

norm_ver() {  # 2, v2, V2 -> v2 ; default v1
  local n; n=$(printf '%s' "$1" | tr -cd '0-9')
  printf 'v%s' "${n:-1}"
}

norm_tool() { printf '%s' "$1" | awk '{print $1}' | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9'; }

# Last real extension, lower case: "x.mp4,.mp4" -> mp4, "a.jpg.png" -> png
ext_of() {
  local base="${1##*/}"
  case "$base" in *.*) ;; *) return;; esac
  printf '%s' "${base##*.}" | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9'
}

next_take() {  # dest prefix -> 1 + highest take already there
  local dest="$1" prefix="$2" max=0 n f
  for f in "$dest/$prefix"-take*; do
    [ -e "$f" ] || continue
    n=$(printf '%s' "${f##*/}" | sed -E "s/^.*-take([0-9]+).*$/\1/")
    case "$n" in ''|*[!0-9]*) continue;; esac
    [ "$n" -gt "$max" ] && max=$n
  done
  echo $((max + 1))
}

case "${1:-}" in
  find-dest) find_dest ;;
  set-dest)  [ -d "${2:-}" ] && printf '%s\n' "$2" > "$DEST_FILE" ;;
  last)      [ -f "$LAST_FILE" ] && cat "$LAST_FILE" ;;
  tools)     cat "$TOOLS_FILE" ;;
  file)
    shift
    id=$(norm_id "${1:-}"); ver=$(norm_ver "${2:-}"); tool=$(norm_tool "${3:-}")
    shift 3 2>/dev/null || { echo "ERROR: usage: file ID version tool files..."; exit 2; }
    [ -n "$id" ]   || { echo "ERROR: that isn't a shot ID (try V2c or T1a)"; exit 2; }
    [ -n "$tool" ] || { echo "ERROR: no tool picked"; exit 2; }
    dest=$(find_dest)
    [ -n "$dest" ] || { echo "ERROR: can't find the ODHC shot results folder"; exit 3; }
    printf '%s %s %s\n' "$id" "$ver" "$tool" > "$LAST_FILE"
    prefix="$id-$ver-$tool"
    for src in "$@"; do
      [ -f "$src" ] || { echo "SKIP: ${src##*/} (not a file)"; continue; }
      take=$(next_take "$dest" "$prefix")
      ext=$(ext_of "$src")
      name="$prefix-take$take${ext:+.$ext}"
      if mv -n "$src" "$dest/$name" && [ -e "$dest/$name" ]; then
        echo "OK: $name"
        printf '%s\t%s\t%s\n' "$(date '+%Y-%m-%d %H:%M')" "${src##*/}" "$name" >> "$LOG_FILE"
      else
        echo "FAIL: ${src##*/}"
      fi
    done ;;
  *) sed -n '2,12p' "$0"; exit 1 ;;
esac
