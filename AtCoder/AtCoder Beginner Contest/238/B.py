N=int(input())
A=list(map(int,input().split()))
l=[0]*360
i=0
l[i]=1
for j in range(N):
    i+=A[j]
    if i>360:i-=360
    l[i]=1
kakudo=[]
first=0
last=0
for j in range(1,360):
    if l[j]==1:
        last=j
        kakudo.append(last-first)
        first=last
kakudo.append(360-sum(kakudo))
print(max(kakudo))