from common import build
G=r'''
amb.intensity=0.85;sun.intensity=0.7;
var TITLE='ROBOT FÁBRICA';
var LV=[
 {name:'Una sala pequeña: una caja y un destino',rows:['#######','#.....#','#.RCX.#','#.....#','#######']},
 {name:'Dos cajas y una pared en medio',rows:['#########','#.......#','#.R.C...#','#...#.C.#','#.X.#.X.#','#########']},
 {name:'Tres destinos y una esquina peligrosa',rows:['#########','#X..#..X#','#...C...#','#.R.C.C.#','#...#.X.#','#########']}];
function isWall(x,z){var c=cellCh(x,z);return c===undefined||c==='#'}
var robot=new THREE.Group(),armL,armR,eyeG;
(function(){var g=robot;
  bx(1.5,0.5,1.7,'#475569',0,0.35,0,g);bx(0.35,0.5,1.9,'#1F2937',-0.85,0.3,0,g);bx(0.35,0.5,1.9,'#1F2937',0.85,0.3,0,g);
  bx(1.3,1.0,1.3,'#F59E0B',0,1.1,0,g);bx(1.3,0.2,1.3,'#B45309',0,1.7,0,g);bx(1.0,0.8,1.0,'#E2E8F0',0,2.2,0,g);bx(0.8,0.3,0.1,basic('#22D3EE'),0,2.25,0.52,g);bx(0.12,0.5,0.12,'#475569',0,2.85,0,g);bx(0.3,0.3,0.3,'#EF4444',0,3.2,0,g);
  armL=new THREE.Group();armL.position.set(-0.85,1.2,0);bx(0.3,0.3,1.0,'#94A3B8',0,0,0.5,armL);g.add(armL);armR=new THREE.Group();armR.position.set(0.85,1.2,0);bx(0.3,0.3,1.0,'#94A3B8',0,0,0.5,armR);g.add(armR)})();
function makeBox(placed){var g=new THREE.Group(),c=placed?'#22C55E':'#B45309',d=placed?'#15803D':'#92400E';bx(1.7,1.7,1.7,c,0,0.85,0,g);bx(1.8,0.2,1.8,d,0,1.7,0,g);bx(1.8,0.2,1.8,d,0,0.1,0,g);bx(0.25,1.7,1.72,d,0,0.85,0,g);bx(1.72,1.7,0.25,d,0,0.85,0,g);return g}
var floorTex=checker('#9CA3AF','#8B93A1',1,1);
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var rows=L.rows,nz=rows.length,nx=rows[0].length,r=rng(5+n);
  scene.background.set('#2B3347');scene.fog.color.set('#2B3347');scene.fog.near=70;scene.fog.far=170;
  S.boxes=[];S.tg=[];S.hist=[];S.moves=0;S.anim=0;S.done=false;
  var fl=new THREE.Mesh(new THREE.BoxGeometry(nx*C,0.4,nz*C),new THREE.MeshLambertMaterial({map:floorTex}));floorTex.repeat.set(nx,nz);fl.position.set((nx-1)*C/2,-0.2,(nz-1)*C/2);lvGroup.add(fl);
  for(var z=0;z<nz;z++)for(var x=0;x<nx;x++){var c=rows[z][x],wx=x*C,wz=z*C;
    if(c==='#'){bx(C,1.6,C,'#64748B',wx,0.8,wz,lvGroup);bx(C*1.02,0.2,C*1.02,'#475569',wx,1.7,wz,lvGroup);bx(C*0.9,0.06,0.3,'#FACC15',wx,1.82,wz,lvGroup);bx(C*0.5,0.5,0.1,'#334155',wx,0.9,wz+C/2,lvGroup)}
    if(c==='X'){bx(C*0.9,0.06,C*0.9,'#FACC15',wx,0.04,wz,lvGroup);bx(C*0.7,0.08,0.3,'#92400E',wx,0.07,wz,lvGroup);var d1=bx(C*0.8,0.08,0.28,'#92400E',wx,0.08,wz,lvGroup);d1.rotation.y=Math.PI/4;var d2=bx(C*0.8,0.08,0.28,'#92400E',wx,0.08,wz,lvGroup);d2.rotation.y=-Math.PI/4;S.tg.push({x:x,z:z})}
    if(c==='R'){S.rb={x:x,z:z,px:wx,pz:wz,fx:0,fz:1}}
    if(c==='C'){var bm=makeBox(false);bm.position.set(wx,0,wz);scene.add(bm);lvGroup.add(bm);S.boxes.push({x:x,z:z,px:wx,pz:wz,mesh:bm,placed:false})}}
  scene.add(robot);S.zoomY=Math.max(nx*1.7,nz*2.5)+4;S.camx=(nx-1)*C/2;S.camz=(nz-1)*C/2;S.dead=false;
}
function boxAt(x,z){for(var i=0;i<S.boxes.length;i++)if(S.boxes[i].x===x&&S.boxes[i].z===z)return S.boxes[i];return null}
function isTarget(x,z){return S.tg.some(function(t){return t.x===x&&t.z===z})}
function placedCount(){return S.boxes.filter(function(b){return isTarget(b.x,b.z)}).length}
function hud(){setHud('Nivel '+(S.lv+1)+'/3','Cajas '+(S.boxes?placedCount():0)+'/'+(S.boxes?S.boxes.length:0),'Movimientos '+(S.moves||0),'Espacio: deshacer')}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: cajas colocadas = 0, nivel = 1');buildLevel(0);showOv('ROBOT FÁBRICA','Pulsa Espacio o toca para empezar','Flechas: mover (empuja las cajas) · Espacio: deshacer')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Robot, '+S.boxes.length+' caja(s) y '+S.tg.length+' zona(s) de destino')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡ALMACÉN ORDENADO!','Todas las cajas están en su sitio','Pulsa Espacio para repetir')}}
function snapshot(){return {rx:S.rb.x,rz:S.rb.z,fx:S.rb.fx,fz:S.rb.fz,b:S.boxes.map(function(b){return [b.x,b.z]}),m:S.moves}}
function onSpace(){if(S.anim>0||!S.hist.length)return;var h=S.hist.pop();S.rb.x=h.rx;S.rb.z=h.rz;S.rb.fx=h.fx;S.rb.fz=h.fz;S.moves=h.m;h.b.forEach(function(p,i){S.boxes[i].x=p[0];S.boxes[i].z=p[1]});ev('Input: tecla Espacio');ac('Deshacer el último movimiento');S.dead=false}
function stuck(b){if(isTarget(b.x,b.z))return false;var w=function(x,z){return isWall(x,z)};return (w(b.x-1,b.z)||w(b.x+1,b.z))&&(w(b.x,b.z-1)||w(b.x,b.z+1))}
function tryMove(dx,dz){
  var rb=S.rb,nx=rb.x+dx,nz=rb.z+dz;rb.fx=dx;rb.fz=dz;if(isWall(nx,nz))return false;
  var bx_=boxAt(nx,nz),snap=snapshot();
  if(bx_){var mx=nx+dx,mz=nz+dz;if(isWall(mx,mz)||boxAt(mx,mz))return false;S.hist.push(snap);bx_.x=mx;bx_.z=mz;ev('El robot empuja una caja');ac('La caja avanza una casilla');
    if(isTarget(mx,mz)){ev('On Trigger Enter (Caja ∩ Destino)');ac('La caja cambia a verde, cajas colocadas = '+placedCount()+'/'+S.boxes.length)}}
  else S.hist.push(snap);
  rb.x=nx;rb.z=nz;S.moves++;S.anim=0.14;return true}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  S.anim=Math.max(0,S.anim-dt);
  if(S.anim<=0&&!S.done){
    var dx=(held.right?1:0)-(held.left?1:0),dz=(held.down?1:0)-(held.up?1:0);if(dx&&dz)dz=0;
    if(dx||dz)tryMove(dx,dz);
    if(placedCount()===S.boxes.length){S.done=true;ev('Todas las cajas colocadas');co('¿cajas colocadas = total? SÍ');ac('Cargar el siguiente nivel');toNext();return}
    var st=S.boxes.filter(stuck)[0];if(st&&!S.dead){S.dead=true;ev('Caja en una esquina');co('¿Está en un destino? NO');ac('Mostrar Game Over');S.mode='over';showOv('¡CAJA ATASCADA!','Una caja quedó en una esquina','Pulsa Espacio para reintentar este nivel')}}
}
function render(dt){
  var rb=S.rb,t=S.t/1000,k=Math.min(1,18*dt);
  rb.px+=(rb.x*C-rb.px)*k;rb.pz+=(rb.z*C-rb.pz)*k;
  var ty=Math.atan2(rb.fx,rb.fz),df=ty-(rb.ry||0);while(df>Math.PI)df-=6.283;while(df<-Math.PI)df+=6.283;rb.ry=(rb.ry||0)+df*Math.min(1,16*dt);
  robot.position.set(rb.px,0,rb.pz);robot.rotation.y=rb.ry;armL.rotation.x=armR.rotation.x=Math.sin(t*12)*0.15*(S.anim>0?1:0.2);
  S.boxes.forEach(function(b){b.px+=(b.x*C-b.px)*k;b.pz+=(b.z*C-b.pz)*k;b.mesh.position.set(b.px,0,b.pz);var pl=isTarget(b.x,b.z);if(pl!==b.placed){b.placed=pl;lvGroup.remove(b.mesh);scene.remove(b.mesh);var nm=makeBox(pl);nm.position.copy(b.mesh.position);b.mesh=nm;lvGroup.add(nm)}});
  var nx=S.L.rows[0].length,nz=S.L.rows.length,cx=(nx-1)*C/2,cz=(nz-1)*C/2;
  S.camx+=(cx-S.camx)*Math.min(1,6*dt);S.camz+=(cz-S.camz)*Math.min(1,6*dt);
  cam.position.set(S.camx,S.zoomY,S.camz+S.zoomY*0.42);cam.lookAt(S.camx,0.4,S.camz+0.2);
}
'''
build('robot3d.html','Robot Fábrica','DESHACER<br>(Espacio)','Flechas o WASD: mover el robot, que empuja las cajas (solo una a la vez, nunca tirar de ellas). Lleva todas las cajas a las zonas amarillas. Espacio: deshacer el último movimiento. Si una caja queda en una esquina fuera de un destino, pierdes.','#2B3347',G)
