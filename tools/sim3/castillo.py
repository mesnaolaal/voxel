from common import build
G=r'''
amb.intensity=0.85;sun.intensity=0.7;
var TITLE='DEFENSA DEL CASTILLO';
var COST=50,UPG=40,REP=30;
var LV=[
 {name:'Camino recto con tres goblins',hp:3,coins:150,path:[[-26,0],[26,0]],slots:[[-8,-4.5],[9,4.5]],
  waves:[[0,1.5],[1,1.5],[2,1.5]].map(function(a){return {t:a[0]*2.2,k:'g'}})},
 {name:'Más goblins y tres torres',hp:4,coins:150,path:[[-26,-8],[-10,-8],[-10,6],[8,6],[8,-8],[26,-8]],slots:[[-18,-3.5],[-1,-1],[17,-3.5]],
  waves:(function(){var w=[];for(var i=0;i<10;i++)w.push({t:i*1.2,k:'g'});return w})()},
 {name:'Un ogro jefe acompañado de goblins',hp:5,coins:150,path:[[-28,-10],[-10,-10],[-10,0],[12,0],[12,10],[26,10]],slots:[[-19,-5],[-1,-5],[1,5],[19,5]],
  waves:(function(){var w=[];for(var i=0;i<7;i++)w.push({t:i*1.3,k:'g'});w.push({t:7*1.3+1,k:'o'});for(i=0;i<4;i++)w.push({t:7*1.3+3+i*1.2,k:'g'});return w})()}];
var PREP=6;
function lenOf(path){var s=0,i,seg=[];for(i=1;i<path.length;i++){var d=Math.hypot(path[i][0]-path[i-1][0],path[i][1]-path[i-1][1]);seg.push(d);s+=d}return {total:s,seg:seg}}
function posAt(path,info,d){var i=0;while(i<info.seg.length-1&&d>info.seg[i]){d-=info.seg[i];i++}var a=path[i],b=path[i+1],t=Math.min(1,d/info.seg[i]);return [a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t,Math.atan2(b[0]-a[0],b[1]-a[1])]}
function makeGoblin(){var g=new THREE.Group();bx(0.9,0.9,0.7,'#16A34A',0,0.9,0,g);bx(0.8,0.7,0.7,'#22C55E',0,1.6,0.1,g);bx(0.5,0.25,0.2,'#22C55E',-0.6,1.7,0.1,g);bx(0.5,0.25,0.2,'#22C55E',0.6,1.7,0.1,g);bx(0.15,0.15,0.1,basic('#FDE047'),-0.2,1.7,0.5,g);bx(0.15,0.15,0.1,basic('#FDE047'),0.2,1.7,0.5,g);bx(0.3,0.7,0.3,'#15803D',-0.25,0.35,0,g);bx(0.3,0.7,0.3,'#15803D',0.25,0.35,0,g);bx(0.15,1.2,0.15,'#92400E',0.7,1.0,0.3,g);return g}
function makeOgre(){var g=new THREE.Group();bx(2.4,2.2,1.8,'#65A30D',0,2.2,0,g);bx(1.6,1.4,1.4,'#84CC16',0,3.8,0.2,g);bx(0.4,0.7,0.4,'#F8FAFC',-0.6,4.8,0.4,g);bx(0.4,0.7,0.4,'#F8FAFC',0.6,4.8,0.4,g);bx(0.3,0.3,0.1,basic('#EF4444'),-0.4,4.0,0.95,g);bx(0.3,0.3,0.1,basic('#EF4444'),0.4,4.0,0.95,g);
  bx(0.9,1.8,0.9,'#4D7C0F',-1.6,2.0,0,g);bx(0.9,1.8,0.9,'#4D7C0F',1.6,2.0,0,g);bx(0.9,1.2,0.9,'#3F6212',-0.6,0.6,0,g);bx(0.9,1.2,0.9,'#3F6212',0.6,0.6,0,g);bx(0.5,2.6,0.5,'#92400E',1.9,2.4,0.6,g);bx(1.0,0.9,1.0,'#78716C',1.9,3.9,0.6,g);return g}
function makeTower(){var g=new THREE.Group();bx(2.4,1.4,2.4,'#94A3B8',0,0.7,0,g);bx(2.0,1.6,2.0,'#CBD5E1',0,2.2,0,g);bx(2.6,0.4,2.6,'#64748B',0,3.2,0,g);[-1,1].forEach(function(a){[-1,1].forEach(function(b){bx(0.5,0.6,0.5,'#64748B',a*1.0,3.6,b*1.0,g)})});
  bx(0.6,0.9,0.6,'#92400E',0,3.7,0,g);bx(0.5,0.5,0.5,'#FCD9A6',0,4.4,0,g);bx(0.6,0.3,0.6,'#DC2626',0,4.8,0,g);var fl=bx(0.1,1.6,0.1,'#FACC15',1.0,4.6,1.0,g);bx(0.7,0.5,0.08,'#FACC15',1.35,5.1,1.0,g);g.userData.up=[fl];return g}
function makeCastle(){var g=new THREE.Group();bx(5,3.6,5,'#CBD5E1',0,1.8,0,g);bx(5.6,0.5,5.6,'#94A3B8',0,3.8,0,g);[[-2.5,-2.5],[2.5,-2.5],[-2.5,2.5],[2.5,2.5]].forEach(function(o){bx(1.6,5,1.6,'#E2E8F0',o[0],2.5,o[1],g);bx(2.0,0.5,2.0,'#94A3B8',o[0],5.2,o[1],g);bx(1.5,1.4,1.5,'#DC2626',o[0],6.0,o[1],g)});
  bx(1.8,2.6,0.3,'#78350F',0,1.3,2.6,g);bx(0.15,3.5,0.15,'#F8FAFC',0,6.2,0,g);bx(1.4,0.9,0.1,'#EF4444',0.75,7.5,0,g);return g}
var grassT=checker('#6BCB4F','#62BE48',1,1),pathT=checker('#D6B77A','#CCAC6C',1,1),ray=new THREE.Raycaster();
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var r=rng(111+n*3),i;
  scene.background.set('#BFE6FF');scene.fog.color.set('#D4EEFF');scene.fog.near=110;scene.fog.far=220;
  var gm=new THREE.Mesh(new THREE.BoxGeometry(80,0.6,40),new THREE.MeshLambertMaterial({map:grassT}));grassT.repeat.set(40,20);gm.position.set(0,-0.3,0);lvGroup.add(gm);
  var out=new THREE.Mesh(new THREE.PlaneGeometry(240,240),new THREE.MeshLambertMaterial({color:'#4FA43A'}));out.rotation.x=-Math.PI/2;out.position.set(0,-0.62,0);lvGroup.add(out);
  S.info=lenOf(L.path);
  // camino
  for(i=1;i<L.path.length;i++){var a=L.path[i-1],b=L.path[i],ln=Math.hypot(b[0]-a[0],b[1]-a[1]),m=bx(ln+3.4,0.25,3.4,'#D6B77A',(a[0]+b[0])/2,0.05,(a[1]+b[1])/2,lvGroup);m.rotation.y=Math.atan2(b[1]-a[1],b[0]-a[0])*-1;bx(0.8,0.06,0.8,'#B8955A',a[0],0.2,a[1],lvGroup)}
  var end=L.path[L.path.length-1],cs=makeCastle();cs.position.set(end[0]+3,0,end[1]);lvGroup.add(cs);S.castle=cs;S.cpos={x:end[0]+3,z:end[1]};
  var st=L.path[0];bx(1.2,3,1.2,'#7F1D1D',st[0]-2,1.5,st[1]-2,lvGroup);bx(1.2,3,1.2,'#7F1D1D',st[0]-2,1.5,st[1]+2,lvGroup);bx(0.4,1.2,4.4,'#991B1B',st[0]-2,3.2,st[1],lvGroup);
  // árboles decorativos
  for(i=0;i<26;i++){var tx=(r()-0.5)*76,tz=(r()<0.5?-1:1)*(15+r()*4);bx(0.7,2.2,0.7,'#78350F',tx,1.1,tz,lvGroup);bx(2.6,2.2,2.6,'#16A34A',tx,3.0,tz,lvGroup)}
  // huecos
  S.slots=[];S.slotMeshes=[];L.slots.forEach(function(s,k){var d=new THREE.Group(),pl=bx(3.2,0.3,3.2,'#475569',0,0.2,0,d);bx(2.7,0.12,2.7,'#94A3B8',0,0.4,0,d);bx(1.2,0.1,0.35,'#FACC15',0,0.5,0,d);bx(0.35,0.1,1.2,'#FACC15',0,0.5,0,d);d.position.set(s[0],0,s[1]);lvGroup.add(d);pl.userData.slot=k;S.slotMeshes.push(pl);S.slots.push({x:s[0],z:s[1],tw:null,lv:0,cd:0,grp:d,ring:null})});
  S.en=[];S.bolts=[];S.coins=L.coins;S.chp=L.hp;S.sel=0;S.next=0;S.clock=-PREP;S.killed=0;S.spawned=0;S.prevL=false;S.prevR=false;S.flashC=0;
}
function build(i){var s=S.slots[i];if(s.tw||S.coins<COST){return false}S.coins-=COST;s.tw=makeTower();s.tw.position.set(s.x,0.5,s.z);lvGroup.add(s.tw);s.lv=1;s.cd=0;ev('Clic en un hueco');co('¿Hay monedas suficientes? SÍ');ac('Instantiate Torre, monedas = '+S.coins);return true}
function upgrade(i){var s=S.slots[i];if(!s.tw||s.lv>=2||S.coins<UPG)return false;S.coins-=UPG;s.lv=2;s.tw.scale.setScalar(1.15);ev('Clic en una torre');co('¿Hay monedas suficientes? SÍ');ac('Mejorar torre: daño × 2, monedas = '+S.coins);return true}
function hud(){var h='';for(var i=0;i<(S.L?S.L.hp:3);i++)h+=i<(S.chp||0)?'♥':'♡';var left=S.L?S.L.waves.length-(S.killed||0):0;
  setHud('Nivel '+(S.lv+1)+'/3 · Castillo '+h,'Monedas '+(S.coins||0),S.clock<0?'Oleada en '+Math.ceil(-S.clock)+' s':'Enemigos '+left,S.slots&&S.slots[S.sel]?(S.slots[S.sel].tw?(S.slots[S.sel].lv<2?'Mejorar ('+UPG+')':'Torre al máximo'):'Construir ('+COST+')'):'')}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: monedas = 150, vidas del castillo = 3');buildLevel(0);showOv('DEFENSA DEL CASTILLO','Pulsa Espacio o toca para empezar','Clic en un hueco: construir una torre · ← → elegir hueco · Espacio: construir / mejorar · R: reparar')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Castillo ('+S.L.hp+' vidas), '+S.slots.length+' huecos para torre y camino; oleada en '+PREP+' s')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡CASTILLO SALVADO!','Has resistido las 3 oleadas','Pulsa Espacio para repetir')}}
function over(){S.mode='over';showOv('¡CASTILLO DESTRUIDO!','Los enemigos llegaron hasta el castillo','Pulsa Espacio para reintentar este nivel')}
function onSpace(){if(S.mode!=='play')return;var s=S.slots[S.sel];if(!s)return;if(!s.tw){if(!build(S.sel))flash('Faltan monedas (cuesta '+COST+')',1000)}else if(s.lv<2){if(!upgrade(S.sel))flash('Faltan monedas (cuesta '+UPG+')',1000)}else flash('La torre ya está al máximo',900)}
function repair(){if(S.mode!=='play')return;if(S.coins>=REP&&S.chp<S.L.hp){S.coins-=REP;S.chp++;ev('Tecla R');ac('Reparar castillo: vidas = '+S.chp+', monedas = '+S.coins);flash('Castillo reparado',900)}else flash('No se puede reparar',900)}
if(typeof window!=='undefined')window.addEventListener('keydown',function(e){if((e.key==='r'||e.key==='R')&&S&&S.mode==='play')repair()});
if(renderer.domElement&&typeof renderer.domElement.addEventListener==='function')renderer.domElement.addEventListener('pointerdown',function(e){
  if(!S||S.mode!=='play'||!S.slotMeshes)return;var rc=renderer.domElement.getBoundingClientRect(),nx=((e.clientX-rc.left)/rc.width)*2-1,ny=-((e.clientY-rc.top)/rc.height)*2+1;
  ray.setFromCamera({x:nx,y:ny},cam);var hits=ray.intersectObjects(S.slotMeshes.concat(S.slots.filter(function(s){return s.tw}).map(function(s){return s.tw.children[0]})),false);
  if(hits.length){var o=hits[0].object,k=o.userData.slot;if(k===undefined){S.slots.forEach(function(s,i){if(s.tw&&s.tw.children[0]===o)k=i})}if(k!==undefined){S.sel=k;onSpace()}}});
function spawn(k){var m=k==='o'?makeOgre():makeGoblin(),p=S.L.path[0];m.position.set(p[0],0,p[1]);lvGroup.add(m);
  var bar=bx(2,0.3,0.3,basic('#22C55E'),0,0,0,lvGroup);var e={k:k,d:0,hp:k==='o'?30:3,max:k==='o'?30:3,spd:k==='o'?1.6:3.3,mesh:m,bar:bar,x:p[0],z:p[1],dead:false,ph:Math.random()*6};S.en.push(e);S.spawned++;ev('Pasa el tiempo (siguiente '+(k==='o'?'ogro':'goblin')+')');ac('Instantiate '+(k==='o'?'Ogro':'Goblin')+' al inicio del camino')}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  if(held.left&&!S.prevL){S.sel=(S.sel+S.slots.length-1)%S.slots.length}if(held.right&&!S.prevR){S.sel=(S.sel+1)%S.slots.length}S.prevL=held.left;S.prevR=held.right;
  S.clock+=dt;
  while(S.next<S.L.waves.length&&S.clock>=S.L.waves[S.next].t){spawn(S.L.waves[S.next].k);S.next++}
  S.flashC=Math.max(0,S.flashC-dt);
  S.en.forEach(function(e){if(e.dead)return;e.d+=e.spd*dt;if(e.d>=S.info.total){e.dead=true;e.mesh.visible=false;e.bar.visible=false;var dm=e.k==='o'?3:1;S.chp-=dm;S.killed++;S.flashC=0.5;ev('On Trigger Enter ('+(e.k==='o'?'Ogro':'Goblin')+' ∩ Castillo)');ac('vidas del castillo = vidas − '+dm+' → '+Math.max(0,S.chp));if(S.chp<=0){ac('Load Scene "GameOver"');over()}return}
    var p=posAt(S.L.path,S.info,e.d);e.x=p[0];e.z=p[1];e.ry=p[2]});
  if(S.mode!=='play')return;
  S.slots.forEach(function(s,i){if(!s.tw)return;s.cd-=dt;if(s.cd>0)return;var rng_=10,best=null,bd=1e9;S.en.forEach(function(e){if(e.dead)return;var d=Math.hypot(e.x-s.x,e.z-s.z);if(d<rng_&&e.d>(best?best.d:-1)){best=e;bd=d}});
    if(best){s.cd=s.lv>1?0.5:0.75;S.bolts.push({x:s.x,y:4.4,z:s.z,t:best,dmg:s.lv>1?2:1,mesh:bx(0.35,0.35,0.9,'#FDE047',s.x,4.4,s.z,lvGroup)});if(!s.said){s.said=true;ev('On Trigger Enter ('+(best.k==='o'?'Ogro':'Goblin')+' ∩ Alcance de la torre)');ac('Disparar flecha a la torre más cercana')}}});
  for(var i=S.bolts.length-1;i>=0;i--){var b=S.bolts[i],t=b.t;if(t.dead){lvGroup.remove(b.mesh);S.bolts.splice(i,1);continue}var dx=t.x-b.x,dy=1.5-b.y,dz=t.z-b.z,d=Math.hypot(dx,dy,dz),st=30*dt;
    if(d<=st+0.3){t.hp-=b.dmg;lvGroup.remove(b.mesh);S.bolts.splice(i,1);if(t.hp<=0&&!t.dead){t.dead=true;t.mesh.visible=false;t.bar.visible=false;S.killed++;var gain=t.k==='o'?60:15;S.coins+=gain;ev('Vida del enemigo = 0');ac('Destroy('+(t.k==='o'?'Ogro':'Goblin')+'), monedas + '+gain+' = '+S.coins)}}
    else{b.x+=dx/d*st;b.y+=dy/d*st;b.z+=dz/d*st;b.mesh.position.set(b.x,b.y,b.z);b.mesh.rotation.y=Math.atan2(dx,dz)}}
  if(S.mode==='play'&&S.next>=S.L.waves.length&&S.en.every(function(e){return e.dead})){ev('Termina la última oleada');co('¿Castillo con vidas? SÍ ('+S.chp+')');ac('Cargar el siguiente nivel');toNext()}
}
function render(dt){
  var t=S.t/1000;
  S.en.forEach(function(e){if(e.dead)return;e.mesh.position.set(e.x,Math.abs(Math.sin(t*(e.k==='o'?4:9)+e.ph))*0.15,e.z);e.mesh.rotation.y=e.ry||0;var f=Math.max(0.01,e.hp/e.max);e.bar.scale.x=f;e.bar.position.set(e.x,e.k==='o'?6.2:2.6,e.z);e.bar.material=basic(f>0.5?'#22C55E':(f>0.25?'#FACC15':'#EF4444'))});
  S.slots.forEach(function(s,i){s.grp.children[0].material=i===S.sel?basic('#FACC15'):mat('#475569');if(s.tw&&s.lv>1)s.tw.userData.up[0].visible=true;else if(s.tw)s.tw.userData.up[0].visible=false});
  S.castle.position.x=S.cpos.x+(S.flashC>0?Math.sin(t*60)*0.25:0);
  cam.position.set(0,52,34);cam.lookAt(0,0,0.5);
}
'''
build('castillo3d.html','Defensa del Castillo','CONSTRUIR<br>(Espacio)','Clic o toque en un hueco gris: construir una torre (50). Clic en una torre: mejorarla (40). Con el teclado: ← → elegir hueco, Espacio construir o mejorar, R reparar el castillo (30). Cada enemigo derrotado da monedas. Si te llegan al castillo pierde vidas.','#BFE6FF',G)
