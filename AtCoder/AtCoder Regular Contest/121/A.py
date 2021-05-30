N = int(input())
x = [0]*N
y = [0]*N
for i in range(N):
  x[i],y[i] = map(int,input().split())

if x.index(max(x))==y.index(max(y)) and x.index(min(x))==y.index(min(y)):
  x.sort()
  y.sort()
  print(max(x[N-1]-x[1],x[N-2]-x[0],y[N-1]-y[1],y[N-2]-y[0]))
else:
  x.sort()
  y.sort()  
  if (max(x)-min(x))>(max(y)-min(y)):
    print(max(x[N-1]-x[1],x[N-2]-x[0],y[N-1]-y[0]))
  elif (max(x)-min(x))==(max(y)-min(y)):
    print(x[N-1]-x[0])
  else:
    print(max(x[N-1]-x[0],y[N-1]-y[1],y[N-2]-y[0]))