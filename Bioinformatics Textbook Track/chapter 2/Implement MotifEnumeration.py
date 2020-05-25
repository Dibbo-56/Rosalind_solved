import itertools

k,d=map(int,input().split())
DNA=[]

DNA_cnt=0

while True:
    s=input()
    if s=="":
        break
    DNA.append(s)
    DNA_cnt+=1
    
kmers = []
S="ACGT"

for i in itertools.product(S,repeat=k):
    kmers.append(''.join(i))
        
def Ham_dis(s1,s2):
    cnt=0
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            cnt+=1
    return cnt    
 
def substring_generate(string):
    substring=[]
    for i in range(len(string)-k+1):
        s=string[i:i+k]
        substring.append(s)
    return substring
        
motif=""

for i in kmers:
    cnt=0
    for j in DNA:
        sublist=substring_generate(j)
        for K in sublist:
            if(Ham_dis(K,i)<=d):
                #print(i+" "+K)
                cnt+=1
                break
    if(cnt==DNA_cnt):
        A.append(i)
        motif=motif+" "+i

print(motif)
