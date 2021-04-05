MOD = 10**9+7
N, K = map(int, input().split())
A = list(map(int,input().split()))
ans = 0

#Aの転倒数
c = 0
for i in range(N):
  for j in range(i+1,N):
    if A[i]>A[j]:c+=1

#2つのAの間の転倒数
d = 0
for i in range(N):
  for j in range(N):
    if A[i]>A[j]:d+=1

ans = c*K + d*K*(K-1)//2
print(ans%MOD)
