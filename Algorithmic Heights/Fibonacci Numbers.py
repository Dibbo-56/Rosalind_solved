f1=0
f2=1
n=21
for i in range(2,n+1):
    f=f1+f2
    f1=f2
    f2=f
print(f)
