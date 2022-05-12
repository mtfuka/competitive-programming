N,Q=map(int,input().split())
ball=[i for i in range(1,N+1)]
pos=[i for i in range(N)]
for i in range(Q):
    x=int(input())
    x-=1
    i=pos[x]
    j=i+1
    if j==N:j=i-1
    y=ball[j]-1
    ball[i],ball[j]=ball[j],ball[i]
    pos[x],pos[y]=pos[y],pos[x] #pos[ball[j]]でインデックスjのballのposが取得できる
print(*ball)