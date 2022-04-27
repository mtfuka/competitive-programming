N=int(input())
T=list(map(int,input().split()))
A=0
for i in range(N):
  A=(A//2**T[i]+1)*2**T[i]
  if A%2**(T[i]+1)==0:
    A+=2**T[i]
print(A)