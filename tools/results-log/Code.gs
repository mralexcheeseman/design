/**
 * ODHC Results log. Paste into the shot sheet: Extensions > Apps Script.
 * Run setup() once. After that, every 5 minutes, any new file in the Drive
 * folder "ODHC shot results" gets a row on the Results tab (columns A to C
 * only; the sheet's formulas fill D to I). Free, no Zapier tasks.
 */
const FOLDER_ID = '1dIJrRxIywfnxHROh_GCwqa9NHleMXZPo'; // ODHC shot results
const SHEET_ID = '1r8FMSsbHvxBS9qPwK21IHm8-Z4q7tZZhlceBrdRi7zY'; // ODHC shot ideas
const TAB = 'Results';
const TZ = 'Europe/London';

function setup() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'logNewResults')
    .forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('logNewResults').timeBased().everyMinutes(5).create();
  logNewResults();
}

function logNewResults() {
  const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(TAB);
  const last = lastFilledRow_(sheet);
  const links = last > 1 ? sheet.getRange(2, 3, last - 1, 1).getValues().flat() : [];
  const known = new Set(links.map(l => (String(l).match(/\/d\/([\w-]+)/) || [])[1]).filter(Boolean));

  const fresh = [];
  const files = DriveApp.getFolderById(FOLDER_ID).getFiles();
  while (files.hasNext()) {
    const f = files.next();
    if (!known.has(f.getId())) fresh.push(f);
  }
  if (!fresh.length) return;
  fresh.sort((a, b) => a.getDateCreated() - b.getDateCreated());
  const rows = fresh.map(f => [
    Utilities.formatDate(f.getDateCreated(), TZ, 'yyyy-MM-dd HH:mm'),
    f.getName(),
    'https://drive.google.com/file/d/' + f.getId() + '/view',
  ]);
  sheet.getRange(last + 1, 1, rows.length, 3).setValues(rows);
}

// Last row with a file name in column B (formula columns don't count).
function lastFilledRow_(sheet) {
  const col = sheet.getRange('B1:B' + sheet.getMaxRows()).getValues();
  for (let i = col.length - 1; i >= 0; i--) if (col[i][0] !== '') return i + 1;
  return 1;
}
