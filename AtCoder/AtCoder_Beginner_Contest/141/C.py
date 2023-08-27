N,K,Q = map(int,input().split())
ans = [0]*N
for i in range(Q):
    A = int(input())
    ans[A-1] += 1
for a in ans:
    if K-Q+a>0:print("Yes")
    else:print("No")
