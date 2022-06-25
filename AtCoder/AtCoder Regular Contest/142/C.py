from cmath import inf
N=int(input())
d=[[0 for j in range(N+1)]for i in range(3)]
for j in range(3,N+1):
    print(f"? 1 {j}")
    d[1][j]=int(input())   
for j in range(3,N+1):
    print(f"? 2 {j}")
    d[2][j]=int(input())
dist=inf
for j in range(3,N+1):
    dist=min(dist,d[1][j]+d[2][j])
if dist!=3:exit(print(f"! {dist}"))
m=[]
for j in range(3,N+1):
    if dist==d[1][j]+d[2][j]:m.append(j)
if len(m)!=2:exit(print(f"! 1"))
else:
    print(f"? {m[0]} {m[1]}")
    if int(input())==1:exit(print(f"! {dist}"))
    else:exit(print(f"! 1"))