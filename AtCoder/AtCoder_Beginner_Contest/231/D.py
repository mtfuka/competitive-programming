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

N,M=map(int,input().split())
uf=UnionFind(N)
hasLoop=False
A=[0]*M
B=[0]*M
for i in range(M):
    A[i],B[i]=map(int,input().split())
    A[i]-=1
    B[i]-=1
    if uf.find(A[i]) == uf.find(B[i]):
            hasLoop = True
    uf.union(A[i], B[i])
if hasLoop:
    print("No")
    exit()

count=[0]*N
for i in range(M):
    count[A[i]]+=1
    count[B[i]]+=1
if max(count)>2:
    print("No")
    exit()

print("Yes")