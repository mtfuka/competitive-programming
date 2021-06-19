N = int(input())
A = list(map(int,input().split()))

a = {}
for Ai in A:
    a[Ai]=a.get(Ai,0)+1

ans = 0
for i in a:
  ans += (N-a[i])*a[i]
print(ans//2)