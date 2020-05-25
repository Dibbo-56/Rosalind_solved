Text=input()
k=int(input())

L=[]
mx=-99999
A=set()

for i in range(len(Text)-k+1):
    string1=Text[i:i+k]
    if(string1 not in A):
        A.add(string1)
    else:
        continue
    cnt=0
    for j in range(len(Text)-k+1):
        string2=Text[j:j+k]
        if(string1==string2):
            cnt+=1
    if(mx<=cnt):
        if(mx==cnt):
            L.append(string1)
        else:
            mx=cnt
            L.clear()
            L.append(string1)
print(" ".join(L))
