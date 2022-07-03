from collections import defaultdict
MOD=998244353 
H,W=map(int,input().split())
S=[]
for i in range(H):
  S.append(list(input()))
d=defaultdict(set)
ans=1
for i in range(H):
  for j in range(W):
    d[i+j].add(S[i][j])
for s in d.values():
  if 'R' in s and 'B' in s:exit(print(0))
  elif s=={'.'}:ans=ans*2%MOD
print(ans)