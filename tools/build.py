import json, re
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('style','script','svg'): s.skip+=1
    def handle_endtag(s,t):
        if t in('style','script','svg'): s.skip-=1
    def handle_data(s,d):
        if not s.skip and d.strip(): s.out.append(d.strip())
def txt(f):
    p=P(); p.feed(open('/home/claude/voxel/project/%s.dc.html'%f,encoding='utf-8').read()); return p.out
games=[('cofre-pirata','Main','Cofre-Pirata'),('gato-ninja','Gato-Ninja','Gato-Ninja'),('cueva-del-jefe','Cueva-del-Jefe','Cueva-del-Jefe'),('granja-perdida','Granja-Perdida','Granja-Perdida'),
('rally-voxel',None,'Rally-Voxel'),('templo-perdido',None,'Templo-Perdido'),('vallas-voxel',None,'Vallas-Voxel'),('regata-voxel',None,'Regata-Voxel'),('pez-hambriento',None,'Pez-Hambriento'),
('mision-espacial',None,'Mision-Espacial'),('bombero-voxel',None,'Bombero-Voxel'),('casa-encantada',None,'Casa-Encantada'),('pasteleria-loca',None,'Pasteleria-Loca'),('minigolf-voxel',None,'Minigolf-Voxel'),
('valle-nevado',None,'Valle-Nevado'),('dino-parque',None,'Dino-Parque'),('robot-fabrica',None,'Robot-Fabrica'),('defensa-castillo',None,'Defensa-Castillo'),('jardin-abejas',None,'Jardin-Abejas'),('laberinto-dinamita',None,'Laberinto-Dinamita')]
out=[]
for n,(slug,pf,name) in enumerate(games,1):
    t=txt(pf if pf else 'Poster-'+name)
    i_g=t.index('Se gana'); i_p=t.index('Se pierde'); i_pw=t.index('Mis poderes'); i_mv=t.index('En MagicaVoxel creo'); i_un=[k for k,v in enumerate(t) if v.startswith('En Unity')][0]
    g=dict(n=n,slug=slug,title=t[3],tag=t[4],gana=t[i_g+1],pierde=t[i_p+1])
    g['legend']=t[i_p+2:i_pw]
    pw=t[i_pw+1:i_mv]; g['powers']=[[pw[k],pw[k+1]] for k in range(0,len(pw)-1,2)]
    md=t[i_mv+1:i_un]; g['models']=[[md[k],md[k+1]] for k in range(0,len(md)-1,2)]
    sp=t[i_un+1:]; g['spells']=[[sp[k+1],sp[k+3]] for k in range(0,len(sp)-3,4)]
    nv=txt('Niveles-'+name)
    lv=[]; k=0
    while k<len(nv):
        if re.fullmatch(r'NIVEL \d',nv[k]):
            lvl=dict(n=nv[k][-1],nov=nv[k+2],meta=nv[k+4],pasa=None)
            nxt=nv[k+5]
            if not nxt.startswith('NIVEL') and not nxt.startswith('¿CÓMO'): lvl['pasa']=nxt
            lv.append(lvl)
        k+=1
    ic=[k for k,v in enumerate(nv) if v.startswith('¿CÓMO')][0]
    g['levels']=lv
    g['flow']=[['Evento',nv[ic+2]],['Condición',nv[ic+4]],['Acción',nv[ic+6]],['Acción',nv[ic+8]]]
    g['notes']=nv[ic+9:]
    pt=txt('Pantalla-'+name); g['hint']=pt[-1]
    g['cover']=txt('Portada-'+name)[-2]
    out.append(g)
    assert len(lv)==3 and len(g['spells'])==3 and len(g['powers']) in (2,3) and len(g['models']) in (2,3,4) and len(g['notes'])==3,(slug,len(lv),len(g['spells']),len(g['powers']),len(g['models']),g['notes'])
json.dump(out,open('games.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps(out[17],ensure_ascii=False,indent=1)[:2500])
