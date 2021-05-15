import math
A,B = map(int,input().split())
GCD = math.gcd(A,B)
a = A//GCD
b = B//GCD
if a*b>10**18/GCD:print('Large')
else:print(GCD*a*b)