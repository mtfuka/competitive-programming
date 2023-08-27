N=int(input())
A=list(map(int,input().split()))
l=[0 for i in range(2*10**5+1)]
for i in range(N):
    l[A[i]]+=1
ans=0
for i in range(1,2*10**5+1):
    for j in range(1,int(2*10**5/i)+1):
        ans+=l[i]*l[j]*l[i*j]
print(ans)