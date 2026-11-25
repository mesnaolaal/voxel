from common import build
G=r'''
amb.intensity=0.75;sun.intensity=0.55;
var TITLE='GATO NINJA';
var LV=[
 {name:'Un tejado, un robot y una llave',rows:[
  '...........',
  '.G.........',
  '...C....R..',
  '...........',
  '.....L.....',
  '...........',
  '.........S.']},
 {name:'Dos tejados con un hueco en medio y dos robots',rows:[
  '.......~.......',
  '.G.....~....L..',
  '..C....~..R....',
  '.......~.......',
  '..R....~...C...',
  '.......~......S',
  '.......~.......']},
 {name:'Tres robots y dos llaves',rows:[
  '.......~.......',
  '.G.....~...L...',
  '..R....~.......',
  '.......~...C...',
  '.L.....~.R.....',
  '.......~.......',
  '..C....~....V..',
  '.......~......S',
  '.......~.......']}];
function ch(x,z){return cellCh(Math.round(x/C),Math.round(z/C))}
function solidAt(x,z){var c=ch(x,z);return c===undefined||c==='C'}
function canMove(x,z,r){return !solidAt(x-r,z-r)&&!solidAt(x+r,z-r)&&!solidAt(x-r,z+r)&&!solidAt(x+r,z+r)}
function walk(cx,cz){var c=cellCh(cx,cz);return c!==undefined&&c!=='~'&&c!=='C'}
var cat=new THREE.Group(),tailG;
(function(){var g=cat,k='#1F2937';
  bx(0.9,0.8,1.5,k,0,0.8,0,g);bx(0.8,0.7,0.8,k,0,1.2,0.9,g);bx(0.25,0.3,0.2,k,-0.28,1.7,0.9,g);bx(0.25,0.3,0.2,k,0.28,1.7,0.9,g);
  bx(0.9,0.2,0.85,'#DC2626',0,1.2,0.92,g);bx(0.2,0.1,0.06,'#FACC15',0.2,1.3,1.33,g);bx(0.2,0.1,0.06,'#FACC15',-0.2,1.3,1.33,g);bx(0.2,0.14,0.08,'#F9A8D4',0,1.1,1.33,g);
  [[-0.3,0.55],[0.3,0.55],[-0.3,-0.5],[0.3,-0.5]].forEach(function(p){bx(0.22,0.6,0.22,k,p[0],0.3,p[1],g)});
  tailG=new THREE.Group();tailG.position.set(0,1.0,-0.8);bx(0.2,0.2,1.2,k,0,0.2,-0.5,tailG);bx(0.2,0.5,0.2,k,0,0.5,-1.1,tailG);bx(0.2,0.15,0.3,'#DC2626',0,0.05,-0.3,tailG);g.add(tailG)})();
function makeRobot(){var g=new THREE.Group();bx(1.4,1.5,1.2,'#94A3B8',0,1.3,0,g);bx(1.0,0.8,0.9,'#CBD5E1',0,2.3,0,g);bx(0.9,0.3,0.1,basic('#EF4444'),0,2.35,0.5,g);bx(0.12,0.5,0.12,'#475569',0,2.95,0,g);bx(0.3,0.3,0.3,'#EF4444',0,3.3,0,g);
  bx(0.4,1.0,0.4,'#64748B',-0.9,1.3,0,g);bx(0.4,1.0,0.4,'#64748B',0.9,1.3,0,g);bx(0.45,0.7,0.5,'#475569',-0.4,0.35,0,g);bx(0.45,0.7,0.5,'#475569',0.4,0.35,0,g);return g}
function makeKey(){var g=new THREE.Group(),m=emi('#FACC15','#B45309');bx(0.7,0.7,0.2,m,0,0.8,0,g);bx(0.3,0.3,0.22,'#1F2937',0,0.8,0,g);bx(0.2,1.0,0.2,m,0,0.15,0,g);bx(0.5,0.2,0.2,m,0.2,-0.2,0,g);return g}
var roofTop=checker('#6B7280','#5F6673',1,1),roofMat=[mat('#374151'),mat('#374151'),new THREE.MeshLambertMaterial({map:roofTop}),mat('#374151'),mat('#374151'),mat('#374151')];
var door=null;
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var rows=L.rows,nz=rows.length,nx=rows[0].length,r=rng(71+n*3);
  scene.background.set('#1B2145');scene.fog.color.set('#1B2145');scene.fog.near=60;scene.fog.far=150;
  S.rb=[];S.keys=[];S.nk=0;S.got=0;S.exit=null;
  var street=new THREE.Mesh(new THREE.PlaneGeometry(240,240),new THREE.MeshLambertMaterial({color:'#0F172A'}));street.rotation.x=-Math.PI/2;street.position.set((nx-1)*C/2,-12,(nz-1)*C/2);lvGroup.add(street);
  for(var i=0;i<26;i++){var bw=4+r()*6,bh=6+r()*14,ang=r()*6.283,rd=(Math.max(nx,nz)*C*0.5)+16+r()*24,bxm=bx(bw,bh,bw,'#243055',(nx-1)*C/2+Math.cos(ang)*rd*1.3,-12+bh/2,(nz-1)*C/2+Math.sin(ang)*rd,lvGroup);
    for(var w=0;w<4;w++)if(r()<0.6)bx(0.8,0.8,0.1,basic('#FDE68A'),bxm.position.x+(r()-0.5)*bw*0.7,bxm.position.y+(r()-0.5)*bh*0.7,bxm.position.z+bw/2+0.05,lvGroup)}
  bx(5,5,0.5,basic('#FEF3C7'),(nx-1)*C/2-30,28,-60,lvGroup);
  for(var z=0;z<nz;z++)for(var x=0;x<nx;x++){var c=rows[z][x],wx=x*C,wz=z*C;
    if(c!=='~'){var m=new THREE.Mesh(new THREE.BoxGeometry(C,1.2,C),roofMat);m.position.set(wx,-0.6,wz);lvGroup.add(m);
      if(x===0||!walk(x-1,z)&&cellCh(x-1,z)==='~')bx(0.2,0.3,C,'#4B5563',wx-C/2+0.1,0.15,wz,lvGroup)}
    if(c==='G'){S.start={x:wx,z:wz}}
    else if(c==='R'||c==='V'){var rb=makeRobot();rb.position.set(wx,0,wz);lvGroup.add(rb);S.rb.push({x:wx,z:wz,mesh:rb,dx:c==='R'?1:0,dz:c==='V'?1:0,ph:r()*6,sx:wx,sz:wz})}
    else if(c==='L'){var k=makeKey();k.position.set(wx,0,wz);lvGroup.add(k);S.keys.push({x:wx,z:wz,mesh:k,got:false});S.nk++}
    else if(c==='C'){bx(1.8,1.6,1.8,'#B45309',wx,0.8,wz,lvGroup);bx(1.9,0.2,1.9,'#92400E',wx,1.6,wz,lvGroup);bx(0.3,1.5,1.92,'#92400E',wx,0.8,wz,lvGroup)}
    else if(c==='S'){var d=new THREE.Group();bx(2.2,0.15,2.2,'#1F2937',0,0.08,0,d);bx(0.3,2.6,0.3,'#9CA3AF',-0.95,1.3,0,d);bx(0.3,2.6,0.3,'#9CA3AF',0.95,1.3,0,d);bx(2.2,0.3,0.3,'#9CA3AF',0,2.65,0,d);var pn=bx(1.6,2.4,0.15,basic('#EF4444'),0,1.25,0,d);d.userData.pn=pn;d.position.set(wx,0,wz);lvGroup.add(d);S.exit={x:wx,z:wz,g:d}}}
  scene.add(cat);
  S.p={x:S.start.x,z:S.start.z,ry:0,air:0,bob:0,fall:false};S.camx=S.start.x;S.camz=S.start.z;S.warn=0;S.zoomY=Math.max(nx*1.75,nz*2.6)+4;
}
function hud(){var p=S.p;setHud('Nivel '+(S.lv+1)+'/3','Llaves '+(S.got||0)+'/'+(S.nk||0),(S.got>=S.nk&&S.nk)?'Puerta abierta':'Puerta cerrada',p&&p.air>0?'Saltando…':'En el tejado')}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,tries:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: llaves = 0, nivel = 1');buildLevel(0);showOv('GATO NINJA','Pulsa Espacio o toca para empezar')}
function loadLevel(n,quiet){S.lv=n;S.mode='play';buildLevel(n);hideOv();if(!quiet)flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Gato, '+S.rb.length+' robot(s), '+S.nk+' llave(s) y Salida')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡MISIÓN CUMPLIDA!','El gato ninja escapó de los 3 tejados','Pulsa Espacio para repetir')}}
function onSpace(){var p=S.p;if(p.air>0)return;p.air=0.6;ev('Input: tecla Espacio');co('¿Está en el suelo? SÍ');ac('Saltar: 0,6 s en el aire')}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p,h=p.air>0?Math.sin(Math.PI*(1-p.air/0.6))*1.9:0;
  var dx=(held.right?1:0)-(held.left?1:0),dz=(held.down?1:0)-(held.up?1:0),m=Math.hypot(dx,dz);
  if(m>0){dx/=m;dz/=m;var sp=(p.air>0?8:5.8)*dt,nx=p.x+dx*sp,nz=p.z+dz*sp;if(canMove(nx,p.z,0.4))p.x=nx;if(canMove(p.x,nz,0.4))p.z=nz;
    var ty=Math.atan2(dx,dz),df=ty-p.ry;while(df>Math.PI)df-=6.283;while(df<-Math.PI)df+=6.283;p.ry+=df*Math.min(1,14*dt);p.bob+=dt*12}
  if(p.air>0){p.air-=dt;if(p.air<=0){p.air=0;
    if(ch(p.x,p.z)==='~'){ev('On Trigger Enter (Gato ∩ Calle)');ac('Teleport al inicio');flash('¡Caíste a la calle! Vuelves al inicio',1400);p.x=S.start.x;p.z=S.start.z}}}
  S.keys.forEach(function(k){if(!k.got&&Math.hypot(k.x-p.x,k.z-p.z)<1.2){k.got=true;k.mesh.visible=false;S.got++;ev('On Trigger Enter (Gato ∩ Llave)');ac('Destroy(Llave), llaves = '+S.got+'/'+S.nk);if(S.got>=S.nk){ac('Puerta abierta (cambia a verde)')}}});
  S.rb.forEach(function(g){var step=3.0*dt;
    var cx=Math.round(g.x/C),cz=Math.round(g.z/C),ccx=cx*C,ccz=cz*C,near=Math.hypot(g.x-ccx,g.z-ccz)<=step*1.01+0.01;
    if(near&&(g.last!==cx+','+cz)){g.last=cx+','+cz;if(!walk(cx+g.dx,cz+g.dz)){g.dx=-g.dx;g.dz=-g.dz;g.x=ccx;g.z=ccz}}
    g.x+=g.dx*step;g.z+=g.dz*step;
    if(h<1.0&&Math.hypot(g.x-p.x,g.z-p.z)<1.5){ev('On Trigger Enter (Robot ∩ Gato)');co('¿Está saltando por encima? NO');ac('Reiniciar el nivel');S.tries++;loadLevel(S.lv,true);flash('¡Te pilló un robot! Se reinicia el nivel',1800)}});
  if(S.mode!=='play'||!S.exit)return;
  if(Math.hypot(S.exit.x-p.x,S.exit.z-p.z)<1.5){
    if(S.got>=S.nk){ev('On Trigger Enter (Gato ∩ Salida)');co('¿Tiene todas las llaves? SÍ');ac('Cargar el siguiente nivel');toNext()}
    else if(S.t>S.warn){S.warn=S.t+2500;ev('On Trigger Enter (Gato ∩ Salida)');co('¿Tiene todas las llaves? NO ('+S.got+'/'+S.nk+')');ac('La puerta sigue cerrada');flash('Faltan llaves: '+S.got+'/'+S.nk,1500)}}
}
function render(dt){
  var p=S.p,t=S.t/1000,h=p.air>0?Math.sin(Math.PI*(1-p.air/0.6))*1.9:0;
  cat.position.set(p.x,h+Math.abs(Math.sin(p.bob))*0.08,p.z);cat.rotation.y=p.ry;tailG.rotation.x=Math.sin(t*5)*0.4;
  S.rb.forEach(function(g){g.mesh.position.set(g.x,Math.abs(Math.sin(t*6+g.ph))*0.1,g.z);g.mesh.rotation.y=Math.atan2(g.dx,g.dz)});
  S.keys.forEach(function(k){if(!k.got){k.mesh.rotation.y=t*2.5;k.mesh.position.y=Math.sin(t*3+k.x)*0.2}});
  if(S.exit)S.exit.g.userData.pn.material=basic(S.got>=S.nk?'#22C55E':'#EF4444');
  var nx=S.L.rows[0].length,nz=S.L.rows.length,cx=(nx-1)*C/2,cz=(nz-1)*C/2;
  S.camx+=(cx-S.camx)*Math.min(1,6*dt);S.camz+=(cz-S.camz)*Math.min(1,6*dt);
  cam.position.set(S.camx,S.zoomY,S.camz+S.zoomY*0.42);cam.lookAt(S.camx,0.4,S.camz+0.2);
}
'''
build('gato3d.html','Gato Ninja','SALTAR<br>(Espacio)','Flechas o WASD para moverte por los tejados · Espacio: saltar (huecos entre tejados, y hasta por encima de un robot). Coge todas las llaves y llega a la puerta sin que te toque ningún robot.','#1B2145',G)
