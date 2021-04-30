A,B,C = map(int,input().split())
import math
from functools import reduce
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)
GCD = my_gcd(A,B,C)
print(A//GCD-1+B//GCD-1+C//GCD-1)