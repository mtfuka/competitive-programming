N,X=map(int,input().split())
L=[0 for i in range(N)]
a=[0 for i in range(N)]
for i in range(N):
    l=list(map(int,input().split()))
    L[i]=l[0]
    a[i]=l[1:]
ans=0
def dfs(i,s):
    global ans
    if i==N:
        if s==X:ans+=1
        return
    for aij in a[i]:
        dfs(i+1,s*aij)
dfs(0,1)
print(ans)