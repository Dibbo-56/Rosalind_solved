import itertools

Text=input()
k,d=map(int,input().split())

kmers={}
mx=-99999
words=""
mx=-9999999

S="ACTG"
dict={'A':'T','T':'A','C':'G','G':'C'}

for i in itertools.product(S,repeat=k):
    kmers.update({''.join(i):0})
    

for t in kmers:
    string1=t
    hmd=0
    for i in range(len(Text)-k+1):
        string2=Text[i:i+k]
        cnt=0
        for j in range(len(string1)):
            if(string1[j]!=string2[j]):
                cnt+=1
        if(cnt<=d):
            hmd+=1
    
    kmers.update({string1:hmd})
    if(mx<kmers[string1]):
        mx=kmers[string1]

        
for i in kmers:
    if(mx==kmers[i]):
        words+=i+" "

print(words)
