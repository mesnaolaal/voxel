import json,re,html,sys
exec(open('posters_eu.py',encoding='utf8').read().split("jobs=")[0])
ui.update({'VOXELART · PROYECTO FINAL':'VOXELART · AZKEN PROIEKTUA'})

G={'NOVEDAD':'BERRIA','META':'HELBURUA','EVENTO':'GERTAERA','CONDICIÓN':'BALDINTZA','ACCIÓN':'EKINTZA',
'¿CÓMO SE PASA AL SIGUIENTE NIVEL? (VISUAL SCRIPTING)':'NOLA PASATZEN DA HURRENGO MAILARA? (VISUAL SCRIPTING)',
'1 JUGADOR · MAGICAVOXEL + UNITY':'JOKALARI 1 · MAGICAVOXEL + UNITY','JEFE':'NAGUSIA',
'NIVEL 1':'MAILA 1','NIVEL 2':'MAILA 2','NIVEL 3':'MAILA 3',
'TIEMPO 0:38':'DENBORA 0:38','POSICIÓN 1º':'POSIZIOA 1.A','PLANCTON 2 / 5':'PLANKTONA 2 / 5','FUEGOS 1 / 4':'SUAK 1 / 4','SALVADOS 1 / 2':'SALBATUAK 1 / 2','INGREDIENTES 2 / 3':'OSAGAIAK 2 / 3','GOLPES 2':'KOLPEAK 2','HOYO 2 · PAR 3':'ZULOA 2 · PAR 3','PUERTAS 2 / 4':'ATEAK 2 / 4','HUEVOS 1 / 3':'ARRAUTZAK 1 / 3','CAJAS 1 / 3':'KUTXAK 1 / 3','MOVIMIENTOS 12':'MUGIMENDUAK 12','OLEADA 2 / 3':'OLATUA 2 / 3','FLORES 2 / 4':'LOREAK 2 / 4','BOMBAS 1 / 2':'BONBAK 1 / 2'}
T={'cofre-pirata':('PIRATAREN','KUTXA'),'gato-ninja':('KATU','NINJA'),'cueva-del-jefe':('NAGUSIAREN','KOBAZULOA'),'granja-perdida':('BASERRI','GALDUA'),'rally-voxel':('RALLY','VOXEL'),'templo-perdido':('TENPLU','GALDUA'),'vallas-voxel':('HESI','VOXEL'),'regata-voxel':('VOXEL','ERREGATA'),'pez-hambriento':('ARRAIN','GOSETUA'),'mision-espacial':('ESPAZIO','MISIOA'),'bombero-voxel':('SUHILTZAILE','VOXEL'),'casa-encantada':('ETXE','SORGINDUA'),'pasteleria-loca':('GOZOTEGI','ZOROA'),'minigolf-voxel':('MINIGOLF','VOXEL'),'valle-nevado':('ELUR','HARANA'),'dino-parque':('DINO','PARKEA'),'robot-fabrica':('ROBOT','FABRIKA'),'defensa-castillo':('GAZTELUAREN','DEFENTSA'),'jardin-abejas':('ERLEEN','LORATEGIA'),'laberinto-dinamita':('DINAMITA','LABIRINTOA')}
TES={'cofre-pirata':('COFRE','PIRATA'),'gato-ninja':('GATO','NINJA'),'cueva-del-jefe':('LA CUEVA','DEL JEFE'),'granja-perdida':('LA GRANJA','PERDIDA'),'rally-voxel':('RALLY','VOXEL'),'templo-perdido':('EL TEMPLO','PERDIDO'),'vallas-voxel':('VALLAS','VOXEL'),'regata-voxel':('REGATA','VOXEL'),'pez-hambriento':('EL PEZ','HAMBRIENTO'),'mision-espacial':('MISIÓN','ESPACIAL'),'bombero-voxel':('BOMBERO','VOXEL'),'casa-encantada':('CASA','ENCANTADA'),'pasteleria-loca':('PASTELERÍA','LOCA'),'minigolf-voxel':('MINIGOLF','VOXEL'),'valle-nevado':('VALLE','NEVADO'),'dino-parque':('DINO','PARQUE'),'robot-fabrica':('ROBOT','FÁBRICA'),'defensa-castillo':('DEFENSA','CASTILLO'),'jardin-abejas':('JARDÍN DE','ABEJAS'),'laberinto-dinamita':('LABERINTO','DINAMITA')}
COV={'cofre-pirata':'Bildu 5 txanponak eta ireki altxor-kutxa.','gato-ninja':'Saihestu robotak eta ihes egin teilatuko atetik.','cueva-del-jefe':'Garaitu munstroa eta lortu kristala.','granja-perdida':'Aurkitu 4 oiloak iluntzea baino lehen.','rally-voxel':'Zeharkatu helmuga denbora amaitu aurretik.','templo-perdido':'Aurkitu giltza, saihestu slime-ak eta ireki tenplua.','vallas-voxel':'Jauzi hesiak eta zeharkatu helmuga lehenengo.','regata-voxel':'Inguratu boiak eta zeharkatu helmuga denak baino lehen.','pez-hambriento':'Jan planktona, saihestu marrazoak eta iritsi kobazulora.','mision-espacial':'Bildu kristalak eta iritsi planetara talka egin gabe.','bombero-voxel':'Itzali suak eta erreskatatu guztiak.','casa-encantada':'Aurkitu giltzak eta ihes egin mamuengandik.','pasteleria-loca':'Bildu osagaiak eta entregatu tarta.','minigolf-voxel':'Sartu bola zuloan kolpe gutxitan.','valle-nevado':'Jaitsi mendia bidetik atera gabe.','dino-parque':'Erreskatatu arrautzak T-Rex-ak aurkitu aurretik.','robot-fabrica':'Bultzatu kutxak dagokien tokira.','defensa-castillo':'Jarri dorreak eta defendatu gaztelua.','jardin-abejas':'Pospolatu loreak eta itzuli erlauntzera.','laberinto-dinamita':'Apurtu kutxak, saihestu slime-ak eta ihes egin.'}
import json as _j
TITLE_EU={g['title']:tr.get(g['title'],g['title']) for g in _j.load(open('games.json'))}

COVES={g['slug']:g['cover'] for g in _j.load(open('games.json'))}
jobs=[l.strip().split('|') for f in ('jobs.txt','jobs2.txt') for l in open(f) if l.strip() and '-poster' not in l]
miss={};out=[]
for file,slug,w,h,o in jobs:
    t=open(f'/home/claude/voxel/project/{file}.dc.html',encoding='utf8').read()
    def rep(m):
        s=m.group(1);st=html.unescape(s.strip())
        if not st or len(st)<=2 or st.startswith(('body{','class Component','.')) or '{' in st:return m.group(0)
        if st in (TES[slug]): new=T[slug][TES[slug].index(st)]
        elif st==COVES[slug]: new=COV[slug]
        elif st in G: new=G[st]
        elif st.startswith('Niveles: '): new='Mailak: '+TITLE_EU.get(st[9:],st[9:])
        elif re.fullmatch(r'(.*), (portada|pantalla de juego|niveles)',st): m2=re.fullmatch(r'(.*), (portada|pantalla de juego|niveles)',st); new=TITLE_EU.get(m2.group(1),m2.group(1))+', '+{'portada':'azala','pantalla de juego':'jokoaren pantaila','niveles':'mailak'}[m2.group(2)]
        elif re.fullmatch(r'EJEMPLO \d+',st):new='ADIBIDEA '+st.split()[1]
        elif st in ui:new=ui[st]
        elif st in tr:new=tr[st]
        else:miss.setdefault(st,[]).append(slug);return m.group(0)
        lead=s[:len(s)-len(s.lstrip())];trail=s[len(s.rstrip()):]
        return '>'+lead+html.escape(new,quote=False)+trail+'<'
    t2=re.sub(r'>([^<>]+)<',rep,t).replace('<html lang="es">','<html lang="eu">')
    open(f'/home/claude/voxel/project/{file}-eu.dc.html','w',encoding='utf8').write(t2)
    out.append(f'{file}-eu|{slug}|{w}|{h}|{o}-eu')
open('jobs_eu2.txt','w').write('\n'.join(out)+'\n')
print(len(out));
for k,v in miss.items():print(len(v),repr(k[:90]))
