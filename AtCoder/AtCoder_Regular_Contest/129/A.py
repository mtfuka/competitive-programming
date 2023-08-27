N,L,R=map(int,input().split())
ans=0
cnt=0
while N>0:
  if N%2==1:
    ans+=max(0,min(R,2**(cnt+1)-1)-max(L,2**cnt)+1)
  N//=2
  cnt+=1
print(ans)