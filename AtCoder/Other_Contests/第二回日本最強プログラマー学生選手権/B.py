N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = []
for i in range(N):
  a = True
  for j in range(M):
    if A[i]==B[j]:
      a = False
  if a:ans.append(A[i])
for i in range(M):
  a = True
  for j in range(N):
    if B[i]==A[j]:
      a = False
  if a:ans.append(B[i])
ans.sort()
print(*ans)