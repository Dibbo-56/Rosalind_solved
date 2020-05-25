file=open("rosalind_gc.txt","r")
f=0
mx=-100
final=""
dict={}
for i in file:
    if (i[0]=='>'):
        if(f==1):
            cnt=0
            nw=0
            for j in str:
                if(j=='C' or j=='G'):
                    cnt+=1
                if(j=='\n'):
                    nw+=1
            dict.update({head:(100*(cnt))/(len(str)-nw)})
            if (mx<dict[head]):
                mx=dict[head]
                final=head
        head=i
        str=""
        f=1
    else:
        str+=i

cnt=0
nw=0
for j in str:
    if(j=='C' or j=='G'):
        cnt+=1
    if(j=='\n'):
        nw+=1
dict.update({head:(100*(cnt))/(len(str)-nw)})
if (mx<dict[head]):
    mx=dict[head]
    final=head
final=final.replace("\n", "")
print(final)
print("%.6f" %mx)
