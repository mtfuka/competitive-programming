from cmath import inf
N,X=map(int,input().split())
A=[0 for i in range(N)]
B=[0 for i in range(N)]
C=[0 for i in range(N+1)]
for i in range(N):
    A[i],B[i]=map(int,input().split())
    C[i+1]=C[i]+A[i]+B[i]
ans=inf
for i in range(N):
    if X-i<=0:break
    ans=min(ans,C[i]+A[i]+B[i]*(X-i))
print(ans)