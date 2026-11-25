from common import build
G=r'''
var TITLE='VALLAS VOXEL';
var LEN=200;
var LV=[
 {name:'Pista recta de 100 m con dos vallas y un rival',lanes:2,pl:0,hurd:[70,130],pit:null,riv:[16.0],seed:2},
 {name:'Tres calles, más vallas y dos rivales',lanes:3,pl:1,hurd:[36,66,96,126,156],pit:null,riv:[16.6,17.0],seed:5},
 {name:'Un foso de agua y barro en mitad de la pista',lanes:3,pl:1,hurd:[34,62,150,178],pit:[100,108],riv:[16.8,17.2],seed:9}];
var LW=4.4;
function laneX(i){return (i-(S.L.lanes-1)/2)*LW}
function makeRunner(shirt,short){var g=new THREE.Group(),arms=[],legs=[];
  bx(0.9,1.0,0.5,shirt,0,1.8,0,g);bx(0.9,0.5,0.52,short,0,1.2,0,g);
  var h=bx(0.6,0.6,0.6,'#FCD9A6',0,2.65,0,g);bx(0.64,0.2,0.64,'#3B2314',0,2.9,0,g);bx(0.8,0.16,0.1,'#FFFFFF',0,2.85,0.3,g);
  [-0.6,0.6].forEach(function(x){var a=new THREE.Group();a.position.set(x,2.15,0);bx(0.28,0.9,0.3,shirt,0,-0.4,0,a);bx(0.3,0.25,0.32,'#FCD9A6',0,-0.9,0,a);g.add(a);arms.push(a)});
  [-0.22,0.22].forEach(function(x){var l=new THREE.Group();l.position.set(x,1.1,0);bx(0.34,0.95,0.36,'#FCD9A6',0,-0.5,0,l);bx(0.38,0.2,0.5,'#F8FAFC',0,-1.0,0.08,l);g.add(l);legs.push(l)});
  g.userData.arms=arms;g.userData.legs=legs;return g}
function makeHurdle(){var g=new THREE.Group();bx(0.22,1.0,0.22,'#F8FAFC',-1.7,0.5,0,g);bx(0.22,1.0,0.22,'#F8FAFC',1.7,0.5,0,g);bx(3.8,0.28,0.2,'#F59E0B',0,1.0,0,g);bx(3.8,0.12,0.2,'#FFFFFF',0,0.7,0,g);bx(0.3,0.1,0.8,'#475569',-1.7,0.05,0,g);bx(0.3,0.1,0.8,'#475569',1.7,0.05,0,g);return g}
var athlete=makeRunner('#2563EB','#111827'),rivalG=[makeRunner('#DC2626','#111827'),makeRunner('#16A34A','#111827')];
var trackTex=checker('#C2410C','#B93C0B',1,1);
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var r=rng(L.seed*19+1),i,nl=L.lanes,W=nl*LW;
  scene.background.set('#9AD4F5');scene.fog.color.set('#BFE3F7');scene.fog.near=70;scene.fog.far=230;amb.intensity=0.85;sun.intensity=0.7;
  cam.far=400;cam.updateProjectionMatrix();
  var pit=L.pit,segs=pit?[[0,pit[0]],[pit[1],LEN+30]]:[[0,LEN+30]];
  segs.forEach(function(s){var len=s[1]-s[0],m=new THREE.Mesh(new THREE.BoxGeometry(W+1.2,0.5,len),new THREE.MeshLambertMaterial({map:(function(){var t=checker('#C2410C','#B93C0B',(W+1.2)/2,len/2);return t})()}));m.position.set(0,-0.25,-(s[0]+s[1])/2);lvGroup.add(m)});
  // líneas de calle
  for(i=0;i<=nl;i++){var x=(i-nl/2)*LW;bx(0.14,0.04,LEN+30,'#F8FAFC',x,0.02,-(LEN+30)/2+15-15+0,lvGroup)}
  if(pit){var pw=bx(W+1.2,0.4,pit[1]-pit[0],'#7C4A1E',0,-0.8,-(pit[0]+pit[1])/2,lvGroup);bx(W+1.2,0.2,pit[1]-pit[0]-1.5,'#3B82F6',0,-0.55,-(pit[0]+pit[1])/2,lvGroup);bx(W+1.2,0.6,0.4,'#7C4A1E',0,-0.5,-pit[0],lvGroup);bx(W+1.2,0.6,0.4,'#7C4A1E',0,-0.5,-pit[1],lvGroup)}
  // hierba y gradas
  var gr=bx(260,0.3,LEN+200,'#4FA43A',0,-0.9,-LEN/2,lvGroup);
  [-1,1].forEach(function(sd){for(i=0;i<4;i++){bx(10,1.6+i*1.4,LEN+30,i%2?'#94A3B8':'#CBD5E1',sd*(W/2+9+i*4),0.8+i*0.7,-LEN/2+8,lvGroup)}});
  var nc=420,crowd=new THREE.InstancedMesh(new THREE.BoxGeometry(0.9,1.2,0.9),new THREE.MeshLambertMaterial({color:0xffffff}),nc),dm=new THREE.Object3D(),cols=['#EF4444','#3B82F6','#FACC15','#22C55E','#EC4899','#F8FAFC'];
  for(i=0;i<nc;i++){var sd=i%2?-1:1,row=Math.floor(r()*4);dm.position.set(sd*(W/2+7+row*4+r()*2),3.3+row*1.4+(row===0?-0.5:0),-r()*(LEN+20)+8);dm.updateMatrix();crowd.setMatrixAt(i,dm.matrix);crowd.setColorAt(i,new THREE.Color(cols[Math.floor(r()*cols.length)]))}
  lvGroup.add(crowd);
  // vallas
  S.hd=[];L.hurd.forEach(function(z){for(var li=0;li<nl;li++){var h=makeHurdle();h.position.set(laneX(li),0,-z);h.scale.x=1.0;lvGroup.add(h);S.hd.push({z:z,lane:li,mesh:h,hit:false,fall:0})}});
  // línea de salida y meta
  bx(W+1.2,0.05,0.6,'#F8FAFC',0,0.04,0,lvGroup);
  var fg=new THREE.Group();fg.position.set(0,0,-LEN);bx(0.8,8,0.8,'#F8FAFC',-W/2-1.5,4,0,fg);bx(0.8,8,0.8,'#F8FAFC',W/2+1.5,4,0,fg);
  var ban=new THREE.Mesh(new THREE.BoxGeometry(W+4,2,0.4),new THREE.MeshBasicMaterial({map:checker('#111827','#F8FAFC',(W+4)/1.2,1.2)}));ban.position.set(0,7.6,0);fg.add(ban);
  var cs=new THREE.Mesh(new THREE.PlaneGeometry(W+1.2,1.6),new THREE.MeshBasicMaterial({map:checker('#111827','#F8FAFC',(W+1.2)*1.2,1.5)}));cs.rotation.x=-Math.PI/2;cs.position.set(0,0.06,0);fg.add(cs);
  S.tape=bx(W+1,0.15,0.1,basic('#FACC15'),0,1.6,0,fg);lvGroup.add(fg);
  // marcas de distancia
  for(i=1;i<10;i++){bx(0.7,0.08,3,'#F8FAFC',W/2+1.9,0.05,-i*20,lvGroup)}
  scene.add(athlete);S.rv=[];
  rivalG.forEach(function(g){scene.remove(g)});
  var rl=[];for(i=0;i<nl;i++)if(i!==L.pl)rl.push(i);
  L.riv.forEach(function(sp,k){scene.add(rivalG[k]);S.rv.push({z:0,v:0,vmax:sp,lane:rl[k],mesh:rivalG[k],air:0,slow:0,done:false,ph:k*1.3,hdl:{},pitT:0})});
  S.p={z:0,v:0,air:0,spr:0,scd:0,slow:0,ph:0,done:false,mud:false};S.clock=0;S.rank=0;S.camz=0;S.started=false;
}
function hud(){var p=S.p,d=Math.min(100,Math.max(0,Math.round(-(p?-p.z:0)/2*1)));var ahead=0;if(S.rv&&p)S.rv.forEach(function(r){if(r.z>p.z)ahead++});
  setHud('Nivel '+(S.lv+1)+'/3','Tiempo '+(S.clock||0).toFixed(1)+' s',Math.round(Math.max(0,Math.min(200,p?p.z:0))/2)+' / 100 m','Posición '+(ahead+1)+'º · '+((p&&p.spr>0)?'¡Esprint!':(p&&p.scd>0?'Esprint '+Math.ceil(p.scd)+' s':'Esprint listo')))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,clock:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: tiempo = 0, nivel = 1');buildLevel(0);showOv('VALLAS VOXEL','Pulsa Espacio o toca para empezar','↑ o → mantener para correr · Espacio: saltar')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Atleta, '+S.rv.length+' rival(es), '+S.L.hurd.length*S.L.lanes+' valla(s)'+(S.L.pit?', foso de barro':'')+' y Meta')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡CAMPEÓN DE VALLAS!','Has ganado las 3 carreras','Pulsa Espacio para repetir')}}
function over(t,w){S.mode='over';showOv(t,w,'Pulsa Espacio para reintentar esta carrera')}
function onSpace(){var p=S.p;if(p.air>0)return;p.air=0.55;ev('Input: tecla Espacio');co('¿Está en el suelo? SÍ');ac('Saltar sobre la valla (0,55 s en el aire)')}
function jh(a){return Math.sin(Math.PI*(1-a/0.55))*1.8}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p,L=S.L;
  var run=held.up||held.right;
  if(run)S.started=true;if(S.started)S.clock+=dt;
  p.spr=Math.max(0,p.spr-dt);if(p.spr<=0)p.scd=Math.max(0,p.scd-dt);
  if(held.shift&&p.scd<=0&&p.spr<=0&&p.v>8){p.spr=1.5;p.scd=5.5;ev('Input: tecla Shift');ac('Esprintar: velocidad máxima × 1,3 durante 1,5 s')}
  var vmax=(p.spr>0?23.5:18)*(p.mud?0.35:1);
  if(run){if(p.v<vmax)p.v=Math.min(vmax,p.v+15*dt)}else p.v=Math.max(0,p.v-12*dt);
  if(p.v>vmax)p.v=Math.max(vmax,p.v-30*dt);
  p.z-=0;var nz=p.z+p.v*dt;p.z=nz;p.ph+=dt*p.v*0.55;
  if(p.air>0){p.air-=dt;if(p.air<0)p.air=0}
  var h=p.air>0?jh(p.air):0;
  var inPit=!!(L.pit&&p.z>=L.pit[0]&&p.z<=L.pit[1]&&h<0.3);p.mudT=inPit?(p.mudT||0)+dt:0;if(p.mudT>0.12&&!p.mud){ev('On Trigger Enter (Atleta ∩ Barro)');ac('velocidad máxima × 0,35 mientras esté en el barro');flash('¡Barro!',800)}p.mud=p.mudT>0.12;
  S.hd.forEach(function(d){if(d.lane===L.pl&&!d.hit&&Math.abs(p.z-d.z)<0.9&&h<1.1){d.hit=true;p.v*=0.45;ev('On Trigger Enter (Atleta ∩ Valla)');ac('velocidad = velocidad × 0,45 (valla derribada)');flash('¡Valla!',700)}});
  S.hd.forEach(function(d){if(d.hit&&d.fall<1.5)d.fall+=dt*5});
  S.rv.forEach(function(r){
    if(r.done||!S.started)return;
    r.slow=Math.max(0,r.slow-dt);var vm=r.vmax*(r.slow>0?0.55:1)*(r.pitT>0?0.4:1);
    r.v+=(vm-r.v)*Math.min(1,3*dt);r.z+=r.v*dt;r.ph+=dt*r.v*0.55;
    S.hd.forEach(function(d){if(d.lane===r.lane&&!r.hdl[d.z]&&r.z>d.z-5){r.hdl[d.z]=true;if(Math.random()<0.2){r.slow=1.0;r.fail=d.z}else r.air=0.55}});
    if(r.air>0)r.air=Math.max(0,r.air-dt);
    if(L.pit){if(!r.hdl.pit&&r.z>L.pit[0]-3.5){r.hdl.pit=true;if(Math.random()<0.75)r.air=0.55;}
      r.pitT=(r.z>L.pit[0]&&r.z<L.pit[1]&&r.air<=0)?1:0;if(r.air>0&&r.z>L.pit[0]-3&&r.z<L.pit[1]){}}
    if(r.z>=LEN){r.done=true;if(!p.done){ev('Rival cruza la meta');co('¿Ha llegado el jugador antes? NO');ac('Mostrar Game Over');over('¡UN RIVAL GANÓ!','Cruzó la meta antes que tú')}}});
  if(S.mode!=='play')return;
  if(p.z>=LEN&&!p.done){p.done=true;var ahead=S.rv.filter(function(r){return r.done}).length;ev('On Trigger Enter (Atleta ∩ Meta)');co('¿Ha llegado antes que los rivales? SÍ ('+(ahead+1)+'º)');ac('Parar el cronómetro: '+S.clock.toFixed(1)+' s');toNext()}
}
function render(dt){
  var p=S.p,t=S.t/1000,L=S.L;
  function pose(g,ph,air,sp){var s=Math.sin(ph*2),k=air>0?0:1;g.userData.legs[0].rotation.x=air>0?-0.9:s*0.9*k;g.userData.legs[1].rotation.x=air>0?0.5:-s*0.9*k;g.userData.arms[0].rotation.x=air>0?-1.6:-s*0.9*k;g.userData.arms[1].rotation.x=air>0?-1.6:s*0.9*k;g.rotation.x=-0.12-(sp>0?0.12:0)}
  var h=p.air>0?jh(p.air):0;athlete.position.set(laneX(L.pl),h,-p.z);athlete.rotation.y=Math.PI;pose(athlete,p.ph,p.air,p.v/20);athlete.rotation.x=0.1+p.v*0.004;
  S.rv.forEach(function(r){var rh=r.air>0?jh(r.air):0;r.mesh.position.set(laneX(r.lane),rh,-r.z);r.mesh.rotation.y=Math.PI;pose(r.mesh,r.ph,r.air,0)});
  S.hd.forEach(function(d){if(d.hit)d.mesh.rotation.x=Math.min(1.4,d.fall)});
  S.camz+=(p.z-S.camz)*Math.min(1,8*dt);
  cam.fov=60+p.v*0.25;cam.updateProjectionMatrix();
  cam.position.set(laneX(L.pl)*0.8,3.6,-S.camz+8.5);cam.lookAt(laneX(L.pl)*0.8,1.5,-S.camz-14);
}
'''
build('vallas3d.html','Vallas Voxel','SALTAR<br>(Espacio)','Mantén ↑ o → para correr · Espacio: saltar las vallas (y el foso del nivel 3) · Shift: esprintar (teclado). Cruza la meta antes que tus rivales; si tocas una valla pierdes velocidad.','#9AD4F5',G)
