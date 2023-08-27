MOD = 10**9+7
N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = A[0]+1
for i in range(N-1):
  ans *= (A[i+1]-A[i]+1)%MOD
print(ans%MOD)