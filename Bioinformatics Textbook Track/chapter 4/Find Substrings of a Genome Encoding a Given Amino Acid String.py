DNA=input()
acid=input()

k=len(acid)*3
m=len(acid)

sub_str=[]

dict={'AUU':'I','AUC':'I','AUA':'I','AUG':'M','AGU':'S','AGC':'S','AGA':'R','AGG':'R','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAA':'K','AAG':'K','AAC':'N','AAU':'N',
     'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CGU':'R','CGC':'R','CGA':'R','CGG':'R','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
     'UUG':'L','UUA':'L','UUC':'F','UUU':'F','UGG':'W','UGA':'*','UGC':'C','UGU':'C','UCG':'S','UCA':'S','UCC':'S','UCU':'S','UAG':'*','UAA':'*','UAC':'Y','UAU':'Y',
     'GAU':'D','GAC':'D','GAA':'E','GAG':'E','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GGU':'G','GGC':'G','GGA':'G','GGG':'G','GUG':'V','GUA':'V','GUC':'V','GUU':'V'}


def reverse_com(string):
    s=""
    string=string[::-1]
    for i in range(len(string)):
        if(string[i]=='A'):
            s+='T'
        elif(string[i]=='T'):
            s+='A'
        elif(string[i]=='C'):
            s+='G'
        elif(string[i]=='G'):
            s+='C'
    return s
 
    
def T_to_U(string):
    s=""
    for i in range(len(string)):
        if(string[i]=='T'):
            s+='U'
        else:
            s+=string[i]
    return s
    
    
def codon(string):
    s=""
    i=0
    while(i<len(string)-3+1):
        st=string[i:i+3]
        s+=dict[st]
        i=i+3
    return s
 
    
for i in range(len(DNA)-k+1):
    string1=DNA[i:i+k]
    string2=reverse_com(DNA[i:i+k])
    if(codon(T_to_U(string1))==acid):
        sub_str.append(string1)
    if(codon(T_to_U(string2))==acid):
        sub_str.append(string1)

for i in sub_str:
    print(i)
        
    
