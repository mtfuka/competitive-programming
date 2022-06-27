import math
f=math.factorial
MOD=998244353
N=int(input())
ng=N**2%MOD
ng=ng*f(N**2)//f(N**2-2*N+1)//f(2*N-1)%MOD
ng=ng*f(N-1)**2%MOD
ng=ng*f(N**2-2*N+1)%MOD
print((f(N**2)-ng)%MOD)