N=int(input())
A=list(map(int,input().split()))
l=[0 for i in range(N)]
for Ai in A:
    l[Ai-1]+=1
for i in range(N):
    if l[i]==3:
        print(i+1)