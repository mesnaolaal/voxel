function play(n,smart){loadLevel(n);var steps=0;
 while(S.mode==='play'&&steps<60000){steps++;held.left=held.right=false;
  if(smart){for(var i=0;i<S.slots.length;i++){S.sel=i;if(!S.slots[i].tw&&S.coins>=COST){onSpace()}}
   for(var j=0;j<S.slots.length;j++){S.sel=j;if(S.slots.every(function(s){return s.tw})&&S.slots[j].lv<2&&S.coins>=UPG)onSpace()}}
  update(0.016);}
 return S.mode+' castillo '+S.chp+'/'+S.L.hp+' monedas '+S.coins+' t '+(S.t/1000).toFixed(0)}
for(var n=0;n<3;n++){console.log('nivel',n+1,'con torres:',play(n,true));if(S.mode==='next')S.mode='play'}
for(var n2=0;n2<3;n2++){console.log('nivel',n2+1,'sin hacer nada:',play(n2,false))}
