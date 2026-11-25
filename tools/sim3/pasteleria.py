from common import build
G=r'''
amb.intensity=0.55;sun.intensity=0.45;
var TITLE='PASTELERÍA LOCA';
var LV=[
 {name:'Dos ingredientes',time:45,rec:['H','A'],rows:[
  '###H#A#####',
  '#.........#',
  '#.........O',
  '#.C.......#',
  '#.........#',
  '#.........#',
  '#####T#####']},
 {name:'Tres ingredientes en orden',time:50,rec:['H','A','F'],rows:[
  '###H#A#F#####',
  '#...........#',
  '#...........O',
  '#.C.........#',
  '#...........#',
  '#...........#',
  '######T######']},
 {name:'Dos hornos y muy poco tiempo',time:40,rec:['H','A','F','F'],rows:[
  '###H#A#F#######',
  '#.............#',
  'O.............O',
  '#.............#',
  '#......#......#',
  '#..C...#......#',
  '#.............#',
  '#.............#',
  '#######T#######']}];
var NAMES={H:'Huevo',A:'Harina',F:'Fresa'},COL={H:'#FEF3C7',A:'#F8FAFC',F:'#EF4444'};
scene.background=new THREE.Color('#FDE9D4');scene.fog=null;
var chef=new THREE.Group(),hold=new THREE.Group();
(function(){var g=chef;
  bx(0.3,0.7,0.32,'#1F2937',-0.2,0.35,0,g);bx(0.3,0.7,0.32,'#1F2937',0.2,0.35,0,g);
  bx(0.95,0.95,0.6,'#FFFFFF',0,1.15,0,g);bx(0.2,0.2,0.05,'#2563EB',0.2,1.3,0.31,g);bx(0.2,0.2,0.05,'#2563EB',-0.2,1.3,0.31,g);
  bx(0.25,0.8,0.28,'#FFFFFF',-0.62,1.1,0,g);bx(0.25,0.8,0.28,'#FFFFFF',0.62,1.1,0,g);
  bx(0.55,0.5,0.5,'#FCD9A6',0,1.95,0,g);bx(0.1,0.1,0.05,'#111827',0.13,2.0,0.26,g);bx(0.1,0.1,0.05,'#111827',-0.13,2.0,0.26,g);
  bx(0.7,0.2,0.7,'#FFFFFF',0,2.3,0,g);bx(0.8,0.55,0.8,'#FFFFFF',0,2.7,0,g);
  hold.position.set(0,3.5,0);g.add(hold)})();
function setHold(k){while(hold.children.length)hold.remove(hold.children[0]);if(!k)return;
  if(k==='cake'){bx(1.1,0.4,1.1,'#F9A8D4',0,0,0,hold);bx(0.8,0.3,0.8,'#FDF2F8',0,0.35,0,hold);bx(0.25,0.3,0.25,'#EF4444',0,0.65,0,hold)}
  else{bx(0.6,0.6,0.6,COL[k],0,0,0,hold);bx(0.64,0.14,0.64,'#374151',0,0.4,0,hold)}}
var floorMat=new THREE.MeshLambertMaterial({map:checker('#FFF7ED','#FDE7CB',2,2)});
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var rows=L.rows,nz=rows.length,nx=rows[0].length;
  S.st=[];S.ovens=[];S.table=null;S.nIns=0;S.cakeMade=false;S.lastOven=null;S.cake=null;S.hold=null;
  var fl=new THREE.Mesh(new THREE.BoxGeometry(nx*C,0.4,nz*C),floorMat);floorMat.map.repeat.set(nx,nz);fl.position.set((nx-1)*C/2,-0.2,(nz-1)*C/2);lvGroup.add(fl);
  for(var z=0;z<nz;z++)for(var x=0;x<nx;x++){var ch=rows[z][x],wx=x*C,wz=z*C;
    if(ch==='#'){bx(C,1.8,C,'#F9A8D4',wx,0.9,wz,lvGroup);bx(C*1.02,0.2,C*1.02,'#FDF2F8',wx,1.85,wz,lvGroup)}
    else if('HAF'.indexOf(ch)>=0){bx(C,1.8,C,'#F9A8D4',wx,0.9,wz,lvGroup);bx(C*1.4,1.0,C*0.9,COL[ch],wx,0.5,wz+0.5,lvGroup);bx(C*1.45,0.18,C*0.95,'#374151',wx,1.05,wz+0.5,lvGroup);
      var tp=bx(1.0,1.0,1.0,COL[ch],wx,1.9,wz+0.2,lvGroup);S.st.push({k:ch,x:wx,z:wz+1.0,mesh:tp})}
    else if(ch==='O'){bx(C,1.8,C,'#9CA3AF',wx,0.9,wz,lvGroup);var side=x===0?1:-1;bx(0.2,1.1,1.4,'#111827',wx+side*0.95,0.9,wz,lvGroup);
      var gl=bx(0.12,0.8,1.1,basic('#78350F'),wx+side*1.05,0.9,wz,lvGroup);S.ovens.push({x:wx+side*1.3,z:wz,cx:wx,glow:gl,t:0,busy:false,has:0,done:false})}
    else if(ch==='T'){bx(C*1.8,1.1,C,'#D97706',wx,0.55,wz-0.3,lvGroup);bx(C*2,0.15,C*1.1,'#FEF3C7',wx,1.15,wz-0.3,lvGroup);bx(0.7,0.12,0.7,'#EF4444',wx,1.25,wz-0.3,lvGroup);S.table={x:wx,z:wz-1.2}}
    else if(ch==='C'){S.start={x:wx,z:wz}}}
  scene.add(chef);setHold(null);
  S.p={x:S.start.x,z:S.start.z,ry:0,bob:0};S.time=L.time;S.camx=(nx-1)*C/2;S.camz=(nz-1)*C/2;S.cakeMesh=null;S.pickCd=0;
  S.zoomY=Math.max(nx*1.6,nz*2.3)+2;
}
function isSolid(x,z){var c=cellCh(Math.round(x/C),Math.round(z/C));return c===undefined||'#HAFOT'.indexOf(c)>=0}
function canMove(x,z,r){return !isSolid(x-r,z-r)&&!isSolid(x+r,z-r)&&!isSolid(x-r,z+r)&&!isSolid(x+r,z+r)}
function hud(){var L=S.L,s='';if(L){s=L.rec.map(function(k,i){return i<S.nIns?'✓':(i===S.nIns?'['+NAMES[k][0]+']':NAMES[k][0])}).join(' ')}
  setHud('Nivel '+(S.lv+1)+'/3','Tiempo '+Math.max(0,Math.ceil(S.time||0))+' s','Receta '+s,'Manos: '+(S.hold?(S.hold==='cake'?'Tarta':NAMES[S.hold]):'vacías'))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,time:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: ingredientes = 0, nivel = 1');buildLevel(0);showOv('PASTELERÍA LOCA','Pulsa Espacio o toca para empezar')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2400);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Chef, '+S.ovens.length+' horno(s), mesa; receta de '+S.L.rec.length+' ingredientes; cronómetro = '+S.L.time+' s')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡PASTELERO DEL AÑO!','Has entregado las 3 tartas a tiempo','Pulsa Espacio para repetir')}}
function nearest(list,p,d){var b=null,bd=d;list.forEach(function(o){var dd=Math.hypot(o.x-p.x,o.z-p.z);if(dd<bd){bd=dd;b=o}});return b}
function onSpace(){
  var p=S.p,R=2.6,L=S.L,st=nearest(S.st,p,R),ov=nearest(S.ovens,p,R),tb=Math.hypot(S.table.x-p.x,S.table.z-p.z)<R?S.table:null;
  ev('Input: tecla Espacio');
  // tarta
  if(!S.hold&&S.cake&&Math.hypot(S.cake.x-p.x,S.cake.z-p.z)<R){S.hold='cake';lvGroup.remove(S.cakeMesh);S.cake=null;setHold('cake');co('¿Hay tarta lista? SÍ');ac('Coger tarta (manos = tarta)');return}
  if(S.hold==='cake'){if(tb){co('¿Está en la mesa con la tarta? SÍ');ac('Entregar tarta y parar el cronómetro');S.hold=null;setHold(null);toNext();return}
    co('¿Está en la mesa? NO');ac('Soltar la tarta');S.hold=null;setHold(null);return}
  if(!S.hold){
    if(st){S.hold=st.k;setHold(st.k);co('¿Tiene las manos vacías? SÍ');ac('Coger '+NAMES[st.k]+' (manos = '+NAMES[st.k]+')');return}
    return}
  // lleva ingrediente
  if(ov){var need=L.rec[S.nIns];
    if(ov.busy){co('¿Horno libre? NO');ac('Mostrar "Horno ocupado"');flash('Horno ocupado',1000);return}
    if(S.hold===need){co('¿Es el siguiente ingrediente de la receta? SÍ ('+NAMES[need]+')');S.nIns++;ov.busy=true;ov.t=3.2+(S.nIns*0.1);ov.has++;S.hold=null;setHold(null);ac('Meter '+NAMES[need]+' en el horno, ingredientes = '+S.nIns+'/'+L.rec.length);return}
    co('¿Es el siguiente ingrediente de la receta? NO (toca '+NAMES[need]+')');ac('Mostrar mensaje de error');flash('Ese no es: ahora toca '+NAMES[need],1600);return}
  co('¿Está cerca de algo útil? NO');ac('Soltar '+NAMES[S.hold]);S.hold=null;setHold(null);
}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p;S.time-=dt;
  if(S.time<=0){S.time=0;ev('Cronómetro = 0');co('¿Ha entregado la tarta? NO');ac('Mostrar Game Over');S.mode='over';showOv('¡SE ACABÓ EL TIEMPO!','La tarta no llegó a la mesa','Pulsa Espacio para reintentar este nivel');return}
  var dx=(held.right?1:0)-(held.left?1:0),dz=(held.down?1:0)-(held.up?1:0),m=Math.hypot(dx,dz);
  if(m>0){dx/=m;dz/=m;var sp=(held.shift?8:5)*dt,nx=p.x+dx*sp,nz=p.z+dz*sp;if(canMove(nx,p.z,0.42))p.x=nx;if(canMove(p.x,nz,0.42))p.z=nz;
    var ty=Math.atan2(dx,dz),df=ty-p.ry;while(df>Math.PI)df-=6.283;while(df<-Math.PI)df+=6.283;p.ry+=df*Math.min(1,14*dt);p.bob+=dt*(held.shift?16:11)}
  S.ovens.forEach(function(o){if(o.busy){o.t-=dt;if(o.t<=0){o.busy=false;o.last=true;S.lastOven=o;ev('Cronómetro del horno = 0');ac('Horno libre')}}});
  if(!S.cake&&S.nIns===S.L.rec.length&&S.ovens.every(function(o){return !o.busy})&&S.hold!=='cake'&&!S.cakeMade){
    S.cakeMade=true;var o=S.lastOven;S.cake={x:o.x,z:o.z};var g=new THREE.Group();bx(1.3,0.5,1.3,'#F9A8D4',0,0.25,0,g);bx(0.95,0.4,0.95,'#FDF2F8',0,0.7,0,g);bx(0.3,0.35,0.3,'#EF4444',0,1.1,0,g);g.position.set(o.cx+(o.x>o.cx?1.0:-1.0)*1.0,1.9,o.z);
    lvGroup.add(g);S.cakeMesh=g;S.cake.x=o.x;S.cake.z=o.z;ev('Todos los ingredientes horneados');ac('Instantiate Tarta en el horno');flash('¡Tarta lista! Cógela del horno',2000)}
}
function render(dt){
  var p=S.p,t=S.t/1000;
  chef.position.set(p.x,Math.abs(Math.sin(p.bob))*0.1,p.z);chef.rotation.y=p.ry;
  S.ovens.forEach(function(o){o.glow.material.color.set(o.busy?(Math.floor(t*6)%2?'#F97316':'#FACC15'):'#78350F')});
  S.st.forEach(function(s){s.mesh.rotation.y=t*0.8});
  if(S.cakeMesh)S.cakeMesh.rotation.y=t*2;
  var nx=S.L.rows[0].length,nz=S.L.rows.length,cx=(nx-1)*C/2,cz=(nz-1)*C/2;
  S.camx+=(cx-S.camx)*Math.min(1,6*dt);S.camz+=(cz-S.camz)*Math.min(1,6*dt);
  cam.position.set(S.camx,S.zoomY,S.camz+S.zoomY*0.42);cam.lookAt(S.camx,0.4,S.camz+0.2);
}
'''
build('pasteleria3d.html','Pastelería Loca','COGER / SOLTAR<br>(Espacio)','Flechas o WASD para mover al chef · Espacio: coger ingrediente en los estantes, meterlo en el horno (en el orden de la receta), coger la tarta y dejarla en la mesa · Shift: correr. Acércate al objeto antes de pulsar Espacio.','#FDE9D4',G)
