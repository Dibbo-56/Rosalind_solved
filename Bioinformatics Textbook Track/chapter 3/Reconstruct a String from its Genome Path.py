file=open("rosalind_ba3b.txt","r")
mylist=[]
    
for i in file.readlines():
    s=""
    for j in range(len(i)):
        if(i[j] != '\n'):
            s+=i[j]
    mylist.append(s)

path=""

for i in range(len(mylist)):
    if(i==0):
        path+=mylist[i]
    else:
        path+=mylist[i][len(mylist[i])-1]
        
print(path)
