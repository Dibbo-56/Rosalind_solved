s=input()
k=int(input())
Mat={}
final=""
alp={'A':1,'C':2,'G':3,'T':4}

for i in range(1,5):
    a=list(map(float,input().split()))
    for j in range(1,k+1):
        m=a[j-1]
        Mat[i,j]=m

mx=-99999

for i in range(0,len(s)-k+1):
    string=s[i:i+k]
    score=0
    for j in range(0,len(string)):
        score+=Mat[alp[string[j]],j+1]
    if(mx<score):
        mx=score
        final=string
    

print(final)
 
