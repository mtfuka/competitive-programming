MOD = 10**9+7
N = int(input())
ans = 1
for i in range(N):
    A = map(int,input().split())
    ans *= sum(A)
    ans %= MOD
print(ans)