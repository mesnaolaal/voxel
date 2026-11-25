import re,sys
name,autofile=sys.argv[1],sys.argv[2]
s=open(name).read()
js=re.search(r'<script>\n\(function(.*)\}\)\(\);\n</script>',s,re.S)
body="(function"+js.group(1)
body=body.replace("new THREE.WebGLRenderer({antialias:true})","{setPixelRatio(){},setSize(){},domElement:{},render(){}}").replace("stage.insertBefore(renderer.domElement,stage.firstChild);","").replace("newGame();requestAnimationFrame(loop);","newGame();")
t=open('/tmp/t3.js').read();head=t[:t.index("(function")]
head=head.replace("var THREE=require('/tmp/thr/package/build/three.min.js');","") if "var THREE" in head else head
head="var THREE=require('/tmp/thr/package/build/three.min.js');\n"+head
open('/tmp/auto_run.js','w').write(head+body+"\n"+open(autofile).read()+"\n})();\n")
