N,X=map(int,input().split())
dp=[[0 for i in range(X+1)] for j in range(N+1)]
dp[0][0]=1
for i in range(N):
    a,b=map(int,input().split())
    for j in range(X+1):
        if dp[i][j]==1 and j+a<=X:
            dp[i+1][j+a]=1
        if dp[i][j]==1 and j+b<=X:
            dp[i+1][j+b]=1
if dp[N][X]:print('Yes')
else:print('No')