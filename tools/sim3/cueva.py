from common import build
G=r'''
amb.intensity=0.5;sun.intensity=0.25;
var TITLE='LA CUEVA DEL JEFE';
var LV=[
 {name:'Una cueva con un monstruo',rows:[
  '#############',
  '#A.........A#',
  '#...........#',
  '#.H.......J.#',
  '#...........#',
  '#...........#',
  '#...........#',
  '#A#########A#']},
 {name:'Una pared en medio y dos esbirros',rows:[
  '###############',
  '#A...........A#',
  '#.H.....#.....#',
  '#.......#..m..#',
  '#...m...#.....#',
  '#.......#.....#',
  '#.............#',
  '#.............#',
  '#A###########A#']},
 {name:'El jefe final y dos esbirros',rows:[
  '###############',
  '#A...........A#',
  '#.....#...m...#',
  '#.....#.......#',
  '#.H...#...J...#',
  '#.....#.......#',
  '#.....#...m...#',
  '#.............#',
  '#A###########A#']}];
function ch(x,z){return cellCh(Math.round(x/C),Math.round(z/C))}
function solidAt(x,z){var c=ch(x,z);return c===undefined||c==='#'||c==='A'}
function canMove(x,z,r){return !solidAt(x-r,z-r)&&!solidAt(x+r,z-r)&&!solidAt(x-r,z+r)&&!solidAt(x+r,z+r)}
function walk(cx,cz){var c=cellCh(cx,cz);return c!==undefined&&c!=='#'&&c!=='A'}
var hero=new THREE.Group(),swordG,shield;
(function(){var g=hero;
  bx(0.34,0.8,0.36,'#1E3A8A',-0.22,0.4,0,g);bx(0.34,0.8,0.36,'#1E3A8A',0.22,0.4,0,g);bx(1.0,1.1,0.6,'#3B82F6',0,1.35,0,g);bx(1.02,0.2,0.62,'#92400E',0,0.95,0,g);bx(0.28,0.9,0.3,'#3B82F6',-0.65,1.3,0,g);
  bx(0.7,0.65,0.65,'#FCD9A6',0,2.3,0,g);bx(0.78,0.4,0.72,'#94A3B8',0,2.6,0,g);bx(0.14,0.5,0.1,'#EF4444',0,3.0,0,g);bx(0.12,0.12,0.06,'#111827',0.17,2.3,0.34,g);bx(0.12,0.12,0.06,'#111827',-0.17,2.3,0.34,g);
  shield=bx(0.12,0.9,0.7,'#FACC15',-0.85,1.3,0.2,g);
  swordG=new THREE.Group();swordG.position.set(0.7,1.3,0.3);bx(0.28,0.28,0.9,'#3B82F6',0,0,0,swordG);bx(0.18,0.18,1.8,'#E5E7EB',0,0,1.3,swordG);bx(0.7,0.14,0.14,'#FACC15',0,0,0.5,swordG);g.add(swordG)})();
function makeBoss(){var g=new THREE.Group(),c='#7C3AED';bx(2.8,2.4,2.4,c,0,2.2,0,g);bx(1.8,1.5,1.7,'#8B5CF6',0,4.0,0.3,g);bx(0.4,1.0,0.4,'#E5E7EB',-0.7,5.0,0.4,g);bx(0.4,1.0,0.4,'#E5E7EB',0.7,5.0,0.4,g);bx(0.4,0.4,0.15,basic('#FDE047'),-0.5,4.2,1.2,g);bx(0.4,0.4,0.15,basic('#FDE047'),0.5,4.2,1.2,g);bx(1.2,0.3,0.15,'#111827',0,3.6,1.2,g);
  bx(0.8,2.0,0.8,'#6D28D9',-1.8,2.2,0.3,g);bx(0.8,2.0,0.8,'#6D28D9',1.8,2.2,0.3,g);bx(1.0,0.8,1.0,'#4C1D95',-1.8,0.9,0.4,g);bx(1.0,0.8,1.0,'#4C1D95',1.8,0.9,0.4,g);bx(0.9,1.1,0.9,'#4C1D95',-0.8,0.5,0,g);bx(0.9,1.1,0.9,'#4C1D95',0.8,0.5,0,g);return g}
function makeMinion(){var g=new THREE.Group(),c='#16A34A';bx(1.4,1.1,1.2,c,0,1.1,0,g);bx(1.0,0.9,0.9,'#22C55E',0,2.0,0.2,g);bx(0.25,0.5,0.25,'#DCFCE7',-0.35,2.6,0.2,g);bx(0.25,0.5,0.25,'#DCFCE7',0.35,2.6,0.2,g);bx(0.25,0.25,0.1,basic('#FDE047'),-0.25,2.1,0.7,g);bx(0.25,0.25,0.1,basic('#FDE047'),0.25,2.1,0.7,g);
  bx(0.4,0.9,0.4,c,-0.5,0.4,0,g);bx(0.4,0.9,0.4,c,0.5,0.4,0,g);return g}
function makeCrystal(){var g=new THREE.Group();var m=new THREE.Mesh(new THREE.OctahedronGeometry(1.1,0),new THREE.MeshLambertMaterial({color:'#67E8F9',emissive:'#0891B2'}));m.scale.y=1.5;m.position.y=2;g.add(m);var l=new THREE.PointLight(0x67e8f9,1.4,14);l.position.y=2;g.add(l);bx(1.6,0.4,1.6,'#57534E',0,0.2,0,g);return g}
var rockTex=checker('#57534E','#4B4642',1,1);
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var rows=L.rows,nz=rows.length,nx=rows[0].length,r=rng(23+n*7);
  scene.background.set('#0B0A12');scene.fog.color.set('#0B0A12');scene.fog.near=45;scene.fog.far=95;
  S.mon=[];S.cry=null;S.torch=0;S.heroStart=null;
  var fl=new THREE.Mesh(new THREE.BoxGeometry(nx*C,0.4,nz*C),new THREE.MeshLambertMaterial({map:rockTex}));rockTex.repeat.set(nx,nz);fl.position.set((nx-1)*C/2,-0.2,(nz-1)*C/2);lvGroup.add(fl);
  for(var z=0;z<nz;z++)for(var x=0;x<nx;x++){var c=rows[z][x],wx=x*C,wz=z*C;
    if(c==='#'||c==='A'){var hh=3.2+r()*1.4;bx(C,hh,C,'#3F3A36',wx,hh/2,wz,lvGroup);bx(C*0.8,0.8,C*0.8,'#57534E',wx+(r()-0.5)*0.3,hh+0.2,wz,lvGroup)}
    if(c==='A'){var t=new THREE.Group();bx(0.3,1.6,0.3,'#78350F',0,0,0,t);bx(0.7,0.7,0.7,emi('#FB923C','#EA580C'),0,1.1,0,t);if(S.torch++%2===0){var pl=new THREE.PointLight(0xffa24d,1.2,18);pl.position.set(0,1.4,0);t.add(pl)}var side=z===0?1:-1;t.position.set(wx,2.4,wz+(z===0?C/2+0.2:(z===nz-1?-C/2-0.2:0)));if(x===0||x===nx-1)t.position.set(wx+(x===0?C/2+0.2:-C/2-0.2),2.4,wz);lvGroup.add(t)}
    if(c==='H'){S.hs={x:wx,z:wz}}
    else if(c==='J'){var j=makeBoss(),hp=n===0?3:5;j.position.set(wx,0,wz);lvGroup.add(j);S.mon.push({x:wx,z:wz,hp:hp,max:hp,mesh:j,boss:true,rad:2.0,spd:n===0?3.0:3.3,stun:0,flash:0,kx:0,kz:0,ry:0,dead:0,tx:wx,tz:wz})}
    else if(c==='m'){var m=makeMinion();m.position.set(wx,0,wz);lvGroup.add(m);S.mon.push({x:wx,z:wz,hp:2,max:2,mesh:m,boss:false,rad:1.1,spd:3.6,stun:0,flash:0,kx:0,kz:0,ry:0,dead:0,tx:wx,tz:wz})}
    else if(c==='.'&&r()<0.12){bx(0.6,0.5,0.6,'#6B635C',wx+(r()-0.5)*1.2,0.25,wz+(r()-0.5)*1.2,lvGroup)}}
  scene.add(hero);
  S.p={x:S.hs.x,z:S.hs.z,ry:0,inv:0,bob:0,sw:0,swc:0,hit:false,kx:0,kz:0,fx:0,fz:1};S.lives=3;S.camx=(nx-1)*C/2;S.camz=(nz-1)*C/2;S.zoomY=Math.max(nx*1.7,nz*2.5)+4;S.dist=null;S.dcell='';S.clear=false;
}
function hud(){var h='';for(var i=0;i<3;i++)h+=i<(S.lives||0)?'♥':'♡';var alive=S.mon?S.mon.filter(function(m){return m.hp>0}).length:0;
  setHud('Nivel '+(S.lv+1)+'/3 · '+h,'Enemigos '+alive,S.cry?'¡Coge el cristal!':'Cristal oculto',S.p&&S.p.swc>0?'Espada recargando':'Espada lista')}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,lives:3};logEl.innerHTML='';ev('Start del juego');ac('Variables: vidas = 3, nivel = 1');buildLevel(0);showOv('LA CUEVA DEL JEFE','Pulsa Espacio o toca para empezar','Flechas: mover · Espacio: atacar con la espada')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Héroe, '+S.mon.length+' monstruo(s), antorchas y Cristal (oculto)')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡CRISTAL CONSEGUIDO!','El héroe venció al jefe final','Pulsa Espacio para repetir')}}
function over(){S.mode='over';showOv('¡HÉROE DERROTADO!','Perdiste tus 3 vidas','Pulsa Espacio para reintentar este nivel')}
function onSpace(){var p=S.p;if(p.swc>0)return;p.sw=0.28;p.swc=0.5;p.hit=false;ev('Input: tecla Espacio');ac('Atacar: animación de espada (0,28 s)')}
function bfsField(cx,cz){var W=S.L.rows[0].length,Hh=S.L.rows.length,d=[],i,j;for(j=0;j<Hh;j++){d.push([]);for(i=0;i<W;i++)d[j].push(1e9)}
  var q=[[cx,cz]];d[cz][cx]=0;while(q.length){var c=q.shift();[[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){var a=c[0]+v[0],b=c[1]+v[1];if(walk(a,b)&&d[b][a]>1e8){d[b][a]=d[c[1]][c[0]]+1;q.push([a,b])}})}return d}
function los(ax,az,bx_,bz){var n=Math.ceil(Math.hypot(bx_-ax,bz-az)/0.5);for(var i=1;i<n;i++){var t=i/n;if(solidAt(ax+(bx_-ax)*t,az+(bz-az)*t))return false}return true}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p;p.swc=Math.max(0,p.swc-dt);
  var dx=(held.right?1:0)-(held.left?1:0),dz=(held.down?1:0)-(held.up?1:0),m=Math.hypot(dx,dz);
  p.kx*=Math.max(0,1-6*dt);p.kz*=Math.max(0,1-6*dt);
  if(m>0){dx/=m;dz/=m;p.fx=dx;p.fz=dz;var sp=5.6*dt;var nx=p.x+dx*sp+p.kx*dt,nz=p.z+dz*sp+p.kz*dt;if(canMove(nx,p.z,0.5))p.x=nx;if(canMove(p.x,nz,0.5))p.z=nz;p.bob+=dt*11}
  else{var nx2=p.x+p.kx*dt,nz2=p.z+p.kz*dt;if(canMove(nx2,p.z,0.5))p.x=nx2;if(canMove(p.x,nz2,0.5))p.z=nz2}
  var ty=Math.atan2(p.fx,p.fz),df=ty-p.ry;while(df>Math.PI)df-=6.283;while(df<-Math.PI)df+=6.283;p.ry+=df*Math.min(1,16*dt);
  if(p.sw>0){p.sw-=dt;if(!p.hit&&p.sw<0.2){p.hit=true;S.mon.forEach(function(g){if(g.hp<=0)return;var d=Math.hypot(g.x-p.x,g.z-p.z),reach=2.6+g.rad;if(d<reach){var a=Math.atan2(g.x-p.x,g.z-p.z),da=a-p.ry;while(da>Math.PI)da-=6.283;while(da<-Math.PI)da+=6.283;
      if(Math.abs(da)<1.25||d<g.rad+0.8){g.hp--;g.flash=0.25;g.stun=0.75;g.kx=Math.sin(a)*9;g.kz=Math.cos(a)*9;ev('On Trigger Enter (Espada ∩ '+(g.boss?'Monstruo':'Esbirro')+')');ac('vida del '+(g.boss?'monstruo':'esbirro')+' = vida − 1 → '+g.hp);
        if(g.hp<=0){g.dead=0.6;ac('Destroy('+(g.boss?'Monstruo':'Esbirro')+')')}}}})}}
  // campo de distancias hacia el héroe
  var hc=Math.round(p.x/C)+','+Math.round(p.z/C);if(hc!==S.dcell){S.dcell=hc;S.dist=bfsField(Math.round(p.x/C),Math.round(p.z/C))}
  S.mon.forEach(function(g){
    if(g.hp<=0){g.dead=Math.max(0,g.dead-dt);return}
    g.stun=Math.max(0,g.stun-dt);g.flash=Math.max(0,g.flash-dt);g.kx*=Math.max(0,1-7*dt);g.kz*=Math.max(0,1-7*dt);
    var nx=g.x+g.kx*dt,nz=g.z+g.kz*dt;if(canMove(nx,g.z,g.rad*0.6))g.x=nx;if(canMove(g.x,nz,g.rad*0.6))g.z=nz;
    if(g.stun<=0){var tx=p.x,tz=p.z;
      if(!los(g.x,g.z,p.x,p.z)){var cx=Math.round(g.x/C),cz=Math.round(g.z/C),best=null,bd=S.dist[cz]?S.dist[cz][cx]:1e9;[[1,0],[-1,0],[0,1],[0,-1]].forEach(function(v){var a=cx+v[0],b=cz+v[1];if(walk(a,b)&&S.dist[b][a]<bd){bd=S.dist[b][a];best=[a*C,b*C]}});if(best){tx=best[0];tz=best[1]}}
      var a=Math.atan2(tx-g.x,tz-g.z),sp=g.spd*dt,mr=g.rad*0.6,nx3=g.x+Math.sin(a)*sp,nz3=g.z+Math.cos(a)*sp;if(canMove(nx3,g.z,mr))g.x=nx3;if(canMove(g.x,nz3,mr))g.z=nz3;g.ry=Math.atan2(p.x-g.x,p.z-g.z)}
    if(p.inv<=S.t&&g.stun<=0&&Math.hypot(g.x-p.x,g.z-p.z)<g.rad+0.7){p.inv=S.t+1900;S.lives--;ev('On Trigger Enter ('+(g.boss?'Monstruo':'Esbirro')+' ∩ Héroe)');ac('vidas = vidas − 1 → '+S.lives);flash('¡Te han tocado! Vidas: '+S.lives,1100);var a2=Math.atan2(p.x-g.x,p.z-g.z);p.kx=Math.sin(a2)*16;p.kz=Math.cos(a2)*16;g.stun=0.5;
      if(S.lives<=0){ac('Load Scene "GameOver"');over()}}});
  if(S.mode!=='play')return;
  if(!S.cry&&S.mon.every(function(g){return g.hp<=0})){var last=S.mon[S.mon.length-1];var bs=S.mon.filter(function(g){return g.boss})[0]||last;var cr=makeCrystal();cr.position.set(bs.x,0,bs.z);lvGroup.add(cr);S.cry={x:bs.x,z:bs.z,mesh:cr};ev('Todos los monstruos derrotados');ac('Instantiate Cristal en '+(bs.boss?'el lugar del jefe':'la cueva'))}
  if(S.cry&&Math.hypot(S.cry.x-p.x,S.cry.z-p.z)<1.8){ev('On Trigger Enter (Héroe ∩ Cristal)');co('¿Están todos derrotados? SÍ');ac('Cargar el siguiente nivel');toNext()}
}
function render(dt){
  var p=S.p,t=S.t/1000;
  hero.position.set(p.x,Math.abs(Math.sin(p.bob))*0.08,p.z);hero.rotation.y=p.ry;hero.visible=!(p.inv>S.t&&Math.floor(S.t/90)%2);
  swordG.rotation.x=p.sw>0?-1.4+Math.sin((0.28-p.sw)/0.28*Math.PI)*0.2+((0.28-p.sw)/0.28)*2.2:0;swordG.rotation.y=p.sw>0?-0.6+((0.28-p.sw)/0.28)*1.2:0;
  S.mon.forEach(function(g){var s=g.hp>0?1:Math.max(0.01,g.dead/0.6);g.mesh.scale.setScalar(s);g.mesh.position.set(g.x,g.hp>0?Math.abs(Math.sin(t*(g.boss?4:8)+g.x))*0.1:0,g.z);g.mesh.rotation.y=g.ry;
    g.mesh.traverse(function(o){if(o.material&&o.material.emissive&&!o.material.isMeshBasicMaterial){}});g.mesh.visible=g.hp>0||g.dead>0;g.mesh.rotation.z=g.flash>0?Math.sin(t*60)*0.15:0});
  if(S.cry){S.cry.mesh.rotation.y=t*1.5}
  var nx=S.L.rows[0].length,nz=S.L.rows.length,cx=(nx-1)*C/2,cz=(nz-1)*C/2;
  S.camx+=(cx-S.camx)*Math.min(1,6*dt);S.camz+=(cz-S.camz)*Math.min(1,6*dt);
  cam.position.set(S.camx,S.zoomY,S.camz+S.zoomY*0.42);cam.lookAt(S.camx,0.4,S.camz+0.2);
}
'''
build('cueva3d.html','La Cueva del Jefe','ATACAR<br>(Espacio)','Flechas o WASD para moverte · Espacio: golpear con la espada hacia donde miras. Los monstruos te persiguen: derrótalos (el jefe aguanta más golpes) y coge el cristal. Tienes 3 vidas.','#0B0A12',G)
