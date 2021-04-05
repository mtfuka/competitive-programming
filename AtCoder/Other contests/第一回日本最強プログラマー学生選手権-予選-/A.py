M, D = map(int, input().split())
ans = 0
for m in range(1,M+1):
  for d in range(22,D+1):
    if d%10==0 or d%10==1:continue
    if d%10*(d//10)==m:
      ans+=1
print(ans)
