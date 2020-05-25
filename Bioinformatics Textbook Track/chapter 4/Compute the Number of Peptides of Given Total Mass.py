mass=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
m=int(input())

cm=[]
cm.append(1)

for i in range(1,m+1):
    cm.append(0)
    
for i in range(m+1):
    for j in range(len(mass)):
        if(i>=mass[j]):
            cm[i]+=cm[i-mass[j]]
        
print(cm[m])        
        
