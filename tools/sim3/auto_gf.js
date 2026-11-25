function simShot(ang,pw){var b={x:S.b.x,z:S.b.z,vx:Math.sin(ang)*(4+12*pw),vz:-Math.cos(ang)*(4+12*pw)},wt0=S.wt,res=null,k=0;
 while(k<1500&&!res){res=physStep(b,0.008);S.wt+=0.008;k++;if(b.vx===0&&b.vz===0)break}
 S.wt=wt0;var H=S.H,d=Math.hypot(b.x-H.hole[0],b.z-H.hole[1]);
 if(res==='hole')return -1000+0*k;if(res==='water')return 5000;var sandy=H.sand.some(function(r){return inR(b.x,b.z,r)});return d+(sandy?4:0)}
for(var n=0;n<3;n++){S.total=0;loadLevel(n);var guard=0;
 while(S.mode==='play'&&guard<30){guard++;
  // esperar a que pare
  var best=1e9,ba=0,bp=0;
  for(var a=0;a<360;a+=1){for(var pw=0.15;pw<=1.001;pw+=0.05){var sc=simShot(a*Math.PI/180,pw);if(sc<best){best=sc;ba=a*Math.PI/180;bp=pw}}}
  S.ang=ba;shoot(bp);
  var sg=0;while((S.moving||S.sink>0)&&S.mode==='play'&&sg<4000){update(0.016);sg++}
 }
 console.log('hoyo',n+1,S.mode,'golpes',S.strokes,'agua',S.water,'par',S.H.par);
 if(S.mode==='next')S.mode='play'}
