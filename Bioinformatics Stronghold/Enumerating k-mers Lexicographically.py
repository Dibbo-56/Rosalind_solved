A=list(input().split())
n=int(input())

def k_mers(string):
    if(len(string)==n):
        print(string)
        return 
    s=string
    for i in A:
        k_mers(s+i)
    
    
s=""
k_mers(s)
