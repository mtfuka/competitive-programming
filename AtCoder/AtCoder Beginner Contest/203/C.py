N,K = map(int,input().split())
A = [0] * N
for i in range(N):
    A[i]= list(map(int, input().split()))
ans = 0
sumK = K
n = 0
A.sort(reverse=True)
while K>0:
  ans += K
  K = 0
  if n==N:break
  for i in range(1,N+1):
    if A[-1][0]>sumK:
      break
    sumK += A[-1][1]
    K += A[-1][1]
    A.pop()
    n += 1
print(ans)
