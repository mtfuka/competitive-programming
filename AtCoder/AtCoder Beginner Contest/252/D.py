N=int(input())
A=list(map(int,input().split()))
cnt=[0 for i in range(2*10**5+1)]
for i in range(N):
    cnt[A[i]]+=1
for i in range(2*10**5):
    cnt[i+1]+=cnt[i]
#cnt[i]=i以下の値の個数
ans=0
for i in range(N):
    ans+=cnt[A[i]-1]*(N-cnt[A[i]])
print(ans)