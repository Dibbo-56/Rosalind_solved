file=open("rosalind_ba3e.txt","r")

edge_list=[]
node_list={}

def make_node(string):
    s=string[0:len(string)-1]
    return s

def make_edge(string):
    s=""
    for i in range(len(string)):
        if(string[i]!='\n'):
            s+=string[i]
    return s

for i in file.readlines():
    edge_list.append(make_edge(i))

edge_list.sort()
  
for i in edge_list:
    node_list.update({make_node(i):0})
    
for i in node_list:
    B=[]
    for j in edge_list:
        string1=j[0:len(j)-1]
        if(i==string1):
            string2=j[1:len(j)]
            B.append(string2)
    node_list.update({i:B})
    
for i in node_list:
    if(node_list[i]!=[]):
        s=str(node_list[i])
        edge=""
        for j in s:
            if((j>='A' and j<='Z') or j==','):
                edge+=j
            
        print(i+" -> "+edge)
