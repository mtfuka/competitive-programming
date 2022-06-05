N=2**20
A=[-1 for i in range(N)]
Q=int(input())
parent=[i for i in range(N)]
def find(x):
  if parent[x]==x:return x
  else:
    parent[x]=find(parent[x])
    return parent[x]
for i in range(Q):
  t,x=map(int,input().split())
  if t==1:
    h=x%N
    A[find(h)]=x
    parent[find(h)]=(find(h)+1)%N
  else:
    print(A[x%N])