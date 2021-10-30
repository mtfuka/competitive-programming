import bisect
N = int(input())
S = input()
maru = []
batu = []
for i in range(N):
    if S[i]=='o':
        maru.append(i)
    else:
        batu.append(i)
ans=0
for i in range(N):
    if S[i]=='o':
        if bisect.bisect(batu,i)>len(batu)-1:continue
        ans += N-batu[bisect.bisect(batu,i)]
    else:
        if bisect.bisect(maru,i)>len(maru)-1:continue
        ans += N-maru[bisect.bisect(maru,i)]
print(ans)