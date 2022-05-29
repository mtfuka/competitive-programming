H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(list(input()))
ans=[]
for i in range(H):
    for j in range(W):
        if S[i][j]=='o':
            ans.append([i,j])
print(abs(ans[0][0]-ans[1][0])+abs(ans[0][1]-ans[1][1]))