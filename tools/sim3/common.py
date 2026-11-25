import re
base=open('/home/claude/gen/sim/templo3d.html').read()
HEAD0=base[:base.index('<script src=')]

def head(title,btn,help_,bg):
    h=HEAD0.replace('El Templo Perdido – simulación jugable 3D',title+' – simulación jugable 3D').replace('<h1>El Templo Perdido <span','<h1>'+title+' <span')
    h=h.replace('ESPADA<br>(Espacio)',btn).replace('background:#A5DBFF;aspect-ratio','background:'+bg+';aspect-ratio')
    h=re.sub(r'<p class="help">.*?</p>','<p class="help">'+help_+'</p>',h,flags=re.S)
    return h

A=r'''<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){
var VW=640,VH=420,C=2;
var stage=document.getElementById('stage'),logEl=document.getElementById('log'),bn=document.getElementById('bn'),ov=document.getElementById('ov');
function log(k,t,x){var li=document.createElement('li');li.className=k;li.innerHTML='<span class="t">'+t+'</span>'+x;logEl.insertBefore(li,logEl.firstChild);while(logEl.children.length>10)logEl.removeChild(logEl.lastChild)}
function ev(t){log('ev','EVENTO',t)}function co(t){log('co','CONDICIÓN',t)}function ac(t){log('ac','ACCIÓN',t)}
function setHud(a,b,c,d){document.getElementById('hA').textContent=a;document.getElementById('hB').textContent=b;document.getElementById('hC').textContent=c;document.getElementById('hD').textContent=d}
var renderer=new THREE.WebGLRenderer({antialias:true});
renderer.setPixelRatio(Math.min(2,window.devicePixelRatio||1));renderer.setSize(VW,VH,false);
stage.insertBefore(renderer.domElement,stage.firstChild);
var scene=new THREE.Scene();scene.background=new THREE.Color('#A5DBFF');scene.fog=new THREE.Fog('#BFE4FF',45,110);
var cam=new THREE.PerspectiveCamera(42,VW/VH,0.1,400);
var amb=new THREE.AmbientLight(0xffffff,0.85);scene.add(amb);
var sun=new THREE.DirectionalLight(0xffffff,0.7);sun.position.set(-20,40,15);scene.add(sun);
var lvGroup=null,mats={};
function mat(c){return mats[c]||(mats[c]=new THREE.MeshLambertMaterial({color:c}))}
function basic(c){var k='b'+c;return mats[k]||(mats[k]=new THREE.MeshBasicMaterial({color:c}))}
function emi(c,e){var k=c+'|'+e;return mats[k]||(mats[k]=new THREE.MeshLambertMaterial({color:c,emissive:e}))}
function bx(w,h,d,col,x,y,z,parent){var m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),typeof col==='string'?mat(col):col);m.position.set(x,y,z);if(parent)parent.add(m);return m}
function checker(c1,c2,rx,ry){var c=document.createElement('canvas');c.width=c.height=2;var g=c.getContext('2d');g.fillStyle=c1;g.fillRect(0,0,2,2);g.fillStyle=c2;g.fillRect(0,0,1,1);g.fillRect(1,1,1,1);var t=new THREE.CanvasTexture(c);t.magFilter=THREE.NearestFilter;t.minFilter=THREE.NearestFilter;t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(rx,ry);return t}
function rng(seed){return function(){seed|=0;seed=seed+0x6D2B79F5|0;var t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function clearLevel(){if(lvGroup){scene.remove(lvGroup);lvGroup.traverse(function(o){if(o.geometry)o.geometry.dispose()})}lvGroup=new THREE.Group();scene.add(lvGroup)}
function showOv(t,s,s2){ov.style.display='flex';ov.innerHTML='<b>'+t+'</b><span>'+s+'</span>'+(s2?'<span>'+s2+'</span>':'')}
function hideOv(){ov.style.display='none'}
var S=null,held={};
function cellCh(cx,cz){var r=S.L.rows[cz];return r?r[cx]:undefined}
function flash(txt,ms){S.msg=txt;S.msgT=S.t+(ms||1400)}
'''

B=r'''
var KEYS={ArrowUp:'up',ArrowDown:'down',ArrowLeft:'left',ArrowRight:'right',w:'up',s:'down',a:'left',d:'right',W:'up',S:'down',A:'left',D:'right'};
function pressSpace(){if(S.mode==='title')loadLevel(0);else if(S.mode==='over'){if(typeof retry==='function')retry();else newGame()}else if(S.mode==='won')newGame();else if(S.mode==='play')onSpace()}
window.addEventListener('keydown',function(e){
  if(KEYS[e.key]){held[KEYS[e.key]]=true;e.preventDefault()}
  else if(e.key==='Shift')held.shift=true;
  else if(e.key===' '){e.preventDefault();held.space=true;if(!e.repeat)pressSpace()}});
window.addEventListener('keyup',function(e){if(KEYS[e.key])held[KEYS[e.key]]=false;if(e.key==='Shift')held.shift=false;if(e.key===' ')held.space=false});
document.querySelectorAll('.dpad button').forEach(function(b){var d=b.dataset.d;
  function on(e){e.preventDefault();held[d]=true}function off(e){e.preventDefault();held[d]=false}
  b.addEventListener('pointerdown',on);b.addEventListener('pointerup',off);b.addEventListener('pointerleave',off);b.addEventListener('pointercancel',off)});
var bb=document.getElementById('bBomb');
bb.addEventListener('pointerdown',function(e){e.preventDefault();held.space=true;pressSpace()});
['pointerup','pointerleave','pointercancel'].forEach(function(n){bb.addEventListener(n,function(){held.space=false})});
document.getElementById('bRestart').addEventListener('click',function(){newGame()});
stage.addEventListener('pointerdown',function(){if(S.mode!=='play')pressSpace()});
var last=performance.now();
function loop(now){var dt=Math.min(50,now-last)/1000;last=now;update(dt);hud();render(dt);var txt=(S.msg&&S.t<S.msgT)?S.msg:(S.mode==='next'?'¡Nivel superado!':'');if(txt){bn.style.display='block';bn.textContent=txt}else bn.style.display='none';renderer.render(scene,cam);requestAnimationFrame(loop)}
newGame();requestAnimationFrame(loop);
})();
</script>
</body>
</html>
'''

def build(name,title,btn,help_,bg,game):
    open(name,'w').write(head(title,btn,help_,bg)+A+game+B)
