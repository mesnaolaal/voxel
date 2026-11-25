var wins=0;
for(var n=0;n<3;n++){loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<40000){steps++;held.up=true;held.shift=false;var p=S.p,L=S.L;
  S.hd.forEach(function(d){if(d.lane===L.pl&&!d.hit&&p.z<d.z&&d.z-p.z<4.2&&p.air<=0)onSpace()});
  if(L.pit&&p.z<L.pit[0]&&L.pit[0]-p.z<0.5&&p.air<=0)onSpace();
  if(p.scd<=0&&p.v>16)held.shift=true;
  update(0.016);}
 console.log('nivel',n+1,S.mode,'clock',S.clock.toFixed(1),'z',S.p.z.toFixed(0))
 if(S.mode==='next')S.mode='play'}
