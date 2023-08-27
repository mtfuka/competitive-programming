N = int(input())
ans=0
for i in range(1,10**6):
  if int(str(i)+str(i))<=N:ans+=1
print(ans)
