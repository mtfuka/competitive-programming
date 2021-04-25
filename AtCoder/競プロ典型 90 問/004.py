#PyPyでないとTLEになる
H,W = map(int,input().split())
A = []
for i in range(H):
  a = list(map(int,input().split()))
  A.append(a)
  
sumH = [sum(A[i]) for i in range(H)]
sumW = [0]*W
for i in range(H):
  for j in range(W):
    sumW[j] += A[i][j]

for i in range(H):
  for j in range(W):
    ans = -A[i][j]
    ans += sumH[i]+sumW[j]
    if j==W-1:print(ans)
    else:print(ans,end=" ")