# FileCard

An essay from The Last Animal, filed as a manuscript sliding out of a manila folder.

**Consumer provides:** `title`, `deck` (subtitle), `excerpt`, `arena`, `read_time`, `published_on`, `url` (the essay on thelastanimal.base44.app), and a `seed`.

**Rules**
- A folder tab on top: `label` with the file number ("FILE 021") and the arena. The tab alternates left, centre and right by seed.
- The sheet beneath it: title in `shout-sm` (no letterpress mask at this size; it breaks the letters up), deck in `type` in `ink-2`, then the excerpt's first two lines. Read time and date in `label`, `ink-3`.
- On hover the sheet slides up out of the folder by 24px over `duration-slide`.
- The whole card is one link to the essay, opened in a new tab and announced as such ("opens The Last Animal").
- In lists, at most one stain per three cards.

**Never:** rewrite an essay's title or excerpt, or invent a date or read time that isn't in the source.
