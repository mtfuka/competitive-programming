N=int(input())
sx,sy,tx,ty=map(int,input().split())
x=[0 for i in range(N)]
y=[0 for i in range(N)]
r=[0 for i in range(N)]
for i in range(N):
    x[i],y[i],r[i]=map(int,input().split())
s,t=0,0
for i in range(N):
    if (sx-x[i])**2+(sy-y[i])**2==r[i]**2:s=i
    if (tx-x[i])**2+(ty-y[i])**2==r[i]**2:t=i
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

uf=UnionFind(N)
for i in range(N):
    for j in range(N):
        d=(x[i]-x[j])**2+(y[i]-y[j])**2
        if abs(r[i]-r[j])**2<=d<=(r[i]+r[j])**2:
            uf.union(i,j)
if uf.same(s,t):print("Yes")
else:print("No")