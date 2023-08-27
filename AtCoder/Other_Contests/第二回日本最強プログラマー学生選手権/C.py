A,B = map(int,input().split())
N = B-A
for i in range(N):
  if (B//(N-i) - (A+N-i-1)//(N-i))>=1:
    print(N-i)
    exit()