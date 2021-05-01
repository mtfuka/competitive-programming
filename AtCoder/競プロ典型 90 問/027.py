N = int(input())
S = {}
for i in range(N):
    S.setdefault(input(),i)
for i in S:
    print(S[i]+1)
