import json,re,glob,os
u=json.load(open('/tmp/ulits.json'))
tr={}
for l in open('/tmp/eu2.txt',encoding='utf8').read().splitlines():
    if '|' in l:
        i,t=l.split('|',1);tr[u[int(i)]]=t.strip()
extra="""(ideal: =>(egokiena:
asteroide(s)=>asteroide
caja(s) y =>kutxa eta
calabaza(s) y Puerta=>kalabaza eta Atea
cangrejo(s)=>karramarro
cono(s),=>kono,
cristal(es),=>kristal,
fantasma(s) paralizado(s) 3 s=>mamu geldituta 3 s-z
fantasma(s),=>mamu,
flor(es),=>lore,
fuego(s),=>su,
gallina(s)=>oilo
gallinas=>oilo
golpes=>kolpe
huevo(s),=>arrautza,
llave(s) y Salida=>giltza eta Irteera
llave(s),=>giltza,
mancha(s),=>orban,
medusa(s)=>medusa
ovni(s)=>ufo
plancton=>plankton
puerta(s),=>ate,
rival(es),=>arerio,
robot(s),=>robot,
slime(s)=>slime
valla(s)=>hesi
vidas),=>bizitza),
y Cueva=>eta Kobazuloa
y Meta=>eta Helmuga
y Planeta=>eta Planeta
zorro(s)=>azeri
∩ Castillo)=>∩ Gaztelua)
∩ Dino)=>∩ Dinoa)
∩ Nave)=>∩ Ontzia)
∩ Pez)=>∩ Arraina)
, Agua=>, Ura
, Molino=>, Errota
, llave=>, giltza
, puerta=>, atea
Asteroide=>Asteroidea
Cofre=>Kutxa
Esbirro=>Morroia
Escondido=>Ezkutatuta
Espacio: deshacer=>Zuriunea: desegin
Fresa=>Marrubia
Goblin=>Goblina
Golpes: =>Kolpeak: 
Harina=>Irina
Huevo=>Arrautza
Lava=>Laba
Llave: =>Giltza: 
Llave: —=>Giltza: —
Manos: =>Eskuak: 
Monstruo=>Munstroa
NO (ideal: =>EZ (egokiena: 
Ogro=>Ogroa
Ovni=>Ufoa
Puntos: =>Puntuak: 
Saltando…=>Jauzi egiten…
Vela: =>Bela: 
Volando=>Hegan
cazada=>estua
media=>erdia
suelta=>askea
esbirro=>morroia
goblin=>goblina
monstruo=>munstroa
ogro=>ogroa
SÍ=>BAI
NO=>EZ"""
ex={}
for l in extra.split('\n'):
    a,b=l.split('=>',1);ex[a]=b
# exact-match (with whitespace-sensitive) extras: keys where original has spaces handled by strip
def conv(s):
    st=s.strip()
    if st in ('SÍ','NO') : return s.replace(st,ex[st])
    if s in tr or st in tr:
        t=tr.get(s,tr.get(st))
        lead=s[:len(s)-len(s.lstrip())];trail=s[len(s.rstrip()):]
        return lead+t+trail
    # extras: match on stripped and also raw
    for k in (s,st):
        if k in ex:
            t=ex[k];lead=s[:len(s)-len(s.lstrip())];trail=s[len(s.rstrip()):]
            return lead+(t if k==s and t!=t.strip() else t.strip())+trail
    return None
NAMES={'bombero3d':'Suhiltzaile Voxel','casa3d':'Etxe Sorgindua','regata3d':'Voxel Erregata','templo3d':'Tenplu Galdua','valle3d':'Elur Harana','abejas3d':'Erleen Lorategia','castillo3d':'Gazteluaren Defentsa','cofre3d':'Pirataren Kutxa','cueva3d':'Nagusiaren Kobazuloa','dino3d':'Dino Parkea','espacio3d':'Espazio Misioa','gato3d':'Katu Ninja','golf3d':'Minigolf Voxel','granja3d':'Baserri Galdua','pasteleria3d':'Gozotegi Zoroa','pez3d':'Arrain Gosetua','rally3d':'Rally Voxel','robot3d':'Robot Fabrika','vallas3d':'Hesi Voxel','laberinto':'Dinamita Labirintoa'}
BTN={'bombero3d':'URA BOTA<br>(eutsi Zuriunea)','casa3d':'HARTU / LANTERNA<br>(Zuriunea)','regata3d':'BELA<br>(Zuriunea)','templo3d':'EZPATA<br>(Zuriunea)','valle3d':'BALAZTATU<br>(Zuriunea)','abejas3d':'PAUSATU<br>(Zuriunea)','castillo3d':'ERAIKI<br>(Zuriunea)','cofre3d':'JAUZI<br>(Zuriunea)','cueva3d':'ERASO<br>(Zuriunea)','dino3d':'KORRIKA<br>(Zuriunea)','espacio3d':'TIRO EGIN<br>(Zuriunea)','gato3d':'JAUZI<br>(Zuriunea)','golf3d':'KOLPATU<br>(eutsi eta askatu)','granja3d':'JAUZI<br>(Zuriunea)','pasteleria3d':'HARTU / UTZI<br>(Zuriunea)','pez3d':'ESPRINTATU<br>(Zuriunea)','rally3d':'TURBOA<br>(Zuriunea)','robot3d':'DESEGIN<br>(Zuriunea)','vallas3d':'JAUZI<br>(Zuriunea)','laberinto':'DINAMITA<br>(Zuriunea)'}
HELP={
'bombero3d':'Geziak edo WASD mugitzeko · eutsi Zuriunea begiratzen duzun tokira ura botatzeko (depositua husten da). Bete ezazu hidrantearen ondoan geldituz. Itzali su guztiak, erreskatatu pertsonak ukituz eta saihestu sugarrak denbora amaitu aurretik.',
'casa3d':'Geziak edo WASD mugitzeko · Zuriunea: giltza bat hartu ondoan baduzu; bestela, lanterna pizten du (inguruko mamuak 3 s-z geldiarazten ditu, 4 s-z birkargatzen da). Bildu giltza guztiak eta ukitu atea. Saihestu mamuak eta kalabazak.',
'regata3d':'◀ ▶ lema · Zuriunea: bela doitu (estua → erdia → askea) · ▲ bultzada (3 maila bakoitzeko). Ontziaren gaineko geziak hurrengo boia erakusten du. Belak errendimendu handiagoa du haizearen angeluarekin bat badator (mastako banderak haizea nondik datorren adierazten du): haizearen aurka, estua; alboan, erdia; haizea popatik, askea. Inguratu 3 boiak, saihestu harkaitzak eta zeharkatu helmuga garaiz.',
'templo3d':'Geziak edo WASD mugitzeko · Zuriunea: ezpata-kolpea begiratzen duzun tokira. Hartu giltza, ireki atea eta heldu altxorrera. Slimeek bihotz bat kentzen dizute ukitzen bazaituzte; harrizko zaindariak 5 kolpe jasaten ditu. Bihotz gorriek sendatu egiten zaituzte.',
'valle3d':'◀ ▶ eskiatzeko · Zuriunea: balaztatu · ▼ turboa maldan. Pasatu ate bakoitzeko makilen artetik (berde jartzen dira) eta saihestu zuhaitzak eta elur-gizonak.',
'abejas3d':'Geziak edo WASD hegan egiteko · Zuriunea: inguruko lore batean pausatu eta polinizatu · Maius: armiarmak izutzen dituen burrunba. Polinizatu lore guztiak eta itzuli erlauntzera. 3 bizitza dituzu.',
'castillo3d':'Klik edo ukitu zuloa grisean: dorre bat eraiki (50). Klik dorre batean: hobetu (40). Teklatuarekin: ← → zuloa aukeratu, Zuriunea eraiki edo hobetu, R gaztelua konpondu (30). Garaitutako etsai bakoitzak txanponak ematen ditu. Gaztelura iristen bazaizkizu, bizitzak galtzen ditu.',
'cofre3d':'Geziak edo WASD mugitzeko · Zuriunea: jauzi egin (ur-putzuak eta gelaxka bateko ur-kanalak zeharkatzeko balio du). Bildu 5 txanponak eta ireki kutxa denbora amaitu aurretik. Uretara erortzen bazara, hasierara itzultzen zara; karramarroek 4 segundo kentzen dizkizute.',
'cueva3d':'Geziak edo WASD mugitzeko · Zuriunea: ezpatarekin kolpatu begiratzen duzun tokira. Munstroek jarraitzen zaituzte: garaitu (nagusiak kolpe gehiago jasaten ditu) eta hartu kristala. 3 bizitza dituzu.',
'dino3d':'Geziak edo WASD mugitzeko · Maius edo Zuriunea: une batez korrika egin. Bildu arrautzak eta eraman habiara. T-Rex-ak harrapatzen zaitu ikusten bazaitu: ezkutatu palmondoen ondoan. Saihestu laba. 3 bizitza dituzu.',
'espacio3d':'Geziak edo WASD ontzia gora, behera, ezkerrera eta eskuinera mugitzeko · Zuriunea: asteroideei tiro egin · Eutsi Maius propultsorrerako (abiadura handiagoa, teklatuan bakarrik). Bildu kristal guztiak eta ukitu planeta. Saihestu asteroideak eta ufoak: 3 bizitza dituzu.',
'gato3d':'Geziak edo WASD teilatuetan mugitzeko · Zuriunea: jauzi egin (teilatuen arteko zuloak, eta baita robot baten gainetik ere). Hartu giltza guztiak eta heldu atera inongo robotek ukitu gabe.',
'golf3d':'← → (edo A/D): zuzendu (Maius: fintzeko) · Eutsi Zuriunea indarra kargatzeko eta askatu kolpatzeko. Sartu bola zuloan kolpe gutxirekin. 3 aldiz uretara erortzen bada, galtzen duzu.',
'granja3d':'Geziak edo WASD mugitzeko · Zuriunea: hesiak saltatu. Aurkitu oilo guztiak gaua jo aurretik. Azeriek 5 segundo kentzen dizkizute.',
'pasteleria3d':'Geziak edo WASD sukaldaria mugitzeko · Zuriunea: osagaia apalean hartu, labean sartu (errezetaren ordenan), tarta hartu eta mahaian utzi · Maius: korrika egin. Hurbildu objektura Zuriunea sakatu aurretik.',
'pez3d':'Geziak edo WASD igeri egiteko · Zuriunea: hegatsarekin esprintatu. Jan plankton guztia eta sartu kobazulora. Medusek eta marrazoak bizitza bat kentzen dizute (3 dituzu); algen artean ezkutatzen zara.',
'rally3d':'Geziak edo WASD: ↑ azeleratu, ↓ balaztatu / atzera, ← → biratu · Zuriunea: turboa. Heldu helmugara denbora amaitu aurretik. Konoek eta olioak moteltzen zaituzte, bidoi horiek +5 s ematen dituzte eta errepidetik kanpo oso mantso zoaz.',
'robot3d':'Geziak edo WASD: robota mugitu, kutxak bultzatzen ditu (bat aldi berean, inoiz ez tiratu). Eraman kutxa guztiak zona horietara. Zuriunea: azken mugimendua desegin. Kutxa bat izkinan geratzen bada helburutik kanpo, galtzen duzu.',
'vallas3d':'Eutsi ↑ edo → korrika egiteko · Zuriunea: hesiak saltatu (eta 3. mailako zuloa) · Maius: esprintatu (teklatua). Zeharkatu helmuga zure arerioak baino lehen; hesi bat ukitzen baduzu, abiadura galtzen duzu.',
'laberinto':'Geziak edo WASD mugitzeko · Zuriunea dinamita jartzeko. Apurtu kaxoiak, saihestu edo garaitu slimeak eta heldu ate horira. Ez gelditu leherketaren gurutzean.'}
SUB='Proiektu-adibidearen jokoa 3D-n. Eskuinean ikusiko duzu une bakoitzean Visual Scripting-eko zein GERTAERA → BALDINTZA → EKINTZA aktibatzen den.'
SUB2='Proiektu-adibidearen jokoa. Eskuinean ikusiko duzu une bakoitzean Visual Scripting-eko zein GERTAERA → BALDINTZA → EKINTZA aktibatzen den.'
os.makedirs('/home/claude/simeu/out',exist_ok=True)
files=sorted(glob.glob('/home/claude/gen/sim3/*3d.html')+glob.glob('/home/claude/gen/sim/*3d.html'))+['/home/claude/gen/laberinto.html']
miss={}
for f in files:
    key=os.path.basename(f).replace('.html','')
    t=open(f,encoding='utf8').read()
    i=t.find('<script src=') if '<script src=' in t else t.find('<script')
    # head
    h=t[:i];sc=t[i:]
    h=h.replace('<html lang="es">','<html lang="eu">')
    h=re.sub(r'<title>.*?</title>','<title>'+NAMES[key]+(' – Jokoa 3D' if key!='laberinto' else ' – Jokoa')+'</title>',h)
    h=re.sub(r'(<h1>)[^<]*',lambda m:m.group(1)+NAMES[key]+' ',h,count=1)
    h=re.sub(r'<p class="sub">.*?</p>','<p class="sub">'+(SUB2 if key=='laberinto' else SUB)+'</p>',h,flags=re.S)
    h=re.sub(r'(<button class="bomb"[^>]*>).*?(</button>)',lambda m:m.group(1)+BTN[key]+m.group(2),h,flags=re.S)
    h=re.sub(r'<p class="help">.*?</p>','<p class="help">'+HELP[key]+'</p>',h,flags=re.S)
    for a,b in [('aria-label="Arriba"','aria-label="Gora"'),('aria-label="Izquierda"','aria-label="Ezkerrera"'),('aria-label="Abajo"','aria-label="Behera"'),('aria-label="Derecha"','aria-label="Eskuinera"'),('Visual Scripting en vivo','Visual Scripting zuzenean'),('Reiniciar partida','Partida berrabiarazi')]:
        h=h.replace(a,b)
    def rep(m):
        q=m.group(0)[0]
        if q=='`':return m.group(0)
        s=m.group(1) if m.group(1) is not None else m.group(2)
        c=conv(s)
        if c is None:
            return m.group(0)
        c=c.replace('\\','\\\\').replace(q,'\\'+q) if False else c
        return q+c+q
    sc2=re.sub(r"'((?:[^'\\\n]|\\.)*)'|\"((?:[^\"\\\n]|\\.)*)\"",rep,sc)
    open('/home/claude/simeu/out/'+key+'.html','w',encoding='utf8').write(h+sc2)
print('ok',len(files))
