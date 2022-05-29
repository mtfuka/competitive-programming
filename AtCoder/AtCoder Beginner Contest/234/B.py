N=int(input())
x,y=[0 for i in range(N)],[0 for i in range(N)]
for i in range(N):
    x[i],y[i]=map(int,input().split())
ans=0
for i in range(N):
    for j in range(i+1,N):
        ans=max(ans,((x[j]-x[i])**2+(y[j]-y[i])**2)**0.5)
print(ans)