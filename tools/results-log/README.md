# Results log

A Google Apps Script bound to the shot sheet. Every 5 minutes it lists the Drive folder **ODHC shot results** and gives each new file a row on the Results tab: Added, File, Drive link (columns A to C). The formula columns D to I do the rest. It replaces the Results Zap, so logging uses no Zapier tasks.

It matches on the Drive file id in column C, so files already logged (by hand or by the old Zap) are never logged twice, and anything missed gets picked up on the next run.

## Install (once)

1. In Zapier, switch the "ODHC shot results to Results tab" Zap **off**, so the two don't both log the same file.
2. Open the shot sheet, then **Extensions > Apps Script**.
3. Delete what's in `Code.gs`, paste in [`Code.gs`](Code.gs) from this folder, and save.
4. Pick `setup` in the function menu at the top and press **Run**. Approve the Google sign-in (Advanced > Go to project if it warns, since it's your own script).

That's it. `setup` logs anything new straight away and then runs every 5 minutes. To check it, open **Triggers** (clock icon) in Apps Script: one trigger, `logNewResults`, every 5 minutes.
