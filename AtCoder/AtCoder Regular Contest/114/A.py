N = int(input())
X = list(map(int, input().split()))
from math import gcd
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans = float("INFINITY")
l = len(P)
for i in range(1<<l):
  m = 1
  for j in range(l):
    if (1<<j)&i:
      m *= P[j]
  a = True
  for x in X:
    if gcd(x,m)==1:
      a = False
      break
  if a:
    ans = min(ans,m)
print(ans)