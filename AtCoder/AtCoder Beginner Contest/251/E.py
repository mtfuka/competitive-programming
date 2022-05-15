from cmath import inf
N=int(input())
A=list(map(int,input().split()))
dp=[[0 for i in range(2)]for j in range(N+1)]
#A1を払わない
dp[1][0]=0
dp[1][1]=inf
for i in range(2,N+1):
    dp[i][0]=dp[i-1][1]
    dp[i][1]=min(dp[i-1][0],dp[i-1][1])+A[i-1]
ans=dp[N][1]
#A1を払う
dp[1][0]=inf
dp[1][1]=A[0]
for i in range(2,N+1):
    dp[i][0]=dp[i-1][1]
    dp[i][1]=min(dp[i-1][0],dp[i-1][1])+A[i-1]
ans=min(ans,dp[N][0],dp[N][1])
print(ans)