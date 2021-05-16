import math
A,B = map(int,input().split())
GCD = math.gcd(A,B)
C = A//GCD
if B>10**18//C:print('Large')
else:print(B*C)