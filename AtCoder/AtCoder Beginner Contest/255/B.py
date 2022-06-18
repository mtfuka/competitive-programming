from cmath import inf
N,K=map(int,input().split())
A=list(map(int,input().split()))
X,Y=[0 for i in range(N)],[0 for i in range(N)]
for i in range(N):
    X[i],Y[i]=map(int,input().split())
ans=-1
for i in range(N):
    temp=inf
    for j in range(K):
        temp=min(temp,((X[i]-X[A[j]-1])**2+(Y[i]-Y[A[j]-1])**2)**0.5)
    ans=max(ans,temp)
print(ans)