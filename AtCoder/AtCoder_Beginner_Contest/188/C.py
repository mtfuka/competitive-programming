N = int(input())
A = list(map(int,input().split()))
if N==1:
  print(A.index(min(A))+1)
  exit()
i = A.index(max(A))+1
if 2*i<=2**N:
  print(A.index(max(A[2**(N-1)+1:]))+1)
else:
  print(A.index(max(A[:2**(N-1)]))+1)