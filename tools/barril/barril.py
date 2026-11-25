import re,sys
from common import build,head,A,B
G=r'''
amb.intensity=0.9;sun.intensity=0.8;
var LEN=30,GAP=6,R=0.9;
var LV=[{N:2,iv:4.2,pl:0,ham:false,gor:[[3,1]],time:90},{N:3,iv:3.2,pl:0.3,ham:true,gor:[[3,1]],time:80},{N:4,iv:2.4,pl:0.45,ham:true,gor:[[3,1],[26,-1]],time:70}];
function dirOf(i){return ((S.L.N-1-i)%2===0)?1:-1}
function ladX(i){return ((S.L.N-1-i)%2===0)?22:7}
var wk=null,hamM=null,catG=null,gorM=[];
function mkWorker(){var g=new THREE.Group(),o={g:g};
  function limb(w,h,d,col,x,y){var p=new THREE.Group();p.position.set(x,y,0);bx(w,h,d,col,0,-h/2,0,p);g.add(p);return p}
  o.legL=limb(0.55,1.1,0.55,'#1E3A8A',-0.35,1.1);o.legR=limb(0.55,1.1,0.55,'#1E3A8A',0.35,1.1);
  bx(1.4,1.4,0.8,'#F97316',0,1.8,0,g);bx(1.42,0.3,0.82,'#FDE68A',0,1.9,0,g);
  o.armL=limb(0.4,1.2,0.45,'#FCD9A6',-0.9,2.4);o.armR=limb(0.4,1.2,0.45,'#FCD9A6',0.9,2.4);
  bx(0.95,0.85,0.8,'#FCD9A6',0,2.9,0,g);bx(1.05,0.35,0.9,'#FACC15',0,3.45,0,g);bx(1.3,0.12,1.15,'#FACC15',0,3.25,0.15,g);
  bx(0.14,0.14,0.06,'#111827',-0.22,2.95,0.41,g);bx(0.14,0.14,0.06,'#111827',0.22,2.95,0.41,g);
  var h=new THREE.Group();h.position.set(0,-1.1,0.35);bx(0.2,1.8,0.2,'#92400E',0,0.4,0,h);bx(1.2,0.8,0.5,'#9CA3AF',0,1.4,0,h);bx(1.2,0.2,0.52,'#D1D5DB',0,1.7,0,h);o.armR.add(h);h.visible=false;o.ham=h;
  return o}
function mkGorilla(){var g=new THREE.Group(),o={g:g},B1='#5B3A29',B2='#44281B',F='#B98B5E';
  bx(1.1,1.4,1.1,B2,-0.9,0.7,0,g);bx(1.1,1.4,1.1,B2,0.9,0.7,0,g);
  bx(3.4,2.4,1.8,B1,0,2.5,0,g);bx(2.2,1.7,0.2,F,0,2.4,0.95,g);
  bx(2.0,1.6,1.5,B1,0,4.1,0.05,g);bx(1.3,0.9,0.2,F,0,3.95,0.85,g);bx(0.3,0.3,0.1,'#FFFFFF',-0.5,4.45,0.82,g);bx(0.3,0.3,0.1,'#FFFFFF',0.5,4.45,0.82,g);bx(0.14,0.14,0.1,'#111827',-0.5,4.4,0.88,g);bx(0.14,0.14,0.1,'#111827',0.5,4.4,0.88,g);bx(2.1,0.25,0.3,B2,0,4.75,0.8,g);
  function arm(x){var p=new THREE.Group();p.position.set(x,3.5,0);bx(1.0,2.8,1.0,B1,0,-1.3,0,p);bx(1.1,0.8,1.1,F,0,-2.9,0,p);g.add(p);return p}
  o.armL=arm(-2.2);o.armR=arm(2.2);g.scale.set(1.15,1.15,1.15);return o}
function mkBarrel(){var g=new THREE.Group();bx(1.8,1.8,1.6,'#B45309',0,0,0,g);var b=bx(1.8,1.8,1.6,'#B45309',0,0,0,g);b.rotation.z=Math.PI/4;
  var a=bx(1.9,0.35,1.7,'#78350F',0,0.55,0,g),c=bx(1.9,0.35,1.7,'#78350F',0,-0.55,0,g);bx(0.7,0.7,0.1,'#78350F',0,0,0.85,g);return g}
function mkCat(){var g=new THREE.Group(),c='#FDBA74';bx(1.8,1.2,2.2,c,0,0.8,0,g);bx(1.7,1.7,1.6,c,0,2.0,0.5,g);bx(0.5,0.6,0.5,c,-0.6,3.1,0.5,g);bx(0.5,0.6,0.5,c,0.6,3.1,0.5,g);bx(0.25,0.25,0.1,'#111827',-0.4,2.2,1.32,g);bx(0.25,0.25,0.1,'#111827',0.4,2.2,1.32,g);bx(0.3,0.25,0.1,'#F9A8D4',0,1.8,1.32,g);bx(0.4,0.4,1.4,c,0,1.4,-1.5,g);bx(1.2,0.5,0.1,'#FFFFFF',0,0.6,1.12,g);return g}
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var r=rng(77+n*5),i,N=L.N;
  scene.background.set('#2E1065');scene.fog.color.set('#4C1D95');scene.fog.near=70;scene.fog.far=170;
  bx(140,2,60,'#1E1B4B',LEN/2,-2,-6,lvGroup);
  for(i=0;i<22;i++){var hh=8+r()*34,xx=-30+i*5.6;bx(4.6,hh,3,'#3B1D7A',xx,hh/2-1,-14-r()*6,lvGroup)}
  for(i=0;i<N;i++){var top=i*GAP;
    bx(LEN+2,1,3.6,'#DC2626',LEN/2,top-0.5,0,lvGroup);bx(LEN+2,0.45,0.2,'#991B1B',LEN/2,top-0.45,1.85,lvGroup);
    for(var k=0;k<=LEN;k+=3)bx(0.5,0.5,3.7,'#B91C1C',k,top-0.25,0,lvGroup);
    for(k=1;k<LEN;k+=4)bx(0.35,1.6,0.35,'#7F1D1D',k,top-1.8,1.2,lvGroup)}
  bx(0.9,(N-1)*GAP+2,0.9,'#7F1D1D',-1,((N-1)*GAP+2)/2-1,0,lvGroup);bx(0.9,(N-1)*GAP+2,0.9,'#7F1D1D',LEN+1,((N-1)*GAP+2)/2-1,0,lvGroup);
  for(i=1;i<N;i++){var lx=ladX(i),y0=(i-1)*GAP;bx(0.3,GAP,0.4,'#FBBF24',lx+0.2,y0+GAP/2,0.3,lvGroup);bx(0.3,GAP,0.4,'#FBBF24',lx+2.8,y0+GAP/2,0.3,lvGroup);
    for(k=0.6;k<GAP;k+=1)bx(2.6,0.2,0.3,'#FDE68A',lx+1.5,y0+k,0.3,lvGroup)}
  wk=mkWorker();lvGroup.add(wk.g);
  S.gor=[];gorM=[];L.gor.forEach(function(gg,j){var m=mkGorilla(),lvl=N-1-j;m.g.position.set(gg[0],lvl*GAP,0);lvGroup.add(m.g);gorM.push(m);S.gor.push({x:gg[0],dir:gg[1],lvl:lvl,t:j*1.2,iv:L.iv,throwT:0,m:m})});
  catG=mkCat();catG.position.set(LEN-3,(N-1)*GAP,0);lvGroup.add(catG);
  hamM=null;S.ham=null;if(L.ham){hamM=new THREE.Group();bx(0.25,2.2,0.25,'#92400E',0,0,0,hamM);bx(1.5,1.0,0.7,'#9CA3AF',0,1.2,0,hamM);bx(1.5,0.25,0.72,'#D1D5DB',0,1.55,0,hamM);hamM.position.set(15,GAP+1.6,0);lvGroup.add(hamM);S.ham={x:15,y:GAP}}
  S.barrels=[];S.w={x:3,y:0,vy:0,ground:true,climb:false,cl:null,cx:0,face:1,inv:0,hammer:0,walk:0};S.timeLeft=L.time;S.jumped=0;S.smashed=0;S.cat={x:LEN-3,y:(N-1)*GAP};
  var d=Math.max((LEN/2+3)/(0.3839*1.524),((N-1)*GAP+8)/2/0.3839)+4,cy=((N-1)*GAP+6)/2-0.5;S.camD=d;S.camY=cy;
}
function hud(){var W=S.w||{},m=Math.floor((S.timeLeft||0)/60),s=Math.floor((S.timeLeft||0)%60);setHud('«Nivel|Maila» '+((S.lv||0)+1)+'/3','«Vidas|Bizitzak» '+(S.lives||0),'«Tiempo|Denbora» '+m+':'+(s<10?'0':'')+s,W.hammer>0?'«Martillo|Mailua» '+W.hammer.toFixed(1)+' s':'«Barriles saltados|Saltatutako upelak» '+(S.jumped||0))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,lives:3};logEl.innerHTML='';ev('«Start del juego|Jokoaren Start»');ac('«Variables: vidas = 3, nivel = 1|Aldagaiak: bizitzak = 3, maila = 1»');buildLevel(0);showOv('«BARRIL LOCO|BARRIL ZOROA»','«Pulsa Espacio o toca para empezar|Sakatu Zuriunea edo ukitu hasteko»','«← → moverse · ↑ ↓ escaleras · Espacio saltar|← → mugitu · ↑ ↓ eskailerak · Zuriunea salto egin»')}
function loadLevel(n){S.lv=n;S.mode='play';var lv=S.lives;buildLevel(n);S.lives=lv;hideOv();flash('«Nivel|Maila» '+(n+1)+': '+(['«Obra pequeña|Obra txikia»','«Obra media|Erdi-mailako obra»','«Rascacielos|Zeru-harraskaria»'][n]),2400);
  ev('Load Scene "«Nivel|Maila»'+(n+1)+'"');ac('Instantiate «Obrero, Gorila, Gatita|Langilea, Gorila, Katutxoa»'+(LV[n].ham?', «Martillo|Mailua»':'')+'; «vidas = |bizitzak = »'+S.lives)}
function retry(){S.lives=3;loadLevel(0)}
function over(k){S.mode='over';showOv(k==='time'?'«¡SE ACABÓ EL TIEMPO!|DENBORA AMAITU DA!»':'«¡SIN VIDAS!|BIZITZARIK GABE!»',k==='time'?'«El tiempo llegó a 0|Denbora 0ra iritsi da»':'«Los barriles te han ganado|Upelek irabazi dizute»','«Pulsa Espacio para reintentar desde el nivel 1|Sakatu Zuriunea 1. mailatik berriro saiatzeko»')}
function toNext(){ev('On Trigger Enter («Obrero|Langilea» ∩ «Gatita|Katutxoa»)');co('«¿Le quedan vidas? SÍ|Bizitzarik geratzen zaio? BAI»');
  if(S.lv<2){S.mode='next';flash('«¡Gatita rescatada!|Katutxoa erreskatatu da!»',2000);S.nextAt=S.t+2300;ac('«Mostrar nivel superado, esperar 2 s, Load Scene "Nivel|Maila gainditu dela erakutsi, 2 s itxaron, Load Scene "Maila»'+(S.lv+2)+'"')}
  else{S.mode='won';ac('Load Scene "«Victoria|Garaipena»"');showOv('«¡GATITA RESCATADA!|KATUTXOA ERREDESKATATU DA!»'.replace('ERREDESKATATU','ERRESKATATU'),'«Has superado los 3 niveles con |3 mailak gainditu dituzu »'+S.lives+' «vidas|bizitzarekin»','«Pulsa Espacio para jugar otra vez|Sakatu Zuriunea berriro jokatzeko»')}}
function onSpace(){var W=S.w;if(S.mode!=='play')return;if(W.ground&&!W.climb){W.vy=14;W.ground=false;ev('Input: «Espacio|Zuriunea»');co('«¿Está en el suelo? SÍ|Lurrean dago? BAI»');ac('«AddForce hacia arriba (saltar)|AddForce gorantz (salto egin)»')}}
function spawn(g){var L=S.L,b={x:g.x+g.dir*2,lvl:g.lvl,y:g.lvl*GAP+R,dir:g.dir,sp:6.5+S.lv*0.9,st:'roll',cl:false,jc:false,dead:false,m:null};S.barrels.push(b);g.throwT=0.5;
  ev('Timer: «pasan |pasatzen dira »'+g.iv.toFixed(1)+' «segundos|segundo»');ac('Instantiate «Barril en la mano del gorila + AddForce|Upela gorilaren eskuan + AddForce»')}
function loseLife(b){var W=S.w;S.lives--;b.dead=true;ev('On Trigger Enter («Obrero|Langilea» ∩ «Barril|Upela»)');co('«¿Tiene el martillo? NO|Mailua du? EZ»');ac('«vidas = |bizitzak = »'+S.lives+', Destroy(«Barril|Upela»)');
  if(S.lives<=0){ac('Load Scene "GameOver"');over('lives');return}
  S.barrels.forEach(function(x){x.dead=true});W.x=3;W.y=0;W.vy=0;W.ground=true;W.climb=false;W.inv=1.8;S.gor.forEach(function(g){g.t=0});flash('«¡Auch! Te quedan |Aucs! Geratzen zaizkizu »'+S.lives+' «vidas|bizitza»',1600)}
function findLadder(W){for(var i=1;i<S.L.N;i++){var cx=ladX(i)+1.5;if(Math.abs(W.x-cx)<1.4&&W.y>=(i-1)*GAP-0.05&&W.y<=i*GAP+0.05)return{i:i,cx:cx,bot:(i-1)*GAP,top:i*GAP}}return null}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var W=S.w,L=S.L,i;
  S.timeLeft-=dt;if(S.timeLeft<=0){S.timeLeft=0;ev('Timer: «se acaba el tiempo|denbora amaitzen da»');ac('Load Scene "GameOver"');over('time');return}
  S.gor.forEach(function(g){g.t+=dt;g.throwT=Math.max(0,g.throwT-dt);if(g.t>=g.iv){g.t=0;spawn(g)}});
  W.inv=Math.max(0,W.inv-dt);W.hammer=Math.max(0,W.hammer-dt);
  var mv=(held.right?1:0)-(held.left?1:0);
  if(W.climb){var d=(held.up?1:0)-(held.down?1:0);W.y+=d*5*dt;W.x+=(W.cx-W.x)*Math.min(1,15*dt);
    if(W.y>=W.cl.top){W.y=W.cl.top;W.climb=false;W.vy=0;W.ground=true}else if(W.y<=W.cl.bot){W.y=W.cl.bot;W.climb=false;W.vy=0;W.ground=true}}
  else{
    var lad=findLadder(W);
    if(lad&&W.ground&&((held.up&&W.y<lad.top-0.1)||(held.down&&W.y>lad.top-0.1))){W.climb=true;W.cl=lad;W.cx=lad.cx;W.ground=false;W.vy=0;ev('Input: «↑ dentro del trigger de la escalera|↑ eskailerako trigger-aren barruan»');ac('«Gravedad desactivada, subir/bajar|Grabitatea desaktibatuta, igo/jaitsi»')}
    else{
      if(mv){W.x+=mv*7*dt;W.face=mv;W.walk+=dt*12}
      W.x=Math.max(0.6,Math.min(LEN-0.6,W.x));
      var py=W.y;W.vy-=38*dt;W.y+=W.vy*dt;W.ground=false;
      for(i=L.N-1;i>=0;i--){var top=i*GAP;if(py>=top-0.02&&W.y<=top&&W.vy<=0){W.y=top;W.vy=0;W.ground=true;break}}
    }
  }
  if(S.ham&&Math.abs(W.x-S.ham.x)<1.4&&Math.abs(W.y-S.ham.y)<1.6){W.hammer=5;ev('On Trigger Enter («Obrero|Langilea» ∩ «Martillo|Mailua»)');ac('«martillo = 5 s, Destroy(Martillo)|mailua = 5 s, Destroy(Mailua)»');lvGroup.remove(hamM);S.ham=null;hamM=null}
  S.barrels.forEach(function(b){
    if(b.dead)return;
    if(b.st==='roll'){b.x+=b.dir*b.sp*dt;b.y=b.lvl*GAP+R;
      if(b.lvl>0&&!b.cl&&Math.abs(b.x-(ladX(b.lvl)+1.5))<0.3){b.cl=true;if(Math.random()<L.pl){b.st='lad';b.x=ladX(b.lvl)+1.5}}
      if((b.dir>0&&b.x>LEN-0.8)||(b.dir<0&&b.x<0.8)){if(b.lvl===0)b.dead=true;else{b.st='fall';b.tgt=b.lvl-1;b.vy=0}}}
    else if(b.st==='fall'){b.vy-=40*dt;b.y+=b.vy*dt;if(b.y<=b.tgt*GAP+R){b.y=b.tgt*GAP+R;b.lvl=b.tgt;b.st='roll';b.dir=dirOf(b.lvl);b.cl=false;b.x=Math.max(1,Math.min(LEN-1,b.x))}}
    else{b.y-=4*dt;if(b.y<=(b.lvl-1)*GAP+R){b.lvl--;b.y=b.lvl*GAP+R;b.st='roll';b.dir=dirOf(b.lvl);b.cl=false}}
    var dx=Math.abs(b.x-W.x);
    if(dx<1.25&&W.y<b.y+R-0.15&&W.y+2.8>b.y-R+0.2){
      if(W.hammer>0){b.dead=true;S.smashed++;ev('On Trigger Enter («Obrero|Langilea» ∩ «Barril|Upela»)');co('«¿Martillo activo? SÍ|Mailua aktibo? BAI»');ac('Destroy(«Barril|Upela»), «puntos + 100|puntuak + 100»')}
      else if(W.inv<=0&&S.mode==='play')loseLife(b)}
    else if(dx<1.1&&!b.jc&&W.y>=b.y+R-0.15&&!W.ground&&!W.climb){b.jc=true;S.jumped++;if(S.jumped%3===1){ev('On Trigger Enter («Obrero|Langilea» ∩ «zona sobre el barril|upelaren gaineko zona»)');ac('«Barriles saltados = |Saltatutako upelak = »'+S.jumped)}}
  });
  S.barrels=S.barrels.filter(function(b){if(b.dead&&b.m){lvGroup.remove(b.m);b.m=null}return !b.dead});
  if(S.mode==='play'&&Math.abs(W.x-S.cat.x)<1.8&&Math.abs(W.y-S.cat.y)<0.3)toNext();
}
function render(dt){
  var W=S.w,t=S.t/1000;
  wk.g.position.set(W.x,W.y,0.2);wk.g.rotation.y=W.climb?0:W.face*0.6;wk.g.visible=!(W.inv>0&&Math.floor(t*12)%2===0);
  var sw=(!W.climb&&W.ground&&(held.left||held.right))?Math.sin(W.walk)*0.7:0;
  wk.legL.rotation.x=sw;wk.legR.rotation.x=-sw;
  wk.armL.rotation.x=W.climb?-2.4*(Math.sin(t*10)>0?1:0.6):-sw*0.8;wk.armR.rotation.x=W.hammer>0?(-1.2+Math.sin(t*14)*0.8):(W.climb?-2.4*(Math.sin(t*10)>0?0.6:1):sw*0.8);
  if(!W.ground&&!W.climb){wk.armL.rotation.x=-2.6;wk.armR.rotation.x=W.hammer>0?-1.2:-2.6}
  wk.ham.visible=W.hammer>0;
  S.barrels.forEach(function(b){if(!b.m){b.m=mkBarrel();lvGroup.add(b.m)}b.m.position.set(b.x,b.y,0.3);if(b.st==='roll')b.m.rotation.z-=b.dir*b.sp/R*dt;else if(b.st==='fall')b.m.rotation.z-=b.dir*dt*3});
  S.gor.forEach(function(g){var w=g.t>g.iv-0.7||g.throwT>0;g.m.armL.rotation.x=w?-2.6:-0.3+Math.sin(t*3)*0.15;g.m.armR.rotation.x=w?-2.6:-0.3-Math.sin(t*3)*0.15;g.m.g.position.y=g.lvl*GAP+(w?0:Math.abs(Math.sin(t*2.5))*0.18);g.m.g.rotation.y=g.dir>0?0.15:-0.15});
  catG.position.y=(S.L.N-1)*GAP+Math.abs(Math.sin(t*5))*0.6;catG.rotation.y=Math.sin(t*2)*0.3;
  if(hamM){hamM.rotation.y=t*2.5;hamM.position.y=GAP+1.6+Math.sin(t*3)*0.25}
  cam.position.set(LEN/2,S.camY+3,S.camD);cam.lookAt(LEN/2,S.camY+0.5,0);
}
'''
def resolve(s,lang):
    return re.sub(r'«(.*?)\|(.*?)»',lambda m:m.group(1) if lang=='es' else m.group(2),s,flags=re.S)
def make(lang):
    g=resolve(G,lang)
    title='Barril Loco' if lang=='es' else 'Barril Zoroa'
    btn='SALTAR<br>(Espacio)' if lang=='es' else 'SALTO EGIN<br>(Zuriunea)'
    hp=('← → (o A/D): moverse · ↑ ↓: subir o bajar escaleras (colócate sobre ellas) · Espacio: saltar. Sube hasta la gatita esquivando o saltando los barriles. El martillo rompe barriles durante 5 s. Si pierdes las 3 vidas o se acaba el tiempo, pierdes.' if lang=='es' else '← → (edo A/D): mugitu · ↑ ↓: eskailerak igo edo jaitsi (jarri haien gainean) · Zuriunea: salto egin. Igo katutxoraino upelak saihestuz edo gainetik salto eginez. Mailuak upelak apurtzen ditu 5 s-z. 3 bizitzak galtzen badituzu edo denbora amaitzen bada, galtzen duzu.')
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
