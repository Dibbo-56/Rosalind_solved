pattern=input()
Text=input()
d=int(input())

k=len(pattern)
Position=""

for i in range(len(Text)-k+1):
    string=Text[i:i+k]
    cnt=0
    for j in range(len(pattern)):
        if(string[j]!=pattern[j]):
            cnt+=1
    if(cnt<=d):
        Position+=str(i)+" "
    
print(Position)
