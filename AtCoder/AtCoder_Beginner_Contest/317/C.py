import sys
sys.setrecursionlimit(10000)
N,M=map(int,input().split())
G=[[]for i in range(N)]
for i in range(M):
    A,B,C=map(int,input().split())
    G[A-1].append([B-1,C])
    G[B-1].append([A-1,C])
ans=0
seen=[False for i in range(N)]
def dfs(v,len):
    global ans
    seen[v]=True
    for next_v in G[v]:
        if seen[next_v[0]]:continue
        dfs(next_v[0],len+next_v[1])
    seen[v]=False
    ans=max(len,ans)
    len=0
for i in range(N):
    dfs(i,0)
print(ans)
