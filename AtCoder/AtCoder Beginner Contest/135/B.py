N = int(input())
p = list(map(int, input().split()))
P = []
for _ in range(1,N+1):
  P.append(_)
if p==P:
  print("YES")
  exit()
for i in range(N):
  for j in range(N):
    p[i],p[j]=p[j],p[i]
    if p==P:
      print("YES")
      exit()
    else:
      p[j],p[i]=p[i],p[j]
print("NO")
