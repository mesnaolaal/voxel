from common import build
G=r'''
var TITLE='MISIÓN ESPACIAL';
var LV=[
 {name:'Espacio abierto con un asteroide',len:420,crystals:3,asts:1,ufos:0,seed:3},
 {name:'Un campo de asteroides',len:520,crystals:4,asts:22,ufos:0,seed:7},
 {name:'Dos ovnis patrullan el sector',len:560,crystals:5,asts:10,ufos:2,seed:11}];
var BX=13,BY=7.5;
scene.background=new THREE.Color('#04061A');scene.fog=null;
amb.intensity=0.55;sun.intensity=0.95;sun.position.set(-20,30,40);
var ship=new THREE.Group(),flame;
(function(){var g=ship;
  bx(0.9,0.6,3.0,'#E5E7EB',0,0,0,g);bx(0.5,0.45,1.0,'#E5E7EB',0,0,-1.9,g);bx(0.25,0.3,0.6,'#E5E7EB',0,0,-2.6,g);
  bx(0.55,0.4,0.9,emi('#22D3EE','#0E7490'),0,0.45,-0.4,g);
  var w1=bx(3.4,0.14,1.5,'#EF4444',-1.7,-0.05,0.5,g);w1.rotation.y=-0.35;var w2=bx(3.4,0.14,1.5,'#EF4444',1.7,-0.05,0.5,g);w2.rotation.y=0.35;
  bx(0.14,0.7,1.0,'#EF4444',0,0.6,1.1,g);
  bx(0.5,0.5,0.5,'#4B5563',-0.5,0,1.5,g);bx(0.5,0.5,0.5,'#4B5563',0.5,0,1.5,g);
  flame=new THREE.Group();bx(0.35,0.35,1.2,basic('#F97316'),-0.5,0,2.2,flame);bx(0.35,0.35,1.2,basic('#F97316'),0.5,0,2.2,flame);bx(0.2,0.2,1.5,basic('#FDE047'),-0.5,0,2.3,flame);bx(0.2,0.2,1.5,basic('#FDE047'),0.5,0,2.3,flame);g.add(flame)})();
// estrellas
var NS=1800,sp=new Float32Array(NS*3);for(var i=0;i<NS;i++){sp[i*3]=(Math.random()-0.5)*260;sp[i*3+1]=(Math.random()-0.5)*160;sp[i*3+2]=-Math.random()*900+60}
var sg=new THREE.BufferGeometry();sg.setAttribute('position',new THREE.BufferAttribute(sp,3));var stars=new THREE.Points(sg,new THREE.PointsMaterial({color:0xffffff,size:2,sizeAttenuation:false,fog:false}));stars.frustumCulled=false;scene.add(stars);
var astMat=new THREE.MeshLambertMaterial({color:'#8B7B6B',flatShading:true}),crysMat=new THREE.MeshLambertMaterial({color:'#22D3EE',emissive:'#0891B2',flatShading:true});
function makeUfo(){var g=new THREE.Group();var d=new THREE.Mesh(new THREE.CylinderGeometry(2.2,2.8,0.7,8),mat('#9CA3AF'));g.add(d);var t=new THREE.Mesh(new THREE.CylinderGeometry(1.2,2.2,0.5,8),mat('#6B7280'));t.position.y=0.55;g.add(t);
  var c=new THREE.Mesh(new THREE.SphereGeometry(1.0,8,6),new THREE.MeshLambertMaterial({color:'#86EFAC',emissive:'#16A34A',flatShading:true}));c.position.y=1.0;g.add(c);
  for(var i=0;i<6;i++){var a=i/6*6.283;bx(0.35,0.35,0.35,basic(i%2?'#FDE047':'#F87171'),Math.cos(a)*2.4,0,Math.sin(a)*2.4,g)}return g}
var planet=null;
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var r=rng(L.seed*13+5),i;
  S.asts=[];S.crys=[];S.ufos=[];S.bul=[];S.deb=[];
  function free(x,y,z,d){return S.asts.every(function(a){return Math.hypot(a.x-x,a.y-y,a.z-z)>a.r+d})}
  for(i=0;i<L.asts;i++){var rr=1.3+r()*1.6,x,y,z,tries=0;do{x=(r()*2-1)*(BX+2);y=(r()*2-1)*(BY+1);z=-60-r()*(L.len-120);tries++}while(!free(x,y,z,rr+1)&&tries<8);
    var m=new THREE.Mesh(new THREE.IcosahedronGeometry(rr,0),astMat);m.position.set(x,y,z);m.rotation.set(r()*6,r()*6,0);lvGroup.add(m);S.asts.push({x:x,y:y,z:z,r:rr,mesh:m,rs:(r()-0.5)*1.2,dead:false})}
  for(i=0;i<L.crystals;i++){var x2,y2,z2,t2=0;do{x2=(r()*2-1)*(BX-1);y2=(r()*2-1)*(BY-0.5);z2=-70-(i+0.3+r()*0.4)*((L.len-150)/L.crystals);t2++}while(!free(x2,y2,z2,3)&&t2<10);
    var cm=new THREE.Mesh(new THREE.OctahedronGeometry(0.95,0),crysMat);cm.position.set(x2,y2,z2);cm.scale.y=1.5;lvGroup.add(cm);S.crys.push({x:x2,y:y2,z:z2,mesh:cm,got:false})}
  for(i=0;i<L.ufos;i++){var u=makeUfo();var z3=-170-i*180-r()*40;u.position.set(0,0,z3);lvGroup.add(u);S.ufos.push({bx:(r()*2-1)*6,by:(r()*2-1)*3,z:z3,mesh:u,ph:r()*6,x:0,y:0,sx:0.7+r()*0.4,sy:0.9+r()*0.4})}
  planet=new THREE.Group();var pl=new THREE.Mesh(new THREE.SphereGeometry(30,10,8),new THREE.MeshLambertMaterial({color:'#38BDF8',flatShading:true}));planet.add(pl);
  [[8,12,20],[-14,6,24],[16,-10,18],[-6,-18,22]].forEach(function(o){var c=new THREE.Mesh(new THREE.IcosahedronGeometry(7,0),new THREE.MeshLambertMaterial({color:'#4ADE80',flatShading:true}));c.position.set(o[0],o[1],o[2]).normalize().multiplyScalar(29);planet.add(c)});
  var ring=new THREE.Mesh(new THREE.RingGeometry(40,52,24),new THREE.MeshBasicMaterial({color:0xFDE68A,transparent:true,opacity:0.55,side:THREE.DoubleSide}));ring.rotation.x=1.3;planet.add(ring);
  planet.position.set(0,0,-L.len-45);lvGroup.add(planet);
  var sunL=new THREE.Mesh(new THREE.SphereGeometry(9,8,6),new THREE.MeshBasicMaterial({color:0xFDE68A}));sunL.position.set(-90,50,-L.len-300);lvGroup.add(sunL);
  scene.add(ship);
  S.p={x:0,y:0,z:0,vx:0,vy:0,inv:0,roll:0};S.cd=0;S.cr=0;S.camx=0;S.camy=0;S.shake=0;S.plT=0;
}
function hud(){var p=S.p,d=Math.max(0,Math.round((S.L?S.L.len+15:0)+(p?p.z:0)));var h='';for(var i=0;i<3;i++)h+=i<(S.lives||0)?'♥':'♡';
  setHud('Nivel '+(S.lv+1)+'/3 · '+h,'Cristales '+(S.cr||0)+'/'+(S.L?S.L.crystals:0),'Planeta a '+d+' m',held.shift?'Propulsor ON':'Láser listo')}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,lives:3,cr:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: vidas = 3, cristales = 0');buildLevel(0);showOv('MISIÓN ESPACIAL','Pulsa Espacio o toca para empezar')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2400);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Nave, '+S.L.crystals+' cristal(es), '+S.L.asts+' asteroide(s)'+(S.L.ufos?', '+S.L.ufos+' ovni(s)':'')+' y Planeta')}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡MISIÓN CUMPLIDA!','Has llegado al planeta en los 3 sectores','Pulsa Espacio para repetir')}}
function over(){S.mode='over';showOv('¡NAVE DESTRUIDA!','Te has quedado sin vidas','Pulsa Espacio para reintentar')}
function onSpace(){if(S.cd>0)return;S.cd=0.22;var p=S.p;S.bul.push({x:p.x,y:p.y,z:p.z-2,t:1.3,mesh:(function(){var b=bx(0.25,0.25,2.2,basic('#F472B6'),p.x,p.y,p.z-2,lvGroup);return b})()});if(!S.lastSh||S.t-S.lastSh>1200){ev('Input: tecla Espacio');ac('Instantiate Láser hacia delante')}S.lastSh=S.t}
function hurt(why){var p=S.p;if(p.inv>S.t)return;S.lives--;p.inv=S.t+2000;S.shake=0.5;ev('On Trigger Enter ('+why+' ∩ Nave)');ac('vidas = vidas − 1 → '+S.lives);if(S.lives<=0){ac('Load Scene "GameOver"');over()}}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p;S.cd=Math.max(0,S.cd-dt);S.shake=Math.max(0,S.shake-dt);
  var dx=(held.right?1:0)-(held.left?1:0),dy=(held.up?1:0)-(held.down?1:0);
  p.vx+=(dx*15-p.vx)*Math.min(1,7*dt);p.vy+=(dy*12-p.vy)*Math.min(1,7*dt);
  p.x=Math.max(-BX,Math.min(BX,p.x+p.vx*dt));p.y=Math.max(-BY,Math.min(BY,p.y+p.vy*dt));
  var sp=held.shift?44:26;p.z-=sp*dt;p.roll+=((-dx*0.7)-p.roll)*Math.min(1,6*dt);
  S.crys.forEach(function(c){if(!c.got&&Math.hypot(c.x-p.x,c.y-p.y,c.z-p.z)<2.1){c.got=true;c.mesh.visible=false;S.cr++;ev('On Trigger Enter (Nave ∩ Cristal)');ac('Destroy(Cristal), cristales = '+S.cr+'/'+S.L.crystals)}});
  S.asts.forEach(function(a){if(!a.dead&&Math.hypot(a.x-p.x,a.y-p.y,a.z-p.z)<a.r*0.85+1.0)hurt('Asteroide')});
  if(S.mode!=='play')return;
  S.ufos.forEach(function(u){u.x=u.bx+9*Math.sin(S.t/1000*u.sx+u.ph);u.y=u.by+4.5*Math.sin(S.t/1000*u.sy*1.3+u.ph*2);if(Math.hypot(u.x-p.x,u.y-p.y,u.z-p.z)<2.9)hurt('Ovni')});
  if(S.mode!=='play')return;
  for(var i=S.bul.length-1;i>=0;i--){var b=S.bul[i];b.z-=95*dt;b.t-=dt;b.mesh.position.z=b.z;var hit=false;
    S.asts.forEach(function(a){if(!hit&&!a.dead&&Math.hypot(a.x-b.x,a.y-b.y,a.z-b.z)<a.r+0.8){hit=true;a.dead=true;a.mesh.visible=false;ev('On Trigger Enter (Láser ∩ Asteroide)');ac('Destroy(Asteroide) y Destroy(Láser)');for(var k=0;k<7;k++){var d=bx(0.45,0.45,0.45,'#A8A29E',a.x,a.y,a.z,lvGroup);S.deb.push({m:d,vx:(Math.random()-0.5)*16,vy:(Math.random()-0.5)*16,vz:(Math.random()-0.5)*16,t:0.7})}}});
    if(hit||b.t<=0){lvGroup.remove(b.mesh);S.bul.splice(i,1)}}
  for(var j=S.deb.length-1;j>=0;j--){var d=S.deb[j];d.t-=dt;d.m.position.x+=d.vx*dt;d.m.position.y+=d.vy*dt;d.m.position.z+=d.vz*dt;d.m.scale.setScalar(Math.max(0.01,d.t/0.7));if(d.t<=0){lvGroup.remove(d.m);S.deb.splice(j,1)}}
  var pl=planet,dist=Math.hypot(p.x-pl.position.x,p.y-pl.position.y,p.z-pl.position.z);
  if(dist<33){ev('On Trigger Enter (Nave ∩ Planeta)');
    if(S.cr>=S.L.crystals){co('¿Tiene todos los cristales? SÍ ('+S.cr+'/'+S.L.crystals+')');ac('Cargar el siguiente nivel');toNext()}
    else{co('¿Tiene todos los cristales? NO ('+S.cr+'/'+S.L.crystals+')');ac('Volver al inicio del sector (cristales restaurados)');flash('Faltan cristales: ¡inténtalo de nuevo!',2200);
      p.z=0;p.x=0;p.y=0;S.cr=0;S.crys.forEach(function(c){c.got=false;c.mesh.visible=true})}}
}
function render(dt){
  var p=S.p,t=S.t/1000;
  ship.position.set(p.x,p.y,p.z);ship.rotation.z=p.roll;ship.rotation.x=p.vy*0.02;ship.visible=!(p.inv>S.t&&Math.floor(S.t/90)%2);
  flame.scale.z=(held.shift?1.8:1)*(0.8+0.3*Math.sin(t*40));
  S.crys.forEach(function(c){if(!c.got){c.mesh.rotation.y=t*2.2;c.mesh.position.y=c.y+Math.sin(t*3+c.z)*0.25}});
  S.asts.forEach(function(a){if(!a.dead){a.mesh.rotation.x+=a.rs*dt;a.mesh.rotation.y+=a.rs*0.7*dt}});
  S.ufos.forEach(function(u){u.mesh.position.set(u.x,u.y,u.z);u.mesh.rotation.y=t*2});
  planet.rotation.y=t*0.05;
  S.camx+=(p.x*0.7-S.camx)*Math.min(1,5*dt);S.camy+=(p.y*0.7-S.camy)*Math.min(1,5*dt);
  var sh=S.shake*0.8;cam.fov=62+(held.shift?10:0);cam.updateProjectionMatrix();
  cam.position.set(S.camx+(Math.random()-0.5)*sh,S.camy+3.2+(Math.random()-0.5)*sh,p.z+9);cam.lookAt(p.x*0.85,p.y*0.85,p.z-22);
  stars.position.z=p.z*0.8;
}
'''
build('espacio3d.html','Misión Espacial','DISPARAR<br>(Espacio)','Flechas o WASD para mover la nave arriba, abajo, izquierda y derecha · Espacio: disparar a los asteroides · Mantén Shift para el propulsor (más velocidad, solo en teclado). Recoge todos los cristales y toca el planeta. Esquiva asteroides y ovnis: tienes 3 vidas.','#04061A',G)
