function bfsJ(sx,sz,tx,tz){var q=[[sx,sz]],prev={},k=function(a,b){return a+','+b};prev[k(sx,sz)]=null;
 while(q.length){var c=q.shift();if(c[0]===tx&&c[1]===tz)break;
  [[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){var a=c[0]+v[0],b=c[1]+v[1];
   if(walk(a,b)){if(prev[k(a,b)]===undefined){prev[k(a,b)]={from:c,jump:false};q.push([a,b])}}
   else if(cellCh(a,b)==='V'){var a2=a+v[0],b2=b+v[1];if(walk(a2,b2)&&prev[k(a2,b2)]===undefined){prev[k(a2,b2)]={from:c,jump:true};q.push([a2,b2])}}})}
 var path=[],c=[tx,tz];if(prev[k(tx,tz)]===undefined)return null;while(prev[k(c[0],c[1])]){var e=prev[k(c[0],c[1])];path.unshift({c:c,jump:e.jump});c=e.from}return path}
for(var n=0;n<3;n++){loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<60000){steps++;held.left=held.right=held.up=held.down=false;var p=S.p;
  var tg=S.hens.filter(function(c){return !c.got}).sort(function(a,b){return Math.hypot(a.x-p.x,a.z-p.z)-Math.hypot(b.x-p.x,b.z-p.z)})[0];
  if(!tg)break;
  var path=bfsJ(Math.round(p.x/C),Math.round(p.z/C),Math.round(tg.x/C),Math.round(tg.z/C));
  var wx=tg.x,wz=tg.z;
  if(path&&path.length){var st=path[0];wx=st.c[0]*C;wz=st.c[1]*C;
   if(st.jump){var pcx=Math.round(p.x/C)*C,pcz=Math.round(p.z/C)*C;
     if(Math.hypot(p.x-pcx,p.z-pcz)>0.35&&p.air<=0){wx=pcx;wz=pcz}else if(p.air<=0)onSpace()}}
  if(p.x<wx-0.2)held.right=true;else if(p.x>wx+0.2)held.left=true;if(p.z<wz-0.2)held.down=true;else if(p.z>wz+0.2)held.up=true;
  update(0.016);}
 console.log('nivel',n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'quedan',S.time.toFixed(1),'gallinas',S.got+'/'+S.nh)
 if(S.mode==='next')S.mode='play'}
