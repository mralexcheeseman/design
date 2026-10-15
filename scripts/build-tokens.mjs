// Usage: node scripts/build-tokens.mjs [brand]   (no brand = every brand)
// Writes brands/<brand>/tokens.css from brands/<brand>/tokens.json, so components and storefronts read one source.
// Pass --check to fail instead of writing when tokens.css is out of date (CI runs this).
import {readFileSync,writeFileSync,readdirSync,existsSync} from 'node:fs';
const args=process.argv.slice(2),check=args.includes('--check');
const brands=args.filter(a=>!a.startsWith('--'));
const all=readdirSync('brands',{withFileTypes:true}).filter(d=>d.isDirectory()&&existsSync(`brands/${d.name}/tokens.json`)).map(d=>d.name);
let stale=0;
for(const b of brands.length?brands:all){
 const t=JSON.parse(readFileSync(`brands/${b}/tokens.json`,'utf8'));
 const lines=[];
 const ref=v=>String(v).replace(/\{color\.([\w-]+)\}/g,'var(--$1)');
 for(const c of t.color.tokens)lines.push(`--${c.name}:${c.value};`);
 for(const [k,v] of Object.entries(t.type.families))lines.push(`--font-${k}:${v};`);
 for(const g of t.type.groups)for(const s of g.styles){
  lines.push(`--type-${s.name}-size:${s.fontSize};`);
  if(s.fontSizeMobile)lines.push(`--type-${s.name}-size-mobile:${s.fontSizeMobile};`);
 }
 for(const group of ['spacing','radius','shadow','motion','focus','layout','zIndex'])
  for(const k of t[group]?.tokens||[])lines.push(`--${k.name}:${ref(k.value)};`);
 const css=`/* Generated from tokens.json by scripts/build-tokens.mjs. Do not edit by hand. */\n:root{\n${lines.map(l=>' '+l).join('\n')}\n}\n`;
 const out=`brands/${b}/tokens.css`;
 if(check){if(!existsSync(out)||readFileSync(out,'utf8')!==css){console.log(`${out} is out of date: run node scripts/build-tokens.mjs ${b}`);stale++;}}
 else{writeFileSync(out,css);console.log(`wrote ${out}`);}
}
if(stale)process.exit(1);
