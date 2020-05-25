a=list(map(int,input().split()))

A=set()
B=set()
A_L=[]
T=[]
P=[]
mass_D={}
F_peptide=[]

for i in a:
    if(i<=186):
        A_L.append(i)
        T.append(0)
    if(i not in A):
        mass_D.update({i:1})
        A.add(i)
    else:
        mass_D.update({i:mass_D[i]+1})
        
n=len(A_L)
D=mass_D.copy()

def cyclospectrum(peptide):
    dict=D.copy()
    mass_list=[]
    s=peptide+peptide
    k=1
    f=1
    while(k<len(peptide)):
        for i in range(len(peptide)):
            mass=s[i:i+k]
            d=sum(mass)
            if(d in dict and dict[d]>0):
                mass_list.append(d)
                dict.update({d:dict[d]-1})
            else:
                f=0
                break
        if(f==0):
            break
        k+=1
    mass_list.append(sum(peptide))
    if(f==0):
        return 0
    else:
        return 1
            
def outfit(peptide):
    s=""
    for i in range(len(peptide)):
        if(i==len(peptide)-1):
            s+=str(peptide[i])
        else:
            s+=str(peptide[i])+"-"
    return s

def backtrack(mass):
    
    if(len(P)==n):
        g=cyclospectrum(P)
        peptide=outfit(P)
        if(g==1 and peptide not in B):
            F_peptide.append(peptide)
            B.add(peptide)
        return 
    
    for i in range(len(A_L)):
        if(mass+A_L[i] in A):
            if(T[i]==0 and mass_D[mass+A_L[i]]>0):
                T[i]=1
                P.append(A_L[i])
                mass_D.update({mass+A_L[i]:mass_D[mass+A_L[i]]-1})
                mass+=A_L[i]
                backtrack(mass)
                T[i]=0
                del P[len(P)-1]
                mass-=A_L[i]
                mass_D.update({mass+A_L[i]:mass_D[mass+A_L[i]]+1})


            
backtrack(0)
Ans=""
for i in F_peptide:
    Ans+=i+" "
print(Ans)

