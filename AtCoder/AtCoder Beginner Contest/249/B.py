S=input()
Oomoji=False
komoji=False
different=False
for c in S:
    if 'A'<=c<='Z':
        Oomoji=True
    if 'a'<=c<='z':
        komoji=True
if len(S)==len(set(S)):
    different=True
if Oomoji and komoji and different:
    print("Yes")
else:
    print("No")