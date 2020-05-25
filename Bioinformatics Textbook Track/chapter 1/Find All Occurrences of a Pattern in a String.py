pattern=input()
genome=input()

k=len(pattern)
Occurence=""

for i in range(len(genome)-k+1):
    string=genome[i:i+k]
    if(string==pattern):
        Occurence+=str(i)+" "
        
print(Occurence)        
        
