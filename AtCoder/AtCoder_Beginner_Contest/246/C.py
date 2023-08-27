N,K,X=map(int,input().split())
A=list(map(int,input().split()))
k=0
s=sum(A)
for i in range(N):
    k+=A[i]//X
    A[i]%=X
if k>=K:
    print(s-K*X)
else:
    A.sort()
    print(sum(A[:-(K-k)]))