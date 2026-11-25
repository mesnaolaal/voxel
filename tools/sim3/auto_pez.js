for(var n=0;n<3;n++){loadLevel(n);var steps=0,t0=S.t;
 while(S.mode==='play'&&steps<90000){steps++;held.left=held.right=held.up=held.down=false;var p=S.p,L=S.L;
  var tg=S.pl.filter(function(c){return !c.got}).sort(function(a,b){return Math.hypot(a.x-p.x,a.y-p.y)-Math.hypot(b.x-p.x,b.y-p.y)})[0];
  var tx,ty;if(tg){tx=tg.x;ty=tg.y}else{tx=L.W+2;ty=5}
  var rx=0,ry=0;
  S.jel.forEach(function(j){var d=Math.hypot(j.x-p.x,j.y+1.6-p.y);if(d<8){var f=(8-d)*1.5;rx+=(p.x-j.x)/(d||1)*f;ry+=(p.y-j.y-1.6)/(d||1)*f}});
  if(S.sh){var d2=Math.hypot(S.sh.x-p.x,S.sh.y-p.y);if(d2<14){var f2=(14-d2)*1.5;rx+=(p.x-S.sh.x)/(d2||1)*f2;ry+=(p.y-S.sh.y)/(d2||1)*f2}if(d2<10&&!p.hid)onSpace()}
  var wx=tx-p.x+rx*2.2,wy=ty-p.y+ry*2.2;
  if(wx>0.4)held.right=true;else if(wx<-0.4)held.left=true;if(wy>0.4)held.up=true;else if(wy<-0.4)held.down=true;
  update(0.016);}
 console.log('nivel',n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'vidas',S.lives,'plancton',S.eat+'/'+S.L.plank)
 if(S.mode==='next')S.mode='play'}
