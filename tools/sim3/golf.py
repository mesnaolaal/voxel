from common import build
G=r'''
amb.intensity=0.8;sun.intensity=0.7;
var TITLE='MINIGOLF VOXEL';
var R=0.4;
var HOLES=[
 {name:'Hoyo 1: recto y sin obstáculos',par:3,x0:-5,x1:5,z0:-16,z1:16,tee:[0,13],hole:[0,-13],water:[],sand:[],walls:[],mill:null},
 {name:'Hoyo 2: arena y un estanque',par:3,x0:-8,x1:8,z0:-16,z1:16,tee:[-5,13],hole:[5,-13],water:[[-3,5,-3,3]],sand:[[1,8,-10,-5],[-8,-4,6,10]],walls:[],mill:null},
 {name:'Hoyo 3: un molino con aspas que giran',par:3,x0:-5,x1:5,z0:-17,z1:17,tee:[0,14],hole:[0,-14],water:[],sand:[],walls:[[2.2,5,-0.8,0.8],[-5,-2.2,-0.8,0.8]],mill:{x:0,z:0,len:4.6,tower:[-0.8,0.8,-0.8,0.8]}}];
function inR(x,z,r){return x>=r[0]&&x<=r[1]&&z>=r[2]&&z<=r[3]}
function millAng(){return S.wt*1.6}
function bladeHit(b){var m=S.H.mill;if(!m)return false;var a=millAng();
  for(var i=0;i<4;i++){var ang=a+i*Math.PI/2,ex=m.x+Math.cos(ang)*m.len,ez=m.z+Math.sin(ang)*m.len,dx=ex-m.x,dz=ez-m.z,t=Math.max(0,Math.min(1,((b.x-m.x)*dx+(b.z-m.z)*dz)/(dx*dx+dz*dz))),px=m.x+dx*t,pz=m.z+dz*t;
    if(Math.hypot(b.x-px,b.z-pz)<R+0.22)return{nx:(b.x-px),nz:(b.z-pz),bx:px,bz:pz,ang:ang}}return false}
function physStep(b,dt){ // devuelve 'water' | 'hole' | null
  var H=S.H,sp=Math.hypot(b.vx,b.vz);
  if(sp>0){var sand=H.sand.some(function(r){return inR(b.x,b.z,r)}),dec=(sand?12:3.5)*dt;var ns=Math.max(0,sp-dec);b.vx*=ns/sp;b.vz*=ns/sp;if(ns<0.3){b.vx=0;b.vz=0}}
  b.x+=b.vx*dt;b.z+=b.vz*dt;
  if(b.x<H.x0+R){b.x=H.x0+R;b.vx=Math.abs(b.vx)*0.8}if(b.x>H.x1-R){b.x=H.x1-R;b.vx=-Math.abs(b.vx)*0.8}
  if(b.z<H.z0+R){b.z=H.z0+R;b.vz=Math.abs(b.vz)*0.8}if(b.z>H.z1-R){b.z=H.z1-R;b.vz=-Math.abs(b.vz)*0.8}
  var boxes=H.walls.slice();if(H.mill)boxes.push(H.mill.tower);
  boxes.forEach(function(w){var cx=Math.max(w[0],Math.min(w[1],b.x)),cz=Math.max(w[2],Math.min(w[3],b.z)),dx=b.x-cx,dz=b.z-cz,d=Math.hypot(dx,dz);
    if(d<R){if(d<1e-4){dx=0;dz=1;d=1}var nx=dx/d,nz=dz/d;b.x=cx+nx*R;b.z=cz+nz*R;var vn=b.vx*nx+b.vz*nz;if(vn<0){b.vx-=1.8*vn*nx;b.vz-=1.8*vn*nz}}});
  var bh=bladeHit(b);if(bh){var d=Math.hypot(bh.nx,bh.nz)||1,nx=bh.nx/d,nz=bh.nz/d;b.x=bh.bx+nx*(R+0.23);b.z=bh.bz+nz*(R+0.23);var vn=b.vx*nx+b.vz*nz;if(vn<0){b.vx-=1.8*vn*nx;b.vz-=1.8*vn*nz}
    var kick=4;b.vx+=-Math.sin(bh.ang)*kick*0.5;b.vz+=Math.cos(bh.ang)*kick*0.5;if(b.vx||b.vz){} }
  if(H.water.some(function(r){return inR(b.x,b.z,r)}))return 'water';
  var dh=Math.hypot(b.x-H.hole[0],b.z-H.hole[1]);if(dh<0.8&&Math.hypot(b.vx,b.vz)<13)return 'hole';
  return null}
var ball=new THREE.Mesh(new THREE.BoxGeometry(0.8,0.8,0.8),basic('#FFFFFF')),golfer=new THREE.Group(),clubG,arrow=new THREE.Group(),arrowBars=[];
(function(){var g=golfer;
  bx(0.4,1.0,0.42,'#1D4ED8',-0.25,0.5,0,g);bx(0.4,1.0,0.42,'#1D4ED8',0.25,0.5,0,g);bx(1.1,1.2,0.6,'#F8FAFC',0,1.6,0,g);bx(1.12,0.25,0.62,'#16A34A',0,1.15,0,g);bx(0.28,0.9,0.3,'#F8FAFC',-0.7,1.55,0,g);bx(0.28,0.9,0.3,'#F8FAFC',0.7,1.55,0,g);
  bx(0.65,0.6,0.6,'#FCD9A6',0,2.5,0,g);bx(0.7,0.2,0.7,'#DC2626',0,2.9,0,g);bx(0.95,0.1,0.9,'#DC2626',0,2.8,0.35,g);bx(0.12,0.12,0.06,'#111827',0.15,2.5,0.31,g);bx(0.12,0.12,0.06,'#111827',-0.15,2.5,0.31,g);
  clubG=new THREE.Group();clubG.position.set(0.75,1.1,0.2);bx(0.12,1.8,0.12,'#94A3B8',0,-0.9,0,clubG);bx(0.5,0.3,0.3,'#475569',0,-1.8,0.1,clubG);g.add(clubG)})();
for(var i=0;i<8;i++){var ab=new THREE.Mesh(new THREE.BoxGeometry(0.35,0.1,0.8),basic('#FACC15'));arrow.add(ab);arrowBars.push(ab)}
var flag=null,millG=null,blades=null;
function buildLevel(n){
  var H=HOLES[n];S.H=H;S.L=H;clearLevel();var r=rng(41+n*9),i;
  scene.background.set('#9AD4F5');scene.fog.color.set('#BFE3F7');scene.fog.near=90;scene.fog.far=220;
  var w=H.x1-H.x0,l=H.z1-H.z0,cx=(H.x0+H.x1)/2,cz=(H.z0+H.z1)/2;
  var gt=checker('#4FBF4A','#46B342',w/2,l/2),fl=new THREE.Mesh(new THREE.BoxGeometry(w,0.6,l),new THREE.MeshLambertMaterial({map:gt}));fl.position.set(cx,-0.3,cz);lvGroup.add(fl);
  var outg=new THREE.Mesh(new THREE.PlaneGeometry(260,260),new THREE.MeshLambertMaterial({color:'#3F9A3B'}));outg.rotation.x=-Math.PI/2;outg.position.set(cx,-0.62,cz);lvGroup.add(outg);
  H.sand.forEach(function(s){bx(s[1]-s[0],0.1,s[3]-s[2],'#F3D58A',(s[0]+s[1])/2,0.02,(s[2]+s[3])/2,lvGroup)});
  H.water.forEach(function(s){bx(s[1]-s[0],0.4,s[3]-s[2],emi('#38BDF8','#0369A1'),(s[0]+s[1])/2,-0.02,(s[2]+s[3])/2,lvGroup);bx(s[1]-s[0]+0.6,0.3,s[3]-s[2]+0.6,'#92400E',(s[0]+s[1])/2,-0.1,(s[2]+s[3])/2,lvGroup)});
  // paredes exteriores
  bx(w+1,1.0,0.8,'#92400E',cx,0.5,H.z0-0.4,lvGroup);bx(w+1,1.0,0.8,'#92400E',cx,0.5,H.z1+0.4,lvGroup);bx(0.8,1.0,l,'#92400E',H.x0-0.4,0.5,cz,lvGroup);bx(0.8,1.0,l,'#92400E',H.x1+0.4,0.5,cz,lvGroup);
  H.walls.forEach(function(s){bx(s[1]-s[0],1.0,s[3]-s[2],'#B45309',(s[0]+s[1])/2,0.5,(s[2]+s[3])/2,lvGroup)});
  // hoyo
  bx(1.6,0.05,1.6,'#0B0B0B',H.hole[0],0.04,H.hole[1],lvGroup);bx(0.12,4,0.12,'#F8FAFC',H.hole[0],2,H.hole[1],lvGroup);flag=bx(1.6,0.9,0.1,'#EF4444',H.hole[0]+0.8,3.5,H.hole[1],lvGroup);
  // tee
  bx(2.2,0.08,2.2,'#2563EB',H.tee[0],0.03,H.tee[1],lvGroup);
  // molino
  millG=null;blades=null;if(H.mill){var m=H.mill;millG=new THREE.Group();bx(1.6,3.2,1.6,'#F8FAFC',0,1.6,0,millG);bx(2.0,0.8,2.0,'#DC2626',0,3.6,0,millG);millG.position.set(m.x,0,m.z);lvGroup.add(millG);
    blades=new THREE.Group();for(i=0;i<4;i++){var b=bx(m.len,0.5,0.5,'#92400E',m.len/2,0,0,blades),b2=bx(m.len*0.8,0.18,0.9,'#F8FAFC',m.len*0.6,0,0,blades);var holder=new THREE.Group();holder.rotation.y=-i*Math.PI/2;blades.remove(b);blades.remove(b2);holder.add(b);holder.add(b2);blades.add(holder)}
    blades.position.set(m.x,1.0,m.z);lvGroup.add(blades)}
  // decoración: árboles
  for(i=0;i<16;i++){var tx=H.x0-4-r()*8,side=i%2?1:-1,tz=H.z0+r()*l;var px=side>0?H.x1+3+r()*8:H.x0-3-r()*8;bx(0.8,2.5,0.8,'#78350F',px,1.25,tz,lvGroup);bx(3,2.5,3,'#16A34A',px,3.4,tz,lvGroup)}
  scene.add(ball);scene.add(golfer);scene.add(arrow);
  S.b={x:H.tee[0],z:H.tee[1],vx:0,vz:0};S.rest={x:H.tee[0],z:H.tee[1]};S.ang=Math.atan2(H.hole[0]-H.tee[0],-(H.hole[1]-H.tee[1]));S.pw=0;S.charging=false;S.moving=false;S.strokes=0;S.water=0;S.wt=0;S.swing=0;S.camx=cx;S.camz=cz;S.zoomY=Math.max(w*1.5,l*1.12)+5;
  S.sink=0;
}
function hud(){var H=S.H||HOLES[0];setHud('Hoyo '+((S.lv||0)+1)+'/3 · par '+H.par,'Golpes '+(S.strokes||0),'Agua '+(S.water||0)+'/3',S.moving?'Bola rodando…':(S.charging?'Fuerza '+Math.round(S.pw*100)+' %':'Fuerza: mantén Espacio'))}
function newGame(){S={mode:'title',lv:0,t:0,msg:'',msgT:0,total:0,res:[]};logEl.innerHTML='';ev('Start del juego');ac('Variables: golpes = 0, hoyo = 1');buildLevel(0);showOv('MINIGOLF VOXEL','Pulsa Espacio o toca para empezar','← → apuntar · mantén Espacio y suéltalo para golpear')}
function loadLevel(n){S.lv=n;S.mode='play';var tot=S.total,res=S.res;buildLevel(n);S.total=tot;S.res=res;hideOv();flash(HOLES[n].name,2600);
  ev('Load Scene "Hoyo '+(n+1)+'"');ac('Instantiate Golfista, Bola, Hoyo'+(S.H.mill?', Molino':'')+(S.H.water.length?', Agua':'')+'; golpes = 0')}
function retry(){S.total=0;S.res=[];loadLevel(0)}
function toNext(){var k=S.strokes,par=S.H.par;S.total+=k;S.res.push(k);var txt=k===1?'¡Hoyo en uno!':(k<par?(k===par-1?'¡Birdie! ':'¡Eagle! ')+k+' golpes':(k===par?'Par: '+k+' golpes':k+' golpes (par '+par+')'));
  if(S.lv<2){S.mode='next';flash(txt,2000);S.nextAt=S.t+2300;ac('Mostrar '+k+' golpes, esperar 2 s, Load Scene "Hoyo '+(S.lv+2)+'"')}else{S.mode='won';ac('Load Scene "Victoria"');showOv('¡TERMINASTE EL CAMPO!','Golpes: '+S.res.join(' + ')+' = '+S.total+' (par total 9)','Pulsa Espacio para jugar otra vez')}}
function over(){S.mode='over';showOv('¡DEMASIADA AGUA!','La bola cayó al agua 3 veces','Pulsa Espacio para reintentar desde el hoyo 1')}
function shoot(pw){var H=S.H,sp=4+12*pw;S.b.vx=Math.sin(S.ang)*sp;S.b.vz=-Math.cos(S.ang)*sp;S.strokes++;S.moving=true;S.swing=0.35;S.rest={x:S.b.x,z:S.b.z};
  ev('Input: soltar Espacio');ac('Golpear con fuerza '+Math.round(pw*100)+' %, golpes = '+S.strokes)}
function onSpace(){if(S.moving||S.mode!=='play')return;S.charging=true;S.pw=0}
function update(dt){
  S.t+=dt*1000;
  if(S.mode==='next'&&S.t>=S.nextAt)loadLevel(S.lv+1);
  if(S.mode!=='play')return;
  S.wt+=dt;
  if(S.sink>0){S.sink-=dt;if(S.sink<=0){ev('On Trigger Enter (Bola ∩ Hoyo)');co('¿Cae en el hoyo? SÍ');ac('Destroy(Bola), cargar el siguiente hoyo');toNext()}return}
  if(!S.moving){
    var rot=((held.right?1:0)-(held.left?1:0))*(held.shift?0.5:1.5)*dt;S.ang+=rot;
    if(S.charging){S.pw=Math.min(1,S.pw+dt/1.3);if(!held.space){var pw=Math.max(0.12,S.pw);S.charging=false;S.pw=0;shoot(pw)}}
  }else{
    var steps=Math.ceil(dt/0.008),h=dt/steps,res=null;
    for(var i=0;i<steps&&!res;i++)res=physStep(S.b,h);
    if(res==='water'){S.water++;S.strokes++;S.b.vx=S.b.vz=0;S.moving=false;ev('On Trigger Enter (Bola ∩ Agua)');ac('Teleport al inicio del golpe, golpes + 1, agua = '+S.water+'/3');flash('¡Al agua! +1 golpe',1400);S.b.x=S.rest.x;S.b.z=S.rest.z;if(S.water>=3){ac('Load Scene "GameOver"');over();return}}
    else if(res==='hole'){S.moving=false;S.b.vx=S.b.vz=0;S.b.x=S.H.hole[0];S.b.z=S.H.hole[1];S.sink=0.9}
    else if(S.b.vx===0&&S.b.vz===0){S.moving=false;S.rest={x:S.b.x,z:S.b.z};var H=S.H;S.ang=Math.atan2(H.hole[0]-S.b.x,-(H.hole[1]-S.b.z))}}
}
function render(dt){
  var H=S.H,b=S.b,t=S.t/1000;
  var y=S.sink>0?0.4-(0.9-S.sink)*1.2:0.4;ball.position.set(b.x,y,b.z);ball.rotation.x+=b.vz*dt*1.5;ball.rotation.z-=b.vx*dt*1.5;ball.visible=!(S.sink>0&&S.sink<0.3);
  var show=S.mode==='play'&&!S.moving&&S.sink<=0;arrow.visible=show;golfer.visible=show||S.swing>0;
  if(show){var len=1.5+(S.charging?S.pw:0.2)*8;for(var i=0;i<8;i++){var ab=arrowBars[i];ab.visible=i*1.1<len+1;ab.position.set(b.x+Math.sin(S.ang)*(1.2+i*1.1),0.12,b.z-Math.cos(S.ang)*(1.2+i*1.1));ab.rotation.y=-S.ang;ab.material.color.set(S.charging?(i/8<S.pw?'#EF4444':'#FACC15'):'#FACC15')}}
  S.swing=Math.max(0,S.swing-dt);
  var gx=b.x-Math.sin(S.ang)*1.5+Math.cos(S.ang)*1.3,gz=b.z+Math.cos(S.ang)*1.5+Math.sin(S.ang)*1.3;golfer.position.set(gx,0,gz);golfer.rotation.y=-S.ang+Math.PI;
  clubG.rotation.x=S.swing>0?-1.2+Math.sin((0.35-S.swing)/0.35*Math.PI)*1.6:(S.charging?0.9*S.pw+0.1:0.1);
  if(blades){blades.rotation.y=-millAng()}
  flag.position.x=H.hole[0]+0.8+Math.sin(t*3)*0.1;
  var cx=(H.x0+H.x1)/2,cz=(H.z0+H.z1)/2;S.camx+=(cx-S.camx)*Math.min(1,6*dt);S.camz+=(cz-S.camz)*Math.min(1,6*dt);
  cam.position.set(S.camx,S.zoomY,S.camz+S.zoomY*0.5);cam.lookAt(S.camx,0.2,S.camz+0.3);
}
'''
build('golf3d.html','Minigolf Voxel','GOLPEAR<br>(mantén y suelta)','← → (o A/D): apuntar (Shift: afinar) · Mantén Espacio para cargar la fuerza y suéltalo para golpear. Mete la bola en el hoyo con pocos golpes. Si cae al agua 3 veces, pierdes.','#9AD4F5',G)
