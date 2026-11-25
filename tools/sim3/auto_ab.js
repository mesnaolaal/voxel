for(var n=0;n<3;n++){loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<90000){steps++;held.left=held.right=held.up=held.down=held.shift=false;var p=S.p;
  var tg=S.fl.filter(function(c){return !c.done}).sort(function(a,b){return Math.hypot(a.x-p.x,a.z-p.z)-Math.hypot(b.x-p.x,b.z-p.z)})[0];
  var tx,tz;if(tg){tx=tg.x;tz=tg.z}else{tx=S.hive.x;tz=S.hive.z}
  var rx=0,rz=0;S.sp.forEach(function(g){var d=Math.hypot(g.x-p.x,g.z-p.z);if(d<7&&g.flee<=0){var f=(7-d)*1.2;rx+=(p.x-g.x)/(d||1)*f;rz+=(p.z-g.z)/(d||1)*f;if(d<4.5)held.shift=true}});
  if(tg&&Math.hypot(tx-p.x,tz-p.z)<1.6&&p.land<=0){onSpace()}
  var wx=tx-p.x+rx*1.6,wz=tz-p.z+rz*1.6;
  if(wx>0.3)held.right=true;else if(wx<-0.3)held.left=true;if(wz>0.3)held.down=true;else if(wz<-0.3)held.up=true;
  update(0.016);}
 console.log('nivel',n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'vidas',S.lives,'flores',S.pol+'/'+S.nf)
 if(S.mode==='next')S.mode='play'}
