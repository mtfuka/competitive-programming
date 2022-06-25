N,K,Q=map(int,input().split())
A=list(map(int,input().split()))
L=list(map(int,input().split()))
for i in range(Q):
    if L[i]==K and A[L[i]-1]!=N:
        A[L[i]-1]+=1
    elif A[L[i]-1]!=N and A[L[i]-1]+1!=A[L[i]]:
        A[L[i]-1]+=1
print(*A)