import re,sys
from common import build,head,A,B
G=r'''
amb.intensity=0.95;sun.intensity=0.8;
var LEN=26,GAP=6,R=0.9,SL=0.05;
var LV=[{N:2,iv:2.6,pl:0.15,red:0,ham:false,gor:[[3,1,0]],time:100},{N:3,iv:2.0,pl:0.3,red:0.2,ham:true,gor:[[3,1,0]],time:90},{N:4,iv:1.7,pl:0.45,red:0.3,ham:true,gor:[[3,1,0],[22,-1,0.85]],time:80}];
function dirOf(i){return ((S.L.N-1-i)%2===0)?1:-1}
function tilt(i){return -SL*dirOf(i)}
function gy(i,x){return i*GAP+tilt(i)*(x-LEN/2)}
function ladX(i){return ((S.L.N-1-i)%2===0)?16:5}
var AC=null,MUTE=false,best=0;try{best=+localStorage.getItem('barrilBest')||0}catch(e){}
function saveBest(){if(S.score>best){best=S.score;try{localStorage.setItem('barrilBest',String(best))}catch(e){}}}
function beep(f,d,ty,v,f2){if(MUTE)return;try{if(!AC)AC=new (window.AudioContext||window.webkitAudioContext)();var o=AC.createOscillator(),g=AC.createGain(),t=AC.currentTime;o.type=ty||'square';o.frequency.setValueAtTime(f,t);if(f2)o.frequency.exponentialRampToValueAtTime(f2,t+d);g.gain.setValueAtTime(v||0.05,t);g.gain.exponentialRampToValueAtTime(0.0001,t+d);o.connect(g);g.connect(AC.destination);o.start();o.stop(t+d)}catch(e){}}
var wk=null,hamM=null,catG=null,gorM=[],pops=[],parts=[],shk=0,shadow=null,meowT=3;
function burst(x,y,col,n){for(var i=0;i<n;i++){var m=bx(0.35,0.35,0.35,col,x,y,0.4,lvGroup);parts.push({m:m,vx:(Math.random()-0.5)*9,vy:Math.random()*8+2,vz:Math.random()*2,t:0})}}
function pop(txt,x,y,col){try{var c=document.createElement('canvas');c.width=128;c.height=48;var g=c.getContext('2d');g.font='bold 34px sans-serif';g.textAlign='center';g.lineWidth=6;g.strokeStyle='#1E1B4B';g.strokeText(txt,64,36);g.fillStyle=col||'#FDE047';g.fillText(txt,64,36);var sp=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(c),transparent:true,depthTest:false}));sp.scale.set(4.2,1.6,1);sp.position.set(x,y,2);lvGroup.add(sp);pops.push({m:sp,t:0})}catch(e){}}
function mkWorker(){var g=new THREE.Group(),o={g:g};
  function limb(w,h,d,col,x,y){var p=new THREE.Group();p.position.set(x,y,0);bx(w,h,d,col,0,-h/2,0,p);g.add(p);return p}
  o.legL=limb(0.55,1.1,0.55,'#1E3A8A',-0.35,1.1);o.legR=limb(0.55,1.1,0.55,'#1E3A8A',0.35,1.1);
  bx(0.6,0.25,0.8,'#111827',-0.35,0.12,0.12,g);bx(0.6,0.25,0.8,'#111827',0.35,0.12,0.12,g);
  bx(1.4,1.4,0.8,'#F97316',0,1.8,0,g);bx(1.42,0.3,0.82,'#FDE68A',0,1.9,0,g);
  o.armL=limb(0.4,1.2,0.45,'#FCD9A6',-0.9,2.4);o.armR=limb(0.4,1.2,0.45,'#FCD9A6',0.9,2.4);
  bx(0.95,0.85,0.8,'#FCD9A6',0,2.9,0,g);bx(1.05,0.35,0.9,'#FACC15',0,3.45,0,g);bx(1.3,0.12,1.15,'#FACC15',0,3.25,0.15,g);
  bx(0.14,0.14,0.06,'#111827',-0.22,2.95,0.41,g);bx(0.14,0.14,0.06,'#111827',0.22,2.95,0.41,g);
  var h=new THREE.Group();h.position.set(0,-1.1,0.35);bx(0.2,1.8,0.2,'#92400E',0,0.4,0,h);bx(1.2,0.8,0.5,'#9CA3AF',0,1.4,0,h);bx(1.2,0.2,0.52,'#D1D5DB',0,1.7,0,h);o.armR.add(h);h.visible=false;o.ham=h;
  return o}
function mkBarrel(red){var g=new THREE.Group(),c1=red?'#DC2626':'#B45309',c2=red?'#7F1D1D':'#78350F';bx(1.8,1.8,1.6,c1,0,0,0,g);var b=bx(1.8,1.8,1.6,c1,0,0,0,g);b.rotation.z=Math.PI/4;
  bx(1.9,0.35,1.7,c2,0,0.55,0,g);bx(1.9,0.35,1.7,c2,0,-0.55,0,g);bx(0.7,0.7,0.1,c2,0,0,0.85,g);bx(0.25,0.25,0.12,'#FDE047',0.35,0.35,0.86,g);return g}
function mkGorilla(){var g=new THREE.Group(),o={g:g},B1='#5B3A29',B2='#44281B',F='#B98B5E';
  bx(1.1,1.4,1.1,B2,-0.9,0.7,0,g);bx(1.1,1.4,1.1,B2,0.9,0.7,0,g);
  bx(3.4,2.4,1.8,B1,0,2.5,0,g);bx(2.2,1.7,0.2,F,0,2.4,0.95,g);
  bx(2.0,1.6,1.5,B1,0,4.1,0.05,g);bx(1.3,0.9,0.2,F,0,3.95,0.85,g);bx(0.3,0.3,0.1,'#FFFFFF',-0.5,4.45,0.82,g);bx(0.3,0.3,0.1,'#FFFFFF',0.5,4.45,0.82,g);bx(0.14,0.14,0.1,'#111827',-0.5,4.4,0.88,g);bx(0.14,0.14,0.1,'#111827',0.5,4.4,0.88,g);bx(2.1,0.25,0.3,B2,0,4.75,0.8,g);
  function arm(x){var p=new THREE.Group();p.position.set(x,3.5,0);bx(1.0,2.8,1.0,B1,0,-1.3,0,p);bx(1.1,0.8,1.1,F,0,-2.9,0,p);g.add(p);return p}
  o.armL=arm(-2.2);o.armR=arm(2.2);var hb=mkBarrel();hb.position.set(0,6.6,0.4);hb.visible=false;g.add(hb);o.held=hb;g.scale.set(1.2,1.2,1.2);return o}
function mkCat(){var g=new THREE.Group(),c='#FDBA74';bx(1.8,1.2,2.2,c,0,0.8,0,g);bx(1.7,1.7,1.6,c,0,2.0,0.5,g);bx(0.5,0.6,0.5,c,-0.6,3.1,0.5,g);bx(0.5,0.6,0.5,c,0.6,3.1,0.5,g);bx(0.25,0.25,0.1,'#111827',-0.4,2.2,1.32,g);bx(0.25,0.25,0.1,'#111827',0.4,2.2,1.32,g);bx(0.3,0.25,0.1,'#F9A8D4',0,1.8,1.32,g);bx(0.4,0.4,1.4,c,0,1.4,-1.5,g);bx(1.2,0.5,0.1,'#FFFFFF',0,0.6,1.12,g);
  var h=bx(0.9,0.9,0.3,'#F43F5E',0,4.4,0,g);bx(0.5,0.5,0.31,'#FB7185',0,4.4,0,g);return g}
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();pops=[];parts=[];shk=0;meowT=3;var r=rng(77+n*5),i,k,N=L.N;
  scene.background.set('#2E1065');scene.fog.color.set('#4C1D95');scene.fog.near=80;scene.fog.far=190;
  bx(160,2,70,'#1E1B4B',LEN/2,-2,-6,lvGroup);
  for(i=0;i<80;i++)bx(0.3,0.3,0.3,'#FFFFFF',-25+r()*80,12+r()*70,-30,lvGroup);
  bx(5,5,1,'#FDE68A',LEN+14,N*GAP+8,-28,lvGroup);
  for(i=0;i<24;i++){var hh=10+r()*42,xx=-34+i*4.6,bd=-14-r()*8;bx(4.2,hh,3,'#3B1D7A',xx,hh/2-1,bd,lvGroup);
    for(k=0;k<hh/4;k++)if(r()<0.6)bx(0.7,0.9,0.1,'#FDE68A',xx-1+r()*2,2+k*3.6,bd+1.55,lvGroup)}
  for(i=0;i<N;i++){var g=new THREE.Group();g.position.set(LEN/2,i*GAP-0.5,0);g.rotation.z=Math.atan(tilt(i));lvGroup.add(g);
    bx(LEN+2,1,3.6,'#DC2626',0,0,0,g);bx(LEN+2,0.45,0.2,'#991B1B',0,-0.05,1.85,g);bx(LEN+2,0.15,3.6,'#EF4444',0,0.5,0,g);
    for(k=-LEN/2;k<=LEN/2;k+=3)bx(0.5,0.5,3.7,'#B91C1C',k,0.2,0,g);
    for(k=-LEN/2+1;k<LEN/2;k+=4)bx(0.35,1.6,0.35,'#7F1D1D',k,-1.3,1.2,g)}
  var ph=(N-1)*GAP+3;bx(0.9,ph+2,0.9,'#7F1D1D',-1,ph/2-1,0,lvGroup);bx(0.9,ph+2,0.9,'#7F1D1D',LEN+1,ph/2-1,0,lvGroup);
  S.lad=[];for(i=1;i<N;i++){var lx=ladX(i),cx=lx+1.5,bt=gy(i-1,cx),tp=gy(i,cx),hh2=tp-bt;S.lad.push({i:i,cx:cx,bot:bt,top:tp});
    bx(0.3,hh2,0.4,'#FBBF24',lx+0.2,bt+hh2/2,0.3,lvGroup);bx(0.3,hh2,0.4,'#FBBF24',lx+2.8,bt+hh2/2,0.3,lvGroup);
    for(k=0.6;k<hh2;k+=1)bx(2.6,0.2,0.3,'#FDE68A',cx,bt+k,0.3,lvGroup)}
  wk=mkWorker();lvGroup.add(wk.g);shadow=bx(1.6,0.06,1.6,'#0B0B2A',0,0,0.2,lvGroup);shadow.material=new THREE.MeshBasicMaterial({color:'#0B0B2A',transparent:true,opacity:0.45});
  S.gor=[];gorM=[];L.gor.forEach(function(gg,j){var m=mkGorilla(),lvl=N-1-j;m.g.position.set(gg[0],gy(lvl,gg[0]),0);lvGroup.add(m.g);gorM.push(m);S.gor.push({x:gg[0],dir:gg[1],lvl:lvl,t:L.iv-1.5+gg[2],iv:L.iv,throwT:0,m:m})});
  catG=mkCat();catG.position.set(LEN-3,gy(N-1,LEN-3),0);lvGroup.add(catG);
  hamM=null;S.ham=null;if(L.ham){hamM=new THREE.Group();bx(0.25,2.2,0.25,'#92400E',0,0,0,hamM);bx(1.5,1.0,0.7,'#9CA3AF',0,1.2,0,hamM);bx(1.5,0.25,0.72,'#D1D5DB',0,1.55,0,hamM);var hx=12;hamM.position.set(hx,gy(1,hx)+1.6,0);lvGroup.add(hamM);S.ham={x:hx,y:gy(1,hx)}}
  S.barrels=[];S.w={x:3,y:gy(0,3),vy:0,ground:true,climb:false,cl:null,cx:0,face:1,inv:0,hammer:0,walk:0,jbuf:0,coy:0};S.timeLeft=L.time;S.jumped=0;S.smashed=0;S.cat={x:LEN-3,y:gy(N-1,LEN-3)};
  S.camMin=6;S.camMax=(N-1)*GAP+3;S.camY=Math.min(S.camMax,Math.max(S.camMin,S.w.y+3.5));
}
function hearts(n){var t='';for(var i=0;i<n;i++)t+='♥';return t}
function hud(){var W=S.w||{},m=Math.floor((S.timeLeft||0)/60),s=Math.floor((S.timeLeft||0)%60);setHud('«Nivel|Maila» '+((S.lv||0)+1)+'/3','«Vidas|Bizitzak» '+hearts(S.lives||0),'«Tiempo|Denbora» '+m+':'+(s<10?'0':'')+s,(W.hammer>0?'«Martillo|Mailua» '+W.hammer.toFixed(1)+' s · ':'')+'«Puntos|Puntuak» '+(S.score||0)+' · «Récord|Errekorda» '+Math.max(best,S.score||0))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,lives:3,score:0};logEl.innerHTML='';ev('«Start del juego|Jokoaren Start»');ac('«Variables: vidas = 3, nivel = 1, puntos = 0|Aldagaiak: bizitzak = 3, maila = 1, puntuak = 0»');buildLevel(0);showOv('«BARRIL LOCO|BARRIL ZOROA»','«Pulsa Espacio o toca para empezar|Sakatu Zuriunea edo ukitu hasteko»','«← → moverse · ↑ ↓ escaleras · Espacio saltar · P pausa · M silencio · Récord: |← → mugitu · ↑ ↓ eskailerak · Zuriunea salto egin · P pausa · M mutu · Errekorda: »'+best)}
function loadLevel(n){S.lv=n;S.mode='play';var lv=S.lives,sc=S.score;buildLevel(n);S.lives=lv;S.score=sc;hideOv();flash('«Nivel|Maila» '+(n+1)+': '+(['«Obra pequeña|Obra txikia»','«Obra media|Erdi-mailako obra»','«Rascacielos|Zeru-harraskaria»'][n]),2400);
  ev('Load Scene "«Nivel|Maila»'+(n+1)+'"');ac('Instantiate «Obrero, Gorila, Gatita|Langilea, Gorila, Katutxoa»'+(LV[n].ham?', «Martillo|Mailua»':'')+'; «vidas = |bizitzak = »'+S.lives);beep(440,0.12,'square',0.05,660)}
function retry(){S.lives=3;S.score=0;loadLevel(0)}
function over(k){S.mode='over';saveBest();beep(300,0.6,'sawtooth',0.07,60);showOv(k==='time'?'«¡SE ACABÓ EL TIEMPO!|DENBORA AMAITU DA!»':'«¡SIN VIDAS!|BIZITZARIK GABE!»','«Puntos|Puntuak»: '+S.score+' · «Récord|Errekorda»: '+best,'«Pulsa Espacio para reintentar desde el nivel 1|Sakatu Zuriunea 1. mailatik berriro saiatzeko»')}
function toNext(){ev('On Trigger Enter («Obrero|Langilea» ∩ «Gatita|Katutxoa»)');co('«¿Le quedan vidas? SÍ|Bizitzarik geratzen zaio? BAI»');var bonus=Math.round(S.timeLeft)*10;S.score+=500+bonus;ac('«puntos + 500 + bonus de tiempo (|puntuak + 500 + denbora-bonusa (»'+bonus+')');
  [660,880,1100,1320].forEach(function(f,i){setTimeout(function(){beep(f,0.15,'square',0.05)},i*110)});
  if(S.lv<2){S.mode='next';flash('«¡Gatita rescatada! +|Katutxoa erreskatatu da! +»'+(500+bonus),2000);S.nextAt=S.t+2400;ac('«Mostrar nivel superado, esperar 2 s, Load Scene "Nivel|Maila gainditu dela erakutsi, 2 s itxaron, Load Scene "Maila»'+(S.lv+2)+'"')}
  else{S.mode='won';saveBest();for(var q=0;q<5;q++)setTimeout(function(){burst(5+Math.random()*16,S.cat.y+3+Math.random()*4,['#FDE047','#F472B6','#5EEAD4','#FFFFFF'][Math.floor(Math.random()*4)],10)},q*220);ac('Load Scene "«Victoria|Garaipena»"');showOv('«¡GATITA RESCATADA!|KATUTXOA ERRESKATATU DA!»','«Has superado los 3 niveles · Puntos: |3 mailak gainditu dituzu · Puntuak: »'+S.score+' · «Récord|Errekorda»: '+best,'«Pulsa Espacio para jugar otra vez|Sakatu Zuriunea berriro jokatzeko»')}}
window.addEventListener('keydown',function(e){if(e.key==='m'||e.key==='M'){MUTE=!MUTE;if(S&&S.mode==='play')flash(MUTE?'«Sonido desactivado|Soinua desaktibatuta»':'«Sonido activado|Soinua aktibatuta»',900)}if((e.key==='p'||e.key==='P'||e.key==='Escape')&&S&&(S.mode==='play'||S.paused))togglePause()});
stage.addEventListener('pointerdown',function(){if(S&&S.paused)togglePause()});
function togglePause(){S.paused=!S.paused;if(S.paused)showOv('«PAUSA|ETEN»','«Pulsa P o toca para seguir|Sakatu P edo ukitu jarraitzeko»');else hideOv()}
function onSpace(){if(S.mode!=='play')return;S.w.jbuf=0.15}
function spawn(g){var L=S.L,b={x:g.x+g.dir*2.2,lvl:g.lvl,y:gy(g.lvl,g.x+g.dir*2.2)+R,dir:g.dir,sp:6.5+S.lv*1.4,st:'roll',cl:false,jc:false,dead:false,m:null,red:Math.random()<L.red};S.barrels.push(b);g.throwT=0.45;beep(110,0.12,'triangle',0.08,70);
  ev('Timer: «pasan |pasatzen dira »'+g.iv.toFixed(1)+' «segundos|segundo»');ac('Instantiate «Barril en la mano del gorila + AddForce|Upela gorilaren eskuan + AddForce»')}
function loseLife(b){var W=S.w;S.lives--;b.dead=true;ev('On Trigger Enter («Obrero|Langilea» ∩ «Barril|Upela»)');co('«¿Tiene el martillo? NO|Mailua du? EZ»');ac('«vidas = |bizitzak = »'+S.lives+', Destroy(«Barril|Upela»)');beep(220,0.35,'sawtooth',0.08,70);shk=0.4;burst(W.x,W.y+1.5,'#F97316',10);
  if(S.lives<=0){ac('Load Scene "GameOver"');over('lives');return}
  S.barrels.forEach(function(x){x.dead=true});W.x=3;W.y=gy(0,3);W.vy=0;W.ground=true;W.climb=false;W.inv=1.8;S.gor.forEach(function(g){g.t=g.iv-1.5});flash('«¡Auch! Te quedan |Aucs! Geratzen zaizkizu »'+S.lives+' «vidas|bizitza»',1600)}
function findLadder(W){for(var q=0;q<S.lad.length;q++){var l=S.lad[q];if(Math.abs(W.x-l.cx)<1.3&&W.y>=l.bot-0.3&&W.y<=l.top+0.3)return l}return null}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play'||S.paused)return;
  var W=S.w,L=S.L,i;
  S.timeLeft-=dt;if(S.timeLeft<=0){S.timeLeft=0;ev('Timer: «se acaba el tiempo|denbora amaitzen da»');ac('Load Scene "GameOver"');over('time');return}
  S.gor.forEach(function(g){g.t+=dt;g.throwT=Math.max(0,g.throwT-dt);if(g.t>=g.iv){g.t=0;spawn(g);g.iv=L.iv*(0.7+Math.random()*0.7)}});
  W.inv=Math.max(0,W.inv-dt);W.hammer=Math.max(0,W.hammer-dt);
  var mv=(held.right?1:0)-(held.left?1:0);
  if(W.climb){var d=(held.up?1:0)-(held.down?1:0);W.y+=d*5.5*dt;W.x+=(W.cx-W.x)*Math.min(1,15*dt);
    if(d!==0&&Math.floor(S.t/150)%2===0&&(S.t%150)<17)beep(520+d*60,0.05,'square',0.02);
    if(W.y>=W.cl.top){W.y=W.cl.top;W.climb=false;W.vy=0;W.ground=true}else if(W.y<=W.cl.bot){W.y=W.cl.bot;W.climb=false;W.vy=0;W.ground=true}
    if(W.jbuf>0)W.jbuf=0}
  else{
    var lad=findLadder(W);
    if(lad&&((held.up&&W.y<lad.top-0.15)||(held.down&&Math.abs(W.y-lad.top)<0.45&&W.ground))){W.climb=true;W.cl=lad;W.cx=lad.cx;W.ground=false;W.vy=0;if(held.down)W.y=lad.top-0.05;ev('Input: «↑ dentro del trigger de la escalera|↑ eskailerako trigger-aren barruan»');ac('«Gravedad desactivada, subir/bajar|Grabitatea desaktibatuta, igo/jaitsi»')}
    else{
      if(mv){W.x+=mv*7.2*dt;W.face=mv;W.walk+=dt*12}
      W.x=Math.max(0.6,Math.min(LEN-0.6,W.x));
      W.coy=W.ground?0.1:Math.max(0,W.coy-dt);W.jbuf=Math.max(0,W.jbuf-dt);
      if(W.jbuf>0&&(W.ground||W.coy>0)){W.vy=14.5;W.ground=false;W.coy=0;W.jbuf=0;ev('Input: «Espacio|Zuriunea»');co('«¿Está en el suelo? SÍ|Lurrean dago? BAI»');ac('«AddForce hacia arriba (saltar)|AddForce gorantz (salto egin)»');beep(380,0.18,'square',0.05,760)}
      var py=W.y;W.vy-=38*dt;W.y+=W.vy*dt;W.ground=false;
      for(i=L.N-1;i>=0;i--){var top=gy(i,W.x);if(py>=top-0.4&&W.y<=top&&W.vy<=0){W.y=top;W.vy=0;W.ground=true;break}}
    }
  }
  if(S.ham&&Math.abs(W.x-S.ham.x)<1.5&&Math.abs(W.y-S.ham.y)<1.8){W.hammer=5;S.score+=50;ev('On Trigger Enter («Obrero|Langilea» ∩ «Martillo|Mailua»)');ac('«martillo = 5 s, Destroy(Martillo)|mailua = 5 s, Destroy(Mailua)»');lvGroup.remove(hamM);S.ham=null;hamM=null;beep(700,0.2,'square',0.06,1400);pop('«¡MARTILLO!|MAILUA!»',W.x,W.y+4.5,'#D1D5DB')}
  S.barrels.forEach(function(b){
    if(b.dead)return;
    if(b.st==='roll'){b.x+=b.dir*b.sp*dt;b.y=gy(b.lvl,b.x)+R;
      if(b.lvl>0&&!b.cl&&Math.abs(b.x-(ladX(b.lvl)+1.5))<0.3){b.cl=true;if(b.red||Math.random()<L.pl){b.st='lad';b.x=ladX(b.lvl)+1.5}}
      if((b.dir>0&&b.x>LEN-0.8)||(b.dir<0&&b.x<0.8)){if(b.lvl===0)b.dead=true;else{b.st='fall';b.tgt=b.lvl-1;b.vy=0}}}
    else if(b.st==='fall'){b.vy-=40*dt;b.y+=b.vy*dt;var lt=gy(b.tgt,b.x)+R;if(b.y<=lt){b.y=lt;b.lvl=b.tgt;b.st='roll';b.dir=dirOf(b.lvl);b.cl=false;b.x=Math.max(1,Math.min(LEN-1,b.x))}}
    else{b.y-=4.5*dt;var lt2=gy(b.lvl-1,b.x)+R;if(b.y<=lt2){b.lvl--;b.y=lt2;b.st='roll';b.dir=dirOf(b.lvl);b.cl=false}}
    var dx=Math.abs(b.x-W.x);
    if(dx<1.15&&W.y<b.y+R-0.15&&W.y+2.8>b.y-R+0.25){
      if(W.hammer>0){b.dead=true;S.smashed++;S.score+=300;ev('On Trigger Enter («Obrero|Langilea» ∩ «Barril|Upela»)');co('«¿Martillo activo? SÍ|Mailua aktibo? BAI»');ac('Destroy(«Barril|Upela»), «puntos + 300|puntuak + 300»');beep(200,0.2,'sawtooth',0.07,900);pop('+300',b.x,b.y+2,'#FCA5A5');burst(b.x,b.y,b.red?'#DC2626':'#B45309',9)}
      else if(W.inv<=0&&S.mode==='play')loseLife(b)}
    else if(dx<1.2&&!b.jc&&W.y>=b.y+R-0.15&&!W.ground&&!W.climb){b.jc=true;S.jumped++;S.score+=100;beep(900,0.08,'square',0.04);pop('+100',W.x,W.y+4,'#FDE047');if(S.jumped%3===1){ev('On Trigger Enter («Obrero|Langilea» ∩ «zona sobre el barril|upelaren gaineko zona»)');ac('«puntos + 100 (barriles saltados = |puntuak + 100 (saltatutako upelak = »'+S.jumped+')')}}
  });
  S.barrels=S.barrels.filter(function(b){if(b.dead&&b.m){lvGroup.remove(b.m);b.m=null}return !b.dead});
  if(S.mode==='play'&&Math.abs(W.x-S.cat.x)<1.8&&Math.abs(W.y-S.cat.y)<0.5)toNext();
}
function render(dt){
  var W=S.w,t=S.t/1000;
  wk.g.position.set(W.x,W.y,0.2);wk.g.rotation.y=W.climb?0:W.face*0.6;wk.g.visible=!(W.inv>0&&Math.floor(t*12)%2===0);
  var sw=(!W.climb&&W.ground&&(held.left||held.right))?Math.sin(W.walk)*0.7:0;
  wk.legL.rotation.x=sw;wk.legR.rotation.x=-sw;
  wk.armL.rotation.x=W.climb?-2.4*(Math.sin(t*10)>0?1:0.6):-sw*0.8;wk.armR.rotation.x=W.hammer>0?(-1.2+Math.sin(t*14)*0.8):(W.climb?-2.4*(Math.sin(t*10)>0?0.6:1):sw*0.8);
  if(!W.ground&&!W.climb){wk.armL.rotation.x=-2.6;wk.armR.rotation.x=W.hammer>0?-1.2:-2.6}
  wk.ham.visible=W.hammer>0;
  S.barrels.forEach(function(b){if(!b.m){b.m=mkBarrel(b.red);lvGroup.add(b.m)}b.m.position.set(b.x,b.y,0.3);if(b.st==='roll')b.m.rotation.z-=b.dir*b.sp/R*dt;else if(b.st==='fall')b.m.rotation.z-=b.dir*dt*3});
  S.gor.forEach(function(g){var w=g.t>g.iv-0.7||g.throwT>0;g.m.held.visible=g.t>g.iv-0.7;g.m.armL.rotation.x=w?-2.8:-0.3+Math.sin(t*3)*0.15;g.m.armR.rotation.x=w?-2.8:-0.3-Math.sin(t*3)*0.15;g.m.g.position.y=gy(g.lvl,g.x)+(w?0:Math.abs(Math.sin(t*2.5))*0.18);g.m.g.rotation.y=g.dir>0?0.15:-0.15});
  catG.position.y=gy(S.L.N-1,LEN-3)+Math.abs(Math.sin(t*5))*0.6;catG.rotation.y=Math.sin(t*2)*0.3;
  if(hamM){hamM.rotation.y=t*2.5;hamM.position.y=gy(1,hamM.position.x)+1.6+Math.sin(t*3)*0.25}
  pops=pops.filter(function(p){p.t+=dt;p.m.position.y+=dt*3;p.m.material.opacity=Math.max(0,1-p.t/0.9);if(p.t>0.9){lvGroup.remove(p.m);return false}return true});
  if(S.mode==='play'&&!S.paused){meowT-=dt;if(meowT<=0){meowT=4+Math.random()*3;pop('«¡Miau!|Miau!»',S.cat.x,S.cat.y+5.2,'#FDBA74');beep(900,0.18,'triangle',0.03,600)}}
  parts=parts.filter(function(p){p.t+=dt;p.vy-=22*dt;p.m.position.x+=p.vx*dt;p.m.position.y+=p.vy*dt;p.m.position.z+=p.vz*dt;p.m.rotation.x+=dt*6;if(p.t>0.8){lvGroup.remove(p.m);return false}return true});
  var gt=-9;for(var qi=0;qi<S.L.N;qi++){var tp=gy(qi,W.x);if(tp<=W.y+0.1&&tp>gt)gt=tp}shadow.position.set(W.x,gt+0.06,0.2);shadow.visible=!W.climb&&gt>-9;var sc=Math.max(0.4,1-(W.y-gt)*0.12);shadow.scale.set(sc,1,sc);
  shk=Math.max(0,shk-dt);
  var tgt=Math.min(S.camMax,Math.max(S.camMin,W.y+3.5));S.camY+=(tgt-S.camY)*Math.min(1,4*dt);
  var sx=shk>0?(Math.random()-0.5)*shk*1.6:0,sy=shk>0?(Math.random()-0.5)*shk*1.6:0;cam.position.set(LEN/2+sx,S.camY+4+sy,27);cam.lookAt(LEN/2,S.camY,0);
}
'''
def resolve(s,lang):
    return re.sub(r'«(.*?)\|(.*?)»',lambda m:m.group(1) if lang=='es' else m.group(2),s,flags=re.S)
def make(lang):
    g=resolve(G,lang)
    title='Barril Loco' if lang=='es' else 'Barril Zoroa'
    btn='SALTAR<br>(Espacio)' if lang=='es' else 'SALTO EGIN<br>(Zuriunea)'
    hp=('← → (o A/D): moverse · ↑ ↓: subir o bajar escaleras (colócate sobre ellas) · Espacio: saltar. Sube hasta la gatita esquivando o saltando los barriles. El martillo rompe barriles durante 5 s. Los barriles rojos bajan siempre por las escaleras. P: pausa · M: silencio. Si pierdes las 3 vidas o se acaba el tiempo, pierdes.' if lang=='es' else '← → (edo A/D): mugitu · ↑ ↓: eskailerak igo edo jaitsi (jarri haien gainean) · Zuriunea: salto egin. Igo katutxoraino upelak saihestuz edo gainetik salto eginez. Mailuak upelak apurtzen ditu 5 s-z. Upel gorriek beti jaisten dira eskailerak. P: eten · M: mutu. 3 bizitzak galtzen badituzu edo denbora amaitzen bada, galtzen duzu.')
    out='barril3d_%s.html'%lang
    build(out,title,btn,hp,'#2E1065',g)
    s=open(out,encoding='utf8').read()
    if lang=='eu':
        for a,b in [('<html lang="es">','<html lang="eu">'),('– simulación jugable 3D','– simulazio jokagarria 3D'),
         ('Simulación jugable en 3D del ejemplo de proyecto. A la derecha verás qué EVENTO → CONDICIÓN → ACCIÓN de Visual Scripting se dispara en cada momento.','Proiektu-adibidearen simulazio jokagarria 3D-n. Eskuinean ikusiko duzu une bakoitzean Visual Scripting-eko zein GERTAERA → BALDINTZA → EKINTZA aktibatzen den.'),
         ('aria-label="Arriba"','aria-label="Gora"'),('aria-label="Izquierda"','aria-label="Ezkerrera"'),('aria-label="Abajo"','aria-label="Behera"'),('aria-label="Derecha"','aria-label="Eskuinera"'),
         ('Visual Scripting en vivo','Visual Scripting zuzenean'),('Reiniciar partida','Partida berrabiarazi'),
         ("log('ev','EVENTO',t)","log('ev','GERTAERA',t)"),("log('co','CONDICIÓN',t)","log('co','BALDINTZA',t)"),("log('ac','ACCIÓN',t)","log('ac','EKINTZA',t)"),("'¡Nivel superado!'","'Maila gaindituta!'")]:
            assert a in s,a
            s=s.replace(a,b)
        open(out,'w',encoding='utf8').write(s)
make('es');make('eu')
