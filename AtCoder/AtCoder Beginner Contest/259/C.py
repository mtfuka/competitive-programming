from itertools import groupby
S=list(input())
T=list(input())
def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res
s=runLengthEncode(S)
t=runLengthEncode(T)
if len(s)!=len(t):exit(print("No"))
for i in range(len(s)):
    if s[i][0]!=t[i][0]:exit(print("No"))
    if s[i][1]>t[i][1]:exit(print("No"))
    if s[i][1]==1 and t[i][1]>1:exit(print("No"))
print("Yes")