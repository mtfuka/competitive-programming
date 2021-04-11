N = int(input())
X0,Y0 = map(int, input().split())
XN2,YN2 = map(int, input().split())
X = (X0+XN2)/2
Y = (Y0+YN2)/2
import math
pi = math.pi
X1 = X+(X0-X)*math.cos(2*pi/N)-(Y0-Y)*math.sin(2*pi/N)
Y1 = Y+(X0-X)*math.sin(2*pi/N)+(Y0-Y)*math.cos(2*pi/N)
print(X1,Y1)
