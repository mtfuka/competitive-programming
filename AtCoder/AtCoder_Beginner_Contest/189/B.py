N,X = map(int, input().split())
Alcohol = 0
for i in range(1,N+1):
  V,P = map(int, input().split())
  Alcohol += V*P
  if Alcohol>X*100: #浮動小数点の処理
    print(i)
    exit()
print(-1)
