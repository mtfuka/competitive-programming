N,Q=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in range(N):
    d.setdefault(a[i],[]).append(i+1)
for i in range(Q):
    x,k=map(int,input().split())
    if not x in d or len(d[x])<k:print(-1)
    else:print(d[x][k-1])