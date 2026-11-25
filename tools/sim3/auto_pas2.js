var DBG=1;
function bfs(sx,sz,tx,tz){var q=[[sx,sz]],pv={},k=function(a,b){return a+','+b};pv[k(sx,sz)]=null;
 while(q.length){var c=q.shift();if(c[0]===tx&&c[1]===tz)break;[[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){var a=c[0]+v[0],b=c[1]+v[1],ch=cellCh(a,b);if(ch===undefined||pv[k(a,b)]!==undefined)return;if('#HAFOT'.indexOf(ch)>=0&&!(a===tx&&b===tz))return;pv[k(a,b)]=c;q.push([a,b])})}
 var path=[],c=[tx,tz];if(pv[k(tx,tz)]===undefined)return null;while(pv[k(c[0],c[1])]){path.unshift(c);c=pv[k(c[0],c[1])]}return path}
function goto(tgt){var p=S.p,path=bfs(Math.round(p.x/C),Math.round(p.z/C),tgt.cx,tgt.cz);
 var wx=tgt.x,wz=tgt.z;if(path&&path.length>1){wx=path[0][0]*C;wz=path[0][1]*C;if(Math.hypot(p.x-wx,p.z-wz)<0.3&&path.length>1){wx=path[1]?path[1][0]*C:wx;wz=path[1]?path[1][1]*C:wz}}
 held.shift=true;held.left=held.right=held.up=held.down=false;
 if(p.x<wx-0.25)held.right=true;else if(p.x>wx+0.25)held.left=true;if(p.z<wz-0.25)held.down=true;else if(p.z>wz+0.25)held.up=true}
for(var n=0;n<3;n++){loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<60000){steps++;var p=S.p,tg=null,L=S.L;
  var oc=function(o){return {x:o.x,z:o.z,cx:Math.round(o.cx/C),cz:Math.round(o.z/C)}};
  function cellOf(o,ex){return {x:ex.x,z:ex.z,cx:Math.round(o.x/C),cz:Math.round(o.z/C)}}
  if(S.hold==='cake'){tg={x:S.table.x,z:S.table.z,cx:Math.round(S.table.x/C),cz:Math.round(S.table.z/C)+1}}
  else if(S.cake){tg={x:S.cake.x,z:S.cake.z,cx:Math.round(S.cake.x/C)+(S.cake.x>S.ovens[0].cx&&0?0:0),cz:Math.round(S.cake.z/C)}}
  else if(S.hold){var o=S.ovens.filter(function(o){return !o.busy})[0]||S.ovens[0];tg={x:o.x,z:o.z,cx:Math.round(o.x/C),cz:Math.round(o.z/C)}}
  else if(S.nIns<L.rec.length){var s=S.st.filter(function(s){return s.k===L.rec[S.nIns]})[0];tg={x:s.x,z:s.z,cx:Math.round(s.x/C),cz:Math.round(s.z/C)}}
  if(tg){goto(tg);var d=Math.hypot(tg.x-p.x,tg.z-p.z);if(d<2.2){held.left=held.right=held.up=held.down=false;
     if(S.hold&&S.hold!=='cake'){var oo=S.ovens.filter(function(o){return !o.busy});if(oo.length)onSpace()}else onSpace()}}
  update(0.016);}
  if(S.mode!=="next"&&S.mode!=="won")console.log("dbg",JSON.stringify(S.cake),S.cakeMade,S.nIns,S.hold,JSON.stringify(S.p),S.ovens.map(function(o){return o.busy}));
 console.log("nivel",n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'quedan',S.time.toFixed(1))
 if(S.mode==='next')S.mode='play'}
