N,X = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
maxa = max(A)
for a in A:
  if a+X>=maxa:ans+=1
print(ans)
