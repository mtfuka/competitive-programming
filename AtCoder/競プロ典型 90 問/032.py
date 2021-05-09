N = int(input())
A = [0]*N
for i in range(N):
    A[i] = list(map(int,input().split()))
M = int(input())
X = [0]*M
Y = [0]*M
for i in range(M):
    X[i],Y[i] = map(int,input().split())

bad = [[False for i in range(12)] for j in range(12)]
for i in range(M):
    bad[X[i]-1][Y[i]-1] = True
    bad[Y[i]-1][X[i]-1] = True

ans = float("INFINITY")
import itertools
list = list(itertools.permutations(range(N)))
for i in list:
    rumor = True
    for j in range(N-1):
        if bad[i[j]][i[j+1]]:
            rumor = False
    if rumor:
        sum = 0
        for j in range(N):
            sum += A[i[j]][j]
        ans = min(ans,sum)
if ans==float("INFINITY"):print(-1)
else:print(ans)