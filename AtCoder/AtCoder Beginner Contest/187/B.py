N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
  x[i],y[i] = map(int,input().split())
ans = 0
for i in range(N):
  for j in range(i+1,N):
    if -1<=(y[j]-y[i])/(x[j]-x[i])<=1:
      ans += 1
print(ans)