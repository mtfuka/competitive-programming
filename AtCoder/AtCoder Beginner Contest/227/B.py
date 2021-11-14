N=int(input())
S=list(map(int,input().split()))
l=[]
for a in range(1,1000):
    for b in range(1,1000):
        l.append(4*a*b+3*a+3*b)
ans=0
for s in S:
    if not(s in l):
        ans+=1
print(ans)