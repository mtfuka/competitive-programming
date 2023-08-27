N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

a = {}
b = {}
c = {}
for Ai in A:
    a[Ai%46]=a.get(Ai%46,0)+1
for Bj in B:
    b[Bj%46]=b.get(Bj%46,0)+1
for Ck in C:
    c[Ck%46]=c.get(Ck%46,0)+1

ans = 0
for i in a:
    for j in b:
         for k in c:
             if (i+j+k)%46==0:
                 ans += a[i]*b[j]*c[k]
print(ans)