from cmath import inf
MOD=998244353
N,M,K=map(int,input().split())
dp=[[0 for j in range(M+1)]for i in range(N+1)]
s=[[0 for j in range(M+1)]for i in range(N+1)]
for j in range(1,M+1):
    dp[1][j]=1
    s[1][j]+=s[1][j-1]+dp[1][j]
if M==1:exit(print(sum(dp[1])))
if K==0:
    for i in range(1,N):
        for j in range(1,M+1):
            dp[i+1][j]+=s[i][M]%MOD
            s[i+1][j]+=(s[i+1][j-1]+dp[i+1][j])%MOD
else:
    for i in range(1,N):
        for j in range(1,M+1):
            dp[i+1][j]+=(s[i][max(0,j-K)]+s[i][M]-s[i][min(M,j+K-1)])%MOD
            s[i+1][j]+=(s[i+1][j-1]+dp[i+1][j])%MOD
print(sum(dp[N])%MOD)