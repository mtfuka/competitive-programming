#listのpop(0)もO(N)かかるのでdequeを使う
#listを定数で取り出しておくと高速化されて通ることもある
from collections import deque
Q=int(input())
l=deque()
for i in range(Q):
    query=list(map(int,input().split()))
    if query[0]==1:
        l.append([query[1],query[2]])
    if query[0]==2:
        ans=0
        ball=query[1]
        while ball>0:
            if l[0][1]<=ball:
                ans+=l[0][0]*l[0][1]
                ball-=l[0][1]
                l.popleft()
            else:
                ans+=l[0][0]*ball
                l[0][1]-=ball
                ball=0
        print(ans)