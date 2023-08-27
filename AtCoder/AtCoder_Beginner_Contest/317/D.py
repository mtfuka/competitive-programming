N=int(input())
sum_Z=0
XYZ=[]
for i in range(N):
    X,Y,Z=map(int,input().split())
    sum_Z+=Z
    XYZ.append([(X+Y+1)//2-X,Z])
dp=[[float('inf') for j in range(sum_Z+1)] for i in range(N+1)]
dp[0][0]=0
for i in range(N):   
    for j in range(sum_Z+1):
        dp[i+1][j]=dp[i][j]
        if j>=XYZ[i][1]:
            dp[i+1][j]=min(dp[i][j-XYZ[i][1]]+max(XYZ[i][0],0),dp[i][j])
ans=float('inf')
for i in range(N):
    for j in range(sum_Z+1):
        if j>=(sum_Z+1)//2:
            ans=min(dp[i+1][j],ans)
print(ans)
