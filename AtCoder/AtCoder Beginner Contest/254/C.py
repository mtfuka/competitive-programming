N,K=map(int,input().split())
A=list(map(int,input().split()))
B=[0 for i in range(N)]
for i in range(K):
    B[i::K]=sorted(A[i::K])
if sorted(A)==B:print("Yes")
else:print("No")