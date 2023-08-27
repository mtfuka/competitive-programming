MOD=10**9+7
K=int(input())
if K%9!=0:exit(print(0))
dp=[0 for i in range(K+1)]
dp[0]=1
for i in range(1,K+1):
    k=min(i,9)
    for j in range(1,k+1):
        dp[i]+=dp[i-j]
        dp[i]%=MOD
print(dp[K])