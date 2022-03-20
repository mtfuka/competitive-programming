N,L,W =map(int,input().split())
a=list(map(int,input().split()))
a.sort()
right=0
ans=0
for i in range(N):
    ans+=(a[i]-right+W-1)//W
    right=a[i]+W
ans+=(L-right+W-1)//W
print(ans)