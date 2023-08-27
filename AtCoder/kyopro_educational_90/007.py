import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for i in range(Q):
  B = int(input())
  index = bisect.bisect(A,B)
  if A[N-1]<=B:
    print(B-A[N-1])
  else:
    print(min(abs(B-A[index-1]),abs(B-A[index])))