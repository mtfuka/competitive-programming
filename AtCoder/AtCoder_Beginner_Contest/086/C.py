N = int(input())
t = [0] * (N+1)
x = [0] * (N+1)
y = [0] * (N+1)
for i in range(1,N+1):
  t[i], x[i], y[i] = map(int, input().split())

for i in range(N):
  dt = t[i+1] - t[i]
  distance = abs(x[i+1]-x[i])+abs(y[i+1]-y[i])
  if dt<distance or dt%2!=distance%2:
    print("No")
    exit()
print("Yes")
