k=[4]*13+[8],[8]+[4]*13,[9]+[4]*11+[8],[11]+[4]*10+[11];m='`1234567890-=*','*QWERTYUIOP[]*',"*ASDFGHJKL;'*",'*ZXCVBNM,./*';c,d,e,n,u=0,'','|','\n','_'
for a in 0,1,2,3:
 f=s=t=o='';x=0
 for y in k[a]:g=y-2;f+=' '+u*y;s+=e*2+m[a][x].replace('*','%s')+' |';t+=e*2+u*g+e;o+='|/'+u*g+'\\';x+=1
 d+=f+n+s+e+n+t+e+n+o+e+n
l='SHIFT   ';print d%('BS   ','TAB  ','\\','CAPS  ','ENTER',l,l)
