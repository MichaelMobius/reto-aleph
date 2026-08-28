(()=>{
  const host=document.getElementById('runtime-zone');
  if(!host)return;
  requestAnimationFrame(()=>{
    const node=document.createElement('div');
    node.id='shadow-node';
    node.className='ghost';
    node.dataset.rune=String.fromCharCode(80+5);
    node.dataset.origin='runtime';
    node.textContent='observador';
    host.appendChild(node);
  });
})();