N=int(input())
X=[0]*N
Y=[0]*N
for i in range(N):
    X[i],Y[i]=map(int,input().split())
X.sort()
Y.sort()
ansX=X[N//2]
ansY=Y[N//2]
ans=0
for i in range(N):
    ans+=abs(X[i]-ansX)+abs(Y[i]-ansY)
print(ans)