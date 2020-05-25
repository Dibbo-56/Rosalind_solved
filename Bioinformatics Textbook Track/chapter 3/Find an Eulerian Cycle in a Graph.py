import networkx as nx

f=open("BIO1.txt", "r")

id=0
D={}
total=0
l=[]
N=[]
IN=[]
OUT=[]
E={}
flag=0
edge=0

def euler_cycle(src):
    global flag
    global edge
    if(flag==1):
        return 
    N.append(src)
    if(edge==total):
        flag=1
        node=""
        for i in N:
            node+=str(i)+"->"
        
        print(node[0:len(node)-2])
        return
    
    chk=0
    for i in range(len(D[src])):
        if(E[src]!=0):
            E.update({src:E[src]-1})
            chk=1
            edge=edge+1
            euler_cycle(D[src][i])
            E.update({src:E[src]+1})
            edge=edge-1
            if(flag==1):
                return 
    if(chk==0 or flag==0):
        N.pop(len(N)-1)
            

for i in f:
    s=""
    for j in i:
        if(j!="\n"):
            s+=j
    s1=""
    for j in range(len(s)):
        if(s[j]!=" "):
            s1+=s[j]
        else:
            id=j+4
            break
    s2=""
    L=[]
    for j in range(id,len(s)):
        if(s[j]>='0' and s[j]<='9'):
            s2+=s[j]
        else:
            L.append(int(s2))
            s2=""
    L.append(int(s2))
    total+=len(L)
    D.update({int(s1):L})
    l.append(int(s1))


l.sort()

for i in l:
    E.update({i:len(D[i])})
    OUT.append(len(D[i]))
    IN.append(0)

for i in l:
    List=D[i]
    for j in List:
        IN[j]+=1


    
#euler_cycle(0) This is not optimized  

DG=nx.DiGraph(D)
L=list(nx.eulerian_circuit(DG))

node=[]
for i in L:
    node.append(i[0])

node.append(node[0])

ans=""
for i in range(len(node)):
    if i!=len(node)-1:
        ans+=str(node[i])+"->"
    else:
        ans+=str(node[i])
print(ans)
