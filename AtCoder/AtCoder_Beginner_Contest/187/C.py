N = int(input())
S1 = []
S2 = []
for i in range(N):
  S = input()
  if S[0]!='!': S1.append(S)
  else: S2.append(S[1:])
set = set(S1) & set(S2)
if len(set)==0:print('satisfiable')
else:print(list(set)[0])
