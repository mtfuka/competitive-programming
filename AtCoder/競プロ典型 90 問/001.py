N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))

#M以上のピースに分割できるか
def solve(M):
  cnt=0
  pre=0
  for Ai in A:
    if Ai-pre>=M and L-Ai>=M:
      cnt+=1
      pre=Ai
  if cnt>=K:
    return True
  return False

#二分探索
left=-1
right=L+1
while right-left>1:
  mid = (left+right)//2
  if solve(mid):
    left=mid
  else:
    right=mid

print(left)