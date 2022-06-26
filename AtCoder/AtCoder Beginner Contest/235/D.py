from collections import deque
a,N=map(int,input().split())
M=10**6
dist=[-1 for i in range(M)]
Q=deque()
dist[1]=0
Q.append(1)
while len(Q):
    x=Q.popleft()
    dx=dist[x]
    op1=x*a
    if op1<M and dist[op1]==-1:
        dist[op1]=dx+1
        Q.append(op1)
    if x>=10 and x%10!=0:
        y=str(x)
        op2=int(y[-1]+y[:-1])
        if op2<M and dist[op2]==-1:
            dist[op2]=dx+1
            Q.append(op2)
print(dist[N])