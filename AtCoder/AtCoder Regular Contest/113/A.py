K = int(input())
ans = 0
for A in range (1,K+1):
  for B in range (1,K+1):
    if A*B>K:break
    for C in range (1,K+1):
      if A*B*C>K:break
      ans+=1
print(ans)
