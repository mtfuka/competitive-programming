N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

a = {}
c = {}
for Ai in A:
    a[Ai]=a.get(Ai,0)+1
for Cj in C:
    c[Cj]=c.get(Cj,0)+1

ans = 0
for i in c:
  ans += a.get(B[i-1],0)*c[i]
print(ans)
