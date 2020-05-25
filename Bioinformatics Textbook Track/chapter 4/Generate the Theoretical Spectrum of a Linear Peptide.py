dict={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

amino_acid=input()
mass_list=[]
linear_spectrum=""
k=1
mass_list.append(0)

def calu_mass(s):
    mass=0
    for i in s:
        mass+=dict[i]

    return mass 


while(k<len(amino_acid)):
    for i in range(len(amino_acid)-k+1):
        s=amino_acid[i:i+k]
        mass_list.append(calu_mass(s))
    k+=1

mass_list.append(calu_mass(amino_acid))
mass_list.sort()

for i in mass_list:
    linear_spectrum+=str(i)+" "

print(linear_spectrum)
