import copy
N = int(input())
S = [0] * N
T = [0] * N
for i in range(N):
  S[i], T[i] = input().split()
T = list(map(int,T))
R = copy.deepcopy(T)
R.sort()
print(S[T.index(R[-2])])