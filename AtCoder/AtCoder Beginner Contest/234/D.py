N,K=map(int,input().split())
P=list(map(int,input().split()))
s=set(P[:K])
ans=min(P[:K])
print(ans)
for i in range(K,N):
    s.add(P[i])
    if ans<P[i]:
        ans+=1
        while not ans in s:
            ans+=1
    print(ans)