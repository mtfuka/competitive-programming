N,M = map(int,input().split())
B=[]
for i in range(N):
  B.append(list(map(int,input().split())))
for i in range(N):
  for j in range(M-1):
    if B[i][j]+1!=B[i][j+1]:
      print('No')
      exit()
for i in range(N-1):
  for j in range(M):
    if B[i][j]+7!=B[i+1][j]:
      print('No')
      exit()
for j in range(M-1):
  if B[0][j]%7==0:
    print('No')
    exit()
print('Yes')