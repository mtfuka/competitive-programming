N=int(input())
ans=10**18+1
c=0
for a in reversed(range(10**6+1)):
    for b in range(c,10**6+1):
        if a**3+a**2*b+b**2*a+b**3>=N:
            ans=min(ans,a**3+a**2*b+b**2*a+b**3)
            c=b
            break
print(ans)