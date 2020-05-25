k,m,n=map(int,input().split())

p=k+m+n

ans=((4*k*(k-1))+(8*k*m)+(8*k*n)+(3*m*(m-1))+(4*m*n))/(4*p*(p-1))

print(ans)

