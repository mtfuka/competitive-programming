N = int(input())
A = list(map(int,input().split()))
A.sort()
x2 = A[(N-1)//2]
ans = 0
for i in range(N):
    ans += A[i]
    ans -= min(A[i],x2)
print(ans/N + A[(N-1)//2]/2)