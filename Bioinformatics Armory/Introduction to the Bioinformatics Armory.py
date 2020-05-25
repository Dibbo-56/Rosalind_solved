s=input()
a,c,g,t=0,0,0,0

for i in range(len(s)):
    if(s[i]=='A'):
        a+=1
    elif(s[i]=='C'):
        c+=1
    elif(s[i]=='G'):
        g+=1
    elif(s[i]=='T'):
        t+=1
print(str(a)+" "+str(c)+" "+str(g)+" "+str(t))
