H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
B=[[0]*H for i in range(W)]
for i in range(H):
    for j in range(W):
        B[j][i]=A[i][j]
for Bi in B:
    print(*Bi)