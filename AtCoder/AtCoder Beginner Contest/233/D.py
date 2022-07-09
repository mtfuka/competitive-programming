from collections import defaultdict
N,K=map(int,input().split())
A=list(map(int,input().split()))
S=[0 for i in range(N+1)]
for i in range(N):
    S[i+1]=S[i]+A[i]
d=defaultdict(int)
ans=0
for i in range(N+1):
    ans+=d[S[i]]
    d[S[i]+K]+=1
print(ans)