T = int(input())
for _ in range(T):
  L, R = map(int, input().split())
  if R-2*L+1<=0:print(0)
  else:print((R-2*L+1)*(R-2*L+2)//2)
