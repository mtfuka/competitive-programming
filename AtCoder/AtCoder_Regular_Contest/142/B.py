N=int(input())
masu=[[0 for j in range(N)]for i in range(N)]
cnt=1
for i in range(N):
    for j in range(N):
        if (i+j)%2==0:
            masu[i][j]=cnt
            cnt+=1
for i in range(N):
    for j in range(N):
        if (i+j)%2==1:
            masu[i][j]=cnt
            cnt+=1
for i in range(N):
    print(*masu[i])