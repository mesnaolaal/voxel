function key(){return S.rb.x+','+S.rb.z+'|'+S.boxes.map(function(b){return b.x+','+b.z}).sort().join(';')}
function solve(){var tg=S.tg.map(function(t){return t.x+','+t.z}).sort().join(';');
 var q=[{r:[S.rb.x,S.rb.z],b:S.boxes.map(function(b){return [b.x,b.z]}),p:[]}],seen={};seen[key()]=1;
 function k2(r,b){return r[0]+','+r[1]+'|'+b.map(function(x){return x[0]+','+x[1]}).sort().join(';')}
 while(q.length){var s=q.shift();if(s.b.map(function(x){return x[0]+','+x[1]}).sort().join(';')===tg)return s.p;
  [[1,0],[-1,0],[0,1],[0,-1]].forEach(function(d){var nx=s.r[0]+d[0],nz=s.r[1]+d[1];if(isWall(nx,nz))return;var nb=s.b.map(function(x){return [x[0],x[1]]});
   var bi=nb.findIndex(function(x){return x[0]===nx&&x[1]===nz});
   if(bi>=0){var mx=nx+d[0],mz=nz+d[1];if(isWall(mx,mz)||nb.some(function(x){return x[0]===mx&&x[1]===mz}))return;nb[bi]=[mx,mz]}
   var kk=k2([nx,nz],nb);if(seen[kk])return;seen[kk]=1;q.push({r:[nx,nz],b:nb,p:s.p.concat([d])})})}return null}
for(var n=0;n<3;n++){loadLevel(n);var path=solve();var i=0,steps=0;
 while(S.mode==='play'&&steps<20000&&path&&i<path.length+3){steps++;held.left=held.right=held.up=held.down=false;
  if(S.anim<=0&&i<path.length){var d=path[i];if(d[0]>0)held.right=true;if(d[0]<0)held.left=true;if(d[1]>0)held.down=true;if(d[1]<0)held.up=true;i++}
  update(0.016);}
 console.log('nivel',n+1,S.mode,'pasos',path?path.length:'sin solucion','mov',S.moves)
 if(S.mode==='next')S.mode='play'}
