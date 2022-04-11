from cmath import inf
N,K=map(int,input().split())
A=list(map(int,input().split()))
l=[]
for i in range(N):
  l.append((A[i],-i))
l.sort()
change,ans=inf,inf
for i in range(N):
  if -l[i][1]<=K-1:
    change=min(change,l[i][1])
  else:
    ans=min(ans,-l[i][1]+change)
if ans==inf:
  ans=-1
print(ans)