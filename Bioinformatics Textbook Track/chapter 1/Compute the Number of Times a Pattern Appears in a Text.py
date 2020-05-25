Text=input()
pattern=input()

k=len(pattern)
cnt=0

for i in range(len(Text)-k+1):
    string=Text[i:i+k]
    if(pattern==string):
        cnt+=1
print(cnt)
