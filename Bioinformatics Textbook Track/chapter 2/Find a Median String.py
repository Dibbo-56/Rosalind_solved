import itertools

k=int(input())

DNA=[]
kmers={}
pattern=""

while True:
    s=input()
    if(s==""):
        break
    DNA.append(s)
    

S="ACGT"    
for i in itertools.product(S,repeat=k):    
    kmers.update({''.join(i):0})
        
def ham_dis(s1,s2):    
    cnt=0
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            cnt+=1
    return cnt

def substring_generate(string):
    list=[]
    for i in range(len(string)-k+1):
        s=string[i:i+k]
        list.append(s)
    return list

ham_val=999999
for i in kmers:
    value=0
    for j in DNA:
        ham=99999999
        sub_list=substring_generate(j)
        for K in sub_list:
            d=ham_dis(i,K)
            if(ham>d):
                ham=d
        value+=ham
    kmers.update({i:value})
    if(ham_val>=value):
        pattern=i
        ham_val=value
 
print(pattern)

    
