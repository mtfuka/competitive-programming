N,M=map(int,input().split())
A=[0 for i in range(M)]
B=[0 for i in range(M)]
for i in range(M):
    A[i],B[i]=map(int,input().split())
K=int(input())
C=[0 for i in range(K)]
D=[0 for i in range(K)]
for i in range(K):
    C[i],D[i]=map(int,input().split())
ans=-1
for i in range(1<<K):
    dish=set()
    cnt=0
    for j in range(K):
        if i>>j&1:dish.add(C[j])
        else:dish.add(D[j])
    for j in range(M):
        if A[j] in dish and B[j] in dish:cnt+=1
    ans=max(ans,cnt)
print(ans)