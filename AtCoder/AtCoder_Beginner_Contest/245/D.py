N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
B=[0 for i in range(M+1)]
for i in range(M+1):
    B[M-i]+=C[N+M-i]
    for j in range(1,N+1):
        if -i+j>0:
            break
        B[M-i]-=A[N-j]*B[M-i+j]
    B[M-i]//=A[N]
print(*B)