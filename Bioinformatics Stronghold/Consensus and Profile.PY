file=open("rosalind_cons.txt","r")
A,C,G,T=[],[],[],[]
for i in range(0,2005):
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)
f,str1=0,""
for i in file:
    if(i[0]=='>' and f==1):
        for j in range(len(str1)):
            if(str1[j]=='A'):
                A[j]+=1
            if(str1[j]=='C'):
                C[j]+=1
            if(str1[j]=='G'):
                G[j]+=1
            if(str1[j]=='T'):
                T[j]+=1
        str1=""
    elif(i[0]!='>'):    
        str1+=i.strip('\n')
        f=1
for i in range(len(str1)):
    if(str1[i]=='A'):
        A[i]+=1
    if(str1[i]=='C'):
        C[i]+=1
    if(str1[i]=='G'):
        G[i]+=1
    if(str1[i]=='T'):
        T[i]+=1
a,c,g,t="","","",""
for i in range(len(str1)):
    a+=" "+str(A[i])
    c+=" "+str(C[i])
    g+=" "+str(G[i])
    t+=" "+str(T[i])
final=""
mx=-99
for i in range(len(str1)):
    mx=max(A[i],C[i],G[i],T[i])
    if(A[i]==mx):
        final+='A'
    elif(C[i]==mx):
        final+='C'
    elif(G[i]==mx):
        final+='G'
    elif(T[i]==mx):
        final+='T'
print(final)
print("A:"+a)
print("C:"+c)
print("G:"+g)
print("T:"+t)
