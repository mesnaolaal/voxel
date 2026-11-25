for(var n=0;n<3;n++){loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<80000){steps++;held.left=held.right=held.up=held.down=false;var p=S.p;
  held.up=true;
  var la=14+Math.abs(p.v)*0.45,tz=p.z-la,tx=cxOf(tz);
  // evitar obstaculos
  var best=0;S.cones.forEach(function(c){if(c.hit)return;var dz=p.z-c.z;if(dz>-1&&dz<26){var dx=p.x-c.x;if(Math.abs(dx)<3.2)tx=c.x+(dx>=0?4.2:-4.2)}});
  S.oils.forEach(function(o){var dz=p.z-o.z;if(dz>-1&&dz<26){var dx=p.x-o.x;if(Math.abs(dx)<4.2)tx=o.x+(dx>=0?5:-5)}});
  S.gas.forEach(function(g){if(g.got)return;var dz=p.z-g.z;if(dz>0&&dz<40&&Math.abs(g.x-p.x)<5)tx=g.x});
  var lim=S.L.w/2-1.5,c0=cxOf(tz);tx=Math.max(c0-lim,Math.min(c0+lim,tx));
  var want=Math.atan2(tx-p.x,p.z-tz),err=want-p.psi;
  if(err>0.03)held.right=true;else if(err<-0.03)held.left=true;
  if(p.tcd<=0&&p.v>30&&Math.abs(err)<0.05)onSpace();
  update(0.016);}
 console.log('nivel',n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'quedan',S.time.toFixed(1),'z',S.p.z.toFixed(0),'off',S.p.off)
 if(S.mode==='next')S.mode='play'}
