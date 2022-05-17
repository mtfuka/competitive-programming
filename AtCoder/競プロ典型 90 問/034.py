N,K=map(int,input().split())
a=list(map(int,input().split()))
ans=0
j=0
cnt=0
d={}
for i in range(N):
    while j<N: #尺取法
        if cnt==K and (not a[j] in d or d[a[j]]==0):
            break
        if not a[j] in d or d[a[j]]==0:
            d[a[j]]=1
            cnt+=1
        else:
            d[a[j]]+=1
        j+=1
    ans=max(ans,j-i)
    if d[a[i]]==1:cnt-=1
    d[a[i]]-=1
print(ans)