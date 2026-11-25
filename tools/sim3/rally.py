from common import build
G=r'''
var TITLE='RALLY VOXEL';
var LV=[
 {name:'Un circuito en óvalo sin obstáculos',len:900,amp:14,w:20,time:36,cones:0,oil:0,gas:1,night:false,rival:false,seed:2},
 {name:'Curvas, conos y una mancha de aceite',len:1300,amp:22,w:17,time:48,cones:9,oil:3,gas:3,night:false,rival:false,seed:5},
 {name:'De noche y con un coche rival',len:1500,amp:24,w:16,time:50,cones:10,oil:3,gas:3,night:true,rival:true,seed:9}];
function cxOf(z){var s=-z;return S.L.amp*(Math.sin(s*0.0065)+0.4*Math.sin(s*0.0145))}
function slopeOf(z){var s=-z;return S.L.amp*(0.0065*Math.cos(s*0.0065)+0.4*0.0145*Math.cos(s*0.0145))}
var dummy=new THREE.Object3D();
function makeCar(body,cab){var g=new THREE.Group();
  bx(2.0,0.7,4.2,body,0,0.7,0,g);bx(1.7,0.6,2.0,cab,0,1.3,0.2,g);bx(1.5,0.4,0.1,'#93C5FD',0,1.35,-0.85,g);bx(1.9,0.15,0.6,'#111827',0,1.45,1.9,g);bx(0.15,0.4,0.15,'#111827',-0.7,1.15,1.9,g);bx(0.15,0.4,0.15,'#111827',0.7,1.15,1.9,g);
  bx(0.5,0.25,0.12,basic('#FEF9C3'),-0.65,0.75,-2.12,g);bx(0.5,0.25,0.12,basic('#FEF9C3'),0.65,0.75,-2.12,g);bx(0.5,0.2,0.1,basic('#EF4444'),-0.65,0.75,2.12,g);bx(0.5,0.2,0.1,basic('#EF4444'),0.65,0.75,2.12,g);
  [[-1.05,-1.3],[1.05,-1.3],[-1.05,1.3],[1.05,1.3]].forEach(function(w){bx(0.35,0.8,0.8,'#1F2937',w[0],0.4,w[1],g)});
  var fl=new THREE.Group();bx(0.4,0.4,1.4,basic('#F97316'),-0.5,0.7,2.9,fl);bx(0.4,0.4,1.4,basic('#F97316'),0.5,0.7,2.9,fl);bx(0.2,0.2,1.8,basic('#FDE047'),-0.5,0.7,3.0,fl);bx(0.2,0.2,1.8,basic('#FDE047'),0.5,0.7,3.0,fl);fl.visible=false;g.add(fl);g.userData.fl=fl;return g}
var car=makeCar('#2563EB','#E5E7EB'),rivalCar=makeCar('#DC2626','#FEE2E2'),hl=new THREE.PointLight(0xfff2c0,0,38),ground=null,gTex=checker('#58B947','#4FA83F',60,60);
var ghLast=0;
function ribbon(z0,z1,off0,off1,colA,colB,y){ // franja a lo largo de la carretera, offsets laterales relativos al centro
  var step=4,n=Math.ceil((z0-z1)/step),pos=[],col=[],idx=[],cA=new THREE.Color(colA),cB=new THREE.Color(colB),i;
  for(i=0;i<=n;i++){var z=z0-i*step,cx=cxOf(z),c=(Math.floor(i/2)%2)?cA:cB;
    pos.push(cx+off0,y,z,cx+off1,y,z);col.push(c.r,c.g,c.b,c.r,c.g,c.b)}
  for(i=0;i<n;i++){var a=i*2;idx.push(a,a+2,a+1,a+1,a+2,a+3)}
  var g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));g.setAttribute('color',new THREE.BufferAttribute(new Float32Array(col),3));g.setIndex(idx);g.computeVertexNormals();
  var m=new THREE.Mesh(g,new THREE.MeshLambertMaterial({vertexColors:true,side:THREE.DoubleSide}));return m}
function makeCone(){var g=new THREE.Group();bx(1.2,0.15,1.2,'#1F2937',0,0.08,0,g);bx(0.9,0.5,0.9,'#F97316',0,0.4,0,g);bx(0.6,0.5,0.6,'#FB923C',0,0.9,0,g);bx(0.3,0.45,0.3,'#F97316',0,1.35,0,g);bx(0.62,0.12,0.62,'#FFFFFF',0,0.9,0,g);return g}
function makeGas(){var g=new THREE.Group();bx(1.1,1.5,1.1,emi('#FACC15','#A16207'),0,0.9,0,g);bx(1.15,0.2,1.15,'#B91C1C',0,0.5,0,g);bx(1.15,0.2,1.15,'#B91C1C',0,1.3,0,g);bx(0.35,0.3,0.35,'#374151',0,1.8,0,g);return g}
function makeOil(){var g=new THREE.Group(),o=new THREE.Mesh(new THREE.CylinderGeometry(2.4,2.6,0.06,10),new THREE.MeshLambertMaterial({color:'#0B0B14',emissive:'#1E1B4B'}));o.position.y=0.07;g.add(o);var o2=new THREE.Mesh(new THREE.CylinderGeometry(1.2,1.4,0.07,8),new THREE.MeshLambertMaterial({color:'#312E81',emissive:'#4338CA'}));o2.position.set(0.5,0.09,0.3);g.add(o2);return g}
function buildLevel(n){
  var L=LV[n];S.L=L;clearLevel();var r=rng(L.seed*31+7),i,len=L.len,w=L.w;
  var night=L.night;scene.background.set(night?'#050816':'#8FD0F5');scene.fog.color.set(night?'#050816':'#BFE3F7');scene.fog.near=night?25:110;scene.fog.far=night?150:340;
  amb.intensity=night?0.38:0.85;sun.intensity=night?0.22:0.7;hl.intensity=night?1.6:0;
  cam.far=500;cam.updateProjectionMatrix();
  var gm=new THREE.Mesh(new THREE.PlaneGeometry(600,600),new THREE.MeshLambertMaterial({map:gTex}));gm.rotation.x=-Math.PI/2;gm.position.y=-0.05;lvGroup.add(gm);ground=gm;if(night)gm.material.color.set('#4B5E4F');
  lvGroup.add(ribbon(60,-len-80,-w/2,w/2,'#4B5563','#454E5C',0.02));
  lvGroup.add(ribbon(60,-len-80,-w/2-1.3,-w/2,'#EF4444','#F8FAFC',0.03));lvGroup.add(ribbon(60,-len-80,w/2,w/2+1.3,'#EF4444','#F8FAFC',0.03));
  // línea central discontinua
  var nd=Math.floor((len+120)/12),dm=new THREE.InstancedMesh(new THREE.BoxGeometry(0.4,0.05,4),basic('#FDE68A'),nd);
  for(i=0;i<nd;i++){var z=40-i*12;dummy.position.set(cxOf(z),0.06,z);dummy.rotation.set(0,-Math.atan(slopeOf(z)),0);dummy.updateMatrix();dm.setMatrixAt(i,dummy.matrix)}lvGroup.add(dm);
  // meta
  var zf=-len,cxf=cxOf(zf);var fg=new THREE.Group();fg.position.set(cxf,0,zf);fg.rotation.y=-Math.atan(slopeOf(zf));
  bx(1,9,1,'#F8FAFC',-w/2-1.5,4.5,0,fg);bx(1,9,1,'#F8FAFC',w/2+1.5,4.5,0,fg);
  var chk=new THREE.Mesh(new THREE.BoxGeometry(w+4,2.4,0.5),new THREE.MeshBasicMaterial({map:checker('#111827','#F8FAFC',w/2,1.2)}));chk.position.set(0,8,0);fg.add(chk);
  var cs=new THREE.Mesh(new THREE.PlaneGeometry(w,3),new THREE.MeshBasicMaterial({map:checker('#111827','#F8FAFC',w/1.5,2)}));cs.rotation.x=-Math.PI/2;cs.position.set(0,0.07,0);fg.add(cs);lvGroup.add(fg);
  // salida
  var sg=new THREE.Mesh(new THREE.PlaneGeometry(w,2),new THREE.MeshBasicMaterial({color:'#F8FAFC'}));sg.rotation.x=-Math.PI/2;sg.position.set(cxOf(-4),0.07,-4);lvGroup.add(sg);
  // árboles (instanciados)
  var nt=260,tr=new THREE.InstancedMesh(new THREE.BoxGeometry(0.8,3,0.8),mat('#78350F'),nt),cr=new THREE.InstancedMesh(new THREE.BoxGeometry(3,2.6,3),mat(night?'#14532D':'#16A34A'),nt),c2=new THREE.InstancedMesh(new THREE.BoxGeometry(2,1.8,2),mat(night?'#166534':'#22C55E'),nt);
  for(i=0;i<nt;i++){var zt=30-r()*(len+200),side=r()<0.5?-1:1,off=w/2+4+r()*30,sc=0.8+r()*1.0;dummy.rotation.set(0,0,0);
    dummy.scale.set(sc,sc,sc);dummy.position.set(cxOf(zt)+side*off,1.5*sc,zt);dummy.updateMatrix();tr.setMatrixAt(i,dummy.matrix);
    dummy.position.y=3.6*sc;dummy.updateMatrix();cr.setMatrixAt(i,dummy.matrix);dummy.position.y=5.4*sc;dummy.updateMatrix();c2.setMatrixAt(i,dummy.matrix)}
  lvGroup.add(tr);lvGroup.add(cr);lvGroup.add(c2);
  // montañas lejanas
  for(i=0;i<14;i++){var mz=-(i/13)*(len+300)+r()*40,side2=i%2?-1:1,mm=bx(40+r()*40,30+r()*30,40,night?'#1E293B':'#7C8DA6',cxOf(mz)+side2*(130+r()*60),10,mz,lvGroup);mm.rotation.y=r()*3}
  // obstáculos
  S.cones=[];S.oils=[];S.gas=[];var used=[];
  function place(minS,maxS){var s,x,ok,t=0;do{s=minS+r()*(maxS-minS);ok=used.every(function(u){return Math.abs(u-s)>26});t++}while(!ok&&t<40);used.push(s);return s}
  for(i=0;i<L.cones;i++){var s=place(90,len-80),zc=-s,xo=(r()*2-1)*(w/2-2),cn=makeCone();cn.position.set(cxOf(zc)+xo,0,zc);lvGroup.add(cn);S.cones.push({x:cn.position.x,z:zc,mesh:cn,hit:false,vx:0,vy:0,spin:0})}
  for(i=0;i<L.oil;i++){var s2=place(120,len-100),zo=-s2,xo2=(r()*2-1)*(w/2-3),ol=makeOil();ol.position.set(cxOf(zo)+xo2,0,zo);lvGroup.add(ol);S.oils.push({x:ol.position.x,z:zo,mesh:ol})}
  for(i=0;i<L.gas;i++){var s3=place(100,len-120),zg=-s3,xg=(r()*2-1)*(w/2-2.5),gs=makeGas();gs.position.set(cxOf(zg)+xg,0,zg);lvGroup.add(gs);S.gas.push({x:gs.position.x,z:zg,mesh:gs,got:false})}
  scene.add(car);car.add(hl);hl.position.set(0,3,-8);
  var psi0=Math.atan(slopeOf(0));
  S.p={x:cxOf(0)-(L.rival?3.6:0),z:0,psi:psi0,v:0,yawv:0,turbo:0,tcd:0,inv:0,ofs:0,off:false,vis:0};
  S.rival=null;if(L.rival){scene.add(rivalCar);S.rival={z:0,v:0,off:4.2};}else scene.remove(rivalCar);
  S.time=L.time;S.camp=psi0;S.shake=0;S.fin=false;S.wheel=0;
}
function hud(){var p=S.p,d=Math.max(0,Math.round((S.L?S.L.len:0)+(p?p.z:0)));setHud('Nivel '+(S.lv+1)+'/3','Tiempo '+Math.max(0,Math.ceil(S.time||0))+' s',Math.round(Math.abs(p?p.v:0)*3.4)+' km/h',(p&&p.turbo>0)?'¡TURBO!':(p&&p.tcd>0?'Turbo '+Math.ceil(p.tcd)+' s':'Meta a '+d+' m'))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,time:0};logEl.innerHTML='';ev('Start del juego');ac('Variables: tiempo = 36, nivel = 1');buildLevel(0);showOv('RALLY VOXEL','Pulsa Espacio o toca para empezar','Flechas: acelerar, frenar y girar · Espacio: turbo')}
function loadLevel(n){S.lv=n;S.mode='play';buildLevel(n);hideOv();flash('Nivel '+(n+1)+' · '+S.L.name,2600);
  ev('Load Scene "Nivel '+(n+1)+'"');ac('Instantiate Coche, '+S.cones.length+' cono(s), '+S.oils.length+' mancha(s), '+S.gas.length+' bidón(es), Meta'+(S.rival?', Coche rival':'')+'; tiempo = '+S.L.time+' s')}
function retry(){loadLevel(S.lv)}
function toNext(){if(S.lv<2){S.mode='next';flash('¡Nivel superado!',2000);S.nextAt=S.t+2000;ac('Mostrar mensaje, esperar 2 s, Load Scene "Nivel '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡CAMPEÓN DEL RALLY!','Has ganado los 3 circuitos','Pulsa Espacio para repetir')}}
function over(t,w){S.mode='over';showOv(t,w,'Pulsa Espacio para reintentar este nivel')}
function onSpace(){var p=S.p;if(p.tcd>0||p.turbo>0)return;p.turbo=1.6;p.tcd=5.5;ev('Input: tecla Espacio');co('¿Turbo disponible? SÍ');ac('Turbo: velocidad máxima ×1,5 durante 1,6 s')}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  var p=S.p,L=S.L;S.time-=dt;S.shake=Math.max(0,S.shake-dt);
  if(S.time<=0){S.time=0;ev('Tiempo = 0');co('¿Ha cruzado la meta? NO');ac('Mostrar Game Over');over('¡TIEMPO AGOTADO!','No llegaste a la meta');return}
  p.turbo=Math.max(0,p.turbo-dt);if(p.turbo<=0)p.tcd=Math.max(0,p.tcd-dt);
  var cx=cxOf(p.z);p.off=Math.abs(p.x-cx)>L.w/2+0.4;
  var maxV=(p.turbo>0?66:44)*(p.off?0.45:1);
  var acc=(held.up?1:0)-(held.down?1:0);
  if(acc>0){if(p.v<maxV)p.v=Math.min(maxV,p.v+(p.turbo>0?44:24)*dt)}else if(acc<0){p.v-=(p.v>0?42:16)*dt}
  else p.v-=Math.sign(p.v)*Math.min(Math.abs(p.v),7*dt);
  if(p.v>maxV)p.v=Math.max(maxV,p.v-(p.off?30:16)*dt);
  p.v=Math.max(-12,p.v);
  var st=(held.right?1:0)-(held.left?1:0);
  var grip=Math.min(1,Math.abs(p.v)/9)*(p.v<0?-1:1);
  p.psi+=st*1.75*grip*dt+p.ofs*dt;p.ofs*=Math.max(0,1-3*dt);
  p.x+=Math.sin(p.psi)*p.v*dt;p.z-=Math.cos(p.psi)*p.v*dt;
  if(p.z>10){p.z=10}
  S.cones.forEach(function(c){
    if(!c.hit&&p.inv<=S.t&&Math.hypot(c.x-p.x,c.z-p.z)<1.9){c.hit=true;c.vx=(c.x-p.x)*2+(Math.random()-0.5)*6;c.vy=9;c.spin=8;p.v*=0.4;S.shake=0.35;ev('On Trigger Enter (Coche ∩ Cono)');ac('velocidad = velocidad × 0,4; Destroy(Cono)')}
    if(c.hit){c.mesh.position.x+=c.vx*dt;c.mesh.position.y+=c.vy*dt;c.vy-=22*dt;c.mesh.rotation.z+=c.spin*dt;c.mesh.rotation.x+=c.spin*0.6*dt;if(c.mesh.position.y<-5)c.mesh.visible=false}});
  S.oils.forEach(function(o){if(Math.hypot(o.x-p.x,o.z-p.z)<2.4&&p.inv<=S.t){p.inv=S.t+1200;p.v*=0.55;p.ofs=(Math.random()<0.5?-1:1)*1.6;S.shake=0.25;ev('On Trigger Enter (Coche ∩ Aceite)');ac('velocidad = velocidad × 0,55 y derrapar');flash('¡Aceite!',900)}});
  S.gas.forEach(function(g){if(!g.got&&Math.hypot(g.x-p.x,g.z-p.z)<2.0){g.got=true;g.mesh.visible=false;S.time+=5;ev('On Trigger Enter (Coche ∩ Gasolina)');ac('Destroy(Bidón), tiempo = tiempo + 5 s');flash('+5 s',900)}});
  if(S.rival){var rv=S.rival;rv.v+=(L.rival?(32+Math.sin(S.t/2500)*3)-rv.v:0)*Math.min(1,2*dt);rv.z-=rv.v*dt;
    if(-rv.z>=L.len&&p.z>-L.len){ev('El rival cruza la meta');co('¿Ha cruzado el jugador antes? NO');ac('Mostrar Game Over');over('¡EL RIVAL GANÓ!','Cruzó la meta antes que tú');return}}
  if(p.z<=-L.len){ev('On Trigger Enter (Coche ∩ Meta)');co('¿Tiempo > 0'+(S.rival?' y rival detrás':'')+'? SÍ');ac('Parar el cronómetro');toNext();return}
}
function render(dt){
  var p=S.p,t=S.t/1000;
  car.position.set(p.x,0,p.z);car.rotation.y=-p.psi+Math.PI*0;car.rotation.z=0;car.userData.fl.visible=p.turbo>0&&Math.floor(S.t/60)%2===0;
  car.rotation.y=-p.psi;
  if(S.rival){var rz=S.rival.z,rx=cxOf(rz)+(S.rival.off*Math.cos(rz*0.01));rivalCar.position.set(rx,0,rz);rivalCar.rotation.y=-Math.atan(slopeOf(rz));rivalCar.userData.fl.visible=false}
  S.gas.forEach(function(g){if(!g.got)g.mesh.rotation.y=t*2});
  ground.position.x=Math.round(p.x/10)*10;ground.position.z=Math.round(p.z/10)*10;
  var d=p.psi-S.camp;S.camp+=d*Math.min(1,4*dt);
  var back=9+Math.max(0,p.v)*0.06,sh=S.shake*0.6;
  cam.position.set(p.x-Math.sin(S.camp)*back+(Math.random()-0.5)*sh,4.6+(Math.random()-0.5)*sh,p.z+Math.cos(S.camp)*back);
  cam.lookAt(p.x+Math.sin(S.camp)*12,1.4,p.z-Math.cos(S.camp)*12);
  cam.fov=62+Math.max(0,p.v)*0.18+(p.turbo>0?8:0);cam.updateProjectionMatrix();
}
'''
build('rally3d.html','Rally Voxel','TURBO<br>(Espacio)','Flechas o WASD: ↑ acelerar, ↓ frenar / marcha atrás, ← → girar · Espacio: turbo. Llega a la meta antes de que se acabe el tiempo. Los conos y el aceite te frenan, los bidones amarillos dan +5 s y fuera de la carretera vas muy lento.','#8FD0F5',G)
