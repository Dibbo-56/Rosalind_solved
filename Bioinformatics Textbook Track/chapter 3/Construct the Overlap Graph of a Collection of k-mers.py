file=open("rosalind_ba3c.txt","r")
mylist={}
overlap_list={}
num=0    
    
for i in file.readlines():
    s=""
    for j in range(len(i)):
        if(i[j] != '\n'):
            s+=i[j]
    mylist.update({num:s})
    num+=1
    
f_list={}
s_list={}
num=0

for i in mylist:
    string=mylist[i]
    f_list.update({string[0:len(string)-1]:num})
    s_list.update({string[1:len(string)]:num})
    num+=1
    
for j in s_list:
     for i in f_list:
            if(i==j):
                overlap_list.update({mylist[s_list[j]]:mylist[f_list[i]]})

node_list=[]               
                
for i in overlap_list:
    node_list.append(i)

node_list.sort()

for i in node_list:
    print(i+" -> "+overlap_list[i])
    
    
