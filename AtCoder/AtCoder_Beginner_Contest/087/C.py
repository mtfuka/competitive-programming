N = int(input())
A1 = [int(x) for x in input().split()]
A2 = [int(x) for x in input().split()]

ans=0
cnt=0
for i in range(N):
  for j in range(i+1):
    cnt+=A1[j]
  for k in range(i,N):
    cnt+=A2[k]
  ans=max(ans,cnt)
  cnt=0

print(ans)
