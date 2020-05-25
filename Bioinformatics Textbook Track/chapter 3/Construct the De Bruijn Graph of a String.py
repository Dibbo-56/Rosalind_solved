k=4
text="AAGATTCTCTAC"
k=k-1
A=set()
node_list=[]
edge_list={}

for i in range(len(text)-k+1):
    string=text[i:i+k]
    if(string not in A):
        A.add(string)
        node_list.append(string)

node_list.sort()

for i in node_list:
    edge_list.update({i:0})

for i in node_list:
    string1=i[1:len(i)]
    edge=[]
    for j in node_list:
        string2=j[0:len(j)-1]
        if(string1==string2):
            edge.append(j)
    edge_list.update({i:edge})

for i in edge_list:
    if(edge_list[i]!=[]):
        s=str(edge_list[i])
        edge=""
        for j in s:
            if((j>='A' and j<='Z') or j==','):
                edge+=j
            
        print(i+" -> "+edge)

        
