N,K = map(int,input().split())
l = [-1]*100000
count = 0
while l[N]==-1:
    l[N] = count
    N = (N + sum(list(map(int, list(str(N))))))%100000
    count += 1
cycle = count - l[N]
if K>=l[N]:
    print(l.index((K-l[N])%cycle + l[N]))
else:
    print(l.index(K))