dataset="GGCCGAAACAAAAGACATTCTGCGGCTGCGACCGGAAACGCACCCTGTAATATCGCTGTCAGATGTTAACCCCTGCTGGGGATCAACTTTCGCAGACCGTTGTGTTCTCGGTACGCTCCTCTCCGCTTCGGCAGGAAGACCGGTTACTAAATCCAAACCTCCGTCTACTCAATTGGTTTGACTCATAGTTTTGCGCGTTGTCCAGTTGTAGCGTGAATACGAAGTCGCAAGACCCCGTCTAACGACGTTAAAAATGTCGCGATAGGGGGAGTACTGATCATGCAGTATGTATAGAGCAACCCTAGCGCGATAGGAGCAGACCTATTGGCTGCTAAAGCGTGAACTCACAACAACGAGAGACCGAATGACATAGTAAACCTTATACGTAATGTTCCGCCACAGGAAGTGCCTTGATATCCCAATTGTCCGTGAAGGCGCCTATCGATATATCTGGAGAGACTACTTGGGGTATAACTACAAATCGACTCAAATGCTTCATGCTACAGAGGAAGTTTCGTAACCTCGGACAACCTTCCCAGGCAACGCTGTTCACCGTTATATCCGGAAATCATGAAGCGTGTCGAATGGAGGCGAAAGAATGTCTGCGGGGATGTTCTTAACTCGAACTTCCGTTGAACCATTCCTTTGATCCCCACGCCGCCAACACCGGGCATCTTGTAAGCTGCAACGCATGGACTTGCCCCACCTGTACCTTAGGGGTCGAACTTGGCGTACCCGACGTGTAAGAACCAAAAGCGAGCCAGGCGCTGTCCATACAGGTGTATTGTTTCACTTGACGCGGTAACACTCGGCCTTGATGCGTCTCGGCGAAAATTGCAGAGGCACGCGAAACTTTTATGGCTGCTATCATATTCCGTTCCACCGAGCTTTA"

a,c,g,t=0,0,0,0
for i in dataset:
    if (i=='A'):
        a+=1
    if (i=='C'):
        c+=1
    if (i=='G'):
        g+=1
    if (i=='T'):
        t+=1
print(str(a)+' '+str(c)+' '+str(g)+' '+str(t))




