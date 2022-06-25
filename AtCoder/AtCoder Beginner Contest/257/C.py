import bisect
N=int(input())
S=input()
W=list(map(int,input().split()))
child,adult=[],[]
for i in range(N):
    if S[i]=='0':child.append(W[i])
    else:adult.append(W[i])
child.sort()
adult.sort()
ans=0
for i in range(N):
    if S[i]=='0':
        c=bisect.bisect_left(child,W[i]+1)
        a=bisect.bisect_left(adult,W[i]+1)
        ans=max(ans,c+len(adult)-a)
    else:
        c=bisect.bisect_left(child,W[i])
        a=bisect.bisect_left(adult,W[i])
        ans=max(ans,c+len(adult)-a)
print(ans)