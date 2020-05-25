pattern=input()
DNA=list(map(str,input().split()))

k=len(pattern)
d,Hmd=0,0

for t in DNA:
    string=t
    Hmd=999999
    for i in range(0,len(string)-k+1):
        pattern1=string[i:i+k]
        cnt=0
        for j in range(len(pattern)):
            if(pattern[j]!=pattern1[j]):
                cnt+=1
        if(Hmd>cnt):
            Hmd=cnt
    d+=Hmd
    
print(d)
    
