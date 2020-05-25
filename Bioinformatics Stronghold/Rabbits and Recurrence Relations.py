n=35
k=5
dp1=1
dp2=1*k
dp=0
for i in range(1,n-1):
    dp=dp1+dp2
    dp2=dp1*k
    dp1=dp
    
print(dp)
