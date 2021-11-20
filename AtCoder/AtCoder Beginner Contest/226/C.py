N=int(input())
l=[list(map(int,input().split())) for i in range(N)]
used=[False]*N
used[N-1]=True
ans=0
for i in range(N):
  if used[-(i+1)]:
    T=l[-(i+1)][0]
    K=l[-(i+1)][1]
    ans+=T
    for j in range(K):
      used[l[-(i+1)][j+2]-1]=True
print(ans)