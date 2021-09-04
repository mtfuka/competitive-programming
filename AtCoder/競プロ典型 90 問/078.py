N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
ans = 0
for i in range(N):
    cnt = 0
    for j in G[i]:
        if j < i:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)