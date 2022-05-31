MOD=998244353
N,M=map(int,input().split())
m=len(bin(M))-2
dp=[[0 for j in range(m)]for i in range(60)]
if N>60:exit(print(0))
for j in range(m):
    dp[1][j]=2**j%MOD
    if j==m-1:dp[1][j]=(M-2**j+1)%MOD
for i in range(2,N+1):
    for j in range(m):
        for k in range(j+1,m):
            if k==m-1:
                dp[i][k]+=(dp[i-1][j]*(M-2**k+1))%MOD
                break
            dp[i][k]+=(dp[i-1][j]*2**k)%MOD
print(sum(dp[N])%MOD)