from math import gcd
N=int(input())
xy=[]
for i in range(N):
  l=list(map(int,input().split()))
  xy.append(l)
s=set()
for i in range(N):
  for j in range(N):
    if i==j:
      continue
    x=xy[j][0]-xy[i][0]
    y=xy[j][1]-xy[i][1]
    s.add((x//gcd(x,y),y//gcd(x,y)))
print(len(s))