H,W=map(int,input().split())
P=[]
for i in range(H):
    P.append(list(map(int,input().split())))
ans=0
for i in range(1,1<<H):
    R=[]
    for j in range(W):
        value=0
        flag=True
        for k in range(H):
            if (i>>k)&1==0:continue
            if value==0:value=P[k][j]
            if P[k][j]!=value:flag=False
        if flag:R.append(value)
    d={}
    m=0
    for j in range(len(R)):
        if R[j] in d:d[R[j]]=d[R[j]]+1
        else:d[R[j]]=1
        m=max(m,d[R[j]])
    cntH,cntW=0,m
    for j in range(H):
        if (i>>j)&1:cntH+=1
    ans=max(ans,cntH*cntW)
print(ans)