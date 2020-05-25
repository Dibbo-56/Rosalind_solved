import itertools

DNA=input()
d=int(input())
k=len(DNA)

for i in itertools.product("ACGT",repeat=k):
    Neighbor=''.join(i)
    cnt=0
    for j in range(len(Neighbor)):
        if(Neighbor[j]!=DNA[j]):
            cnt+=1
    if(cnt<=d):
        print(Neighbor)
