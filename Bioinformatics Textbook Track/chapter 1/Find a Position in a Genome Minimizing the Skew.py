S=input()
G,C=0,0
L=[]
mn=10000
for i in range(len(S)):
    if(S[i]=='G'):
        G+=1
    if(S[i]=='C'):
        C+=1
    if(G-C<=mn):
        if(G-C==mn):
            L.append(str(i+1))
        if(G-C<mn):
            mn=G-C
            L.clear()
            L.append(str(i+1))
S=" "
print(S.join(L))
