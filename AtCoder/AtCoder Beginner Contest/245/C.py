#コンテスト本番では虚解法だったのでリファクタリング
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
X=[(-1,-1) for i in range(N)]
X[0]=(A[0],B[0])
for i in range(N-1):
    if abs(X[i][0]-A[i+1])<=K and abs(X[i][0]-B[i+1])<=K:
        X[i+1]=(A[i+1],B[i+1])
    elif abs(X[i][0]-A[i+1])<=K and abs(X[i][1]-B[i+1])<=K:
        X[i+1]=(A[i+1],B[i+1])
    elif abs(X[i][1]-A[i+1])<=K and abs(X[i][0]-B[i+1])<=K:
        X[i+1]=(A[i+1],B[i+1])
    elif abs(X[i][1]-A[i+1])<=K and abs(X[i][1]-B[i+1])<=K:
        X[i+1]=(A[i+1],B[i+1])
    elif abs(X[i][0]-A[i+1])<=K:
        X[i+1]=(A[i+1],0)
    elif abs(X[i][0]-B[i+1])<=K:
        X[i+1]=(B[i+1],0)
    elif abs(X[i][1]-A[i+1])<=K:
        X[i+1]=(A[i+1],0)
    elif abs(X[i][1]-B[i+1])<=K:
        X[i+1]=(B[i+1],0)
    else:
        print("No")
        exit()
print("Yes")