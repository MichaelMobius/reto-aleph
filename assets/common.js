function norm(s){return String(s??'').trim().toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'')}
async function sha256Text(s){const d=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s));return [...new Uint8Array(d)].map(x=>x.toString(16).padStart(2,'0')).join('')}
function solveExact(expected,next,rune){
 const inp=document.getElementById('answer'),out=document.getElementById('result');
 const v=String(inp?.value??'').trim();
 if(v===expected)reveal(next,rune);else out.innerHTML='<span class="bad">No coincide. Revisa la evidencia.</span>'
}
async function solveHash(expectedHash,next,rune,opts={}){
 const inp=document.getElementById('answer'),out=document.getElementById('result');
 let v=norm(inp.value);if(opts.compact)v=v.replace(/[^a-z0-9]/g,'');
 if(await sha256Text(v)===expectedHash)reveal(next,rune);else out.innerHTML='<span class="bad">No coincide. Revisa la evidencia.</span>'
}
function reveal(next,rune){
 const out=document.getElementById('result');
 out.innerHTML=`<div class="ok"><span class="rune">${rune}</span>fragmento recuperado</div><div class="next"><a class="btn" href="${next}">continuar →</a></div>`;
 try{localStorage.setItem('aleph_last_rune',rune);const m=location.pathname.match(/\/(\d{2})-[^/]+\//);if(m)localStorage.setItem('aleph_rune_'+m[1],rune)}catch(e){}
}
function parseCoords(v){let m=String(v).replace(/,/g,' ').match(/-?\d+(?:\.\d+)?/g);return m&&m.length>=2?[+m[0],+m[1]]:null}
async function solveGeoCells(acceptedHashes,precision,next,rune){
 const out=document.getElementById('result'),p=parseCoords(document.getElementById('answer').value);
 if(!p){out.innerHTML='<span class="bad">Usa latitud, longitud en decimal.</span>';return}
 const key=p[0].toFixed(precision)+','+p[1].toFixed(precision);
 if(acceptedHashes.includes(await sha256Text(key)))reveal(next,rune);else out.innerHTML='<span class="bad">Coordenadas fuera del área esperada. Revisa el lugar y el orden latitud,longitud.</span>'
}
// Deliberately weak client-side labs still teach View Source in the first ring;
// later OSINT/GPS gates do not carry their answer in plaintext.
addEventListener('DOMContentLoaded',()=>{
 document.querySelectorAll('input').forEach((el,i)=>{if(!el.getAttribute('aria-label'))el.setAttribute('aria-label',el.placeholder||`respuesta ${i+1}`)});
 document.querySelectorAll('audio').forEach((el,i)=>{if(!el.getAttribute('aria-label'))el.setAttribute('aria-label',`audio del reto ${i+1}`)});
});