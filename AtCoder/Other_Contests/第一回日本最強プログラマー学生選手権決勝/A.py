N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#A[i]+B[j]は最大2*10**6通りしかないので全探索可能
d = {}
for i in range(N):
  for j in range(M):
    if A[i]+B[j] in d:
      print(*d[A[i]+B[j]],i,j)
      exit()
    else:
      d[A[i]+B[j]] = i,j
print(-1)
