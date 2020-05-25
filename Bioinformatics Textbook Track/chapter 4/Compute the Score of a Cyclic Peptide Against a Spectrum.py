dict={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

peptide=input()
spectrum=list(map(int,input().split()))

A=set()
score=0
experimental=[]
theoretical=[]

for i in spectrum:
    experimental.append(i)
    
string=peptide+peptide
k=1

def calu_mass(s):
    mass=0
    for i in s:
        mass+=dict[i]

    return mass 

theoretical.append(0)

while(k<len(peptide)):
    for i in range(len(peptide)):
        s=string[i:i+k]
        theoretical.append(calu_mass(s))
    k+=1
    
theoretical.append(calu_mass(peptide))
theoretical.sort()

for i in theoretical:
    if(i not in A):
        A.add(i)
        T=theoretical.count(i)
        E=experimental.count(i)
        score+=min(E,T)

print(score)
