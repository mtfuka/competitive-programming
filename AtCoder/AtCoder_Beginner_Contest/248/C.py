MOD=998244353
N,M,K=map(int,input().split())
dp=[[0 for i in range(K+1)] for j in range(N+1)]
for i in range(1,M+1):
    dp[1][i]=1
for i in range(2,N+1):
    for j in range(1,K+1):
        for k in range(max(1,j-M),j):
            dp[i][j]+=dp[i-1][k]
            dp[i][j]%=MOD
ans=0
for i in range(1,K+1):
    ans+=dp[N][i]
    ans%=MOD
print(ans)