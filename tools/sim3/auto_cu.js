for(var n=0;n<3;n++){loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<60000){steps++;held.left=held.right=held.up=held.down=false;var p=S.p;
  var tg;if(S.cry)tg={x:S.cry.x,z:S.cry.z};else{tg=S.mon.filter(function(g){return g.hp>0}).sort(function(a,b){return Math.hypot(a.x-p.x,a.z-p.z)-Math.hypot(b.x-p.x,b.z-p.z)})[0]}
  var ax=tg.x-p.x,az=tg.z-p.z,d=Math.hypot(ax,az);
  // si hay pared entre medias, seguir el campo BFS
  var tx=tg.x,tz=tg.z;if(!los(p.x,p.z,tg.x,tg.z)&&S.dist){var cx=Math.round(p.x/C),cz=Math.round(p.z/C),bd=S.dist[cz][cx],best=null;var f=bfsField(Math.round(tg.x/C),Math.round(tg.z/C));bd=f[cz][cx];[[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){var a=cx+v[0],b=cz+v[1];if(walk(a,b)&&f[b][a]<bd){bd=f[b][a];best=[a*C,b*C]}});if(best){tx=best[0];tz=best[1]}}
  var wx=tx-p.x,wz=tz-p.z;
  if(!S.cry&&d<tg.rad+3.0){ // atacar: encarar
    p.fx=ax/d;p.fz=az/d;p.ry=Math.atan2(ax,az);if(p.swc<=0)onSpace();
    if(tg.stun<=0&&d<tg.rad+1.6){wx=-ax;wz=-az}else if(d>tg.rad+2.2){} else {wx=0;wz=0}}
  if(wx>0.3)held.right=true;else if(wx<-0.3)held.left=true;if(wz>0.3)held.down=true;else if(wz<-0.3)held.up=true;
  update(0.016);}
 console.log('nivel',n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'vidas',S.lives)
 if(S.mode==='next')S.mode='play'}
