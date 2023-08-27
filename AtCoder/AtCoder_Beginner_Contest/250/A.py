H,W=map(int,input().split())
R,C=map(int,input().split())
dx=[-1,0,1,0]
dy=[0,-1,0,1]
ans=0
for i in range(4):
    if 0<R+dx[i]<=H and 0<C+dy[i]<=W:
        ans+=1
print(ans)