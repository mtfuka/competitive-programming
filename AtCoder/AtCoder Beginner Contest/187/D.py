import heapq
N = int(input())
A = [0] * N
B = [0] * N
C = []
for i in range(N):
  A[i],B[i] = map(int,input().split())
  C.append(-2*A[i]-B[i])
heapq.heapify(C)
ans = 0
sumB = 0
sumA = sum(A)
while sumB<=sumA:
  sumB += heapq.heappop(C)*(-1)
  ans += 1
print(ans)