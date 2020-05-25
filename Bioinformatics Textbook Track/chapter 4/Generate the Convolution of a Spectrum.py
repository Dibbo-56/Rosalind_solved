import operator

spectrum=list(map(int,input().split()))

def convolution(mass):
    
    count={}
    for i in range(len(mass)):
        for j in range(i):
            if(mass[i]==mass[j]):
                continue
            d=abs(mass[i]-mass[j])
            if(d not in count):
                count.update({d:1})
            else:
                count.update({d:count[d]+1})
                
    sort_L=sorted(count.items(),key=operator.itemgetter(1))
    
    return sort_L
    
s=convolution(spectrum)
k=len(s)-1
ans=""

while(k>=0):
    d=s[k][1]
    for i in range(d):
        ans+=str(s[k][0])+" "
    k-=1

print(ans)
