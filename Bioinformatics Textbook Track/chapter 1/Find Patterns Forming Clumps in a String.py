S=input()
k,L,t=map(int,input().split())
A=set()
List=[]
for i in range(len(S)-L+1):
    string1=S[i:i+L]
    for j in range(len(string1)-k+1):
        string2=string1[j:j+k]
        cnt=string1.count(string2)
        if(cnt>=t and (string2 not in A)):
            A.add(string2)
            List.append(string2)
S=" "
print(List)
