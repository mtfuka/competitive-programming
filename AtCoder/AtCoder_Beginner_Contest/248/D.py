import bisect
N=int(input())
A=list(map(int,input().split()))
l=[[] for i in range(N+1)]
for i in range(N):
    l[A[i]].append(i+1)
Q=int(input())
for i in range(Q):
    L,R,X=map(int,input().split())
    left=bisect.bisect_left(l[X],L)
    right=bisect.bisect_right(l[X],R)
    print(right-left)