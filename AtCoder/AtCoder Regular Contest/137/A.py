# Euclidean Algorithm
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n
L,R=map(int,input().split())

ans=0
x=L
y=R
N=0
while True:
    if gcd(x,y)==1:
        ans=y-x
        break
    x+=1
    N+=1
for x in range(L,L+N+1):
    for y in range(R-N,R+1):
        if gcd(x,y)==1:
            ans=max(ans,y-x)
print(ans)