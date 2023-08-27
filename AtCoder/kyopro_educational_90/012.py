import collections
from curses import cbreak
class UnionFind():
    def __init__(self):
        '''
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        '''
        self.parents = dict()                                      # {子要素:親ID,}
        self.members_set = collections.defaultdict(lambda : set()) # keyが根でvalueが根に属する要素要素(tupleや文字列可)
        self.roots_set = set()                                     # 根の集合(tupleや文字列可)
        self.key_ID = dict()                                       # 各要素にIDを割り振る
        self.ID_key = dict()                                       # IDから要素名を復元する
        self.cnt = 0                                               # IDのカウンター

    def dictf(self,x): # 要素名とIDをやり取りするところ
        if x in self.key_ID:
            return self.key_ID[x]
        else:
            self.cnt += 1
            self.key_ID[x] = self.cnt
            self.parents[x] = self.cnt
            self.ID_key[self.cnt] = x
            self.members_set[x].add(x)
            self.roots_set.add(x)
            return self.key_ID[x]

    def find(self, x):
        ID_x = self.dictf(x)
        if self.parents[x] == ID_x:
            return x
        else:
            self.parents[x] = self.key_ID[self.find(self.ID_key[self.parents[x]])]
            return self.ID_key[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in self.members_set[y]:
            self.members_set[x].add(i)
        self.members_set[y] = set()
        self.roots_set.remove(y)
        self.parents[y] = self.key_ID[x]

    def size(self, x):#xが含まれる集合の要素数
        return len(self.members_set[self.find(x)])

    def same(self, x, y):#同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):#xを含む集合の要素
        return self.members_set[self.find(x)]

    def roots(self):#根の要素
        return self.roots_set

    def group_count(self):#根の数
        return len(self.roots_set)

    def all_group_members(self):#根とその要素
        return {r: self.members_set[r] for r in self.roots_set}

def query1(px,py):
  red[px][py]=True
  dx=[-1,0,1,0]
  dy=[0,-1,0,1]
  for i in range(4):
    if 0<=px+dx[i]<H and 0<=py+dy[i]<W:
      if red[px+dx[i]][py+dy[i]]:
        UF.union((px,py),(px+dx[i],py+dy[i]))
        
def query2(px,py,qx,qy):
  if not(red[px][py] and red[qx][qy]):
    print("No")
  else:
    if UF.same((px,py),(qx,qy)):
      print("Yes")
    else:
      print("No")

H,W=map(int,input().split())
Q=int(input())
red=[[False for j in range(W)]for i in range(H)]
UF=UnionFind()
for qi in range(Q):
  q=list(map(int,input().split()))
  if q[0]==1:
    r=q[1]-1
    c=q[2]-1
    query1(r,c)
  if q[0]==2:
    ra=q[1]-1
    ca=q[2]-1
    rb=q[3]-1
    cb=q[4]-1
    query2(ra,ca,rb,cb)