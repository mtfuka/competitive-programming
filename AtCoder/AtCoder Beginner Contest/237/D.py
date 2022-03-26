N=int(input())
S=input()
A=[0 for i in range(N+1)]
first,last=0,N
for i in range(N):
    if S[i]=='L':
        A[last]=i
        last-=1
    else:
        A[first]=i
        first+=1
if S[-1]=='L':
    A[last]=N
else:
    A[first]=N
print(*A)