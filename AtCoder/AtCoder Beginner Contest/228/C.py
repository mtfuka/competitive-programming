N,K=map(int,input().split())
P=[]
Psum=[0]*N
for i in range(N):
  p=list(map(int,input().split()))
  P.append(p)
  Psum[i]=sum(p)
Psum.sort(reverse=True)
for i in range(N):
  if Psum[K-1]<=sum(P[i])+300:
    print('Yes')
  else:
    print('No')