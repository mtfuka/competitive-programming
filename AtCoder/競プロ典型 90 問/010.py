N = int(input())
CP = [map(int, input().split()) for _ in range(N)]
C, P = [list(i) for i in zip(*CP)]
Q = int(input())
LR = [map(int, input().split()) for _ in range(Q)]
L, R = [list(i) for i in zip(*LR)]
Sum1 = [0]*(N+1)
Sum2 = [0]*(N+1)
for i in range(N):
  Sum1[i+1] = Sum1[i]
  Sum2[i+1] = Sum2[i]
  if C[i]==1:Sum1[i+1] += P[i]
  if C[i]==2:Sum2[i+1] += P[i]
for j in range(Q):
  print(Sum1[R[j]]-Sum1[L[j]-1],Sum2[R[j]]-Sum2[L[j]-1])