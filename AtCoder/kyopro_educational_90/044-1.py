from collections import deque
N,Q = map(int,input().split())
A = deque(list(map(int,input().split())))
for i in range(Q):
    T,x,y = map(int,input().split())
    if T==1:
        A[x-1],A[y-1]=A[y-1],A[x-1]
    if T==2:
        A.appendleft(A[N-1])
        A.pop()
    if T==3:
        print(A[x-1])