from cmath import inf
N=int(input())
S=[]
for i in range(N):
    S.append(input())
cnt=[[0 for j in range(10)]for i in range(10)]
for i in range(N):
    for j in range(10):
        cnt[int(S[i][j])][j]+=1
ans=inf
for i in range(10):
    m=0
    for  j in range(10):
        m=max(m,(cnt[i][j]-1)*10+j)
    ans=min(ans,m)
print(ans)