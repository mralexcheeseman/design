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
#   file-result.sh guess <file>              best guess: ID<tab>confidence<tab>tool<tab>shot
#   file-result.sh name <ID> <version> <tool> <file>      the name it would get

set -u
HOME_DIR="${ODHC_HOME:-$HOME/Library/Application Support/ODHC File Result}"
mkdir -p "$HOME_DIR"
DEST_FILE="$HOME_DIR/dest"
LAST_FILE="$HOME_DIR/last"
TOOLS_FILE="$HOME_DIR/tools.txt"
LOG_FILE="$HOME_DIR/filed.log"
MODEL_FILE="$HOME_DIR/model"          # Ollama model, written by install.command
CROP_FILE="$HOME_DIR/crop34"          # "1" = crop 3:4 stills to 4:5 (on by default)
OLLAMA="${OLLAMA_URL:-http://127.0.0.1:11434}"

find_dest() {
  if [ -f "$DEST_FILE" ] && [ -d "$(cat "$DEST_FILE")" ]; then cat "$DEST_FILE"; return; fi
  for d in "$HOME"/Library/CloudStorage/GoogleDrive-*/"My Drive"/"ODHC shot results" \
           "$HOME"/Library/CloudStorage/GoogleDrive-*/*/"ODHC shot results" \
           "/Volumes/GoogleDrive/My Drive/ODHC shot results"; do
    if [ -d "$d" ]; then printf '%s\n' "$d" > "$DEST_FILE"; printf '%s\n' "$d"; return; fi
  done
}

# "ODHC shot list.txt" in My Drive (threads keep it current); falls back to the copy installed with the app.
find_shotlist() {
  local f
  for f in "$HOME"/Library/CloudStorage/GoogleDrive-*/"My Drive"/"ODHC shot list.txt" "$HOME_DIR/shotlist.txt"; do
    [ -f "$f" ] && { printf '%s\n' "$f"; return; }
  done
}

is_video() { case "$(printf '%s' "${1##*.}" | tr '[:upper:]' '[:lower:]')" in mp4|mov|m4v|webm) return 0;; esac; return 1; }

# Tool from the download's own name, then from the shot's usual tool, then nothing.
guess_tool() {  # file hint
  local n v=0; n=$(printf '%s' "${1##*/}" | tr '[:upper:]' '[:lower:]'); is_video "$1" && v=1
  case "$n" in
    *kling*) echo kling; return;;
    *seedance*) echo seedance; return;;
    *higgsfield*|hf_*) [ $v = 1 ] && echo seedance || echo higgsfieldnbpro; return;;
    *firefly*) [ $v = 1 ] && echo fireflyvideo || echo firefly; return;;
    *gemini*) [ $v = 1 ] && echo hydrogen || echo gemini; return;;
    *veo*|*flow*) [ $v = 1 ] && echo flowveolite || echo flow; return;;
    *chatgpt*|*dall*) echo gptimage2; return;;
    *recraft*) echo recraft; return;;
    *picsart*) echo picsart; return;;
    *elevenlabs*) echo elevenlabs; return;;
  esac
  case "$(printf '%s' "$2" | tr '[:upper:]' '[:lower:]')" in
    *seedance*) echo seedance;; *higgsfield*) [ $v = 1 ] && echo seedance || echo higgsfieldnbpro;;
    *firefly*) [ $v = 1 ] && echo fireflyvideo || echo firefly;;
    *flow*) [ $v = 1 ] && echo flowveolite || echo flow;;
    *gemini*) [ $v = 1 ] && echo hydrogen || echo gemini;;
    *kling*) echo kling;; *recraft*) echo recraft;; *picsart*) echo picsart;;
  esac
}

# A small JPEG of the picture, or of a clip's first frame, for the model to look at.
preview_jpg() {  # src out.jpg
  local tmp; tmp=$(mktemp -d)
  if is_video "$1"; then
    qlmanage -t -s 768 -o "$tmp" "$1" >/dev/null 2>&1
    sips -s format jpeg "$tmp"/*.png --out "$2" >/dev/null 2>&1
  else
    sips -s format jpeg -Z 768 "$1" --out "$2" >/dev/null 2>&1
  fi
  rm -rf "$tmp"; [ -s "$2" ]
}

guess() {  # src -> ID<tab>confidence<tab>tool<tab>shot
  local src="$1" list id conf=100 hint shot jpg out model
  list=$(find_shotlist)
  # 1. The name already starts with a shot ID from the list.
  id=$(norm_id "$(printf '%s' "${src##*/}" | sed -E 's/^([A-Za-z]+[0-9]+[A-Za-z]?)[-_ .].*$/\1/')")
  if [ -z "$id" ] || [ -z "$list" ] || ! grep -q "^$id	" "$list"; then
    id=""; conf=0
    # 2. Ask the local model which shot the picture shows.
    model=$(cat "$MODEL_FILE" 2>/dev/null)
    if [ -n "$model" ] && [ -n "$list" ] && curl -s -m 2 "$OLLAMA/api/tags" >/dev/null 2>&1; then
      jpg=$(mktemp).jpg
      if preview_jpg "$src" "$jpg"; then
        out=$(osascript -l JavaScript "$HOME_DIR/classify.js" "$jpg" "$list" "$model" "$OLLAMA" 2>/dev/null)
        id=$(norm_id "$(printf '%s' "$out" | cut -f1)")
        conf=$(printf '%s' "$out" | cut -f2 | tr -cd '0-9'); conf=${conf:-0}
        [ -n "$id" ] && grep -q "^$id	" "$list" || { id=""; conf=0; }
      fi
      rm -f "$jpg" "$jpg.req.json"
    fi
  fi
  hint=""; shot=""
  if [ -n "$id" ]; then
    hint=$(grep "^$id	" "$list" | head -1 | cut -f3)
    shot=$(grep "^$id	" "$list" | head -1 | cut -f2 | cut -c1-140)
  fi
  printf '%s\t%s\t%s\t%s\n' "$id" "$conf" "$(guess_tool "$src" "$hint")" "$shot"
}

# Flow stills come out 3:4; posts are 4:5. Trim top and bottom equally.
crop_34() {
  [ "$(cat "$CROP_FILE" 2>/dev/null || echo 1)" = 1 ] || return 0
  is_video "$1" && return 0
  local w h nh
  w=$(sips -g pixelWidth "$1" 2>/dev/null | awk '/pixelWidth/{print $2}')
  h=$(sips -g pixelHeight "$1" 2>/dev/null | awk '/pixelHeight/{print $2}')
  [ -n "$w" ] && [ -n "$h" ] || return 0
  # within 1% of 3:4 portrait
  [ $(( (h*3 - w*4) * 100 / (w*4) )) -eq 0 ] || return 0
  nh=$(( w * 5 / 4 ))
  sips -c "$nh" "$w" "$1" >/dev/null 2>&1 && echo " (cropped 3:4 to 4:5)"
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
  guess)     guess "$2" ;;
  name)
    id=$(norm_id "${2:-}"); ver=$(norm_ver "${3:-}"); tool=$(norm_tool "${4:-}"); dest=$(find_dest)
    ext=$(ext_of "${5:-}"); echo "$id-$ver-$tool-take$(next_take "$dest" "$id-$ver-$tool")${ext:+.$ext}" ;;
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
        case "$tool" in flow*) note=$(crop_34 "$dest/$name");; *) note="";; esac
        echo "OK: $name$note"
        printf '%s\t%s\t%s\n' "$(date '+%Y-%m-%d %H:%M')" "${src##*/}" "$name" >> "$LOG_FILE"
      else
        echo "FAIL: ${src##*/}"
      fi
    done ;;
  *) sed -n '2,14p' "$0"; exit 1 ;;
esac
