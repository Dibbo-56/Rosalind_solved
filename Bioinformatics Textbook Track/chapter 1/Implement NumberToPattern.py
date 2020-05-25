index=int(input())
k=int(input())

L=[int(1)]
dict={0:'A',1:'C',2:'G',3:'T'}

for i in range(1,k):
    L.append(L[i-1]*4)

L.reverse()
    
DNA=""

for i in range(0,k):
    d=int(index/L[i])
    DNA+=dict[d]
    index=index-(d*L[i])

print(DNA)
