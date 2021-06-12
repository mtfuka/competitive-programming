N = int(input())
A = list(map(int,input().split()))
MaxA = 0
sumA = 0
sum = 0
for k in range(N):
  MaxA = max(MaxA,A[k])
  sumA += A[k]
  sum += sumA
  ans = (k+1)*MaxA+sum
  print(ans)