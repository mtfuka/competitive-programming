N,K=map(int,input().split())
while K%10==0:
    K//=10
K_dash=int("".join(list(reversed(list(str(K))))))
ans=0
if K>K_dash:exit(print(0))
if K!=K_dash:
    while K_dash<=N:
        ans+=1
        K_dash*=10
while K<=N:
    ans+=1
    K*=10
print(ans)