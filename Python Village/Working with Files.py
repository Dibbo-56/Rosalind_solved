file=open("rosalind_ini5.txt","r")
cnt=1
for i in file:
    if(cnt%2==0):
        print(i)
    cnt+=1
