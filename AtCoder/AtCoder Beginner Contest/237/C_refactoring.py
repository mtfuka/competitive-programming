S=input()

for i in range(len(S)):
     if S[-i-1]!='a':
        break
for j in range(len(S)):
    if S[j]!='a':
        break

if i==len(S):
    print("Yes")
    exit()
if j>i:
    print("No")
    exit()
for k in range(len(S)-i-j):
    if S[k+j]!=S[-k-i-1]:
        print("No")
        exit()
print("Yes")