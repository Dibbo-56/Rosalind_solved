RNA=input()
dict={'AUU':'I','AUC':'I','AUA':'I','AUG':'M','AGU':'S','AGC':'S','AGA':'R','AGG':'R','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAA':'K','AAG':'K','AAC':'N','AAU':'N',
     'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CGU':'R','CGC':'R','CGA':'R','CGG':'R','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
     'UUG':'L','UUA':'L','UUC':'F','UUU':'F','UGG':'W','UGA':'*','UGC':'C','UGU':'C','UCG':'S','UCA':'S','UCC':'S','UCU':'S','UAG':'*','UAA':'*','UAC':'Y','UAU':'Y',
     'GAU':'D','GAC':'D','GAA':'E','GAG':'E','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GGU':'G','GGC':'G','GGA':'G','GGG':'G','GUG':'V','GUA':'V','GUC':'V','GUU':'V'}

i=0
Amio_acid=""
ln=len(RNA)-3+1

while(i<ln):
    s=RNA[i:i+3]
    if(dict[s]=='*'):
        break
    Amio_acid+=dict[s]
    i=i+3

print(Amio_acid)
    
