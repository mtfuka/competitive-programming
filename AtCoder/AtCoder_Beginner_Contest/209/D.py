import queue
N,Q=map(int,input().split())
G=[[]for i in range(N)]
for i in range(N-1):
  a,b=map(int,input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
dist=[-1 for i in range(N)]
q=queue.Queue()
q.put(0)
dist[0]=0
while not q.empty():
  i=q.get()
  for j in G[i]:
    if dist[j]==-1:
      dist[j]=dist[i]+1
      q.put(j)
for i in range(Q):
  c,d=map(int,input().split())
  if (dist[c-1]+dist[d-1])%2==0:print("Town")
  else:print("Road")