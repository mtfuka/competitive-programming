N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum = 0
for i in range(N):
    sum += abs(A[i]-B[i])
if sum<=K and (K-sum)%2==0:
    print("Yes")
else:print("No")