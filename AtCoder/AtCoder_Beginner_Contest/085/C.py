N, Y = map(int, input().split())
for x in range(N+1):
  for y in range(N+1-x): #x枚分引くと計算量減るしx+y<=Nなども要らない
      if(10000*x+5000*y+1000*(N-x-y)==Y):
        print(x,y,N-x-y)
        exit()
print(-1,-1,-1)
