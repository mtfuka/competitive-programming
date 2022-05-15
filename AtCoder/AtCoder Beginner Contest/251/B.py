N,W=map(int,input().split())
A=list(map(int,input().split()))
w=[0 for i in range(10**6+1)]
for i in range(N):
    w[A[i]]+=1
for i in range(N):
    for j in range(i+1,N):
        if A[i]+A[j]<=10**6:
            w[A[i]+A[j]]+=1
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i]+A[j]+A[k]<=10**6:
                w[A[i]+A[j]+A[k]]+=1
ans=0
for i in range(1,W+1):
    if w[i]>0:
        ans+=1
print(ans)