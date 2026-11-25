import sys
LANG=sys.argv[1] if len(sys.argv)>1 else 'es'
DX,DY,H=5.2,3,6
def shade(c,f):
    r,g,b=int(c[1:3],16),int(c[3:5],16),int(c[5:7],16)
    return '#%02X%02X%02X'%(min(255,int(r*f)),min(255,int(g*f)),min(255,int(b*f)))
def P(x,y,z):return ((x-y)*DX,(x+y)*DY-z*H)
def render(vox):
    items=sorted(vox.items(),key=lambda k:(k[0][0]+k[0][1]+k[0][2],k[0][2]))
    paths=[];xs=[];ys=[]
    for (x,y,z),c in items:
        if (x+1,y,z) in vox and (x,y+1,z) in vox and (x,y,z+1) in vox: continue
        def poly(pts,col):
            paths.append('<path fill="%s" d="M%s Z"/>'%(col,'L'.join('%.1f,%.1f'%p for p in pts)))
            for p in pts: xs.append(p[0]);ys.append(p[1])
        if (x,y,z+1) not in vox: poly([P(x,y,z+1),P(x+1,y,z+1),P(x+1,y+1,z+1),P(x,y+1,z+1)],c)
        if (x,y+1,z) not in vox: poly([P(x,y+1,z+1),P(x+1,y+1,z+1),P(x+1,y+1,z),P(x,y+1,z)],shade(c,.82))
        if (x+1,y,z) not in vox: poly([P(x+1,y,z+1),P(x+1,y+1,z+1),P(x+1,y+1,z),P(x+1,y,z)],shade(c,.64))
    return ''.join(paths),(min(xs)-2,min(ys)-2,max(xs)-min(xs)+4,max(ys)-min(ys)+4)
def svg(vox,w=None,h=None,style='display:block;flex:none',pad=0):
    body,(x,y,vw,vh)=render(vox)
    wh=(' width="%d"'%w if w else '')+(' height="%d"'%h if h else '')
    return '<svg viewBox="%.1f %.1f %.1f %.1f"%s preserveAspectRatio="xMidYMid meet" aria-hidden="true" style="%s">%s</svg>'%(x,y,vw,vh,wh,style,body)
def box(x0,x1,y0,y1,z0,z1,c,d=None):
    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            for z in range(z0,z1+1): d[(x,y,z)]=c
    return d
def move(m,dx,dy,dz):return {(x+dx,y+dy,z+dz):c for (x,y,z),c in m.items()}
SK='#F5CFA5';
def worker():
    d={}
    box(0,0,0,1,0,1,'#1E3A8A',d);box(2,2,0,1,0,1,'#1E3A8A',d)
    box(0,2,0,1,2,4,'#F97316',d);box(0,2,1,1,3,3,'#FDE68A',d)
    box(-1,-1,0,1,2,4,SK,d);box(3,3,0,1,2,4,SK,d)
    box(0,2,0,1,5,6,SK,d);d[(0,1,6)]='#111827';d[(2,1,6)]='#111827'
    box(0,2,0,1,7,7,'#FACC15',d);box(0,2,1,2,7,7,'#FACC15',d)
    return d
def gorilla():
    d={}
    box(1,2,0,2,0,1,'#44281B',d);box(5,6,0,2,0,1,'#44281B',d)
    box(1,6,0,3,2,5,'#5B3A29',d);box(2,5,3,3,2,4,'#B98B5E',d)
    box(-1,0,0,2,1,6,'#5B3A29',d);box(7,8,0,2,1,6,'#5B3A29',d)
    box(2,5,0,3,6,8,'#5B3A29',d);box(3,4,3,3,6,7,'#B98B5E',d)
    d[(2,3,7)]='#FFFFFF';d[(5,3,7)]='#FFFFFF';d[(2,3,8)]='#111827';d[(5,3,8)]='#111827'
    return d
def barrel(rot=False):
    d={}
    for z in range(3):
        for x in range(3):
            for y in range(3):
                if z in(0,2) and x!=1 and y!=1: continue
                d[(x,y,z)]='#B45309'
    for x in range(3):
        for y in range(3):
            if (x,y,1) in d: d[(x,y,1)]='#78350F'
    return d
def ladder(h=8):
    d={}
    box(0,0,0,0,0,h-1,'#FBBF24',d);box(3,3,0,0,0,h-1,'#FBBF24',d)
    for z in range(1,h,2): box(1,2,0,0,z,z,'#FDE68A',d)
    return d
def hammer():
    d={}
    box(1,1,0,0,0,4,'#92400E',d);box(0,2,0,0,5,6,'#9CA3AF',d);box(0,2,0,0,6,6,'#D1D5DB',d)
    return d
def cat():
    d={}
    box(0,1,0,2,0,1,'#FDBA74',d);box(0,1,2,2,0,0,'#FFFFFF',d)
    box(0,1,2,3,2,3,'#FDBA74',d);d[(0,3,3)]='#111827';d[(1,3,3)]='#111827'
    d[(0,2,4)]='#FDBA74';d[(1,2,4)]='#FDBA74';d[(0,3,2)]='#F9A8D4'
    return d
def beam(x0,x1,z,y0=0,y1=3):
    d={}
    box(x0,x1,y0,y1,z,z,'#DC2626',d)
    for x in range(x0,x1+1,2):
        for y in (y0,y1): d[(x,y,z)]='#B91C1C'
    return d
def scene(levels,barrels,hammer_on=False,gor=1,L=26,gap=9):
    v={}
    for i in range(levels):
        z=i*gap
        v.update(beam(0,L,z))
    # ladders alternate ends
    for i in range(levels-1):
        x=(L-6) if i%2==0 else 3
        z=i*gap+1
        v.update(move(ladder(gap-1),x,1,z))
        # hole in beam above ladder
        for xx in range(x,x+4):
            v.pop((xx,1,(i+1)*gap),None);v.pop((xx,2,(i+1)*gap),None)
    top=(levels-1)*gap+1
    v.update(move(gorilla(),2,0,top))
    v.update(move(barrel(),12,0,top)) if levels<4 else None
    if gor>1: v.update(move(gorilla(),L-12,0,top-gap)) if False else None
    v.update(move(cat(),L-3,1,top))
    # barrels on lower levels
    pos=barrels
    for (lvl,x,y) in pos:
        v.update(move(barrel(),x,y,lvl*gap+1))
    v.update(move(worker(),3,0,1))
    if hammer_on: v.update(move(hammer(),L-14,1,gap+1) if levels>1 else {})
    return v
def full_scene(variant=3):
    if variant==1: return scene(2,[(0,13,0),(0,19,0),(1,16,0)],L=24)
    if variant==2: return scene(3,[(0,12,0),(1,9,0),(1,18,0),(2,16,0)],True,L=24)
    return scene(4,[(0,11,0),(0,19,0),(1,8,0),(2,14,0),(2,21,0),(3,17,0)],True,L=24)

ES=dict(
 title='Barril Loco',t1='BARRIL',t2='LOCO',tag='Un obrero tiene que subir por una obra esquivando los barriles que lanza un gorila, para rescatar a una gatita.',
 cover='Esquiva los barriles y sube hasta la gatita.',players='1 JUGADOR · MAGICAVOXEL + UNITY',final='VOXELART · PROYECTO FINAL',ex='EJEMPLO 21',
 gana='Llegando a la plataforma de arriba y rescatando a la gatita.',pierde='Si un barril te toca 3 veces o se acaba el tiempo.',
 leg=['G · Gorila (lanza barriles)','K · Gatita (meta)','O · Obrero (jugador)','B · Barril (peligro)','E · Escalera','M · Martillo (extra)','Viga (plataforma)'],
 maplab='El mapa de mi nivel',winl='Se gana',losel='Se pierde',pow='Mis poderes',powers=[('Saltar',' barriles'),('Trepar',' escaleras'),('Martillo',' que rompe barriles (extra)')],
 mv='En MagicaVoxel creo',models=[('Obrero','El jugador que escala la obra.'),('Gorila','Lanza barriles desde arriba.'),('Barril','Rueda y quita una vida.')],
 un='En Unity (Visual Scripting) programo',spells=[('CUANDO','pasan 3 segundos','ENTONCES','el gorila lanza un barril'),('CUANDO','el obrero toca un barril','ENTONCES','pierde 1 vida y el barril desaparece'),('CUANDO','coge el martillo','ENTONCES','rompe barriles durante 5 segundos')],
 hud1='VIDAS 3',hud2='NIVEL 2 · 0:42',hint='Flechas: moverse · Espacio: saltar · ↑ en la escalera: trepar',
 lv='Niveles: Barril Loco',lvl=['NIVEL 1','NIVEL 2','NIVEL 3'],nov='NOVEDAD',meta='META',
 nlv=[('Obra pequeña: 2 plataformas y pocos barriles.','Llegar arriba y rescatar a la gatita.'),('3 plataformas, barriles más rápidos y aparece el martillo.','Subir sin perder las 3 vidas.'),('Rascacielos: 4 plataformas y dos gorilas.','Llegar arriba antes de que acabe el tiempo.')],
 trans='El obrero llega a la gatita',how='¿CÓMO SE PASA AL SIGUIENTE NIVEL? (VISUAL SCRIPTING)',
 flow=[('EVENTO','Al entrar en el trigger: el obrero llega a la gatita'),('CONDICIÓN','¿Le quedan vidas?'),('ACCIÓN','Mostrar el mensaje de nivel superado y esperar 2 segundos'),('ACCIÓN','Cargar la escena del siguiente nivel')],
 notes=['Cada nivel es una escena de Unity (Nivel1, Nivel2, Nivel3) y todas se añaden a los ajustes de compilación (Build Settings).','Los puntos y las vidas se guardan en una variable de aplicación para no perderlos al cambiar de escena.','En el último nivel no se carga otra escena: se muestra la pantalla de victoria.'],suf=('póster','portada','pantalla de juego','niveles'),lang='es')
EU=dict(ES,
 title='Barril Zoroa',t1='BARRIL',t2='ZOROA',tag='Langile batek eraikuntza-obra bat igo behar du, gorila batek jaurtitzen dituen upelak saihestuz, katutxo bat erreskatatzeko.',
 cover='Saihestu upelak eta igo katutxora.',players='JOKALARI 1 · MAGICAVOXEL + UNITY',final='VOXELART · AZKEN PROIEKTUA',ex='ADIBIDEA 21',
 gana='Goiko plataformara iritsiz eta katutxoa erreskatatuz.',pierde='Upel batek 3 aldiz jotzen bazaitu edo denbora amaitzen bada.',
 leg=['G · Gorila (upelak jaurtitzen ditu)','K · Katutxoa (helmuga)','O · Langilea (jokalaria)','B · Upela (arriskua)','E · Eskailera','M · Mailua (extra)','Habea (plataforma)'],
 maplab='Nire mailaren mapa',winl='Irabazten da',losel='Galtzen da',pow='Nire ahalmenak',powers=[('Salto egin',' upelen gainetik'),('Igo',' eskailerak'),('Mailua',' upelak apurtzeko (extra)')],
 mv='MagicaVoxel-en sortzen dut',models=[('Langilea','Obra igotzen duen jokalaria.'),('Gorila','Goitik jaurtitzen ditu upelak.'),('Upela','Biraka dator eta bizitza bat kentzen du.')],
 un='Unity-n (Visual Scripting) programatzen dut',spells=[('NOIZ','3 segundo pasatzen dira','ORDUAN','gorilak upel bat jaurtitzen du'),('NOIZ','langileak upel bat ukitzen du','ORDUAN','bizitza 1 galtzen du eta upela desagertzen da'),('NOIZ','mailua hartzen du','ORDUAN','upelak apurtzen ditu 5 segundoz')],
 hud1='BIZITZAK 3',hud2='2. MAILA · 0:42',hint='Geziak: mugitu · Zuriune-barra: salto egin · ↑ eskaileran: igo',
 lv='Mailak: Barril Zoroa',lvl=['MAILA 1','MAILA 2','MAILA 3'],nov='BERRIA',meta='HELBURUA',
 nlv=[('Obra txikia: 2 plataforma eta upel gutxi.','Goraino igo eta katutxoa erreskatatu.'),('3 plataforma, upel azkarragoak eta mailua agertzen da.','Igo 3 bizitzak galdu gabe.'),('Zeru-harraskaria: 4 plataforma eta bi gorila.','Goraino iritsi denbora amaitu aurretik.')],
 trans='Langilea katutxora iristen da',how='NOLA PASATZEN DA HURRENGO MAILARA? (VISUAL SCRIPTING)',
 flow=[('GERTAERA','Trigger-ean sartzean: langilea katutxora iristen da'),('BALDINTZA','Bizitzarik geratzen zaio?'),('EKINTZA','Maila gainditu dela dioen mezua erakutsi eta 2 segundo itxaron'),('EKINTZA','Hurrengo mailako eszena kargatu')],
 notes=['Maila bakoitza Unity-ko eszena bat da (Maila1, Maila2, Maila3) eta guztiak konpilazio-ezarpenetan (Build Settings) gehitzen dira.','Puntuak eta bizitzak aplikazio-aldagai batean gordetzen dira, eszenaz aldatzean galdu ez daitezen.','Azken mailan ez da beste eszenarik kargatzen: garaipen-pantaila erakusten da.'],suf=('posterra','azala','jokoaren pantaila','mailak'),lang='eu')
T=ES if LANG=='es' else EU
BG='#1E293B';Y='#FBBF24';CARD='#FEF3C7';INK='#451A03'
FONT='<link href="https://fonts.googleapis.com/css2?family=Bungee&family=Nunito:wght@600;800&display=swap" rel="stylesheet">'
def page(title,body,css=''):
    return '<!doctype html><html lang="%s"><head><meta charset="utf-8"><title>%s</title>%s<style>body{margin:0}%s</style></head><body>%s</body></html>'%(T['lang'],title,FONT,css,body)
def sky(inner,w,h):
    # night skyline backdrop
    return inner
# ---------- poster
def tile(c,bg,fg='#12202B'): return '<div class="t" style="background:%s;color:%s">%s</div>'%(bg,fg,c)
BEAM='#DC2626';AIR='#334155'
mp=['G..B..K','=====E=','..B..E.','=E=====','O..M...']
col={'G':'#92400E','K':'#FDBA74','E':'#FBBF24','B':'#B45309','O':'#F97316','M':'#9CA3AF'}
cells=''
for r in mp:
    for ch in r:
        if ch=='=': cells+=tile('',BEAM)
        elif ch=='.': cells+=tile('',AIR)
        else: cells+=tile(ch,col[ch],'#FFFFFF' if ch in 'GB' else '#12202B')
legc=['#92400E','#FDBA74','#F97316','#B45309','#FBBF24','#9CA3AF',BEAM]
legend=''.join('<div class="lg"><div class="sw" style="background:%s"></div>%s</div>'%(c,t) for c,t in zip(legc,T['leg']))
mod=[worker(),gorilla(),barrel()]
cards=''.join('<div class="card">%s<b>%s</b><span>%s</span></div>'%(svg(m,None,120,'display:block;width:100%;height:120px;margin-bottom:10px;background:#334155;border-radius:8px'),a,b) for m,(a,b) in zip(mod,T['models']))
pw=''.join('<div class="card" style="padding:10px 14px"><span style="font-weight:800">%s</span><span>%s</span></div>'%p for p in T['powers'])
sp=''.join('<div class="card"><span style="font-weight:800">%s</span><span> %s</span><br><span style="font-weight:800">%s</span><span> %s</span></div>'%s for s in T['spells'])
css_p='''.t{aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;border-radius:5px;font-weight:800;font-size:22px;box-shadow:inset 0 -5px 0 rgba(0,0,0,.22),inset 0 4px 0 rgba(255,255,255,.25)}
.lab{margin:0 0 8px;font-size:14px;letter-spacing:.12em;font-weight:800;color:#FBBF24;text-transform:uppercase}
.card{background:#FEF3C7;color:#451A03;border-radius:12px;padding:14px;box-shadow:0 4px 0 rgba(0,0,0,.35)}
.card b{display:block;font-size:22px;line-height:1.1;margin-bottom:6px}.card span{font-size:15px;line-height:1.3}
.sw{width:16px;height:16px;border-radius:3px;flex:none}.lg{display:flex;align-items:center;gap:8px;font-size:15px}'''
poster='''<div style="width:720px;height:1320px;box-sizing:border-box;padding:40px;background:%(bg)s;color:#FFF;font-family:'Nunito',sans-serif;display:flex;flex-direction:column;justify-content:space-between;gap:16px">
<div style="display:flex;justify-content:space-between;align-items:center;font-size:14px;font-weight:800;letter-spacing:.12em"><span style="background:%(y)s;color:#451A03;padding:6px 12px;border-radius:999px">%(final)s</span><span>%(ex)s</span></div>
<h1 style="margin:0;font-family:'Bungee',sans-serif;font-size:66px;line-height:1;color:%(y)s;font-weight:400">%(title)s</h1>
<p style="margin:0;font-size:24px;line-height:1.3;font-weight:600">%(tag)s</p>
<div style="display:flex;gap:24px;align-items:flex-start"><div style="width:410px;flex:none"><p class="lab">%(maplab)s</p><div style="display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:3px">%(cells)s</div></div>
<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:12px"><div><p class="lab" style="margin-bottom:4px">%(winl)s</p><div style="font-size:16px;line-height:1.3">%(gana)s</div></div><div><p class="lab" style="margin-bottom:4px;color:#FCA5A5">%(losel)s</p><div style="font-size:16px;line-height:1.3">%(pierde)s</div></div><div style="display:flex;flex-direction:column;gap:6px">%(legend)s</div></div></div>
<div><p class="lab">%(pow)s</p><div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px">%(pw)s</div></div>
<div><p class="lab">%(mv)s</p><div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px">%(cards)s</div></div>
<div><p class="lab">%(un)s</p><div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px">%(sp)s</div></div></div>'''%dict(T,bg=BG,y=Y,cells=cells,legend=legend,pw=pw,cards=cards,sp=sp)
open('poster_%s.html'%LANG,'w',encoding='utf8').write(page(T['title']+', '+T['suf'][0],poster,css_p))
# ---------- portada
sc=svg(full_scene(3),None,None,'display:block;height:470px;width:auto')
outl='4px 0 0 #451A03,-4px 0 0 #451A03,0 4px 0 #451A03,0 -4px 0 #451A03,3px 3px 0 #451A03,-3px 3px 0 #451A03,3px -3px 0 #451A03,-3px -3px 0 #451A03,0 9px 0 #451A03'
portada='''<div style="position:relative;width:640px;height:880px;overflow:hidden;background:linear-gradient(#1E1B4B 0%%,#7C3AED 55%%,#FB923C 100%%);font-family:'Nunito',sans-serif;color:#FFF">
<div style="position:absolute;left:24px;top:22px;background:%(y)s;color:#451A03;padding:6px 14px;border-radius:999px;font-size:14px;font-weight:800;letter-spacing:.12em">%(final)s</div>
<h1 style="position:absolute;left:0;top:64px;width:640px;margin:0;text-align:center;font-family:'Bungee',sans-serif;font-weight:400;font-size:96px;line-height:.98;color:%(y)s;text-shadow:%(o)s">%(t1)s<br>%(t2)s</h1>
<div style="position:absolute;left:0;top:262px;width:640px;height:470px;display:flex;align-items:center;justify-content:center">%(sc)s</div>
<div style="position:absolute;left:0;bottom:0;width:640px;height:140px;box-sizing:border-box;padding:22px 40px 0;background:#451A03;text-align:center"><div style="font-size:26px;line-height:1.25;font-weight:800">%(cover)s</div><div style="margin-top:10px;font-size:15px;font-weight:600;letter-spacing:.08em;color:%(y)s">%(players)s</div></div></div>'''%dict(T,y=Y,o=outl,sc=sc)
open('portada_%s.html'%LANG,'w',encoding='utf8').write(page(T['title']+', '+T['suf'][1],portada))
# ---------- pantalla
sc2=svg(full_scene(2),None,None,'display:block;height:480px;width:auto')
skyl=''.join('<div style="position:absolute;bottom:0;left:%dpx;width:%dpx;height:%dpx;background:#1E1B4B;opacity:.55"></div>'%(x,w,h) for x,w,h in [(0,90,200),(100,70,280),(180,110,170),(300,80,240),(390,60,300),(460,100,190),(570,80,260),(660,110,210),(780,70,300),(860,100,180)])
pantalla='''<div style="position:relative;width:960px;height:540px;overflow:hidden;background:linear-gradient(#1E1B4B,#7C3AED 60%%,#FB923C);font-family:'Nunito',sans-serif">%(sk)s
<div style="position:absolute;left:0;top:0;width:960px;height:540px;box-sizing:border-box;padding-top:44px;display:flex;align-items:center;justify-content:center">%(sc)s</div>
<div class="hud" style="left:20px;top:20px">%(w)s<span>%(h1)s</span></div><div class="hud" style="right:20px;top:20px"><span>%(h2)s</span></div><div class="hint">%(hint)s</div></div>'''%dict(T,sk=skyl,sc=sc2,w=svg(worker(),25,34),h1=T['hud1'],h2=T['hud2'],hint=T['hint'])
css_s='''.hud{position:absolute;display:flex;align-items:center;gap:12px;background:rgba(0,0,0,.62);color:#FFF;border-radius:14px;padding:8px 18px;font-family:'Bungee',sans-serif;font-size:24px;line-height:1}
.hint{position:absolute;left:50%;bottom:16px;transform:translateX(-50%);background:rgba(0,0,0,.62);color:#FFF;border-radius:999px;padding:6px 16px;font-family:'Nunito',sans-serif;font-weight:800;font-size:15px;white-space:nowrap}'''
open('pantalla_%s.html'%LANG,'w',encoding='utf8').write(page(T['title']+', '+T['suf'][2],pantalla,css_s))
# ---------- niveles
arrow='<svg width="56" height="36" viewBox="0 0 56 36" aria-hidden="true" style="display:block"><path d="M2 12h30V3l22 15-22 15v-9H2z" fill="%s"/></svg>'%Y
arr2='<svg width="34" height="26" viewBox="0 0 34 26" aria-hidden="true" style="display:block;flex:none"><path d="M1 8h18V1l14 12-14 12v-7H1z" fill="%s"/></svg>'%Y
lcards=[]
for i in range(3):
    lcards.append('''<div style="width:340px;flex:none;background:#FEF3C7;color:#451A03;border-radius:16px;padding:14px;box-sizing:border-box;box-shadow:0 5px 0 rgba(0,0,0,.3)"><div style="display:inline-block;background:#451A03;color:#FFF;border-radius:999px;padding:5px 14px;font-family:'Bungee',sans-serif;font-size:18px;margin-bottom:10px">%s</div><div style="height:250px;display:flex;align-items:center;justify-content:center;background:#334155;border-radius:10px;overflow:hidden">%s</div><div style="margin-top:12px;font-size:13px;font-weight:800;letter-spacing:.1em">%s</div><div style="font-size:17px;line-height:1.3;min-height:44px">%s</div><div style="margin-top:8px;font-size:13px;font-weight:800;letter-spacing:.1em">%s</div><div style="font-size:17px;line-height:1.3;min-height:44px">%s</div></div>'''%(T['lvl'][i],svg(full_scene(i+1),None,None,'display:block;height:236px;width:auto'),T['nov'],T['nlv'][i][0],T['meta'],T['nlv'][i][1]))
mid='<div style="width:90px;flex:none;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;padding-top:170px;box-sizing:border-box"><div style="font-size:15px;font-weight:800;line-height:1.2">%s</div>%s</div>'%(T['trans'],arrow)
flow=arr2.join('<div style="flex:1;min-width:0;background:rgba(0,0,0,.35);border-radius:12px;padding:12px 14px;box-sizing:border-box"><div style="display:inline-block;background:%s;color:#451A03;border-radius:6px;padding:3px 8px;font-size:12px;font-weight:800;letter-spacing:.1em;margin-bottom:8px">%s</div><div style="font-size:17px;line-height:1.3;font-weight:800">%s</div></div>'%(Y,a,b) for a,b in T['flow'])
niv='''<div style="width:1280px;height:920px;box-sizing:border-box;padding:36px 40px;background:%(bg)s;color:#FFF;font-family:'Nunito',sans-serif;display:flex;flex-direction:column;justify-content:space-between">
<div style="display:flex;align-items:baseline;gap:18px"><h1 style="margin:0;font-family:'Bungee',sans-serif;font-weight:400;font-size:40px;line-height:1;color:%(y)s">%(lv)s</h1><span style="font-size:16px;font-weight:800;letter-spacing:.12em">%(final)s</span></div>
<div style="display:flex;align-items:flex-start;justify-content:space-between">%(c)s</div>
<div><div style="font-size:14px;font-weight:800;letter-spacing:.12em;color:%(y)s;margin-bottom:8px">%(how)s</div><div style="display:flex;align-items:stretch;gap:12px">%(flow)s</div>
<div style="margin-top:10px;font-size:15px;line-height:1.4;font-weight:600">%(notes)s</div></div></div>'''%dict(T,bg=BG,y=Y,c=mid.join(lcards),flow=flow,notes=''.join('<div>%s</div>'%n for n in T['notes']))
open('niveles_%s.html'%LANG,'w',encoding='utf8').write(page(T['title']+', '+T['suf'][3],niv))
# model sheet
