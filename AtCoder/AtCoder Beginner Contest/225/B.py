N=int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
for i in G:
    if len(i) == N-1:
        print('Yes')
        exit()
print('No')