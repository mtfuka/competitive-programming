N,Q = map(int,input().split())
nil=-1
front=[nil]*N
back=[nil]*N
for i in range(Q):
  query=list(map(int,input().split()))
  if query[0]==1:
    x=query[1]-1
    y=query[2]-1
    front[y]=x
    back[x]=y
  if query[0]==2:
    x=query[1]-1
    y=query[2]-1
    front[y]=nil
    back[x]=nil
  if query[0]==3:
    x=query[1]-1
    while front[x]!=nil:
      x=front[x] #先頭まで移動
    ans=[]
    while x!=nil:
      ans.append(x+1)
      x=back[x] #先頭から末尾まで
    print(len(ans),*ans)