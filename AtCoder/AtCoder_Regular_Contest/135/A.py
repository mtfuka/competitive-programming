from functools import lru_cache
MOD=998244353
@lru_cache
def f(n):
  if n<=4:
    return n
  else:
    return f(n//2)*f((n+1)//2)%MOD
X=int(input())
print(f(X))