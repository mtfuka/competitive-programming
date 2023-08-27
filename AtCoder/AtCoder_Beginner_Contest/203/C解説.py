N,K = map(int,input().split())
A = [0] * N
for i in range(N):
  A[i]= list(map(int, input().split()))
ans = K
A.sort()
for i in range(N):
  if ans>=A[i][0]:
    ans += A[i][1]
  else:
    break
print(ans)
