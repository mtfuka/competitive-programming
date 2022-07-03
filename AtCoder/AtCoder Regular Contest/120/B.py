MOD=998244353 
H,W=map(int,input().split())
S=[]
for i in range(H):
  S.append(list(input()))
ans=1
for i in range(H):
  s=set()
  for j in range(W):
    if H<=i+j:break
    s.add(S[i+j][W-1-j])
  if 'R' in s and 'B' in s:exit(print(0))
  elif s=={'.'}:ans=ans*2%MOD
for j in range(W-1):
  s=set()
  for i in range(H):
    if j<i:break
    s.add(S[i][j-i])
  if 'R' in s and 'B' in s:exit(print(0))
  elif s=={'.'}:ans=ans*2%MOD
print(ans)