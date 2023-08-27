MOD = 10**9+7
N,L = map(int,input().split())
dp = [1]*(N+1)
for i in range(N+1):
    if i>=L:
        dp[i]=(dp[i-L]+dp[i-1])%MOD
print(dp[N]%MOD)