import collections
N,K=map(int,input().split())
S=[]
for i in range(N):
    S.append(list(input()))
ans=0
for bit in range(1<<N):
    l=[]
    for i in range(N):
        mask=1<<i
        if bit&mask:
            l.extend(S[i])
    c=collections.Counter(l)
    ans=max(ans,list(c.values()).count(K))
print(ans)