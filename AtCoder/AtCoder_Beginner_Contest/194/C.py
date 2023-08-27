N=int(input())
A=list(map(int,input().split()))

sum1=0
sum2=0
for i in range(N):
	sum1+=A[i]**2
	sum2+=A[i]
ans=N*sum1-sum2**2
print(ans)