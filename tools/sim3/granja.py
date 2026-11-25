from common import build
G=r'''
amb.intensity=0.85;sun.intensity=0.7;
var TITLE='LA GRANJA PERDIDA';
var LV=[
 {name:'Una granja con vallas',time:35,night:false,rows:[
  '###############',
  '#G....V.......#',
  '#.TT..V...H...#',
  '#.....V.......#',
  '#H....VVV.....#',
  '#.............#',
  '#..VVVV....H..#',
  '#......T......#',
  '#.E.....H.....#',
  '###############']},
 {name:'Más vallas, una gallina más y un zorro',time:40,night:false,rows:[
  '#################',
  '#G....V.....V...#',
  '#.TT..V..H..V.H.#',
  '#.....V..Z..V...#',
  '#H....VVV.VVV...#',
  '#...............#',
  '#..VVVV....T..H.#',
  '#......T........#',
  '#.E...H......VV.#',
  '#################']},
 {name:'Es de noche: dos zorros y menos tiempo',time:30,night:true,rows:[
  '#################',
  '#G..V...V...V...#',
  '#.T.V.H.V.H.V.H.#',
  '#...V...V.Z.V...#',
  '#.H.VV.VVV.VV...#',
  '#...............#',
  '#..VVVV..Z.T..H.#',
  '#......T........#',
  '#.E..........VV.#',
  '#################']}];
function ch(x,z){return cellCh(Math.round(x/C),Math.round(z/C))}
function solidAt(x,z,h){var c=ch(x,z);return c===undefined||c==='#'||c==='T'||c==='E'||(c==='V'&&h<1.0)}
function canMove(x,z,r,h){return !solidAt(x-r,z-r,h)&&!solidAt(x+r,z-r,h)&&!solidAt(x-r,z+r,h)&&!solidAt(x+r,z+r,h)}
function walk(cx,cz){var c=cellCh(cx,cz);return c!==undefined&&'#TEV'.indexOf(c)<0}
var farmer=new THREE.Group(),lamp=new THREE.PointLight(0xffd9a0,0,26);
(function(){var g=farmer;
  bx(0.3,0.7,0.32,'#1D4ED8',-0.2,0.35,0,g);bx(0.3,0.7,0.32,'#1D4ED8',0.2,0.35,0,g);
  bx(0.95,0.95,0.6,'#2563EB',0,1.15,0,g);bx(0.95,0.3,0.62,'#DC2626',0,1.5,0,g);bx(0.14,0.5,0.05,'#FACC15',0.2,1.1,0.32,g);bx(0.14,0.5,0.05,'#FACC15',-0.2,1.1,0.32,g);
  bx(0.25,0.8,0.28,'#DC2626',-0.62,1.1,0,g);bx(0.25,0.8,0.28,'#DC2626',0.62,1.1,0,g);
  bx(0.55,0.5,0.5,'#FCD9A6',0,1.95,0,g);bx(0.1,0.1,0.05,'#111827',0.13,2.0,0.26,g);bx(0.1,0.1,0.05,'#111827',-0.13,2.0,0.26,g);
  bx(1.5,0.12,1.5,'#FACC15',0,2.3,0,g);bx(0.7,0.35,0.7,'#EAB308',0,2.5,0,g);bx(0.72,0.1,0.72,'#B91C1C',0,2.38,0,g);
  lamp.position.set(0,3,0);g.add(lamp)})();
function makeHen(){var g=new THREE.Group();bx(0.9,0.8,1.1,'#FFFFFF',0,0.7,0,g);bx(0.5,0.6,0.5,'#FFFFFF',0,1.3,0.55,g);bx(0.14,0.25,0.3,'#DC2626',0,1.7,0.55,g);bx(0.2,0.14,0.3,'#F59E0B',0,1.3,0.9,g);bx(0.6,0.5,0.4,'#F3F4F6',0,0.9,-0.7,g);bx(0.1,0.1,0.05,'#111827',0.2,1.4,0.82,g);bx(0.1,0.1,0.05,'#111827',-0.2,1.4,0.82,g);bx(0.12,0.4,0.12,'#F59E0B',-0.2,0.2,0.1,g);bx(0.12,0.4,0.12,'#F59E0B',0.2,0.2,0.1,g);return g}
function makeFox(){var g=new THREE.Group(),o='#EA580C';bx(0.9,0.8,1.7,o,0,0.8,0,g);bx(0.7,0.65,0.7,o,0,1.1,1.1,g);bx(0.3,0.3,0.4,'#1F2937',0,1.0,1.55,g);bx(0.2,0.3,0.15,o,-0.25,1.55,1.1,g);bx(0.2,0.3,0.15,o,0.25,1.55,1.1,g);
  bx(0.2,0.2,0.05,'#111827',0.2,1.25,1.46,g);bx(0.2,0.2,0.05,'#111827',-0.2,1.25,1.46,g);bx(0.4,0.4,1.2,o,0,0.9,-1.4,g);bx(0.42,0.42,0.4,'#F8FAFC',0,0.9,-2.0,g);
  [[-0.3,0.7],[0.3,0.7],[-0.3,-0.6],[0.3,-0.6]].forEach(function(p){bx(0.2,0.5,0.2,'#7C2D12',p[0],0.25,p[1],g)});return g}
function makeTree(r){var g=new THREE.Group(),h=2.2+r()*1.4;bx(0.7,h,0.7,'#78350F',0,h/2,0,g);bx(2.4,1.6,2.4,'#16A34A',0,h+0.5,0,g);bx(1.7,1.2,1.7,'#22C55E',0,h+1.6,0,g);return g}
function makeFence(vertical){var g=new THREE.Group();bx(0.25,1.3,0.25,'#92400E',-0.9,0.65,0,g);bx(0.25,1.3,0.25,'#92400E',0.9,0.65,0,g);bx(2.1,0.2,0.18,'#B45309',0,0.5,0,g);bx(2.1,0.2,0.18,'#B45309',0,1.0,0,g);return g}
function makeBarn(){var g=new THREE.Group();bx(3.4,2.4,3.4,'#DC2626',0,1.2,0,g);bx(3.6,0.3,3.6,'#7F1D1D',0,2.5,0,g);var r=bx(3.7,1.2,2.0,'#991B1B',0,3.1,0,g);bx(1.4,1.7,0.1,'#FEF3C7',0,0.9,1.72,g);bx(1.5,0.2,0.12,'#7F1D1D',0,1.8,1.74,g);return g}
var grassTop=checker('#6BCB4F','#62BE48',1,1),grassMat=[mat('#7A5230'),mat('#7A5230'),new THREE.MeshLambertMaterial({map:grassTop}),mat('#7A5230'),mat('#7A5230'),mat('#7A5230')];
var out=new THREE.Mesh(new THREE.PlaneGeometry(260,260),new THREE.MeshLambertMaterial({color:'#4FA43A'}));out.rotation.x=-Math.PI/2;out.position.y=-0.92;scene.add(out);
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var rows=L.rows,nz=rows.length,nx=rows[0].length,r=rng(97+n*5);
  S.hens=[];S.foxes=[];S.nh=0;S.got=0;
  var bg=L.night?'#0A0F2E':'#A5DBFF';scene.background.set(bg);scene.fog.color.set(L.night?'#0A0F2E':'#BFE4FF');scene.fog.near=L.night?40:60;scene.fog.far=L.night?95:140;
  amb.intensity=L.night?0.5:0.85;sun.intensity=L.night?0.3:0.7;lamp.intensity=L.night?1.4:0;
  for(var z=0;z<nz;z++)for(var x=0;x<nx;x++){var c=rows[z][x],wx=x*C,wz=z*C;
    if(c==='#'){var hh=bx(C,1.6,C,'#15803D',wx,0.8,wz,lvGroup);bx(C*0.8,0.5,C*0.8,'#16A34A',wx,1.7,wz,lvGroup)}
    else{var m=new THREE.Mesh(new THREE.BoxGeometry(C,0.9,C),grassMat);m.position.set(wx,-0.45,wz);lvGroup.add(m)}
    if(c==='G'){S.start={x:wx,z:wz}}
    else if(c==='H'){var h=makeHen();h.position.set(wx,0,wz);h.rotation.y=r()*6;lvGroup.add(h);S.hens.push({x:wx,z:wz,mesh:h,got:false,ph:r()*6});S.nh++}
    else if(c==='Z'){var f=makeFox();f.position.set(wx,0,wz);lvGroup.add(f);S.foxes.push({x:wx,z:wz,mesh:f,dx:1,dz:0,last:''})}
    else if(c==='T'){var t=makeTree(r);t.position.set(wx,0,wz);lvGroup.add(t)}
    else if(c==='E'){var b=makeBarn();b.position.set(wx,0,wz);lvGroup.add(b)}
    else if(c==='V'){var f2=makeFence();f2.position.set(wx,0,wz);var left=cellCh(x-1,z)==='V'||cellCh(x+1,z)==='V';if(!left)f2.rotation.y=Math.PI/2;lvGroup.add(f2)}}
  scene.add(farmer);
  S.p={x:S.start.x,z:S.start.z,ry:Math.PI,inv:0,bob:0,air:0};S.time=L.time;S.jcd=0;S.camx=S.start.x;S.camz=S.start.z;
}
function hud(){var p=S.p;setHud('Nivel '+(S.lv+1)+'/3','Tiempo '+Math.max(0,Math.ceil(S.time||0))+' s','Gallinas '+(S.got||0)+'/'+(S.nh||0),p&&p.air>0?'Saltando…':(S.jcd>0?'Salto recargando':'Salto listo'))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,time:0,jcd:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: gallinas = 0, nivel = 1');buildLevel(0);showOv('LA GRANJA PERDIDA','Pulsa Espacio o toca para empezar')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2400);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Granjera, '+S.nh+' gallinas'+(S.foxes.length?', '+S.foxes.length+' zorro(s)':'')+'; temporizador = '+S.L.time+' s')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡GALLINAS A SALVO!','Has encontrado todas las gallinas en los 3 niveles','Pulsa Espacio para repetir')}}
function onSpace(){var p=S.p;if(p.air>0||S.jcd>0)return;p.air=0.75;ev('Input: tecla Espacio');co('¿Está en el suelo? SÍ');ac('Saltar: 0,75 s sin tocar el suelo (salta las vallas)')}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p;S.time-=dt;
  if(S.time<=0){S.time=0;ev('Temporizador = 0');co('¿Faltan gallinas? SÍ ('+S.got+'/'+S.nh+')');ac('Mostrar Game Over');S.mode='over';showOv('¡HA ANOCHECIDO!','Te faltaron '+(S.nh-S.got)+' gallina(s)','Pulsa Espacio para reintentar este nivel');return}
  S.jcd=Math.max(0,S.jcd-dt);
  var h=p.air>0?Math.sin(Math.PI*(1-p.air/0.75))*1.8:0;
  var dx=(held.right?1:0)-(held.left?1:0),dz=(held.down?1:0)-(held.up?1:0),m=Math.hypot(dx,dz);
  if(m>0){dx/=m;dz/=m;var sp=(p.air>0?8:5.5)*dt,nx=p.x+dx*sp,nz=p.z+dz*sp;if(canMove(nx,p.z,0.4,h))p.x=nx;if(canMove(p.x,nz,0.4,h))p.z=nz;
    var ty=Math.atan2(dx,dz),df=ty-p.ry;while(df>Math.PI)df-=6.283;while(df<-Math.PI)df+=6.283;p.ry+=df*Math.min(1,14*dt);p.bob+=dt*11}
  if(p.air>0){p.air-=dt;if(p.air<=0){p.air=0;S.jcd=0.2;if(solidAt(p.x,p.z,0)){var cx=Math.round(p.x/C)*C,cz=Math.round(p.z/C)*C;
      var best=null;[[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){var a=Math.round(p.x/C)+v[0],b=Math.round(p.z/C)+v[1];if(walk(a,b)&&!best)best=[a*C,b*C]});if(best){p.x=best[0];p.z=best[1]}}}}
  S.hens.forEach(function(g){if(!g.got&&Math.hypot(g.x-p.x,g.z-p.z)<1.2){g.got=true;g.mesh.visible=false;S.got++;ev('On Trigger Enter (Granjera ∩ Gallina)');ac('Destroy(Gallina), gallinas = '+S.got+'/'+S.nh)}});
  if(S.got>=S.nh){ev('gallinas == '+S.nh);co('¿Están todas en el establo? SÍ');ac('Cargar el siguiente nivel');toNext();return}
  S.foxes.forEach(function(g){
    var cx=Math.round(g.x/C),cz=Math.round(g.z/C),ccx=cx*C,ccz=cz*C,step=2.4*dt;
    var near=Math.hypot(g.x-ccx,g.z-ccz)<=step*1.01+0.01,id=cx+','+cz;
    if(near&&g.last!==id){g.last=id;
      var opts=[[1,0],[-1,0],[0,1],[0,-1]].filter(function(v){return walk(cx+v[0],cz+v[1])});
      var fwd=opts.filter(function(v){return !(v[0]===-g.dx&&v[1]===-g.dz)});if(fwd.length)opts=fwd;
      var keep=opts.some(function(v){return v[0]===g.dx&&v[1]===g.dz});
      if(!keep||Math.random()<0.35){var v=opts[Math.floor(Math.random()*opts.length)];if(v){g.x=ccx;g.z=ccz;g.dx=v[0];g.dz=v[1]}}}
    g.x+=g.dx*step;g.z+=g.dz*step;
    if(p.inv<=S.t&&h<0.8&&Math.hypot(g.x-p.x,g.z-p.z)<1.3){p.inv=S.t+1500;S.time=Math.max(1,S.time-5);ev('On Trigger Enter (Zorro ∩ Granjera)');ac('Temporizador − 5 s');flash('¡Un zorro! −5 s',1000);
      var a=Math.atan2(p.x-g.x,p.z-g.z),kx=p.x+Math.sin(a)*1.6,kz=p.z+Math.cos(a)*1.6;if(canMove(kx,p.z,0.4,0))p.x=kx;if(canMove(p.x,kz,0.4,0))p.z=kz}});
}
function render(dt){
  var p=S.p,t=S.t/1000,h=p.air>0?Math.sin(Math.PI*(1-p.air/0.75))*1.8:0;
  farmer.position.set(p.x,h+Math.abs(Math.sin(p.bob))*0.1,p.z);farmer.rotation.y=p.ry;farmer.visible=!(p.inv>S.t&&Math.floor(S.t/90)%2);
  S.hens.forEach(function(g){if(!g.got)g.mesh.position.y=Math.abs(Math.sin(t*4+g.ph))*0.12});
  S.foxes.forEach(function(g){g.mesh.position.set(g.x,Math.abs(Math.sin(t*9))*0.08,g.z);g.mesh.rotation.y=Math.atan2(g.dx,g.dz)});
  if(!S.L.night){var k=Math.max(0,1-S.time/S.L.time);k=k*k;var c1=new THREE.Color('#A5DBFF'),c2=new THREE.Color('#F7A66B');c1.lerp(c2,k);scene.background.copy(c1);scene.fog.color.copy(c1);amb.intensity=0.85-0.3*k}
  S.camx+=(p.x-S.camx)*Math.min(1,6*dt);S.camz+=(p.z-S.camz)*Math.min(1,6*dt);
  cam.position.set(S.camx,22,S.camz+9);cam.lookAt(S.camx,0.4,S.camz-0.8);
}
'''
build('granja3d.html','La Granja Perdida','SALTAR<br>(Espacio)','Flechas o WASD para moverte · Espacio: saltar las vallas. Encuentra todas las gallinas antes de que anochezca. Los zorros te restan 5 segundos.','#A5DBFF',G)
