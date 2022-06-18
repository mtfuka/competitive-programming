N=int(input())
A=list(map(int,input().split()))
A=list(reversed(A))
S=[0 for i in range(N+1)]
for i in range(N):
    S[i+1]=S[i]+A[i]
S.pop(0)
P=0
for i in range(N):
    if S[i]>=4:P+=1
print(P)