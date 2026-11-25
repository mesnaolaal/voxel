from common import build
G=r'''
var TITLE='EL PEZ HAMBRIENTO';
var LV=[
 {name:'Un arrecife tranquilo con una medusa',W:70,H:26,plank:8,jel:1,shark:0,alg:7,dark:false,seed:3},
 {name:'Un bosque de algas con dos medusas',W:80,H:28,plank:10,jel:2,shark:0,alg:26,dark:false,seed:8},
 {name:'Una cueva oscura con un tiburón',W:80,H:26,plank:8,jel:0,shark:1,alg:9,dark:true,seed:13}];
var fish=new THREE.Group(),glow=new THREE.PointLight(0xbfe6ff,0,32),sandTex=checker('#E8D08B','#DFC57C',1,1),fl=null;
(function(){var g=fish;
  bx(2.4,1.5,0.9,'#F97316',0,0,0,g);bx(1.2,1.1,0.8,'#FB923C',1.1,0.1,0,g);bx(0.9,0.5,0.9,'#FFFFFF',0.1,0.15,0,g);bx(0.9,0.5,0.9,'#FFFFFF',-0.7,0.15,0,g);
  var tl=bx(0.4,1.6,0.3,'#EA580C',-1.5,0,0,g);bx(0.8,0.4,0.15,'#EA580C',0,1.0,0,g);bx(0.5,0.35,0.15,'#FDBA74',0.1,-0.9,0.4,g);
  bx(0.35,0.35,0.1,'#FFFFFF',1.0,0.35,0.48,g);bx(0.18,0.18,0.1,'#111827',1.08,0.35,0.52,g);bx(0.35,0.35,0.1,'#FFFFFF',1.0,0.35,-0.48,g);bx(0.18,0.18,0.1,'#111827',1.08,0.35,-0.52,g);
  g.userData.tail=tl;glow.position.set(1,1,2);g.add(glow)})();
function makePlank(){var g=new THREE.Group(),m=emi('#86EFAC','#22C55E');bx(0.5,0.5,0.5,m,0,0,0,g);bx(0.3,0.3,0.3,m,0.5,0.4,0.2,g);bx(0.3,0.3,0.3,m,-0.4,-0.3,-0.2,g);return g}
function makeJelly(){var g=new THREE.Group(),m=emi('#F472B6','#BE185D');bx(2.8,0.7,2.8,m,0,1.6,0,g);bx(2.2,0.7,2.2,m,0,2.2,0,g);bx(1.4,0.5,1.4,m,0,2.7,0,g);
  [[-0.9,-0.9],[0.9,-0.9],[-0.9,0.9],[0.9,0.9],[0,0]].forEach(function(o,i){var t=bx(0.22,2.2,0.22,'#F9A8D4',o[0],0.4,o[1],g);t.userData.i=i});return g}
function makeShark(){var g=new THREE.Group(),m='#64748B';bx(5.4,1.9,1.9,m,0,0,0,g);bx(1.8,1.6,1.7,m,3.0,-0.1,0,g);bx(0.8,0.5,1.6,'#E5E7EB',3.5,-0.55,0,g);bx(5.0,0.6,1.6,'#E5E7EB',-0.2,-0.7,0,g);
  bx(0.4,1.6,0.9,m,0.4,1.7,0,g);bx(0.6,2.4,0.4,m,-3.1,0.4,0,g);bx(0.5,1.6,0.4,m,-3.4,-0.9,0,g);bx(0.3,0.3,0.1,'#111827',3.3,0.4,0.9,g);bx(0.3,0.3,0.1,'#111827',3.3,0.4,-0.9,g);
  for(var i=0;i<4;i++){bx(0.18,0.35,0.1,'#FFFFFF',3.55+(i%2)*0.1,-0.2,-0.6+i*0.4,g)}return g}
function makeAlga(r,h){var g=new THREE.Group();for(var i=0;i<6;i++){var s=bx(0.45,h/6,0.45,i%2?'#16A34A':'#22C55E',0,h/12+i*h/6,0,g);s.userData.i=i}return g}
function makeCoral(r){var g=new THREE.Group(),c=['#F43F5E','#FB7185','#F59E0B','#A855F7'][Math.floor(r()*4)];bx(1.4,1.2,1.4,c,0,0.6,0,g);bx(0.6,1.8,0.6,c,0.5,1.5,0,g);bx(0.6,1.4,0.6,c,-0.5,1.3,0.2,g);bx(0.5,0.5,0.5,'#FDE68A',0.5,2.5,0,g);return g}
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var r=rng(L.seed*17+3),i,W=L.W,H=L.H;
  scene.background.set(L.dark?'#02060F':'#1F7FB8');scene.fog.color.set(L.dark?'#02060F':'#2A8FC8');scene.fog.near=L.dark?14:50;scene.fog.far=L.dark?55:130;
  amb.intensity=L.dark?0.22:0.8;sun.intensity=L.dark?0.05:0.6;glow.intensity=L.dark?2.2:0;
  var fl2=new THREE.Mesh(new THREE.BoxGeometry(W+60,1,60),new THREE.MeshLambertMaterial({map:sandTex}));sandTex.repeat.set((W+60)/2,30);fl2.position.set(W/2,-0.5,-10);lvGroup.add(fl2);
  var bk=bx(W+80,H+14,1,L.dark?'#04101F':'#1C6FA5',W/2,H/2+2,-24,lvGroup);
  S.alg=[];S.coral=[];S.pl=[];S.jel=[];S.sh=null;
  for(i=0;i<L.alg;i++){var h=5+r()*(L.dark?4:6),a=makeAlga(r,h),ax=10+r()*(W-24),az=(r()-0.5)*4;if(n===1&&i<18){az=(r()-0.5)*1.4}a.position.set(ax,0,az);lvGroup.add(a);S.alg.push({x:ax,h:h,mesh:a,ph:r()*6})}
  for(i=0;i<22;i++){var c=makeCoral(r),cz=-3-r()*14;c.position.set(r()*W,0,cz);c.rotation.y=r()*6;c.scale.setScalar(1+r()*1.4);lvGroup.add(c)}
  for(i=0;i<L.plank;i++){var pk=makePlank(),px,py,t=0;do{px=10+(i+0.2+r()*0.6)*((W-24)/L.plank);py=3+r()*(H-7);t++}while(S.jel.length&&false);pk.position.set(px,py,0);lvGroup.add(pk);S.pl.push({x:px,y:py,mesh:pk,got:false,ph:r()*6})}
  for(i=0;i<L.jel;i++){var j=makeJelly(),jx=W*(0.3+0.4*(i+0.5)/Math.max(1,L.jel))+(r()-0.5)*6,jy=H*0.5;j.position.set(jx,jy,0);lvGroup.add(j);S.jel.push({bx:jx,by:jy,x:jx,y:jy,mesh:j,ph:r()*6,sx:0.55+r()*0.3,sy:0.8+r()*0.3})}
  if(L.shark){var sk=makeShark();sk.position.set(W*0.5,H*0.5,0);lvGroup.add(sk);S.sh={x:W*0.5,y:H*0.5,dir:-1,mesh:sk,vx:0,vy:0}}
  // cueva
  var cv=new THREE.Group();bx(3,12,12,'#57534E',-2,6,0,cv);bx(8,3,12,'#78716C',2,12,0,cv);bx(8,2,12,'#57534E',2,1,-5,cv);bx(8,10,2,'#44403C',2,6,-6,cv);S.cvGlow=bx(0.4,8,6,basic('#FDE68A'),2,5,0,cv);S.cvGlow.visible=false;cv.position.set(W+1,0,0);lvGroup.add(cv);
  scene.add(fish);
  S.p={x:4,y:H/2,vx:0,vy:0,dir:1,inv:0,spr:0,scd:0,hid:false,kx:0,ky:0};S.lives=3;S.eat=0;S.camx=4;S.camy=H/2;S.warn=0;S.shake=0;
}
function hud(){var h='';for(var i=0;i<3;i++)h+=i<(S.lives||0)?'♥':'♡';var p=S.p;
  setHud('Nivel '+(S.lv+1)+'/3 · '+h,'Plancton '+(S.eat||0)+'/'+(S.L?S.L.plank:0),(p&&p.hid)?'Escondido':'A la vista',(p&&p.spr>0)?'¡Esprint!':(p&&p.scd>0?'Aleta recargando':'Aleta lista'))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,lives:3,eat:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: vidas = 3, plancton = 0');buildLevel(0);showOv('EL PEZ HAMBRIENTO','Pulsa Espacio o toca para empezar')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Pez, '+S.L.plank+' plancton'+(S.jel.length?', '+S.jel.length+' medusa(s)':'')+(S.sh?', 1 tiburón':'')+' y Cueva')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡EL PEZ ESTÁ A SALVO!','Has llegado a la cueva en los 3 niveles','Pulsa Espacio para repetir')}}
function over(){S.mode='over';showOv('¡SIN VIDAS!','Un enemigo te atrapó','Pulsa Espacio para reintentar este nivel')}
function onSpace(){var p=S.p;if(p.scd>0||p.spr>0)return;p.spr=1.0;p.scd=3.5;ev('Input: tecla Espacio');co('¿Aleta cargada? SÍ');ac('Esprintar: velocidad × 1,8 durante 1 s')}
function hurt(who,fx,fy){var p=S.p;if(p.inv>S.t||p.hid)return;S.lives--;p.inv=S.t+1800;S.shake=0.4;var a=Math.atan2(p.y-fy,p.x-fx);p.kx=Math.cos(a)*14;p.ky=Math.sin(a)*14;
  ev('On Trigger Enter ('+who+' ∩ Pez)');ac('vidas = vidas − 1 → '+S.lives);if(S.lives<=0){ac('Load Scene "GameOver"');over()}}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p,L=S.L;p.spr=Math.max(0,p.spr-dt);if(p.spr<=0)p.scd=Math.max(0,p.scd-dt);S.shake=Math.max(0,S.shake-dt);
  var dx=(held.right?1:0)-(held.left?1:0),dy=(held.up?1:0)-(held.down?1:0),m=Math.hypot(dx,dy);if(m>0){dx/=m;dy/=m}
  var sp=(p.spr>0?17:9.5);
  p.vx+=(dx*sp-p.vx)*Math.min(1,6*dt);p.vy+=(dy*sp-p.vy)*Math.min(1,6*dt);
  p.kx*=Math.max(0,1-5*dt);p.ky*=Math.max(0,1-5*dt);
  p.x=Math.max(1.5,Math.min(L.W+4,p.x+(p.vx+p.kx)*dt));p.y=Math.max(1.4,Math.min(L.H-1.4,p.y+(p.vy+p.ky)*dt));
  if(p.x>L.W-1.5&&S.eat<L.plank)p.x=L.W-1.5;
  if(Math.abs(dx)>0.1)p.dir=dx>0?1:-1;
  p.hid=S.alg.some(function(a){return Math.abs(a.x-p.x)<1.6&&p.y<a.h-0.5});
  S.pl.forEach(function(k){if(!k.got&&Math.hypot(k.x-p.x,k.y-p.y)<1.7){k.got=true;k.mesh.visible=false;S.eat++;ev('On Trigger Enter (Pez ∩ Plancton)');ac('Destroy(Plancton), plancton = '+S.eat+'/'+L.plank)}});
  S.jel.forEach(function(j){j.x=j.bx+4*Math.sin(S.t/1000*j.sx+j.ph);j.y=j.by+5.5*Math.sin(S.t/1000*j.sy+j.ph*2);if(Math.hypot(j.x-p.x,(j.y+1.6)-p.y)<2.3)hurt('Medusa',j.x,j.y)});
  if(S.mode!=='play')return;
  var sh=S.sh;if(sh){var dist=Math.hypot(sh.x-p.x,sh.y-p.y),chase=dist<24&&!p.hid;
    var tvx,tvy;if(chase){var a=Math.atan2(p.y-sh.y,p.x-sh.x);tvx=Math.cos(a)*9.2;tvy=Math.sin(a)*9.2}else{if(sh.x<14)sh.dir=1;if(sh.x>L.W-14)sh.dir=-1;tvx=sh.dir*8;tvy=Math.sin(S.t/1000*0.9)*5-(sh.y-L.H*0.5)*0.6}
    sh.vx+=(tvx-sh.vx)*Math.min(1,2.5*dt);sh.vy+=(tvy-sh.vy)*Math.min(1,2.5*dt);sh.x+=sh.vx*dt;sh.y=Math.max(2,Math.min(L.H-2,sh.y+sh.vy*dt));
    if(Math.abs(sh.x-p.x)<3.4&&Math.abs(sh.y-p.y)<1.6)hurt('Tiburón',sh.x,sh.y)}
  if(S.mode!=='play')return;
  if(p.x>L.W-3&&p.y<11){if(S.eat>=L.plank){ev('On Trigger Enter (Pez ∩ Cueva)');co('¿Tiene todo el plancton? SÍ');ac('Abrir la cueva y cargar el siguiente nivel');toNext()}
    else if(S.t>S.warn){S.warn=S.t+2500;ev('On Trigger Enter (Pez ∩ Cueva)');co('¿Tiene todo el plancton? NO ('+S.eat+'/'+L.plank+')');ac('La cueva sigue cerrada');flash('Falta plancton: '+S.eat+'/'+L.plank,1600)}}
}
function render(dt){
  var p=S.p,t=S.t/1000,L=S.L;
  fish.position.set(p.x,p.y+Math.sin(t*5)*0.1,0);fish.rotation.y=p.dir>0?0:Math.PI;fish.rotation.z=Math.max(-0.5,Math.min(0.5,p.vy*0.04))*p.dir;fish.userData.tail.rotation.y=Math.sin(t*(p.spr>0?30:14))*0.6;fish.visible=!(p.inv>S.t&&Math.floor(S.t/90)%2);
  S.pl.forEach(function(k){if(!k.got){k.mesh.rotation.y=t*2;k.mesh.position.y=k.y+Math.sin(t*2+k.ph)*0.3}});
  S.jel.forEach(function(j){j.mesh.position.set(j.x,j.y,0);j.mesh.children.forEach(function(c){if(c.userData.i!==undefined)c.rotation.z=Math.sin(t*4+c.userData.i)*0.3})});
  if(S.sh){S.sh.mesh.position.set(S.sh.x,S.sh.y,0);S.sh.mesh.rotation.y=S.sh.vx>=0?0:Math.PI;S.sh.mesh.rotation.z=Math.max(-0.4,Math.min(0.4,S.sh.vy*0.05))*(S.sh.vx>=0?1:-1)}
  S.alg.forEach(function(a){a.mesh.children.forEach(function(c,i){c.position.x=Math.sin(t*1.5+a.ph+i*0.5)*0.1*i})});
  S.cvGlow.visible=S.eat>=L.plank;
  S.camx+=(p.x-S.camx)*Math.min(1,4*dt);S.camy+=(p.y-S.camy)*Math.min(1,4*dt);
  var cxm=Math.max(14,Math.min(L.W-14,S.camx)),sh=S.shake*0.5;
  cam.position.set(cxm+(Math.random()-0.5)*sh,S.camy*0.55+5,32);cam.lookAt(cxm,S.camy*0.75+2,0);
}
'''
build('pez3d.html','El Pez Hambriento','ESPRINTAR<br>(Espacio)','Flechas o WASD para nadar · Espacio: esprintar con la aleta. Come todo el plancton y entra en la cueva. Las medusas y el tiburón te quitan una vida (tienes 3); entre las algas te escondes.','#1F7FB8',G)
