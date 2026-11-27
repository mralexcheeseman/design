// File Result: ask a local Ollama vision model which shot a picture shows.
// osascript -l JavaScript classify.js <image.jpg> <shot list.txt> <model> <ollama url>
// Prints: ID<tab>confidence 0-100<tab>reason
ObjC.import('Foundation');

function q(s) { return "'" + String(s).replace(/'/g, "'\\''") + "'"; }

function run(argv) {
  const [img, listPath, model, url] = argv;
  const app = Application.currentApplication();
  app.includeStandardAdditions = true;

  const b64 = $.NSData.dataWithContentsOfFile(img).base64EncodedStringWithOptions(0).js;
  const raw = $.NSString.stringWithContentsOfFileEncodingError(listPath, $.NSUTF8StringEncoding, null).js;
  const shots = raw.split('\n')
    .filter(l => l && l[0] !== '#' && l.indexOf('\t') > 0)
    .map(l => { const p = l.split('\t'); return p[0] + ': ' + p[1]; })
    .join('\n');

  const prompt =
    'You sort pictures for a 1960s resort-hotel clothing brand. Each picture was made from one shot on this list ' +
    '(ID: what is in the frame, then the hotel in brackets):\n\n' + shots + '\n\n' +
    'Look at the picture: the setting (snow and mountains, beach, pool, gate, garden, lake, harbour), the people, ' +
    'what they are doing, the shirt colour and any animal or prop. Pick the ONE ID that fits best. ' +
    'Answer only with JSON: {"id": "<ID from the list>", "confidence": <0-100>, "why": "<under 12 words>"}';

  const body = JSON.stringify({
    model: model, prompt: prompt, images: [b64], stream: false, format: 'json',
    options: { temperature: 0, num_ctx: 8192 }
  });
  const reqPath = img + '.req.json';
  $.NSString.alloc.initWithUTF8String(body).writeToFileAtomicallyEncodingError(reqPath, true, $.NSUTF8StringEncoding, null);

  const out = app.doShellScript(
    'curl -s --max-time 240 ' + q(url + '/api/generate') + ' -H "Content-Type: application/json" --data-binary @' + q(reqPath),
    { alteringLineEndings: false });
  let r = {};
  try { r = JSON.parse(JSON.parse(out).response); } catch (e) { return '\t0\tno answer'; }
  return [String(r.id || '').trim(), Math.round(Number(r.confidence) || 0), String(r.why || '').replace(/\s+/g, ' ')].join('\t');
}
