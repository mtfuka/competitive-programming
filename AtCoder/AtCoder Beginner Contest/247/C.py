#extendは1つのdequeにする
from collections import deque
N=int(input())
S=deque([1])
ans=S
for i in range(2,N+1):
    ans=deque([i])
    ans.extend(S)
    ans.extendleft(S) #extendleftは逆順で連結されるので注意
    S=ans
print(*ans)