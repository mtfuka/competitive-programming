X,Y,Z = list(map(int,input().split()))
for i in range(1000001):
  if X*i>=Y*Z:
    print(i-1)
    exit()