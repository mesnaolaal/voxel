import json,re,html
uniq=json.load(open('/tmp/uniq.json'))
eu={}
for l in open('/tmp/eu.txt',encoding='utf8').read().splitlines():
    if l.strip():
        i,t=l.split('|',1);eu[int(i)]=t
tr={s:eu[i] for i,s in enumerate(uniq)}
ui={'Idea original: un RPG enorme con 10 mapas. Recortada a una sola cueva.':'Jatorrizko ideia: 10 mapako RPG erraldoi bat. Kobazulo bakar batera murriztua.','Idea original: "un personaje que explora y hace cosas". Concretada en un objetivo claro.':'Jatorrizko ideia: "arakatzen eta gauzak egiten dituen pertsonaia bat". Helburu argi batean zehaztua.','VOXELART · PROYECTO FINAL':'VOXELART · AZKEN PROIEKTUA','El mapa de mi nivel':'Nire mailaren mapa','Se gana':'Irabazten da','Se pierde':'Galtzen da','Mis poderes':'Nire ahalmenak','En MagicaVoxel creo':'MagicaVoxel-en sortzen dut','En Unity (Visual Scripting) programo':'Unity-n (Visual Scripting) programatzen dut','CUANDO':'NOIZ','ENTONCES':'ORDUAN'}
jobs=[l.strip().split('|') for f in ('jobs.txt','jobs2.txt') for l in open(f) if '-poster' in l]
miss=set();out=[]
for file,slug,w,h,o in jobs:
    t=open(f'/home/claude/voxel/project/{file}.dc.html',encoding='utf8').read()
    def rep(m):
        s=m.group(1);st=html.unescape(s.strip())
        if not st:return m.group(0)
        if re.fullmatch(r'EJEMPLO \d+',st):new='ADIBIDEA '+st.split()[1]
        elif st in ui:new=ui[st]
        elif st in tr:new=tr[st]
        elif len(st)<=2 or st.startswith('class Component'):return m.group(0)
        else:miss.add((slug,st)) if not (st.startswith(('body{','.t{')) or st.endswith('póster')) else None;return m.group(0)
        lead=s[:len(s)-len(s.lstrip())];trail=s[len(s.rstrip()):]
        return '>'+lead+html.escape(new,quote=False)+trail+'<'
    t2=re.sub(r'>([^<>]+)<',lambda m:rep(m) if rep(m).startswith('>') else m.group(0),t) if False else re.sub(r'>([^<>]+)<',rep,t)
    t2=t2.replace('<html lang="es">','<html lang="eu">')
    t2=re.sub(r'<title>(.*?), póster</title>',lambda m:'<title>'+tr.get(m.group(1),m.group(1))+', posterra</title>',t2)
    open(f'/home/claude/voxel/project/{file}-eu.dc.html','w',encoding='utf8').write(t2)
    out.append(f'{file}-eu|{slug}|{w}|{h}|{o}-eu')
open('jobs_eu.txt','w').write('\n'.join(out)+'\n')
print(len(out),'miss',sorted(miss)[:20])
