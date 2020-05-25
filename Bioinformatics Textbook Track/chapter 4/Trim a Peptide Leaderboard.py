import operator

dict={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

peptides=list(map(str,input().split()))
spectrum=list(map(int,input().split()))
n=int(input())

leaderboard={}
A=set()
S_L=[]
L_L=[]

def Linera_spectrum(peptide):
    
    mass_list=[]
    k=1
    mass_list.append(0)
    
    def calu_mass(s):
        mass=0
        for i in s:
            mass+=dict[i]
        return mass
    
    while(k<len(peptide)):
        for i in range(len(peptide)-k+1):
            s=peptide[i:i+k]
            mass_list.append(calu_mass(s))
        k+=1

    mass_list.append(calu_mass(peptide))
    mass_list.sort()
    
    return mass_list


def compute_score(theoretical):
    A=set()
    score=0
    
    for i in theoretical:
        if(i not in A):
            A.add(i)
            E=experimental.count(i)
            T=theoretical.count(i)
            score+=min(E,T)
    
    return score


experimental=[]

for i in spectrum:
    experimental.append(i)
    
for i in peptides:
    Lt=Linera_spectrum(i)
    Score=compute_score(Lt)
    leaderboard.update({i:Score})
    if(Score not in A):
        A.add(Score)
        S_L.append(Score)
    
sort_L=sorted(leaderboard.items(), key=operator.itemgetter(1))
S_L.sort()
m=S_L[len(S_L)-n]

for i in sort_L:
    if(m<=i[1]):
        L_L.append(i[0])

k=len(L_L)-1
ans=""
while(k>=0):
    ans+=L_L[k]+" "
    k-=1

print(ans)
        
