N=int(input())
A=[0 for i in range(N)]
B=[0 for i in range(N)]
for i in range(N):
	A[i],B[i]=map(int,input().split())
ans=10**6
for i in range(N):
	for j in range(N):
		if(i==j):ans=min(ans,A[i]+B[j])
		else:ans=min(ans,max(A[i],B[j]))
print(ans)