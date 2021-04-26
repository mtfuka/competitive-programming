N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = [0]*1001
for i in range(N):
  for j in range(A[i],B[i]+1):
    a[j] += 1
ans = 0
for i in range(1001):
  if a[i]==N:ans += 1
print(ans)