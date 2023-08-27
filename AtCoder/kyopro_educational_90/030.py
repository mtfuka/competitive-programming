N,K=map(int,input().split())
cnt=[0 for i in range(N+1)]
for i in range(2,N+1):
    if cnt[i]!=0:continue
    for j in range(i,N+1,i):
        cnt[j]+=1
ans=0
for i in range(2,N+1):
    if cnt[i]>=K:
        ans+=1
print(ans)