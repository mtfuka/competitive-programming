MOD=998244353
N=int(input())
dp=[[0 for i in range(10)] for j in range(10**6+1)]
dp[1][1]=1
dp[1][2]=1
dp[1][3]=1
dp[1][4]=1
dp[1][5]=1
dp[1][6]=1
dp[1][7]=1
dp[1][8]=1
dp[1][9]=1
for i in range(2,N+1):
    dp[i][1]=(dp[i-1][1]+dp[i-1][2])%MOD
    dp[i][2]=(dp[i-1][1]+dp[i-1][2]+dp[i-1][3])%MOD
    dp[i][3]=(dp[i-1][2]+dp[i-1][3]+dp[i-1][4])%MOD
    dp[i][4]=(dp[i-1][3]+dp[i-1][4]+dp[i-1][5])%MOD
    dp[i][5]=(dp[i-1][4]+dp[i-1][5]+dp[i-1][6])%MOD
    dp[i][6]=(dp[i-1][5]+dp[i-1][6]+dp[i-1][7])%MOD
    dp[i][7]=(dp[i-1][6]+dp[i-1][7]+dp[i-1][8])%MOD
    dp[i][8]=(dp[i-1][7]+dp[i-1][8]+dp[i-1][9])%MOD
    dp[i][9]=(dp[i-1][8]+dp[i-1][9])%MOD
ans=0
for i in range(9):
    ans+=dp[N][i+1]
print(ans%MOD)