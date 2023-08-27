import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
S=[0 for i in range(N+1)]
for i in range(N):
    S[i+1]=S[i]+A[i]
S.pop(0)
for i in range(Q):
    X=int(input())
    l=bisect.bisect_left(A,X)
    if l==0 or l==N:print(abs(S[N-1]-X*N))
    else:
        f=X*l-S[l-1]
        b=S[N-1]-S[l-1]-X*(N-l)
        print(f+b)