N,X=map(int,input().split())
A=list(map(int,input().split()))
rumor=[False]*N
rumor[X-1]=True
i=X-1
while True:
    if rumor[A[i]-1]:
        break
    else:
        rumor[A[i]-1]=True
        i=A[i]-1
ans=0
for i in range(N):
    if rumor[i]:
        ans+=1
print(ans)