import itertools
s=""
n=5
a=list(itertools.permutations([1,2,3,4,5]))
fact=[1,2,6,24,120,720,5040]
print(fact[n-1])
for i in a:
    s=""
    for j in i:
        s=s+" "+str(j)
    print(s[1:])
