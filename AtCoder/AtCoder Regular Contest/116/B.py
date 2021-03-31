MOD = 998244353
N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = 0

for a in A:
  ans += a*a%MOD

#解説(1)部分
s = 0
for i in range(N):
  ans += (A[-1-i]*s)%MOD
  s = (2*s+A[-1-i])%MOD #()部分はi=Nから降順に漸化式で求められる

print(ans%MOD)
