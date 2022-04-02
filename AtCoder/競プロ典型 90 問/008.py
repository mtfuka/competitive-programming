MOD=10**9+7
T="atcoder"
N=int(input())
S=input()
dp=[[0]*(len(T)+1) for i in range(N+1)]
#文字列Sの最初のi文字から何文字か抜き出して繋げる方法のうち、それが"atcoder"の最初のj文字まで一致するような方法の個数
dp[0][0]=1
#初期値として、Sの最初の0文字と"atcoder"の最初の0文字が一致する個数を1個とする
for i in range(N):
    for j in range(len(T)+1):
        dp[i+1][j]+=dp[i][j] #S[i]を選ばない場合は"atcoder"の文字数進まないのでそれまでの数
        if j<len(T) and S[i]==T[j]:#S[i]を選ぶ場合は"atcoder"の文字数を1文字進めてそれまでの数を足し合わせる
            dp[i+1][j+1]+=dp[i][j]
            dp[i+1][j+1]%=MOD
print(dp[N][len(T)]%MOD)