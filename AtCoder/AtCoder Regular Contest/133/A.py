from aifc import Aifc_write


N = int(input())
A = list(map(int,input().split()))
ans=[]
a=0
for i in range(N-1):
  if A[i]>A[i+1]:
    a=A[i]
    break
if a==0:
  a=max(A)
for Ai in A:
  if Ai!=a:
    ans.append(Ai)
print(*ans)