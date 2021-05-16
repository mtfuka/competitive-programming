import math
K,N,M = map(int,input().split())
A = list(map(int,input().split()))

B = []
for a in A:
  B.append(math.floor(M*a/N))
C = []
for i in range(K):
  C.append(N*B[i]-M*A[i])
n = M - sum(B)
D = []
for i in range(K):
  D.append(N*B[i]-M*A[i])
D.sort()

sum = 0
for i in range(K):
  if C[i]<D[n-1]:
    B[i] += 1
    sum += 1
if sum!=n:
  for i in range(K):
    if C[i]==D[n-1]:
      B[i] += 1
      sum += 1
      if sum==n:
        break
print(*B)