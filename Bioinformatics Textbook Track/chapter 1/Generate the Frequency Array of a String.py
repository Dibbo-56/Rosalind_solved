import itertools

Text=input()
k=int(input())

kmers=[]
frq=""

for i in itertools.product("ACGT",repeat=k):
    kmers.append(''.join(i))
    
for t in kmers:
    string1=t
    cnt=0
    for i in range(len(Text)-k+1):
        string2=Text[i:i+k]
        if(string1==string2):
            cnt+=1
    frq+=str(cnt)+" "

print(frq)
