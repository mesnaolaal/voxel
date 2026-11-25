for(var n=0;n<3;n++){loadLevel(n);var st=0;S.sel=0;onSpace();while(S.mode==='play'&&st<60000){st++;update(0.016)}console.log('nivel',n+1,'una torre:',S.mode,S.chp+'/'+S.L.hp)}
