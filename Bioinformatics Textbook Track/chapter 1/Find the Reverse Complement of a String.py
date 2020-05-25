pattern=input()

D={'A':'T','T':'A','C':'G','G':'C'}
pattern1=""

for i in range(len(pattern)):
    pattern1+=D[pattern[i]]

print(pattern1[::-1])
