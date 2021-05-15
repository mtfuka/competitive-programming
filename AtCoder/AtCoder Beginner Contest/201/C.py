S = input()
maru = [i for i, x in enumerate(S) if x == 'o']
if len(maru)>4:
  print(0)
  exit()
batu = [i for i, x in enumerate(S) if x == 'x']
kouho = []
for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        kouhosub = []
        kouhosub.append(i)
        kouhosub.append(j)
        kouhosub.append(k)
        kouhosub.append(l)
        kouho.append(kouhosub)
ans = 0
for list in kouho:
  a = True
  for i in maru:
    if not i in list:
      a = False
  for j in batu:
    if j in list:
      a = False
  if a:ans += 1
print(ans)
