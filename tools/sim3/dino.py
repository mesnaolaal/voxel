from common import build
G=r'''
var TITLE='DINO PARQUE';
var LV=[
 {name:'Un claro de selva con un T-Rex dormido',kind:'jungle',need:2,sleep:true,rows:[
  '.............',
  '.D...P.......',
  '.............',
  '..H......P...',
  '.............',
  '.....T.......',
  '.P.........H.',
  '.............',
  '............N']},
 {name:'Un pantano de barro con un T-Rex que patrulla',kind:'swamp',need:3,sleep:false,rows:[
  '...............',
  '.D..BBB....P...',
  '....BBB..H.....',
  '.P..BBB........',
  '.......T..BBB..',
  '..H........BBB.',
  '...P....P..BBB.',
  '.......H.......',
  '..............N']},
 {name:'Un volcán con lava y dos T-Rex',kind:'volcano',need:3,sleep:false,rows:[
  '...............',
  '.D....LL.......',
  '......LL...H...',
  '.P..T...LL.....',
  '........LL.P...',
  '..H.......T....',
  '..LL....P......',
  '..LL.......H...',
  '..............N']}];
function ch(x,z){return cellCh(Math.round(x/C),Math.round(z/C))}
function solidAt(x,z){var c=ch(x,z);return c===undefined||c==='P'}
function canMove(x,z,r){return !solidAt(x-r,z-r)&&!solidAt(x+r,z-r)&&!solidAt(x-r,z+r)&&!solidAt(x+r,z+r)}
function walk(cx,cz){var c=cellCh(cx,cz);return c!==undefined&&c!=='P'&&c!=='L'}
var dino=new THREE.Group(),legL,legR;
(function(){var g=dino,c='#22C55E';
  bx(1.3,1.1,2.0,c,0,1.3,0,g);bx(0.9,0.9,0.9,c,0,1.9,1.1,g);bx(0.7,0.5,0.6,'#4ADE80',0,1.75,1.7,g);bx(0.2,0.2,0.1,'#FFFFFF',0.3,2.2,1.55,g);bx(0.1,0.1,0.1,'#111827',0.33,2.2,1.6,g);bx(0.2,0.2,0.1,'#FFFFFF',-0.3,2.2,1.55,g);bx(0.1,0.1,0.1,'#111827',-0.33,2.2,1.6,g);
  bx(0.9,0.7,1.2,'#16A34A',0,1.1,-1.4,g);bx(0.5,0.4,1.0,'#16A34A',0,1.0,-2.2,g);[-0.3,0,0.3].forEach(function(z){bx(0.15,0.3,0.4,'#BBF7D0',0,1.95,z-0.2,g)});
  legL=new THREE.Group();legL.position.set(-0.4,0.9,0);bx(0.4,0.9,0.5,'#15803D',0,-0.4,0,legL);g.add(legL);legR=new THREE.Group();legR.position.set(0.4,0.9,0);bx(0.4,0.9,0.5,'#15803D',0,-0.4,0,legR);g.add(legR)})();
function makeRex(){var g=new THREE.Group(),c='#B45309';bx(2.0,1.8,3.0,c,0,2.2,0,g);bx(1.5,1.3,1.6,c,0,3.4,1.9,g);bx(1.3,0.5,1.0,'#92400E',0,2.9,2.8,g);bx(1.3,0.35,0.9,'#FFFFFF',0,2.65,2.8,g);
  bx(0.3,0.3,0.1,'#FACC15',0.6,3.8,2.7,g);bx(0.3,0.3,0.1,'#FACC15',-0.6,3.8,2.7,g);bx(0.12,0.12,0.1,'#111827',0.6,3.8,2.75,g);bx(0.12,0.12,0.1,'#111827',-0.6,3.8,2.75,g);
  bx(0.4,0.6,0.4,c,-1.1,2.4,1.2,g);bx(0.4,0.6,0.4,c,1.1,2.4,1.2,g);bx(1.4,1.1,1.8,'#92400E',0,2.0,-2.0,g);bx(0.8,0.7,1.6,'#92400E',0,1.9,-3.5,g);
  bx(0.7,1.8,0.9,'#7C2D12',-0.8,0.9,0,g);bx(0.7,1.8,0.9,'#7C2D12',0.8,0.9,0,g);bx(0.9,0.3,1.2,'#7C2D12',-0.8,0.15,0.3,g);bx(0.9,0.3,1.2,'#7C2D12',0.8,0.15,0.3,g);
  [-1,0.2,1.4].forEach(function(z){bx(0.2,0.5,0.5,'#F59E0B',0,3.2+(z>0?0:0.0),z-1.3,g)});return g}
function makeEgg(){var g=new THREE.Group(),m=emi('#FDE68A','#D97706');bx(0.8,0.5,0.8,m,0,0.25,0,g);bx(1.0,0.7,1.0,m,0,0.85,0,g);bx(0.7,0.5,0.7,m,0,1.4,0,g);bx(0.2,0.2,0.1,'#92400E',0.3,0.9,0.52,g);bx(0.2,0.2,0.1,'#92400E',-0.2,1.1,0.52,g);return g}
function makePalm(r){var g=new THREE.Group();bx(0.55,2.6,0.55,'#92400E',0,1.3,0,g);bx(0.5,1.4,0.5,'#92400E',0.2,3.2,0,g);
  [[2,0],[-2,0],[0,2],[0,-2],[1.4,1.4],[-1.4,-1.4]].forEach(function(o){var l=bx(o[0]&&!o[1]?2.2:0.6,0.2,o[1]&&!o[0]?2.2:0.6,'#16A34A',o[0]*0.5+0.2,4.0,o[1]*0.5,g);if(o[0]&&o[1]){l.scale.set(2,1,2)}});bx(0.7,0.6,0.7,'#22C55E',0.2,4.1,0,g);return g}
function makeNest(){var g=new THREE.Group();bx(3.0,0.3,3.0,'#92400E',0,0.15,0,g);bx(3.4,0.5,0.6,'#B45309',0,0.4,1.4,g);bx(3.4,0.5,0.6,'#B45309',0,0.4,-1.4,g);bx(0.6,0.5,2.4,'#B45309',1.4,0.4,0,g);bx(0.6,0.5,2.4,'#B45309',-1.4,0.4,0,g);bx(2.0,0.1,2.0,'#FDE68A',0,0.35,0,g);return g}
var grass=null;
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var rows=L.rows,nz=rows.length,nx=rows[0].length,r=rng(83+n*5);
  var vol=L.kind==='volcano',sw=L.kind==='swamp';
  scene.background.set(vol?'#3B1D1D':(sw?'#9DB88A':'#BFE6FF'));scene.fog.color.set(vol?'#3B1D1D':(sw?'#9DB88A':'#D4EEFF'));scene.fog.near=70;scene.fog.far=160;
  amb.intensity=vol?0.65:0.85;sun.intensity=vol?0.55:0.7;
  var g1=vol?'#7A6A5C':(sw?'#6EA85A':'#6BCB4F'),g2=vol?'#6F5F52':(sw?'#63994F':'#62BE48'),gt=checker(g1,g2,1,1),gm=[mat('#6B4423'),mat('#6B4423'),new THREE.MeshLambertMaterial({map:gt}),mat('#6B4423'),mat('#6B4423'),mat('#6B4423')];
  S.eggs=[];S.rex=[];S.palms=[];S.nest=null;S.mud=[];S.lava=[];S.ne=0;S.got=0;
  var out=new THREE.Mesh(new THREE.PlaneGeometry(220,220),new THREE.MeshLambertMaterial({color:vol?'#4A3A30':(sw?'#52803F':'#4FA43A')}));out.rotation.x=-Math.PI/2;out.position.set((nx-1)*C/2,-0.95,(nz-1)*C/2);lvGroup.add(out);
  for(var z=0;z<nz;z++)for(var x=0;x<nx;x++){var c=rows[z][x],wx=x*C,wz=z*C;
    if(c==='L'){bx(C,0.3,C,emi('#F97316','#EA580C'),wx,-0.3,wz,lvGroup);var lp=new THREE.PointLight(0xff7a30,0.6,9);lp.position.set(wx,1.2,wz);if((x+z)%2===0)lvGroup.add(lp);S.lava.push({x:wx,z:wz})}
    else{var m=new THREE.Mesh(new THREE.BoxGeometry(C,0.9,C),gm);m.position.set(wx,-0.45,wz);lvGroup.add(m);
      if(c==='B'){bx(C*0.96,0.08,C*0.96,'#6B4A2B',wx,0.03,wz,lvGroup);bx(0.7,0.04,0.7,'#8B6A45',wx+0.4,0.07,wz-0.3,lvGroup);S.mud.push({x:wx,z:wz})}}
    if(c==='D'){S.start={x:wx,z:wz}}
    else if(c==='H'){var e=makeEgg();e.position.set(wx,0,wz);lvGroup.add(e);S.eggs.push({x:wx,z:wz,mesh:e,got:false,ph:r()*6});S.ne++}
    else if(c==='T'){var rx=makeRex();rx.position.set(wx,0,wz);lvGroup.add(rx);S.rex.push({x:wx,z:wz,mesh:rx,dx:1,dz:0,last:'',state:L.sleep?'sleep':'patrol',stun:0,ry:0,ph:r()*6,hx:wx,hz:wz})}
    else if(c==='P'){var pm=makePalm(r);pm.position.set(wx,0,wz);pm.rotation.y=r()*6;lvGroup.add(pm);S.palms.push({x:wx,z:wz})}
    else if(c==='N'){var nt=makeNest();nt.position.set(wx,0,wz);lvGroup.add(nt);S.nest={x:wx,z:wz}}
    else if(c==='.'&&r()<0.14){bx(0.5,0.5,0.5,vol?'#57534E':'#22C55E',wx+(r()-0.5)*1.3,0.25,wz+(r()-0.5)*1.3,lvGroup)}}
  scene.add(dino);
  S.p={x:S.start.x,z:S.start.z,ry:0,inv:0,bob:0,run:0,rcd:0,kx:0,kz:0,hid:false};S.lives=3;S.warn=0;S.camx=(nx-1)*C/2;S.camz=(nz-1)*C/2;S.zoomY=Math.max(nx*1.75,nz*2.6)+4;
}
function hud(){var h='';for(var i=0;i<3;i++)h+=i<(S.lives||0)?'♥':'♡';var p=S.p;
  setHud('Nivel '+(S.lv+1)+'/3 · '+h,'Huevos '+(S.got||0)+'/'+(S.L?S.L.need:0),(p&&p.hid)?'Escondido':'A la vista',(p&&p.run>0)?'¡Corriendo!':(p&&p.rcd>0?'Correr '+Math.ceil(p.rcd)+' s':'Correr listo'))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,lives:3,got:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: vidas = 3, huevos = 0');buildLevel(0);showOv('DINO PARQUE','Pulsa Espacio o toca para empezar','Flechas: mover · Mayús: correr')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Dino, '+S.ne+' huevo(s), '+S.rex.length+' T-Rex y Nido')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡HUEVOS A SALVO!','El dino llevó todos los huevos al nido','Pulsa Espacio para repetir')}}
function over(){S.mode='over';showOv('¡ATRAPADO!','El T-Rex te atrapó 3 veces','Pulsa Espacio para reintentar este nivel')}
function onSpace(){var p=S.p;if(p.rcd>0||p.run>0)return;p.run=1.5;p.rcd=4.5;ev('Input: tecla Espacio / Mayús');co('¿Energía cargada? SÍ');ac('Correr: velocidad × 1,6 durante 1,5 s')}
function hurt(why,fx,fz,toStart){var p=S.p;if(p.inv>S.t)return;S.lives--;p.inv=S.t+2200;ev('On Trigger Enter ('+why+' ∩ Dino)');ac('vidas = vidas − 1 → '+S.lives);flash(why==='Lava'?'¡Lava! Vuelves al inicio':'¡El T-Rex te ha tocado!',1200);
  if(toStart){p.x=S.start.x;p.z=S.start.z}else{var a=Math.atan2(p.x-fx,p.z-fz);p.kx=Math.sin(a)*12;p.kz=Math.cos(a)*12}
  if(S.lives<=0){ac('Load Scene "GameOver"');over()}}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p,L=S.L;if(held.shift&&p.rcd<=0&&p.run<=0)onSpace();
  p.run=Math.max(0,p.run-dt);if(p.run<=0)p.rcd=Math.max(0,p.rcd-dt);
  var dx=(held.right?1:0)-(held.left?1:0),dz=(held.down?1:0)-(held.up?1:0),m=Math.hypot(dx,dz);if(m>0){dx/=m;dz/=m}
  var inMud=ch(p.x,p.z)==='B',spd=(p.run>0?8.2:5.2)*(inMud?0.55:1);
  p.kx*=Math.max(0,1-6*dt);p.kz*=Math.max(0,1-6*dt);
  var nx=p.x+(dx*spd+p.kx)*dt,nz=p.z+(dz*spd+p.kz)*dt;if(canMove(nx,p.z,0.45))p.x=nx;if(canMove(p.x,nz,0.45))p.z=nz;
  if(m>0){var ty=Math.atan2(dx,dz),df=ty-p.ry;while(df>Math.PI)df-=6.283;while(df<-Math.PI)df+=6.283;p.ry+=df*Math.min(1,14*dt);p.bob+=dt*(p.run>0?16:11)}
  p.hid=S.palms.some(function(q){return Math.hypot(q.x-p.x,q.z-p.z)<2.7});
  if(ch(p.x,p.z)==='L')hurt('Lava',0,0,true);
  S.eggs.forEach(function(e){if(!e.got&&Math.hypot(e.x-p.x,e.z-p.z)<1.4){e.got=true;e.mesh.visible=false;S.got++;ev('On Trigger Enter (Dino ∩ Huevo)');ac('Destroy(Huevo), huevos = '+S.got+'/'+L.need)}});
  S.rex.forEach(function(g){
    var d=Math.hypot(g.x-p.x,g.z-p.z);g.stun=Math.max(0,g.stun-dt);g.calm=Math.max(0,(g.calm||0)-dt);
    if(g.state==='sleep'){if(d<5&&p.run>0)g.state='chase'}
    else{var sees=d<7&&!p.hid&&g.calm<=0;g.alert=sees?(g.alert||0)+dt:0;if(g.alert>0.45&&g.state!=='chase'){g.state='chase';ev('T-Rex ve al dino');ac('Estado del T-Rex = persecución')}
      else if(g.state==='chase'&&(!sees||d>11)){g.state='patrol';g.alert=0;g.x=Math.round(g.x/C)*C;g.z=Math.round(g.z/C)*C;g.last='';var cc=Math.round(g.x/C),cz=Math.round(g.z/C);if(!walk(cc,cz)){g.x=g.hx;g.z=g.hz}}}
    if(g.stun>0||g.state==='sleep')return;
    if(g.state==='chase'){var a=Math.atan2(p.x-g.x,p.z-g.z),sp=3.7*dt,nx2=g.x+Math.sin(a)*sp,nz2=g.z+Math.cos(a)*sp;
      function okR(x,z){return walk(Math.round((x-0.7)/C),Math.round((z-0.7)/C))||false}
      function cellOk(x,z){var c=ch(x,z);return c!==undefined&&c!=='P'&&c!=='L'}
      if(cellOk(nx2,g.z))g.x=nx2;if(cellOk(g.x,nz2))g.z=nz2;g.dx=Math.sin(a);g.dz=Math.cos(a)}
    else{var cx=Math.round(g.x/C),cz=Math.round(g.z/C),ccx=cx*C,ccz=cz*C,step=2.2*dt,near=Math.hypot(g.x-ccx,g.z-ccz)<=step*1.01+0.01,id=cx+','+cz;
      if(near&&g.last!==id){g.last=id;var opts=[[1,0],[-1,0],[0,1],[0,-1]].filter(function(v){return walk(cx+v[0],cz+v[1])});
        var fwd=opts.filter(function(v){return !(v[0]===-Math.round(g.dx)&&v[1]===-Math.round(g.dz))});if(fwd.length)opts=fwd;
        var keep=opts.some(function(v){return v[0]===Math.round(g.dx)&&v[1]===Math.round(g.dz)});
        if(!keep||Math.random()<0.4){var v=opts[Math.floor(Math.random()*opts.length)];if(v){g.x=ccx;g.z=ccz;g.dx=v[0];g.dz=v[1]}}}
      g.x+=Math.round(g.dx)*step;g.z+=Math.round(g.dz)*step}
    if(Math.hypot(g.x-p.x,g.z-p.z)<2.1){hurt('T-Rex',g.x,g.z,false);g.stun=1.8;g.calm=4;g.state='patrol';g.alert=0}});
  if(S.mode!=='play')return;
  if(Math.hypot(S.nest.x-p.x,S.nest.z-p.z)<2.2){
    if(S.got>=L.need){ev('On Trigger Enter (Dino ∩ Nido)');co('¿Tiene todos los huevos? SÍ');ac('Cargar el siguiente nivel');toNext()}
    else if(S.t>S.warn){S.warn=S.t+2500;ev('On Trigger Enter (Dino ∩ Nido)');co('¿Tiene todos los huevos? NO ('+S.got+'/'+L.need+')');flash('Faltan huevos: '+S.got+'/'+L.need,1500)}}
}
function render(dt){
  var p=S.p,t=S.t/1000;
  dino.position.set(p.x,Math.abs(Math.sin(p.bob))*0.12,p.z);dino.rotation.y=p.ry;dino.visible=!(p.inv>S.t&&Math.floor(S.t/90)%2);legL.rotation.x=Math.sin(p.bob)*0.7;legR.rotation.x=-Math.sin(p.bob)*0.7;
  S.eggs.forEach(function(e){if(!e.got){e.mesh.rotation.y=t*1.5;e.mesh.position.y=Math.sin(t*3+e.ph)*0.12}});
  S.rex.forEach(function(g){var ty=Math.atan2(g.dx,g.dz);var df=ty-g.ry;while(df>Math.PI)df-=6.283;while(df<-Math.PI)df+=6.283;g.ry+=df*Math.min(1,8*dt);g.mesh.position.set(g.x,g.state==='sleep'?0:Math.abs(Math.sin(t*5+g.ph))*0.15,g.z);g.mesh.rotation.y=g.ry;g.mesh.rotation.z=g.state==='sleep'?0.05*Math.sin(t*1.5):0});
  var nx=S.L.rows[0].length,nz=S.L.rows.length,cx=(nx-1)*C/2,cz=(nz-1)*C/2;
  S.camx+=(cx-S.camx)*Math.min(1,6*dt);S.camz+=(cz-S.camz)*Math.min(1,6*dt);
  cam.position.set(S.camx,S.zoomY,S.camz+S.zoomY*0.42);cam.lookAt(S.camx,0.4,S.camz+0.2);
}
'''
build('dino3d.html','Dino Parque','CORRER<br>(Espacio)','Flechas o WASD para moverte · Mayús o Espacio: correr un momento. Recoge los huevos y llévalos al nido. El T-Rex te atrapa si te ve: escóndete cerca de las palmeras. Evita la lava. Tienes 3 vidas.','#BFE6FF',G)
