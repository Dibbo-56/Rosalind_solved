DNA=input()

L=[int(1)]
dict={'A':1,'C':2,'G':3,'T':4}
k=len(DNA)
idx=0

for i in range(1,k):
    L.append(L[i-1]*4)

L.reverse()

for i in range(len(DNA)-1):
    idx+=L[i]*(dict[DNA[i]]-1)

idx+=dict[DNA[len(DNA)-1]]

print(idx-1)
