import json,re,sys
src=open('/home/claude/barril/gen.py',encoding='utf8').read()
ns={'LANG':'es'};exec(src[:src.index('T=ES if')].replace("import sys\nLANG=sys.argv[1] if len(sys.argv)>1 else 'es'",""),ns)
def game(lang):
    T=ns['ES'] if lang=='es' else ns['EU']
    eu=lang=='eu'
    return {"n":21,"slug":"barril-loco","title":T['title'],"tag":T['tag'],"gana":T['gana'],"pierde":T['pierde'],"legend":T['leg'],
     "powers":[[a,b.strip()] for a,b in T['powers']],"models":[[a,b] for a,b in T['models']],"spells":[[s[1],s[3]] for s in T['spells']],
     "levels":[{"n":str(i+1),"nov":T['nlv'][i][0],"meta":T['nlv'][i][1],"pasa":(T['trans'] if i<2 else None)} for i in range(3)],
     "flow":[[a.capitalize(),b] for a,b in T['flow']],"notes":T['notes'],"hint":T['hint'],"lv":3,"lvname":"Zaila" if eu else "Difícil",
     "why":("Erortzen eta biraka dabiltzan upelak, eskailerak, jauziak, mailua, bizitzak eta denbora." if eu else "Barriles que ruedan y caen, escaleras, saltos, martillo, vidas y tiempo.")}
def patch(path,lang,sim,label):
    s=open(path,encoding='utf8').read()
    if '"barril-loco"' in s: return 'already'
    i=s.index('const GAMES = ');j=s.index('];',i)+1
    g=json.loads(s[i+len('const GAMES = '):j])
    orig=s[i+len('const GAMES = '):j]
    ind=None
    for cand in (2,1,None):
        if json.dumps(g,ensure_ascii=False,indent=cand)==orig: ind=cand;break
    else: raise SystemExit('format mismatch '+path)
    g.append(game(lang))
    s=s[:i+len('const GAMES = ')]+json.dumps(g,ensure_ascii=False,indent=ind)+s[j:]
    s=s.replace("const SIMS = {\n","const SIMS = {\n '%s':['%s','%s'],\n"%('barril-loco',sim,label),1)
    if lang=='es':
        s=s.replace('<h1>20 ideas de videojuego','<h1>21 ideas de videojuego').replace('20 ejemplos de proyecto final','21 ejemplos de proyecto final')
    else:
        s=s.replace('<h1>20 bideojoku-ideia','<h1>21 bideojoku-ideia').replace('20 proiektu-adibide','21 proiektu-adibide')
    open(path,'w',encoding='utf8').write(s);return 'ok'
if __name__=='__main__':
    print(patch(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]))
