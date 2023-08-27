from collections import deque
S = input()
T = deque()
reverse = False
for Si in S:
    if Si=='R':
        reverse = not reverse
    else:
        if not reverse:
            T.append(Si)
        else:
            T.appendleft(Si)
if reverse:T.reverse()
ans = deque()
for Ti in T:
    if len(ans)!=0 and ans[-1]==Ti:
        ans.pop()
    else:
        ans.append(Ti)
print(''.join(ans))