R,X,Y = map(int, input().split())
import math
distance = math.sqrt(X*X+Y*Y)
if distance<R:
  print(2)
  exit()
print((math.ceil(distance)+R-1)//R)
