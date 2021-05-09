import math
T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
for i in range(Q):
  E = int(input())
  y = -L/2*math.sin(E/T*2*math.pi)
  z = L/2-L/2*math.cos(E/T*2*math.pi)
  print(math.degrees(math.atan(z/math.sqrt(X**2+(Y-y)**2))))