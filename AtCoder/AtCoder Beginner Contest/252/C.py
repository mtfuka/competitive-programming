from cmath import inf
N=int(input())
S=[]
for i in range(N):
    S.append(input())
ans=inf
for i in range(10):
    l=[0 for j in range(10)]
    s=set()
    for j in range(N):
        for k in range(10):
            if str(i)==S[j][k]:
                l[k]+=1
                s.add(k)
    M=max(l)
    if M==1:
        ans=min(ans,max(s))
    else:
        for j in reversed(range(10)):
            if M==l[j]:
                ans=min(ans,(M-1)*10+j)
                break
print(ans)