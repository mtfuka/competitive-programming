B,C=map(int,input().split())
ans=0
if B==0:
  ans=C
elif B>0:
  if C==1:
    ans=2
  else:
    ans=2*min(2*B,C)-1
    ans+=max(0,C-2*B)
else:
  if C==1:
    ans=2
  else:
    ans=2*min(-2*B+1,C)-1
    ans+=max(0,C+2*B-1)
print(ans)