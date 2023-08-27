N = int(input())
S = input()
T = input()
if S.count('0')!=T.count('0'):
    print(-1)
    exit()
ans = 0
s = []
t = []
for i in range(N):
    if S[i]=='0':
        s.append(i)
    if T[i]=='0':
        t.append(i)
for i in range(len(s)):
    if s[i]!=t[i]:
        ans += 1
print(ans)