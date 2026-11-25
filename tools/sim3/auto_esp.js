for(var n=0;n<3;n++){S.lives=3;loadLevel(n);var steps=0,t0=S.t,tries=0;
 while(S.mode==='play'&&steps<80000){steps++;held.left=held.right=held.up=held.down=held.shift=false;var p=S.p;
  var tx=0,ty=0;var cr=S.crys.filter(function(c){return !c.got&&c.z<p.z+2}).sort(function(a,b){return b.z-a.z})[0];
  if(cr&&cr.z>p.z-90){tx=cr.x;ty=cr.y}
  var rx=0,ry=0;
  S.asts.forEach(function(a){if(a.dead)return;var dz=p.z-a.z;if(dz>-2&&dz<26){var ddx=p.x-a.x,ddy=p.y-a.y,d=Math.hypot(ddx,ddy);if(d<a.r+4){var f=(a.r+4-d)*2.5;rx+=ddx/(d||1)*f+(d<0.1?3:0);ry+=ddy/(d||1)*f}}});
  S.ufos.forEach(function(u){var dz=p.z-u.z;if(dz>-2&&dz<30){var ddx=p.x-u.x,ddy=p.y-u.y,d=Math.hypot(ddx,ddy);if(d<8){var f=(8-d)*2.5;rx+=ddx/(d||1)*f;ry+=ddy/(d||1)*f}}});
  var wx=tx+rx*1.2,wy=ty+ry*1.2;
  if(p.x<wx-0.4)held.right=true;else if(p.x>wx+0.4)held.left=true;if(p.y<wy-0.4)held.up=true;else if(p.y>wy+0.4)held.down=true;
  var ast=S.asts.filter(function(a){return !a.dead&&a.z<p.z-5&&a.z>p.z-60&&Math.abs(a.x-p.x)<a.r+1&&Math.abs(a.y-p.y)<a.r+1})[0];if(ast)onSpace();
  update(0.016);}
 console.log('nivel',n+1,S.mode,'t',((S.t-t0)/1000).toFixed(1),'vidas',S.lives,'cristales',S.cr+'/'+S.L.crystals)
 if(S.mode==='next')S.mode='play'}
