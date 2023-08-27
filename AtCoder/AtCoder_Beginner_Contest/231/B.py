N=int(input())
S=[]
for i in range(N):
    S.append(input())
from statistics import mode
print(mode(S))