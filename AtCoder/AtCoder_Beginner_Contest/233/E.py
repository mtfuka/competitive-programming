from collections import deque
X=list(input())
x=len(X)
y=0
z=0
for Xi in X:
    z+=int(Xi)
d=deque()
for i in range(x-1):
    d.appendleft(str((z+y)%10))
    y=(z+y)//10
    z-=int(X[-1-i])
d.appendleft(str(int(X[0])+y))
print("".join(d))