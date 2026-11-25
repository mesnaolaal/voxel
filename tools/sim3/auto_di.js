function bfs(sx,sz,tx,tz){var q=[[sx,sz]],pv={},k=function(a,b){return a+','+b};pv[k(sx,sz)]=null;
 while(q.length){var c=q.shift();if(c[0]===tx&&c[1]===tz)break;[[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){var a=c[0]+v[0],b=c[1]+v[1];if(!walk(a,b)||pv[k(a,b)]!==undefined)return;pv[k(a,b)]=c;q.push([a,b])})}
 var path=[],c=[tx,tz];if(pv[k(tx,tz)]===undefined)return null;while(pv[k(c[0],c[1])]){path.unshift(c);c=pv[k(c[0],c[1])]}return path}
for(var n=0;n<3;n++){S.lives=3;loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<90000){steps++;held.left=held.right=held.up=held.down=held.shift=false;var p=S.p;
  var tg=S.eggs.filter(function(c){return !c.got}).sort(function(a,b){return Math.hypot(a.x-p.x,a.z-p.z)-Math.hypot(b.x-p.x,b.z-p.z)})[0];
  if(!tg||S.got>=S.L.need)tg=S.nest;
  var path=bfs(Math.round(p.x/C),Math.round(p.z/C),Math.round(tg.x/C),Math.round(tg.z/C));var wx=tg.x,wz=tg.z;
  if(path&&path.length){wx=path[0][0]*C;wz=path[0][1]*C;if(Math.hypot(p.x-wx,p.z-wz)<0.35&&path.length>1){wx=path[1][0]*C;wz=path[1][1]*C}}
  var rx=0,rz=0;S.rex.forEach(function(g){if(g.state==='sleep')return;var d=Math.hypot(g.x-p.x,g.z-p.z);if(d<9){if(d<7)held.shift=true;var f=(9-d)*1.1;rx+=(p.x-g.x)/(d||1)*f;rz+=(p.z-g.z)/(d||1)*f}});
  var ax=wx-p.x+rx*0.7,az=wz-p.z+rz*0.7;if(ch(p.x+Math.sign(ax)*1.8,p.z)==='L'||ch(p.x+Math.sign(ax)*1.8,p.z)==='P'){ax=wx-p.x}if(ch(p.x,p.z+Math.sign(az)*1.8)==='L'||ch(p.x,p.z+Math.sign(az)*1.8)==='P'){az=wz-p.z}
  if(ax>0.25)held.right=true;else if(ax<-0.25)held.left=true;if(az>0.25)held.down=true;else if(az<-0.25)held.up=true;
  update(0.016);}
 console.log('nivel',n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'vidas',S.lives,'huevos',S.got+'/'+S.L.need)
 if(S.mode==='next')S.mode='play'}
