import re,sys,glob,os
BOOST=r'''/*BOOST*/
(function(){
var EU=document.documentElement.lang==='eu',paused=false,mute=false,AC=null,lastT=0;
try{mute=localStorage.getItem('voxMute')==='1'}catch(e){}
function beep(f,d,ty,v,f2,dl){if(mute)return;try{if(!AC)AC=new (window.AudioContext||window.webkitAudioContext)();var o=AC.createOscillator(),g=AC.createGain(),t=AC.currentTime+(dl||0);o.type=ty||'square';o.frequency.setValueAtTime(f,t);if(f2)o.frequency.exponentialRampToValueAtTime(f2,t+d);g.gain.setValueAtTime(v||0.04,t);g.gain.exponentialRampToValueAtTime(0.0001,t+d);o.connect(g);g.connect(AC.destination);o.start(t);o.stop(t+d)}catch(e){}}
function hitFx(){try{if(!STG)return;STG.classList.remove('hit');void STG.offsetWidth;STG.classList.add('hit');setTimeout(function(){STG.classList.remove('hit')},380)}catch(e){}}
function sfx(k,x){var now=performance.now();
  if(/GameOver|Game Over|(vidas|bizitzak) = 0\b/.test(x)){beep(320,0.55,'sawtooth',0.07,60);hitFx();return}
  if(/Victoria|Garaipena/.test(x)){[523,659,784,1047].forEach(function(f,i){beep(f,0.18,'square',0.05,0,i*0.12)});return}
  if(/Load Scene/.test(x)){beep(440,0.1,'square',0.05,660);beep(660,0.12,'square',0.05,880,0.1);return}
  if(/(vidas|bizitzak) = \d/.test(x)){beep(210,0.28,'sawtooth',0.08,70);hitFx();return}
  if(/Destroy/.test(x)){beep(760,0.12,'square',0.05,220);return}
  if(k==='ac'){if(now-lastT>60){lastT=now;beep(/Instantiate|AddForce/.test(x)?420:560,0.06,'triangle',0.04)}return}
  if(k==='ev'&&now-lastT>140){lastT=now;beep(260,0.03,'triangle',0.02)}}
var _log=log;log=function(k,t,x){_log(k,t,x);try{sfx(k,String(x))}catch(e){}};
var _upd=update;update=function(dt){if(paused)return;_upd(dt)};
var STG=(typeof stage!=='undefined'&&stage)||null;
if(!STG){var cvx=document.getElementById('cv');if(cvx){STG=document.createElement('div');STG.style.position='relative';cvx.parentNode.insertBefore(STG,cvx);STG.appendChild(cvx)}}
var bp,bm,vp;
function tp(){paused=!paused;if(vp)vp.style.display=paused?'flex':'none';if(bp)bp.textContent=paused?'▶':'⏸'}
function tm(){mute=!mute;if(bm)bm.textContent=mute?'🔇':'🔊';try{localStorage.setItem('voxMute',mute?'1':'0')}catch(e){}}
function tf(){try{if(document.fullscreenElement)document.exitFullscreen();else STG.requestFullscreen()}catch(e){}}
try{if(STG){STG.classList.add('vstg');
var st=document.createElement('style');st.textContent='@keyframes vshk{0%,100%{transform:translate(0)}20%{transform:translate(-7px,3px)}40%{transform:translate(6px,-4px)}60%{transform:translate(-5px,-2px)}80%{transform:translate(4px,3px)}}.vstg.hit{animation:vshk .38s}.vstg.hit::after{content:"";position:absolute;inset:0;background:rgba(239,68,68,.30);pointer-events:none;z-index:4}.vtb{position:absolute;right:8px;bottom:8px;display:flex;gap:6px;z-index:6}.vtb button{width:34px;height:34px;border-radius:10px;border:0;background:rgba(15,23,42,.62);color:#fff;font-size:16px;cursor:pointer;line-height:1}.vtb button:hover{background:rgba(15,23,42,.85)}.vpz{position:absolute;inset:0;display:none;align-items:center;justify-content:center;flex-direction:column;gap:6px;background:rgba(15,23,42,.6);color:#fff;z-index:5;font-weight:700;font-size:30px;text-align:center}.vpz span{font-size:15px;font-weight:600}.vstg:fullscreen{aspect-ratio:auto;display:flex;justify-content:center;background:#000}.vstg:fullscreen canvas{width:auto;height:100%;max-width:100%}';document.head.appendChild(st);
vp=document.createElement('div');vp.className='vpz';vp.innerHTML=(EU?'ETEN':'PAUSA')+'<span>'+(EU?'Sakatu P edo ukitu jarraitzeko':'Pulsa P o toca para seguir')+'</span>';STG.appendChild(vp);
var tb=document.createElement('div');tb.className='vtb';
function mkb(t,ttl,fn){var b=document.createElement('button');b.textContent=t;b.title=ttl;b.addEventListener('pointerdown',function(e){e.stopPropagation()});b.addEventListener('click',function(e){e.stopPropagation();fn()});tb.appendChild(b);return b}
bp=mkb('⏸',EU?'Eten (P)':'Pausa (P)',tp);bm=mkb(mute?'🔇':'🔊',EU?'Mutu (M)':'Silencio (M)',tm);mkb('⛶',EU?'Pantaila osoa (F)':'Pantalla completa (F)',tf);
STG.appendChild(tb);vp.addEventListener('pointerdown',function(e){e.stopPropagation();tp()})}}catch(e){}
window.addEventListener('keydown',function(e){var k=e.key;
  if(k==='p'||k==='P'||k==='Escape'){if(k==='Escape'&&!paused)return;tp()}
  else if(k==='m'||k==='M')tm();
  else if(k==='f'||k==='F')tf();
  else if(!paused&&(k==='1'||k==='2'||k==='3')&&S&&typeof loadLevel==='function'){try{if(typeof hideOv==='function')hideOv();loadLevel(+k-1)}catch(er){}}});
})();
'''
def lang(s):return 'eu' if '<html lang="eu">' in s else 'es'
def inject(path):
    s=open(path,encoding='utf8').read()
    if '/*BOOST*/' in s: return 'skip'
    tail="newGame();requestAnimationFrame(loop);"
    assert s.count(tail)==1,path
    s=s.replace(tail,BOOST+tail)
    add=' Atajos: P pausa · M silencio · F pantalla completa · 1/2/3 saltar de nivel.' if lang(s)=='es' else ' Lasterbideak: P eten · M mutu · F pantaila osoa · 1/2/3 mailaz aldatu.'
    m=re.search(r'(<p class="help">)(.*?)(</p>)',s,re.S);assert m,path
    s=s[:m.end(2)]+add+s[m.end(2):]
    open(path,'w',encoding='utf8').write(s);return 'ok'
if __name__=='__main__':
    root=sys.argv[1]
    for l in('es','eu'):
        for f in sorted(glob.glob(f'{root}/{l}/*.html')):
            if os.path.basename(f)=='barril3d.html':continue
            print(f,inject(f))
