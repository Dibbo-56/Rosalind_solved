k=int(input())
Text=input()

list=[]

for i in range(len(Text)-k+1):
    s=Text[i:i+k]
    list.append(s)
    
list.sort()

for i in list:
    print(i)
