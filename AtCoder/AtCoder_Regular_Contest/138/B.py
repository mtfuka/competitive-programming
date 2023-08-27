from collections import deque
N=int(input())
A=deque(map(int,input().split()))
flip=False
while len(A)>0:
  head=A[0]^flip
  tail=A[-1]^flip
  if tail==0:
    A.pop()
  elif head==0:
    A.popleft()
    flip^=True
  else:
    exit(print("No"))
print("Yes")