N=int(input())
A=list(map(int,input().split()))
A.insert(0,0)
ans=[0]*N
M,m=(10**6,0),(10**6,0)
for i in range(N):
  if A[i]<A[i+1]:
    M=(i,A[i])
    if m[0]!=10**6:
      ans[m[0]]=1
  if A[i]>=A[i+1]:
    m=(i,A[i])
    if M[0]!=10**6:
      if i==N-1:
        ans[i]=1
      ans[M[0]]=1
print(*ans)