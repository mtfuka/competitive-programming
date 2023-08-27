N=int(input())
LR=[]
for i in range(N):
    LR.append(list(map(int,input().split())))
LR.sort()
L=LR[0][0]
R=LR[0][1]
ans=[]
for i in range(N):
    if R<LR[i][0]:
        ans.append([L,R])
        L=LR[i][0]
        R=LR[i][1]
    elif R<LR[i][1]:
        R=LR[i][1]
ans.append([L,R])
for a in ans:
    print(*a)