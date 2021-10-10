MOD=10**9+7
L,R = map(int,input().split())
l=len(str(L))
r=len(str(R))
ans=0
for i in range(l,r+1):
    if l==r:
        ans+=(l*(L+R)*(R-L+1)//2)%MOD
    elif i==l:
        ans+=(i*(L+10**i-1)*(10**i-1-L+1)//2)%MOD
    elif l<i<r:
        ans+=(i*(10**(i-1)+10**i-1)*(10**i-1-10**(i-1)+1)//2)%MOD
    elif i==r:
        ans+=(i*(10**(i-1)+R)*(R-10**(i-1)+1)//2)%MOD
print(ans%MOD)