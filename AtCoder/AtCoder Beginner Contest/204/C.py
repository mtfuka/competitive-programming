import sys
sys.setrecursionlimit(10000)
N,M=map(int,input().split())
G=[[]for i in range(N)]
for i in range(M):
    A,B=map(int,input().split())
    G[A-1].append(B-1)
def dfs(v):
    seen[v]=True
    for next_v in G[v]:
        if seen[next_v]:continue
        dfs(next_v)
ans=0
for i in range(N):
    seen=[False for j in range(N)]
    dfs(i)
    ans+=sum(seen)
print(ans)