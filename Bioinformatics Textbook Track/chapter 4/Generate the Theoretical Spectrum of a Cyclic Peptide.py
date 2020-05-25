dict={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}
peptide="HWVEHNQNAVVW"
string=peptide+peptide
mass_list=[]
k=1

def calu_mass(s):
    mass=0
    for i in s:
        mass+=dict[i]

    return mass 

mass_list.append(0)

while(k<len(peptide)):
    for i in range(len(peptide)):
        s=string[i:i+k]
        #print(s)
        mass_list.append(calu_mass(s))
    k+=1
mass_list.append(calu_mass(peptide))
mass_list.sort() 
mass=""
for i in mass_list:
    mass+=str(i)+" "

print(mass)
        
        
