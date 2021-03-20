H,W=map(int,input().split())
C = []
for _ in range(H):
    C.append(input().split())
for i in range(H):
    print(*C[i]) #*付けるとリスト外せる
    print(*C[i])
